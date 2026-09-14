"""Régénérer les sept PNG. Dépendances : matplotlib, numpy et Pillow."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
BG='#f7f4ec';INK='#183642';BLUE='#326fa8';TEAL='#178176';RED='#bb4e40';GOLD='#d5a343'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'text.color':INK,'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK})
def canvas(title,sub=None):
 f,a=plt.subplots(figsize=(12,6.8),facecolor=BG);a.set_facecolor(BG);a.set(xlim=(0,12),ylim=(0,6.8));a.axis('off');f.subplots_adjust(0,0,1,1)
 a.text(.6,6.2,title,fontsize=23,weight='bold',va='top')
 if sub:a.text(.6,5.62,sub,fontsize=12)
 return f,a
def box(a,x,y,w,h,title,body='',color=BLUE):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=.16',facecolor='white',edgecolor=color,linewidth=2))
 a.text(x+.22,y+h-.24,title,va='top',fontsize=16,weight='bold',color=color)
 if body:a.text(x+.22,y+h-.70,body,va='top',fontsize=13,linespacing=1.5)
def arrow(a,start,end,color=INK):a.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=17,linewidth=1.8,color=color))
def save(f,n,name):
 d=ROOT/f'partie-{n}'/'images';d.mkdir(exist_ok=True);f.savefig(d/name,dpi=130,facecolor=BG);plt.close(f)
f,a=canvas('Un modèle local : trois pièces','Tout se passe sur le même ordinateur après le téléchargement.')
box(a,.6,2.4,3.05,2,'Client Python','Prépare les messages\nEnregistre la réponse')
box(a,5,2.4,3.25,2,'Serveur llama.cpp','Reçoit la demande\nExécute le modèle',TEAL)
box(a,8.95,.75,2.45,1.8,'Fichier GGUF','Poids sur le disque',GOLD)
arrow(a,(3.7,3.85),(4.9,3.85));a.text(3.8,4.05,'question',fontsize=11)
arrow(a,(4.9,2.9),(3.7,2.9));a.text(3.8,2.55,'réponse',fontsize=11)
arrow(a,(9.35,2.62),(8.30,3.2));a.text(8.65,3.4,'chargement',fontsize=11)
a.text(5,1.7,'127.0.0.1:8080',fontfamily='DejaVu Sans Mono',fontsize=14,color=TEAL)
a.text(.6,.5,'Le client ne lit pas directement les poids. Le moteur réalise les calculs.',fontsize=13)
save(f,3,'installation.png')
f,a=canvas('Une conversation se construit avec des messages','Le client choisit les messages qui partent dans chaque requête.')
box(a,.6,2.4,4.8,2.45,'Nouvel appel, sans historique','user : « Quelle était ma question ? »\n\nLa première question est absente.',RED)
box(a,6,2.4,5.4,2.45,'Nouvel appel, avec historique','user : « Explique une variable. »\nassistant : réponse précédente\nuser : « Quelle était ma question ? »',TEAL)
a.text(.8,1.6,'Même serveur,',fontsize=19,weight='bold');a.text(.8,1.0,'informations différentes.',fontsize=19,weight='bold')
a.text(6.2,1.4,'Les poids n’ont pas été réentraînés\npour conserver cet échange.',fontsize=15,linespacing=1.5)
save(f,3,'historique.png')
f,a=plt.subplots(figsize=(12,6.8),facecolor=BG);a.set_facecolor(BG)
vals=[720,360,180];labels=['16 bits','8 bits','4 bits'];bars=a.barh(labels,vals,color=[BLUE,TEAL,GOLD],height=.55);a.invert_yaxis()
for b,v in zip(bars,vals):a.text(v+12,b.get_y()+b.get_height()/2,f'{v} Mo',va='center',weight='bold',fontsize=18)
a.set_xlim(0,880);a.set_xlabel('Volume théorique des paramètres (millions d’octets)',labelpad=14)
a.set_title('360 millions de paramètres : combien d’octets ?',loc='left',fontsize=21,weight='bold',pad=25)
a.spines[['top','right','left']].set_visible(False);a.grid(axis='x',alpha=.15);a.set_axisbelow(True);a.tick_params(axis='y',length=0,pad=12)
f.text(.15,.045,'Paramètres seuls : hors métadonnées, cache et mémoire de calcul.',fontsize=13)
f.subplots_adjust(left=.15,right=.95,top=.80,bottom=.22);save(f,3,'poids.png')
f,a=canvas('Réduire la précision : garder moins de valeurs','Exemple : arrondir au quart le plus proche.')
vals=np.array([-.92,-.61,-.18,.12,.43,.88]);q=np.round(vals*4)/4
for y,label,color in [(3.9,'Avant',BLUE),(2,'Après',TEAL)]:
 a.plot([1.5,10.6],[y,y],color=INK,lw=1)
 for x in np.arange(-1,1.01,.25):
  px=6+4*x;a.plot([px,px],[y-.08,y+.08],color=INK);a.text(px,y-.26,f'{x:g}'.replace('.',','),ha='center',fontsize=11)
 a.text(.65,y,label,weight='bold',va='center',color=color)
for v,w in zip(vals,q):
 x=6+4*v;xx=6+4*w;a.scatter(x,3.9,color=BLUE,s=90,zorder=3);a.scatter(xx,2,color=TEAL,s=90,zorder=3);arrow(a,(x,3.6),(xx,2.3),GOLD)
a.text(.65,.75,'Des valeurs distinctes peuvent se retrouver au même endroit.\nMoins de précision signifie aussi une approximation.',fontsize=15,linespacing=1.5)
save(f,3,'quantifier.png')
f,a=canvas('Suivre le scénario de remise en stock','Entrée : 2 000 centimes avant et après ; indisponible, puis disponible.')
box(a,.6,3.1,3,1.5,'main','Charge le fichier JSON')
box(a,4.5,3.1,3,1.5,'lire_etat','Construit deux Etat',TEAL)
box(a,8.4,3.1,3,1.5,'notifier','Calcule un booléen',GOLD)
arrow(a,(3.7,3.85),(4.4,3.85));arrow(a,(7.6,3.85),(8.3,3.85))
box(a,3.3,.6,5.4,1.4,'Affichage JSON','Avant : true          Après : false',RED)
arrow(a,(9.9,3),(9.9,1.3));arrow(a,(9.9,1.3),(8.8,1.3))
save(f,4,'projet.png')
f,a=canvas('Les tests passent… jusqu’au cas oublié','Résultats des trois états fournis dans l’atelier.')
ys=[4.4,3,1.6]
for y,label,good,bad in zip(ys,['01-depart','02-test-rouge','03-corrige'],[3,11,13],[0,2,0]):
 a.text(.65,y,label,fontsize=15,va='center',fontfamily='DejaVu Sans Mono')
 for i in range(good+bad):a.add_patch(Rectangle((3.8+i*.40,y-.23),.30,.46,facecolor=TEAL if i<good else RED))
 a.text(9.35,y,f'{good} réussis'+(f'\n{bad} échecs' if bad else ''),va='center',fontsize=14,color=RED if bad else TEAL)
a.text(.65,.55,'Un carré représente un test. Ajouter des cas révèle un comportement jusque-là non contrôlé.',fontsize=12)
save(f,4,'tests.png')
f,a=canvas('Les deux conditions doivent être vraies','Décision attendue après correction, quel que soit l’ancien stock.')
for x,label in [(4,'Prix inchangé\nou en hausse'),(8,'Prix en baisse')]:a.text(x,4.9,label,ha='center',va='top',weight='bold',fontsize=16)
for y,label in [(3.4,'Disponible\nmaintenant'),(1.6,'Indisponible\nmaintenant')]:a.text(.6,y,label,va='center',weight='bold',fontsize=15)
for x,y,answer,c in [(4,3.4,'NON',RED),(8,3.4,'OUI',TEAL),(4,1.6,'NON',RED),(8,1.6,'NON',RED)]:
 a.add_patch(FancyBboxPatch((x-1.45,y-.60),2.9,1.2,boxstyle='round,pad=.03,rounding_size=.14',facecolor='white',edgecolor=c,lw=2));a.text(x,y,answer,ha='center',va='center',color=c,weight='bold',fontsize=23)
save(f,4,'decision.png')
