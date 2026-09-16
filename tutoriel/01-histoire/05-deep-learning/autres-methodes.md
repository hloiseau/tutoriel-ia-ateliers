Dans les années 1990 et 2000, d’autres méthodes d’apprentissage se développent et sont utilisées pour classer des données ou faire des prédictions. Les machines à vecteurs de support, notamment décrites par Corinna Cortes et Vladimir Vapnik en 1995, cherchent des séparations entre catégories. Les forêts aléatoires, présentées par Leo Breiman en 2001, combinent plusieurs arbres de décision.[^h5s2-svm][^h5s2-forets]

Un **arbre de décision** ressemble à une succession de questions. Pour classer nos fruits fictifs, on pourrait commencer par leur diamètre, puis examiner leur masse. Pendant l’apprentissage, l’algorithme choisit les séparations à partir des données. Une forêt combine les résultats de plusieurs arbres.

Vous voyez la différence avec le système expert de notre atelier : nous n’avons pas nécessairement écrit chaque question et chaque seuil à la main. Ils peuvent être déterminés pendant l’apprentissage.

Ces approches font partie de l’histoire de l’IA, même lorsqu’on ne les présente pas avec une interface de conversation. Reconnaître un message indésirable, prévoir une quantité ou classer un document n’exige pas automatiquement un grand modèle génératif.

Nous reviendrons sur le choix d’une méthode dans nos propres expériences. Les réseaux de neurones progressent ici au milieu d’un domaine déjà très divers.


[^h5s2-svm]: [Cortes et Vapnik, Support-vector networks (1995)](https://link.springer.com/article/10.1007/BF00994018).
[^h5s2-forets]: [Leo Breiman, Random Forests (2001)](https://link.springer.com/article/10.1023/A:1010933404324).
