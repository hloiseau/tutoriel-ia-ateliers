# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Schémas originaux de la partie 6 ; génération avec matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT=Path(__file__).resolve().parents[1]/'tutoriel/06-mcp-skills/images'
INK='#243447';BLUE='#dcecf8';GREEN='#def0e6';RED='#f9e2dc';GRAY='#edf0f4';BG='#fbfaf7'

def canvas(title,subtitle):
 fig,ax=plt.subplots(figsize=(12,7.4),dpi=140)
 fig.patch.set_facecolor(BG);ax.set(xlim=(0,12),ylim=(0,7.4));ax.axis('off')
 ax.text(.35,7,title,fontsize=21,color=INK,weight='bold')
 ax.text(.35,6.52,subtitle,fontsize=12,color=INK)
 return fig,ax

def box(ax,x,y,w,h,title,body='',color=BLUE):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.03,rounding_size=0.1',facecolor=color,edgecolor=INK,lw=1.1))
 ax.text(x+w/2,y+h*(.7 if body else .5),title,ha='center',va='center',fontsize=13,weight='bold',color=INK)
 if body:ax.text(x+w/2,y+h*.3,body,ha='center',va='center',fontsize=11,color=INK,linespacing=1.4)

def arrow(ax,a,b,both=False,rad=0):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='<->' if both else '-|>',mutation_scale=14,color=INK,lw=1.5,connectionstyle=f'arc3,rad={rad}'))

def save(fig,name):
 OUT.mkdir(parents=True,exist_ok=True);fig.savefig(OUT/(name+'.png'),bbox_inches='tight',facecolor=BG);plt.close(fig)

fig,ax=canvas('Le serveur est local. Et le modèle ?','Exemple : un assistant sur votre ordinateur utilise un modèle hébergé.')
ax.add_patch(FancyBboxPatch((.4,.6),7.4,5.3,boxstyle='round,pad=.02',facecolor=GRAY,edgecolor=INK))
ax.text(.7,5.5,'VOTRE ORDINATEUR',fontsize=12,weight='bold',color=INK)
box(ax,.8,3.6,3.2,1.4,'Assistant (hôte)','Contient le client MCP')
box(ax,4.7,3.6,2.65,1.4,'Serveur MCP','serveur.py',color=GREEN)
box(ax,4.7,1.15,2.65,1.35,'Données locales','Tickets et documents',color='white')
box(ax,8.65,3.6,2.9,1.4,'Modèle hébergé','Chez le fournisseur',color=RED)
arrow(ax,(4.08,4.3),(4.6,4.3),True);ax.text(4.35,3.12,'stdio',ha='center',fontsize=11,color=INK)
arrow(ax,(6.03,2.6),(6.03,3.5));ax.text(6.4,2.95,'lecture',fontsize=11,color=INK)
arrow(ax,(2.4,5.07),(10.1,5.07),True,rad=-.18)
ax.text(8.05,2.45,'Des résultats d’outils\npeuvent partir dans\nle contexte du modèle.',fontsize=12,color=INK,linespacing=1.5)
ax.text(.85,1.42,'MCP relie le client\nau serveur ; il ne choisit pas\nl’hébergement du modèle.',fontsize=12,color=INK,linespacing=1.5)
save(fig,'trajet')

fig,ax=canvas('Ce qui limite une demande','« Lecture seule » doit correspondre au code et aux droits utilisés.')
box(ax,.45,4.55,3.25,1.2,'Argument reçu','../tickets',color=GRAY)
box(ax,4.4,4.55,3.25,1.2,'Validation','Identifiant mal formé')
box(ax,8.35,4.55,3.1,1.2,'Refus',color=RED)
arrow(ax,(3.8,5.15),(4.3,5.15));arrow(ax,(7.75,5.15),(8.25,5.15))
box(ax,.45,2.65,3.25,1.2,'Outil demandé','modifier_ticket',color=GRAY)
box(ax,4.4,2.65,3.25,1.2,'Inventaire','Outil non exposé')
box(ax,8.35,2.65,3.1,1.2,'Refus',color=RED)
arrow(ax,(3.8,3.25),(4.3,3.25));arrow(ax,(7.75,3.25),(8.25,3.25))
box(ax,.45,.5,11,1.35,'Droits du processus et autres outils','Un terminal peut donner un autre accès aux fichiers.\nLe serveur de l’atelier ne constitue pas un bac à sable.',color=GREEN)
save(fig,'acces')

fig,ax=canvas('Où ranger cette information ?','Trois contenus qui ne changent pas pour les mêmes raisons.')
for x,title,body,color in [(.45,'Conventions','Les prix sont des\nentiers en centimes.',BLUE),(4.4,'Skill','Présenter les décisions\nencore à arbitrer.',GREEN),(8.35,'Documentation','Un retour en stock\nà prix égal ne notifie pas.',GRAY)]:
 box(ax,x,3.6,3.2,2,title,body,color)
for x,why in [(.45,'Commun aux tâches\nsur ce projet'),(4.4,'Procédure pour\npréparer la recette'),(8.35,'Comportement\ndu produit')]:
 ax.text(x+1.6,2.65,why,ha='center',fontsize=12,color=INK,linespacing=1.5)
box(ax,1.1,.55,9.8,1.2,'Des références pour retrouver les sources','Le ticket cite le document ; le skill cite son format de recette.',color='white')
save(fig,'rangement')
