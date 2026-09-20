# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Illustrations originales de la partie 8 ; graphique de durées explicitement fictives."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'tutoriel/09-choisir/images'
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

fig,ax=canvas('Des personnes derrière les fichiers','Exemples de contributions ; leur organisation dépend du système examiné.')
box(ax,.45,4.5,3.2,1.5,'Contenus','Auteurs et personnes\nreprésentées dans les données',GRAY)
box(ax,4.4,4.5,3.2,1.5,'Préparation','Collecte, tri, annotation\net comparaison de réponses',GREEN)
box(ax,8.35,4.5,3.2,1.5,'Conception','Choix du modèle,\nentraînement et évaluation')
box(ax,4.4,2.2,3.2,1.25,'Modèle','Paramètres obtenus',GRAY)
arrow(ax,(2.05,4.4),(4.3,2.85));arrow(ax,(6,4.4),(6,3.55));arrow(ax,(9.95,4.4),(7.7,2.85))
box(ax,.45,.2,3.2,1.3,'Exploitation','Déploiement et maintenance',BLUE)
box(ax,4.4,.2,3.2,1.3,'Application','Réponse affichée',GRAY)
box(ax,8.35,.2,3.2,1.3,'Vérification','Personnes qui relisent\net assument les décisions',RED)
arrow(ax,(6,2.1),(6,1.6));arrow(ax,(3.75,.85),(4.3,.85));arrow(ax,(7.7,.85),(8.25,.85))
save(fig,'travail')

fig,ax=canvas('Qu’avons-nous réellement compté ?','Annoncer le périmètre avant de comparer deux nombres.')
box(ax,.45,3.65,5.3,2,'Calcul ciblé','Exemple : une mesure côté GPU\nNe décrit pas toute la machine.',BLUE)
box(ax,6.25,3.65,5.3,2,'Électricité du service','Ordinateur, attente, infrastructure…\nSelon les appareils effectivement mesurés.',GREEN)
box(ax,.45,.8,5.3,2,'Cycle de vie','Fabrication et usage du matériel,\neau, ressources, fin de vie…',GRAY)
box(ax,6.25,.8,5.3,2,'Évolution des usages','Nombre d’appels, nouveaux services,\ntravail et consommation déplacés…',RED)
ax.text(6,.1,'Une mesure électrique reste utile ; elle ne devient pas automatiquement un bilan complet.',ha='center',fontsize=12,color=INK)
save(fig,'perimetre')

fig,ax=canvas('Une décision que l’on peut expliquer','Commencer par les exigences, puis comparer les options restantes.')
box(ax,.45,4.45,3,1.3,'Besoin précis','Données + résultat attendu',GRAY)
box(ax,4.4,4.45,3.1,1.3,'Exigences','Respectées et vérifiées ?')
box(ax,8.4,4.45,3.1,1.3,'À clarifier / écarter','Condition absente ou inconnue',RED)
arrow(ax,(3.55,5.1),(4.3,5.1));arrow(ax,(7.6,5.1),(8.3,5.1));ax.text(7.95,5.42,'non',ha='center',fontsize=11,color=INK)
box(ax,4.4,2.15,3.1,1.3,'Comparer','Qualité, effort, apprentissage',GREEN)
arrow(ax,(5.95,4.35),(5.95,3.55));ax.text(6.25,3.92,'oui',fontsize=11,color=INK)
box(ax,.45,.2,3.1,1.15,'Sans IA','Script ou travail manuel',GRAY)
box(ax,4.4,.2,3.1,1.15,'Avec une aide','Périmètre et validation',GREEN)
box(ax,8.4,.2,3.1,1.15,'Reporter','Information encore nécessaire',RED)
arrow(ax,(4.3,2.5),(2,1.45));arrow(ax,(5.95,2.05),(5.95,1.45));arrow(ax,(7.6,2.5),(9.95,1.45))
save(fig,'decision')

fig,ax=plt.subplots(figsize=(12,6.3),dpi=140);fig.patch.set_facecolor(BG);ax.set_facecolor(BG)
data=json.loads((ROOT/'ateliers/08-choisir/exemples/temps-fictifs.json').read_text())['essais']
phases=[('preparer','Préparer','#869aa9'),('produire','Produire','#38718e'),('relire','Relire','#66a89a'),('corriger','Corriger','#d68f66'),('verifier','Vérifier','#a89abe'),('attente_bloquante','Attente bloquante','#c6c9ce')]
for y,item in zip([1,0],data):
 left=0
 for key,label,color in phases:
  v=item['minutes'][key];ax.barh(y,v,left=left,color=color,height=.43,label=label if y==1 else None)
  if v:ax.text(left+v/2,y,str(v),va='center',ha='center',fontsize=12,color='white' if key=='produire' else INK)
  left+=v
 ax.text(left+.3,y,f'{left} min',va='center',fontsize=13,color=INK,weight='bold')
ax.set_yticks([1,0],['Sans IA','Avec IA'],fontsize=13);ax.set_xlim(0,32);ax.set_ylim(-.55,1.65)
ax.set_title('Exemple fictif : compter jusqu’au résultat utilisable',loc='left',fontsize=18,pad=20,color=INK,weight='bold')
ax.set_xlabel('Minutes déclarées dans l’exemple — pas une mesure de productivité',fontsize=11,labelpad=14)
ax.spines[['top','right','left']].set_visible(False);ax.tick_params(axis='y',length=0);ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
ax.legend(loc='upper center',ncol=3,frameon=False,fontsize=11);fig.tight_layout();save(fig,'temps')
