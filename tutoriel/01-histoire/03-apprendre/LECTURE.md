# 3. Apprendre à partir de données : les premières approches

[Sommaire de la partie](../README.md) · [Sources](.)

À la fin des années 1950, les neurones du modèle de McCulloch et Pitts ont des connexions fixées à l’avance. Frank Rosenblatt étudie une autre possibilité : modifier certains réglages du système à partir des exemples qu’on lui présente.

L’objectif est de lui faire reconnaître des formes sans écrire à la main une règle pour chaque image possible.

## 1958 : le perceptron

Rosenblatt présente ses travaux sur le **perceptron** dans un article de 1958. Il s’intéresse à la manière dont un système peut apprendre à associer des entrées à des réponses.[^h3s1-rosenblatt]

Prenons une version élémentaire pour comprendre l’idée. Nous avons des nombres en entrée, par exemple des mesures réalisées sur une image. Chaque entrée est multipliée par un **poids**, qui règle son influence sur le résultat. Le programme combine ces valeurs et décide dans quelle catégorie ranger l’exemple.

Lorsqu’il se trompe pendant l’entraînement, une règle d’apprentissage modifie les poids. Nous recommençons avec d’autres exemples. Les poids sont donc des réglages que le programme ajuste, au lieu de nous demander de choisir chacun d’eux.

La différence avec notre neurone de 1943 se trouve notamment là : nous avons maintenant une méthode pour modifier une partie du système à partir de ses erreurs.

Pour le représenter, imaginons des objets que l’on mesure selon deux propriétés. Chaque objet devient un point sur une feuille. Le programme cherche une séparation entre deux catégories.

![À gauche, deux catégories de points peuvent être séparées par une droite ; à droite, des catégories alternées aux quatre coins ne le peuvent pas.](../images/separation.png)
Figure: Deux jeux de points fictifs. Les couleurs et les formes indiquent les catégories ; les axes représentent deux mesures quelconques.

Sur le dessin de gauche, une droite suffit. Celui de droite est plus gênant : les deux points d’une catégorie occupent des coins opposés. Quelle que soit la droite choisie, elle ne séparera pas correctement les quatre points.

Vous pouvez essayer de tracer cette droite mentalement. Le problème ne vient pas d’un manque de patience à l’entraînement : la forme de séparation autorisée ne convient pas.

Cet exemple correspond au motif logique appelé **OU exclusif**, ou XOR. Il illustre une limite d’un seul classifieur linéaire. En ajoutant des transformations ou plusieurs couches, on peut construire d’autres séparations. Encore faut-il savoir régler l’ensemble.


[^h3s1-rosenblatt]: [Frank Rosenblatt, The Perceptron (1958)](https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf).

## Ce que veut dire « apprendre »

Le mot peut faire imaginer une machine qui comprend sa leçon comme nous. Dans notre exemple, l’apprentissage consiste plus précisément à ajuster des nombres pour diminuer les erreurs sur une tâche.

Imaginons un appareil qui doit distinguer de petits fruits à partir de leur masse et de leur diamètre. Nous préparons des exemples avec la bonne catégorie, puis nous comparons les réponses de l’appareil avec celles attendues.

Si nous vérifions uniquement les fruits utilisés pour régler le modèle, nous pouvons avoir une mauvaise surprise avec les suivants. Il faut donc garder des exemples à part, qui ne servent pas à ces réglages.

C’est la différence entre réussir sur ce qui a servi à l’apprentissage et réussir sur de nouvelles situations. Cette seconde capacité s’appelle la **généralisation**.

On peut aussi avoir choisi des exemples trop faciles. Si tous nos petits fruits sont des cerises et tous les gros des pommes, notre modèle peut sembler excellent. Ajoutons une petite pomme, et nous découvrons ce qu’il avait réellement appris à séparer.

Ce sont les choix de données, de représentation et d’évaluation qui donnent un sens au résultat. Un modèle n’apprend pas « tout » : nous lui fournissons une manière de traiter un problème, et nous vérifions ce qu’elle permet d’obtenir.

## 1986 : ajuster plusieurs couches

Les réseaux peuvent comporter plusieurs couches de calcul. Le résultat d’une couche devient l’entrée de la suivante. Cela permet de composer des transformations, mais complique l’apprentissage : lorsqu’une réponse est mauvaise, quels réglages faut-il modifier ?

En 1986, David Rumelhart, Geoffrey Hinton et Ronald Williams publient un article marquant sur la **rétropropagation de l’erreur**. La méthode calcule comment les réglages du réseau influencent l’erreur, en remontant les couches, puis permet de les ajuster.[^h3s3-backprop]

![Un réseau à plusieurs couches reçoit des données à gauche et produit une réponse à droite ; l’information sur l’erreur est propagée en sens inverse pour calculer les ajustements.](../images/couches-erreur.png)
Figure: Chaque cercle représente une unité de calcul du réseau ; les connexions transmettent les résultats d’une couche à la suivante.

Suivez d’abord les flèches vers la droite : le réseau produit une réponse. Nous la comparons à la réponse attendue. Le calcul en sens inverse sert ensuite à déterminer comment modifier les poids.

Cette publication contribue à faire connaître l’intérêt de la méthode pour les réseaux à plusieurs couches. Elle ne signifie pas que toutes les difficultés sont résolues, ni que le principe du calcul des dérivées à travers une suite d’opérations vient d’être inventé.

Nous pouvons maintenant entraîner des réseaux plus élaborés. Le temps de calcul, les données disponibles et le choix de l’architecture restent cependant des contraintes importantes.


[^h3s3-backprop]: [Rumelhart, Hinton et Williams, Learning representations by back-propagating errors (1986)](https://www.nature.com/articles/323533a0).

Les approches fondées sur l’apprentissage ne remplacent pas d’un coup les systèmes de règles. Elles se développent en parallèle, avec leurs propres possibilités et leurs propres difficultés.
