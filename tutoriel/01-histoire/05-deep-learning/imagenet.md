En 2009, une équipe autour de Fei-Fei Li présente **ImageNet**, une grande base d’images organisée en catégories. Son intérêt est de fournir des données pour entraîner et évaluer des systèmes de reconnaissance d’images.[^h5s3-imagenet]

Pour apprendre à reconnaître un chat, un réseau doit voir des exemples. Avant l’entraînement, des personnes rassemblent les images, choisissent les catégories et vérifient ce qu’elles contiennent. L’article d’ImageNet décrit notamment le recours à des personnes chargées de vérifier des annotations via Amazon Mechanical Turk.

Les données ne se sont donc pas rangées toutes seules dans les bons dossiers. Derrière une base d’apprentissage se trouvent des choix et du travail humain.

Prenons trois photographies imaginaires d’un chat : de face, caché derrière un fauteuil, puis très petit au fond d’un jardin. Pour nous, ce sont trois chats. Pour un programme, les pixels sont très différents. Il faut que les exemples et les méthodes lui permettent de traiter cette diversité.

Si toutes les photos d’une catégorie ont le même arrière-plan, le programme peut aussi utiliser un indice qui ne correspond pas à ce qu’on voulait lui apprendre. Une étiquette correcte ne suffit donc pas à rendre un jeu d’exemples représentatif.


[^h5s3-imagenet]: [Deng et ses collègues, ImageNet: A Large-Scale Hierarchical Image Database (2009)](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf).
