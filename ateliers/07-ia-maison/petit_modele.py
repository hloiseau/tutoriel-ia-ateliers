# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Petit modèle de caractères à contexte fixe ; NumPy, entraînement et adaptation LoRA."""
import argparse
import hashlib
import json
from pathlib import Path
import string
import time
import numpy as np
from threadpoolctl import threadpool_limits

ROOT=Path(__file__).resolve().parent
VOCAB='\0\n '+string.ascii_letters+string.digits+'.,;:=!?-()'
CONTEXTE=12


def charger_lot(nom,lot):
    lignes=(ROOT/f'donnees/langage/{nom}-{lot}.txt').read_text(encoding='utf-8').splitlines(keepends=True)
    ids={c:i for i,c in enumerate(VOCAB)}; xs=[];ys=[]
    for ligne in lignes:
        sequence=[0]*CONTEXTE+[ids[c] for c in ligne]
        for j in range(CONTEXTE,len(sequence)):
            xs.append(sequence[j-CONTEXTE:j]);ys.append(sequence[j])
    return np.asarray(xs,dtype=np.int64),np.asarray(ys,dtype=np.int64)


def initialiser(graine=7):
    rng=np.random.default_rng(graine);v=len(VOCAB);d=12;h=64
    return {'E':rng.normal(0,.1,(v,d)), 'W':rng.normal(0,1/np.sqrt(CONTEXTE*d),(CONTEXTE*d,h)),
            'b':np.zeros(h),'U':rng.normal(0,1/np.sqrt(h),(h,v)),'c':np.zeros(v)}


def calculer(p,x,y=None,gradient=False):
    z=p['E'][x].reshape(len(x),-1)
    h=np.tanh(z@p['W']+p['b'])
    sortie=p['U']+(p['A']@p['B'] if 'A' in p else 0)
    logits=h@sortie+p['c'];logits-=logits.max(axis=1,keepdims=True)
    probas=np.exp(logits);probas/=probas.sum(axis=1,keepdims=True)
    if y is None:return probas
    perte=float(-np.log(np.maximum(probas[np.arange(len(x)),y],1e-300)).mean())
    if not gradient:return perte
    dl=probas.copy();dl[np.arange(len(x)),y]-=1;dl/=len(x)
    if 'A' in p:
        # La base est gelée ; seuls les deux petits facteurs reçoivent des gradients.
        return perte,{'A':h.T@dl@p['B'].T,'B':(h@p['A']).T@dl}
    dh=(dl@sortie.T)*(1-h*h)
    de=np.zeros_like(p['E'])
    np.add.at(de,x,(dh@p['W'].T).reshape(len(x),CONTEXTE,-1))
    return perte,{'E':de,'W':z.T@dh,'b':dh.sum(axis=0),'U':h.T@dl,'c':dl.sum(axis=0)}


def perte_lot(p,x,y):
    return sum(calculer(p,x[i:i+256],y[i:i+256])*len(x[i:i+256])
               for i in range(0,len(x),256))/len(x)


def empreinte_base(p):
    return hashlib.sha256(b''.join(p[k].tobytes() for k in ['E','W','b','U','c'])).hexdigest()


def lire(path):
    with np.load(path,allow_pickle=False) as f:
        if str(f['vocab'])!=VOCAB or int(f['contexte'])!=CONTEXTE:raise ValueError('Format de modèle différent.')
        return {k:f[k].copy() for k in f.files if k not in {'vocab','contexte'}}


def sauver(path,p):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as f:np.savez_compressed(f,**p,vocab=np.array(VOCAB),contexte=np.array(CONTEXTE))


def avec_adaptateur(base, chemin):
    if 'A' in base:raise ValueError('Le modèle porte déjà un adaptateur.')
    with np.load(chemin,allow_pickle=False) as f:
        if str(f['base_sha256'])!=empreinte_base(base):
            raise ValueError('Cet adaptateur ne correspond pas aux poids de cette base.')
        a,b=f['A'].copy(),f['B'].copy()
        if a.ndim!=2 or b.ndim!=2 or (a.shape[0],b.shape[1])!=base['U'].shape or a.shape[1]!=b.shape[0]:
            raise ValueError('Dimensions de l’adaptateur incompatibles.')
    return {**base,'A':a,'B':b}


def generer(p,debut='le ',longueur=160,graine=19):
    ids={c:i for i,c in enumerate(VOCAB)}
    contexte=([0]*CONTEXTE+[ids[c] for c in debut])[-CONTEXTE:]
    rng=np.random.default_rng(graine);texte=debut
    for _ in range(longueur):
        probs=calculer(p,np.asarray([contexte]))[0];probs[0]=0;probs/=probs.sum()
        suivant=int(rng.choice(len(VOCAB),p=probs));texte+=VOCAB[suivant]
        contexte=contexte[1:]+[suivant]
    return texte


