Les réseaux peuvent comporter plusieurs couches de calcul. Le résultat d’une couche devient l’entrée de la suivante. Cela permet de composer des transformations, mais complique l’apprentissage : lorsqu’une réponse est mauvaise, quels réglages faut-il modifier ?

En 1986, David Rumelhart, Geoffrey Hinton et Ronald Williams publient un article marquant sur la **rétropropagation de l’erreur**. La méthode calcule comment les réglages du réseau influencent l’erreur, en remontant les couches, puis permet de les ajuster.[^h3s3-backprop]

![Un réseau à plusieurs couches reçoit des données à gauche et produit une réponse à droite ; l’information sur l’erreur est propagée en sens inverse pour calculer les ajustements.](image:images/couches-erreur.png)
Figure: Chaque cercle représente une unité de calcul du réseau ; les connexions transmettent les résultats d’une couche à la suivante.

Suivez d’abord les flèches vers la droite : le réseau produit une réponse. Nous la comparons à la réponse attendue. Le calcul en sens inverse sert ensuite à déterminer comment modifier les poids.

Cette publication contribue à faire connaître l’intérêt de la méthode pour les réseaux à plusieurs couches. Elle s’inscrit dans des travaux antérieurs sur le calcul des dérivées à travers une suite d’opérations, et les réseaux restent difficiles à entraîner.

La méthode ouvre la voie à des réseaux plus élaborés. Leur entraînement dépend encore du temps de calcul, des données disponibles et du choix de l’architecture.


[^h3s3-backprop]: [Rumelhart, Hinton et Williams, Learning representations by back-propagating errors (1986)](https://www.nature.com/articles/323533a0).
