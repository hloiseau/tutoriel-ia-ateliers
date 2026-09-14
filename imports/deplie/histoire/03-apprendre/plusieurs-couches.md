Les réseaux peuvent comporter plusieurs couches de calcul. Le résultat d’une couche devient l’entrée de la suivante. Cela permet de composer des transformations, mais complique l’apprentissage : lorsqu’une réponse est mauvaise, quels réglages faut-il modifier ?

En 1986, David Rumelhart, Geoffrey Hinton et Ronald Williams publient un article marquant sur la **rétropropagation de l’erreur**. La méthode calcule comment les réglages du réseau influencent l’erreur, en remontant les couches, puis permet de les ajuster.[^h3s3-backprop]

![Un réseau à plusieurs couches reçoit des données à gauche et produit une réponse à droite ; l’information sur l’erreur est propagée en sens inverse pour calculer les ajustements.](image:images/couches-erreur.png)
Figure: Chaque cercle représente une unité de calcul du réseau ; les connexions transmettent les résultats d’une couche à la suivante.

Suivez d’abord les flèches vers la droite : le réseau produit une réponse. Nous la comparons à la réponse attendue. Le calcul en sens inverse sert ensuite à déterminer comment modifier les poids.

Cette publication contribue à faire connaître l’intérêt de la méthode pour les réseaux à plusieurs couches. Elle ne signifie pas que toutes les difficultés sont résolues, ni que le principe du calcul des dérivées à travers une suite d’opérations vient d’être inventé.

Nous pouvons maintenant entraîner des réseaux plus élaborés. Le temps de calcul, les données disponibles et le choix de l’architecture restent cependant des contraintes importantes.


[^h3s3-backprop]: [Rumelhart, Hinton et Williams, Learning representations by back-propagating errors (1986)](https://www.nature.com/articles/323533a0).
