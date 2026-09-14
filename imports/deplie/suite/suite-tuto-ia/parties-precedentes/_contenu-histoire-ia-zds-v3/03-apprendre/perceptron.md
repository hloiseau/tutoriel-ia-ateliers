Rosenblatt présente ses travaux sur le **perceptron** dans un article de 1958. Il s’intéresse à la manière dont un système peut apprendre à associer des entrées à des réponses.[^h3s1-rosenblatt]

Prenons une version élémentaire pour comprendre l’idée. Nous avons des nombres en entrée, par exemple des mesures réalisées sur une image. Chaque entrée est multipliée par un **poids**, qui règle son influence sur le résultat. Le programme combine ces valeurs et décide dans quelle catégorie ranger l’exemple.

Lorsqu’il se trompe pendant l’entraînement, une règle d’apprentissage modifie les poids. Nous recommençons avec d’autres exemples. Les poids sont donc des réglages que le programme ajuste, au lieu de nous demander de choisir chacun d’eux.

La différence avec notre neurone de 1943 se trouve notamment là : nous avons maintenant une méthode pour modifier une partie du système à partir de ses erreurs.

Pour le représenter, imaginons des objets que l’on mesure selon deux propriétés. Chaque objet devient un point sur une feuille. Le programme cherche une séparation entre deux catégories.

![À gauche, deux catégories de points peuvent être séparées par une droite ; à droite, des catégories alternées aux quatre coins ne le peuvent pas.](image:images/separation.png)
Figure: Deux jeux de points fictifs. Les couleurs et les formes indiquent les catégories ; les axes représentent deux mesures quelconques.

Sur le dessin de gauche, une droite suffit. Celui de droite est plus gênant : les deux points d’une catégorie occupent des coins opposés. Quelle que soit la droite choisie, elle ne séparera pas correctement les quatre points.

Vous pouvez essayer de tracer cette droite mentalement. Le problème ne vient pas d’un manque de patience à l’entraînement : la forme de séparation autorisée ne convient pas.

Cet exemple correspond au motif logique appelé **OU exclusif**, ou XOR. Il illustre une limite d’un seul classifieur linéaire. En ajoutant des transformations ou plusieurs couches, on peut construire d’autres séparations. Encore faut-il savoir régler l’ensemble.


[^h3s1-rosenblatt]: [Frank Rosenblatt, The Perceptron (1958)](https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf).
