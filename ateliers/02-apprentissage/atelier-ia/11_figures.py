# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

from pathlib import Path
from commun import donnees,graphique,SORTIES,RACINE
from modele import probabilites,initialiser
import numpy as np
R=SORTIES;plt=graphique()
if not (SORTIES/'lineaire.npz').exists():
    raise SystemExit('Lancez d’abord 03_entrainer.py.')
with np.load(SORTIES/'lineaire.npz',allow_pickle=False) as a:p={k:a[k] for k in a.files}
fig,axes=plt.subplots(2,5,figsize=(12,5));lim=abs(p['W']).max()
for i,ax in enumerate(axes.flat):
 ax.imshow(p['W'][:,i].reshape(8,8),cmap='RdBu',vmin=-lim,vmax=lim);ax.set_title(f'Score du {i}');ax.axis('off')
fig.suptitle('Poids appris : rouge négatif, bleu positif',fontsize=17);fig.tight_layout();fig.savefig(R/'poids.png',dpi=140);plt.close(fig)
X,y,tr,va,te=donnees();i=tr[0];before=probabilites(X[i:i+1],initialiser())[0];after=probabilites(X[i:i+1],p)[0]
fig,axes=plt.subplots(1,3,figsize=(12,4));axes[0].imshow(X[i].reshape(8,8),cmap='gray',vmin=0,vmax=1);axes[0].set_title(f'Image étiquetée {y[i]}');axes[0].axis('off')
for a,proba,title in zip(axes[1:],[before,after],['Avant entraînement','Après entraînement']):a.bar(range(10),proba,color='#007e80');a.set(xticks=range(10),ylim=(0,1),title=title,xlabel='Chiffre',ylabel='Probabilité du modèle')
fig.tight_layout();fig.savefig(R/'avant-apres.png',dpi=140);plt.close(fig)
texte=(RACINE/'corpus.txt').read_text(encoding='utf-8')
voc=sorted(set(texte));ids={c:i for i,c in enumerate(voc)};counts=np.zeros((len(voc),len(voc)))
for a,b in zip(texte,texte[1:]):counts[ids[a],ids[b]]+=1
c=counts[voc.index('e')];idx=np.flatnonzero(c);idx=idx[np.argsort(c[idx])[::-1]];labels=[{' ':'espace','\n':'retour ligne'}.get(voc[j],voc[j]) for j in idx]
fig,ax=plt.subplots(figsize=(10,4));ax.bar(labels,c[idx],color='#007e80');ax.set(title='Dans notre corpus, quel caractère suit « e » ?',ylabel='Occurrences');fig.tight_layout();fig.savefig(R/'bigrammes.png',dpi=140);plt.close(fig)
print('Figures supplémentaires produites.')