def entrainer(a):
    if a.sortie.exists():raise ValueError('Le dossier de sortie existe déjà ; choisissez un autre nom.')
    p=lire(a.base) if a.base else initialiser(a.graine)
    if 'A' in p:raise ValueError('Pour cet exercice, partir du modèle de base sans adaptateur.')
    avant_hash=empreinte_base(p)
    if a.mode=='lora':
        if not a.base:raise ValueError('LoRA demande --base.')
        p['A']=np.random.default_rng(a.graine).normal(0,.01,(p['U'].shape[0],a.rang))
        p['B']=np.zeros((a.rang,p['U'].shape[1]))
    noms=['A','B'] if a.mode=='lora' else list(p)
    x,y=charger_lot(a.corpus,'train');vx,vy=charger_lot(a.corpus,'validation')
    avant=perte_lot(p,vx,vy);moments={k:np.zeros_like(p[k]) for k in noms};variances={k:np.zeros_like(p[k]) for k in noms}
    rng=np.random.default_rng(a.graine);courbe=[];debut=time.perf_counter()
    for pas in range(1,a.pas+1):
        choix=rng.integers(len(x),size=48)
        perte,grads=calculer(p,x[choix],y[choix],True)
        norme=np.sqrt(sum(np.sum(g*g) for g in grads.values()))
        for k in noms:
            g=grads[k]/max(1,norme)
            moments[k]=.9*moments[k]+.1*g;variances[k]=.999*variances[k]+.001*g*g
            p[k]-=.01*(moments[k]/(1-.9**pas))/(np.sqrt(variances[k]/(1-.999**pas))+1e-8)
        if pas==1 or pas%100==0 or pas==a.pas:
            courbe.append({'pas':pas,'perte_lot_train':perte,'perte_validation':perte_lot(p,vx,vy)})
    duree=time.perf_counter()-debut
    rapport={'mode':a.mode,'corpus':a.corpus,'pas':a.pas,'graine':a.graine,'contexte_caracteres':CONTEXTE,
             'parametres_base':sum(p[k].size for k in ['E','W','b','U','c']),
             'parametres_entraines':sum(p[k].size for k in noms),'rang':a.rang if a.mode=='lora' else None,
             'perte_validation_avant':avant,'perte_validation_apres':perte_lot(p,vx,vy),
             'empreinte_base_avant':avant_hash,'empreinte_base_apres':empreinte_base(p),
             'duree_entrainement_s':duree,'courbe':courbe,
             'corpus_train_sha256':hashlib.sha256((ROOT/f'donnees/langage/{a.corpus}-train.txt').read_bytes()).hexdigest()}
    if a.mode=='lora':assert rapport['empreinte_base_avant']==rapport['empreinte_base_apres']
    a.sortie.mkdir(parents=True)
    sauver(a.sortie/'modele.npz',p)
    if a.mode=='lora':
        np.savez_compressed(a.sortie/'adaptateur.npz',A=p['A'],B=p['B'],base_sha256=np.array(avant_hash))
    (a.sortie/'rapport.json').write_text(json.dumps(rapport,ensure_ascii=False,indent=2)+'\n')
    (a.sortie/'echantillon.txt').write_text(generer(p,'INFO ' if a.corpus=='adaptation' else 'le '))
    print(json.dumps({k:v for k,v in rapport.items() if k!='courbe'},ensure_ascii=False,indent=2))


def main():
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='commande',required=True)
    t=s.add_parser('entrainer');t.add_argument('--base',type=Path);t.add_argument('--mode',choices=['complet','lora'],default='complet')
    t.add_argument('--corpus',choices=['base','adaptation'],default='base');t.add_argument('--pas',type=int,default=1200)
    t.add_argument('--rang',type=int,default=4);t.add_argument('--graine',type=int,default=7);t.add_argument('--sortie',type=Path,required=True)
    e=s.add_parser('evaluer');e.add_argument('--modele',type=Path,required=True);e.add_argument('--corpus',choices=['base','adaptation'],required=True)
    e.add_argument('--lot',choices=['validation','test'],default='test');e.add_argument('--sortie',type=Path,required=True)
    g=s.add_parser('generer');g.add_argument('--modele',type=Path,required=True);g.add_argument('--debut',default='le ')
    g.add_argument('--adaptateur',type=Path)
    a=p.parse_args()
    with threadpool_limits(limits=1):
        if a.commande=='entrainer':
            if not 1<=a.pas<=20000 or not 1<=a.rang<=32:p.error('Entre 1 et 20000 pas ; rang entre 1 et 32.')
            entrainer(a)
        elif a.commande=='generer':
            modele=lire(a.modele)
            if a.adaptateur:modele=avec_adaptateur(modele,a.adaptateur)
            print(generer(modele,a.debut))
        else:
            from recherche import sauver as sauver_json
            x,y=charger_lot(a.corpus,a.lot);perte=perte_lot(lire(a.modele),x,y)
            rapport={'corpus':a.corpus,'lot':a.lot,'caracteres_predits':len(y),'perte_moyenne':perte,'perplexite':float(np.exp(perte))}
            sauver_json(a.sortie,rapport);print(json.dumps(rapport,indent=2))


if __name__=='__main__':main()
