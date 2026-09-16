En 2012, Alex Krizhevsky, Ilya Sutskever et Geoffrey Hinton présentent un réseau qui obtient un résultat nettement meilleur que ses concurrents dans une épreuve de classification d’images liée à ImageNet. Ce réseau est connu sous le nom **AlexNet**.[^h5s4-alexnet]

Il utilise plusieurs couches de calcul et des GPU pour son entraînement. Un GPU, que l’on rencontre notamment sur une carte graphique, peut exécuter de nombreux calculs en parallèle. Ces capacités sont utiles pour les opérations répétées des réseaux.

Le **deep learning**, ou apprentissage profond, désigne des méthodes utilisant plusieurs couches de transformations apprises. La profondeur compte ici des couches de calcul, pas les pensées de la machine devant la photo. 🙂

![Une image représentée par une grille de pixels traverse plusieurs couches de calcul avant de produire des scores pour des catégories.](image:images/image-couches.png)
Figure: Vue pédagogique d’une classification d’image. Ce dessin ne reproduit pas l’architecture exacte d’AlexNet.

Sur le schéma, nous partons de valeurs de pixels. Les couches les transforment progressivement, puis le réseau produit des scores pour les catégories proposées. Pendant l’entraînement, ses réglages sont modifiés pour améliorer les réponses.

Le résultat d’AlexNet rend très visible l’intérêt de cette combinaison de données, de méthodes et de matériel. Les réseaux à plusieurs couches ont déjà une longue histoire en 2012 ; les travaux de 1986 sur leur apprentissage nous l’ont montré.


[^h5s4-alexnet]: [Krizhevsky, Sutskever et Hinton, ImageNet Classification with Deep Convolutional Neural Networks (2012)](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html).
