# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Recherche TF-IDF dans un petit corpus fictif ; bibliothèque standard uniquement."""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parent
VIDES = set('a au aux avec ce ces cet cette dans de des du elle en est et il la le les leur ne nos notre nous on ou par pas pour que quel quelle quels quelles qui se ses son sont sur un une vos votre vous y'.split())


def mots(texte):
    texte = ''.join(c for c in unicodedata.normalize('NFKD', texte.casefold())
                    if not unicodedata.combining(c))
    return [m for m in re.findall(r'[a-z0-9]+', texte) if m not in VIDES]


def charger(dossier=ROOT/'donnees'):
    passages = []
    for doc in json.loads((dossier/'documents.json').read_text(encoding='utf-8')):
        if doc['statut'] == 'archivé':
            continue
        fichier = (dossier/doc['fichier']).resolve()
        if not fichier.is_relative_to(dossier.resolve()):
            raise ValueError('Document situé hors du corpus.')
        texte = fichier.read_text(encoding='utf-8')
        morceaux = [p.strip() for p in texte.split('\n\n') if p.strip() and not p.startswith('# ')]
        for numero, morceau in enumerate(morceaux, 1):
            passages.append({'id':f'{doc["id"]}#{numero}', 'titre':doc['titre'],
                             'statut':doc['statut'], 'revision':doc['revision'],
                             'fichier':doc['fichier'], 'texte':morceau,
                             'sha256':hashlib.sha256(texte.encode()).hexdigest()})
    return passages


class Index:
    def __init__(self, passages):
        self.passages = passages
        comptes = [Counter(mots(p['texte'])) for p in passages]
        df = Counter(mot for compte in comptes for mot in compte)
        self.idf = {mot: math.log((1+len(passages))/(1+n))+1 for mot,n in df.items()}
        self.vecteurs = [self.vectoriser(c) for c in comptes]

    def vectoriser(self, compte):
        brut = {m: n*self.idf[m] for m,n in compte.items() if m in self.idf}
        norme = math.sqrt(sum(v*v for v in brut.values()))
        return {m:v/norme for m,v in brut.items()} if norme else {}

    def chercher(self, question, k=3, seuil=0.12):
        q = self.vectoriser(Counter(mots(question)))
        notes = [(sum(v*q.get(m,0) for m,v in vec.items()), p)
                 for p,vec in zip(self.passages,self.vecteurs)]
        notes.sort(key=lambda item: (-item[0], item[1]['id']))
        return [{'score':round(score,6), **p} for score,p in notes[:k] if score>0 and score>=seuil]


def sauver(path, rapport):
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8') as f:
        json.dump(rapport,f,ensure_ascii=False,indent=2)
        f.write('\n')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('question')
    parser.add_argument('--k',type=int,default=3)
    parser.add_argument('--seuil',type=float,default=0.12)
    parser.add_argument('--sortie',type=Path,required=True)
    args=parser.parse_args()
    if not 1<=args.k<=10 or not math.isfinite(args.seuil) or not 0<=args.seuil<=1:
        parser.error('k entre 1 et 10 ; seuil fini entre 0 et 1.')
    result=Index(charger()).chercher(args.question,args.k,args.seuil)
    rapport={'question':args.question,'k':args.k,'seuil':args.seuil,'passages':result}
    sauver(args.sortie,rapport)
    print(json.dumps(rapport,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
