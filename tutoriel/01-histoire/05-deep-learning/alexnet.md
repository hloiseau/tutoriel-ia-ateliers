En 2012, Alex Krizhevsky, Ilya Sutskever et Geoffrey Hinton présentent un réseau qui obtient un résultat nettement meilleur que ses concurrents dans une épreuve de classification d’images liée à ImageNet. Ce réseau est connu sous le nom **AlexNet**.[^h5s4-alexnet]

Il utilise plusieurs couches de calcul et des GPU pour son entraînement. Un GPU, que l’on rencontre notamment sur une carte graphique, peut exécuter de nombreux calculs en parallèle. Ces capacités sont utiles pour les opérations répétées des réseaux.

Le **deep learning**, ou apprentissage profond, désigne des méthodes utilisant plusieurs couches de transformations apprises. Le mot « profond » concerne cette organisation ; il ne veut pas dire que la machine réfléchit profondément à la photo. 🙂

![Une image représentée par une grille de pixels traverse plusieurs couches de calcul avant de produire des scores pour des catégories.](image:images/image-couches.png)
Figure: Vue pédagogique d’une classification d’image. Ce dessin ne reproduit pas l’architecture exacte d’AlexNet.

Sur le schéma, nous partons de valeurs de pixels. Les couches les transforment progressivement, puis le réseau produit des scores pour les catégories proposées. Pendant l’entraînement, ses réglages sont modifiés pour améliorer les réponses.

Le résultat d’AlexNet rend très visible l’intérêt de cette combinaison de données, de méthodes et de matériel. Il ne marque pas l’invention soudaine des réseaux à plusieurs couches : nous avons déjà rencontré des travaux sur leur apprentissage en 1986.


[^h5s4-alexnet]: [Krizhevsky, Sutskever et Hinton, ImageNet Classification with Deep Convolutional Neural Networks (2012)](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html).
