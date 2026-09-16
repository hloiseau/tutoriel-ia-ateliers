# Passe adverse — transitions des parties 1 à 4

Lecture enchaînée de l’introduction générale, des conclusions des parties 1 à 3 et des introductions des parties 2 à 4. Aucun fichier du tutoriel n’a été modifié.

## Bilan

Aucun problème sérieux de progression ou de promesse non tenue dans ces trois raccords. Le lecteur passe bien :

1. de l’histoire aux calculs d’un petit modèle construit avec NumPy ;
2. de ce modèle entraîné pendant l’atelier aux poids d’un modèle de langage déjà entraîné ;
3. du petit modèle local sur CPU à un assistant de développement utilisant un modèle hébergé.

Le troisième passage est particulièrement important : la conclusion de la partie 3 dit explicitement que les essais CPU ne mesurent pas une session complète d’agent de code, puis la partie 4 annonce le modèle hébergé, GitHub Copilot comme parcours documenté et la possibilité de suivre sans IA. Cette répétition est utile et doit rester. Elle empêche de transformer l’expérience locale en promesse d’un agent de code utilisable sur CPU.

## Deux répétitions mineures

### Partie 1 → partie 2

La conclusion de la partie 1 annonce successivement « une image de huit pixels de côté », « des poids » et l’entraînement à reconnaître les chiffres. Le TL;DR qui suit reprend immédiatement les mêmes trois éléments, avant que l’introduction propose enfin le geste du trois dessiné au crayon.

Ce n’est pas bloquant : une conclusion peut annoncer la suite et un TL;DR doit rester autonome. Si le coordinateur souhaite alléger la couture, la modification la plus sûre consiste à garder le raccord concret de la partie 1, mais à lui retirer un niveau de détail :

> Dans la partie suivante, nous allons isoler quelques-uns de ces éléments et entraîner nous-mêmes un petit modèle à reconnaître des chiffres.

L’image de huit pixels et les poids resteraient alors au TL;DR et dans l’ouverture de la partie 2, là où le lecteur commence à les manipuler.

### Partie 2 → partie 3

La dernière phrase de la partie 2 promet de « télécharger [les] poids » et de les faire fonctionner sur la machine ; les deux premières phrases de la partie 3 redonnent aussitôt le fichier de poids, le moteur et le programme client. La reprise reste pédagogique, car elle ajoute les trois pièces de l’installation. Aucune correction nécessaire.

Si une coupe est souhaitée, agir uniquement sur la conclusion de la partie 2 : « La partie suivante change d’échelle avec un modèle de langage déjà entraîné, que nous ferons fonctionner sur notre machine. » L’introduction de la partie 3 conserverait ainsi la première explication précise du fichier de poids et du moteur.

## Notions et changements d’outil

- NumPy, poids et entraînement ont été introduits avant la partie 3. Le « moteur » arrive seulement quand il devient utile et son rôle est donné dans la première phrase.
- Le passage de l’entraînement à l’inférence est compréhensible : la conclusion de la partie 2 précise que le modèle suivant est déjà entraîné et que ses poids seront téléchargés.
- Le passage du local à l’hébergé est nommé des deux côtés de la frontière 3 → 4. Le motif est donné : les essais courts sur CPU ne prouvent ni la qualité ni les délais d’une session d’agent.
- L’introduction générale reste cohérente avec le parcours : les premiers ateliers fonctionnent sur CPU, la carte graphique arrive ensuite comme variante, et la partie 4 présente l’outil avant de demander de l’utiliser.

## Ton

Les trois conclusions emploient une variante de « la partie suivante », ce qui produit une petite régularité éditoriale, sans uniformiser les scènes : image de huit pixels, changement d’échelle, puis ticket et diff. Les ouvertures reprennent aussitôt un objet concret (un trois au crayon, les trois pièces du modèle local, un test vert malgré un bug). Je déconseille une réécriture supplémentaire uniquement pour varier la formule.

## Proposition au coordinateur

Conserver le raccord 3 → 4 tel quel. Pour les deux autres, choisir au plus une des coupes proposées ci-dessus ; les appliquer toutes les deux rendrait les conclusions plus uniformes au lieu de les améliorer.
