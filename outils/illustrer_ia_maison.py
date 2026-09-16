# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Schémas et graphique de la partie 7, à partir des résultats enregistrés."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'tutoriel/07-ia-maison/images'
INK='#243447';BLUE='#dcecf8';GREEN='#def0e6';RED='#f9e2dc';GRAY='#edf0f4';BG='#fbfaf7'
def canvas(title,subtitle):
 fig,ax=plt.subplots(figsize=(12,7.4),dpi=140)
 fig.patch.set_facecolor(BG);ax.set(xlim=(0,12),ylim=(0,7.4));ax.axis('off')
 ax.text(.35,7,title,fontsize=21,color=INK,weight='bold')
 ax.text(.35,6.5,subtitle,fontsize=12,color=INK)
 return fig,ax
def box(ax,x,y,w,h,title,body='',color=BLUE):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.03,rounding_size=.1',facecolor=color,edgecolor=INK,lw=1.1))
 ax.text(x+w/2,y+h*(.72 if body else .5),title,ha='center',va='center',fontsize=13,weight='bold',color=INK)
 if body:ax.text(x+w/2,y+h*.3,body,ha='center',va='center',fontsize=11,color=INK,linespacing=1.4)
def arrow(ax,a,b,rad=0):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,color=INK,lw=1.5,connectionstyle=f'arc3,rad={rad}'))
def save(fig,name):
 OUT.mkdir(parents=True,exist_ok=True);fig.savefig(OUT/(name+'.png'),bbox_inches='tight',facecolor=BG);plt.close(fig)

fig,ax=canvas('Les sources voyagent avec la question','La recherche choisit des passages ; les poids du modèle restent identiques.')
box(ax,.45,4.6,3.1,1.3,'Documents','Statut, révision, texte',GRAY)
box(ax,4.35,4.6,3.1,1.3,'Index lexical','Mots et pondérations')
box(ax,8.25,4.6,3.1,1.3,'Passages retenus','Identifiants et provenance',GREEN)
arrow(ax,(3.65,5.25),(4.25,5.25));arrow(ax,(7.55,5.25),(8.15,5.25))
box(ax,.45,2.1,3.1,1.3,'Question','« Quel délai ? »',GRAY)
arrow(ax,(3.65,2.75),(5.9,4.5))
box(ax,8.25,2.1,3.1,1.3,'Modèle local','Question + passages')
arrow(ax,(3.65,2.75),(8.15,2.75));arrow(ax,(9.8,4.5),(9.8,3.5))
box(ax,2.3,.2,7.4,1.1,'Réponse à confronter aux sources','Le modèle peut encore contredire les passages retenus.',RED)
arrow(ax,(9.8,2),(8.8,1.4))
save(fig,'recherche')

fig,ax=canvas('LoRA : une correction à côté de la base','Dans notre atelier, seules A et B apprennent ; U et c restent figés.')
box(ax,.45,3,2.1,1.3,'Entrée h','64 nombres',GRAY)
box(ax,4.6,4.55,3,1.2,'Base U','64 × 75',BLUE)
box(ax,3.35,1.55,2.5,1.2,'Adaptateur A','64 × 4',GREEN)
box(ax,6.4,1.55,2.5,1.2,'Adaptateur B','4 × 75',GREEN)
box(ax,9.5,3,2,1.3,'Somme','+ biais c',GRAY)
arrow(ax,(2.65,3.9),(4.5,5.1));arrow(ax,(7.7,5.1),(10.5,4.4))
arrow(ax,(2.65,3.4),(3.25,2.15));arrow(ax,(5.95,2.15),(6.3,2.15));arrow(ax,(9,2.15),(10.5,2.9))
ax.text(6,.45,'556 paramètres entraînables  •  La correction peut aussi dégrader les anciennes tâches.',ha='center',fontsize=12,color=INK)
save(fig,'lora')

fig,ax=canvas('Un modèle de 15 055 paramètres','Prédire un caractère à partir des douze précédents, sans attention.')
box(ax,.45,4.45,3.2,1.3,'12 caractères','Identifiants + remplissage',GRAY)
box(ax,4.4,4.45,3.2,1.3,'Table E','12 vecteurs de 12 nombres')
box(ax,8.35,4.45,3.2,1.3,'Mise à plat','144 nombres',GRAY)
arrow(ax,(3.75,5.1),(4.3,5.1));arrow(ax,(7.7,5.1),(8.25,5.1))
box(ax,8.35,1.8,3.2,1.3,'W, b et tanh','64 nombres',GREEN)
box(ax,4.4,1.8,3.2,1.3,'U et c','75 scores')
box(ax,.45,1.8,3.2,1.3,'Softmax','75 probabilités',GREEN)
arrow(ax,(9.95,4.35),(9.95,3.2));arrow(ax,(8.25,2.45),(7.7,2.45));arrow(ax,(4.3,2.45),(3.75,2.45))
ax.text(6,.6,'En génération, le caractère tiré devient une entrée du calcul suivant.',ha='center',fontsize=13,color=INK)
save(fig,'modele')

fig,ax=plt.subplots(figsize=(11.5,6.6),dpi=140);fig.patch.set_facecolor(BG);ax.set_facecolor(BG)
labels=['Base','Base + LoRA','Adaptation complète'];ys=[2,1,0]
for domain,offset,color,label in [('base',.17,'#4a7997','Phrases initiales'),('adaptation',-.17,'#d48a53','Lignes INFO')]:
 vals=[json.loads((ROOT/f'ateliers/07-ia-maison/resultats-reference/{m}/test-{domain}.json').read_text())['perte_moyenne'] for m in ['base','lora','complet']]
 ax.barh([y+offset for y in ys],vals,height=.28,color=color,label=label)
 for y,v in zip(ys,vals):ax.text(v+.09,y+offset,f'{v:.2f}'.replace('.',','),va='center',fontsize=12,color=INK)
ax.set_yticks(ys,labels,fontsize=12);ax.set_xlim(0,10);ax.set_xlabel('Perte moyenne sur les caractères du lot de test — plus faible = mieux',fontsize=11,labelpad=14)
ax.set_title('Apprendre le nouveau format, perdre sur l’ancien',loc='left',fontsize=19,pad=25,color=INK,weight='bold')
ax.spines[['top','right','left']].set_visible(False);ax.tick_params(axis='y',length=0);ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True);ax.legend(loc='lower right',frameon=False)
fig.text(.13,.01,'Même petit réseau, mêmes lots de test. Résultats propres à cet atelier.',fontsize=10,color=INK)
fig.tight_layout(rect=(0,.04,1,1));save(fig,'adaptation')
