# 5. Le tournant du deep learning

[Sommaire de la partie](../README.md) · [Sources](.)

À la fin du XXe siècle, l’IA prend des formes variées. Des programmes spécialisés obtiennent des résultats spectaculaires, tandis que les méthodes d’apprentissage progressent sur des tâches moins visibles.

Les années suivantes vont réunir trois ingrédients importants pour les réseaux de neurones : des méthodes plus efficaces, davantage de données et des moyens de calcul adaptés.

## 1997 : Deep Blue gagne contre Kasparov

En 1997, Deep Blue, développé par IBM, remporte un match contre Garry Kasparov, alors champion du monde d’échecs. C’est un événement très médiatisé.[^h5s1-blue]

Deep Blue s’appuie sur une recherche rapide de positions, une évaluation spécialisée et du matériel conçu pour les échecs. Nous retrouvons le problème étudié par Shannon : examiner les suites de coups et décider lesquelles méritent d’être poursuivies.

Le résultat ne signifie pas que Deep Blue peut discuter de n’importe quel sujet ou apprendre tout seul un nouveau métier. Son organisation est consacrée à un jeu précis.

Cela n’enlève rien à la performance. Les règles sont connues, l’adversaire est excellent et le résultat se constate sur l’échiquier. Mais pour raconter correctement l’histoire, il faut garder le nom de la tâche à côté du résultat : **gagner un match d’échecs**.

Ce succès ne repose pas sur les grands réseaux de langage que nous utiliserons plus tard. L’IA rassemble plusieurs familles de techniques, et une victoire célèbre ne marque pas nécessairement le triomphe de la méthode devenue populaire aujourd’hui.


[^h5s1-blue]: [IBM, Deep Blue](https://www.ibm.com/history/deep-blue).

## L’apprentissage ne se limite pas aux réseaux

Dans les années 1990 et 2000, d’autres méthodes d’apprentissage se développent et sont utilisées pour classer des données ou faire des prédictions. Les machines à vecteurs de support, notamment décrites par Corinna Cortes et Vladimir Vapnik en 1995, cherchent des séparations entre catégories. Les forêts aléatoires, présentées par Leo Breiman en 2001, combinent plusieurs arbres de décision.[^h5s2-svm][^h5s2-forets]

Un **arbre de décision** ressemble à une succession de questions. Pour classer nos fruits fictifs, on pourrait commencer par leur diamètre, puis examiner leur masse. Pendant l’apprentissage, l’algorithme choisit les séparations à partir des données. Une forêt combine les résultats de plusieurs arbres.

Vous voyez la différence avec le système expert de notre atelier : nous n’avons pas nécessairement écrit chaque question et chaque seuil à la main. Ils peuvent être déterminés pendant l’apprentissage.

Ces approches font partie de l’histoire de l’IA, même lorsqu’on ne les présente pas avec une interface de conversation. Reconnaître un message indésirable, prévoir une quantité ou classer un document n’exige pas automatiquement un grand modèle génératif.

Nous reviendrons sur le choix d’une méthode lorsque nous construirons nos propres expériences. Pour le moment, retenez que les réseaux de neurones progressent au milieu d’un domaine déjà très divers.


[^h5s2-svm]: [Cortes et Vapnik, Support-vector networks (1995)](https://link.springer.com/article/10.1007/BF00994018).
[^h5s2-forets]: [Leo Breiman, Random Forests (2001)](https://link.springer.com/article/10.1023/A:1010933404324).

## Des images et des personnes pour les classer

En 2009, une équipe autour de Fei-Fei Li présente **ImageNet**, une grande base d’images organisée en catégories. Son intérêt est de fournir des données pour entraîner et évaluer des systèmes de reconnaissance d’images.[^h5s3-imagenet]

Pour apprendre à reconnaître un chat, un réseau doit voir des exemples. Mais il faut d’abord rassembler les images, choisir les catégories et vérifier ce qu’elles contiennent. Le papier d’ImageNet décrit notamment le recours à des personnes chargées de vérifier des annotations via Amazon Mechanical Turk.

Les données ne se sont donc pas rangées toutes seules dans les bons dossiers. Derrière une base d’apprentissage se trouvent des choix et du travail humain.

Prenons trois photographies imaginaires d’un chat : de face, caché derrière un fauteuil, puis très petit au fond d’un jardin. Pour nous, ce sont trois chats. Pour un programme, les pixels sont très différents. Il faut que les exemples et les méthodes lui permettent de traiter cette diversité.

Si toutes les photos d’une catégorie ont le même arrière-plan, le programme peut aussi utiliser un indice qui ne correspond pas à ce qu’on voulait lui apprendre. Une étiquette correcte ne suffit donc pas à rendre un jeu d’exemples représentatif.


[^h5s3-imagenet]: [Deng et ses collègues, ImageNet: A Large-Scale Hierarchical Image Database (2009)](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf).

## 2012 : le succès d’AlexNet

En 2012, Alex Krizhevsky, Ilya Sutskever et Geoffrey Hinton présentent un réseau qui obtient un résultat nettement meilleur que ses concurrents dans une épreuve de classification d’images liée à ImageNet. Ce réseau est connu sous le nom **AlexNet**.[^h5s4-alexnet]

Il utilise plusieurs couches de calcul et des GPU pour son entraînement. Un GPU, que l’on rencontre notamment sur une carte graphique, peut exécuter de nombreux calculs en parallèle. Ces capacités sont utiles pour les opérations répétées des réseaux.

Le **deep learning**, ou apprentissage profond, désigne des méthodes utilisant plusieurs couches de transformations apprises. Le mot « profond » concerne cette organisation ; il ne veut pas dire que la machine réfléchit profondément à la photo. 🙂

![Une image représentée par une grille de pixels traverse plusieurs couches de calcul avant de produire des scores pour des catégories.](../images/image-couches.png)
Figure: Vue pédagogique d’une classification d’image. Ce dessin ne reproduit pas l’architecture exacte d’AlexNet.

Sur le schéma, nous partons de valeurs de pixels. Les couches les transforment progressivement, puis le réseau produit des scores pour les catégories proposées. Pendant l’entraînement, ses réglages sont modifiés pour améliorer les réponses.

Le résultat d’AlexNet rend très visible l’intérêt de cette combinaison de données, de méthodes et de matériel. Il ne marque pas l’invention soudaine des réseaux à plusieurs couches : nous avons déjà rencontré des travaux sur leur apprentissage en 1986.


[^h5s4-alexnet]: [Krizhevsky, Sutskever et Hinton, ImageNet Classification with Deep Convolutional Neural Networks (2012)](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html).

## 2016 : apprendre à jouer au go

En 2016, AlphaGo, développé par DeepMind, bat Lee Sedol dans un match de go. Le système combine des réseaux de neurones et une recherche dans les suites de coups possibles.[^h5s5-alphago]

Le go pose lui aussi un problème de choix parmi de nombreuses possibilités. Les réseaux aident à orienter la recherche et à évaluer les positions. Le programme associe donc des méthodes que nous avons déjà croisées, au lieu de se contenter d’une seule idée.

En 2017, AlphaGo Zero montre une autre façon d’entraîner un joueur : il progresse en jouant contre lui-même, sans partir d’un ensemble de parties humaines comme le faisaient les versions précédentes. Il reçoit néanmoins les règles du jeu et fonctionne dans un système conçu par des humains.[^h5s5-gozero]

On parle d’**apprentissage par renforcement** lorsque le système apprend à choisir des actions à partir de leurs conséquences et d’un signal de récompense. Dans un jeu, le résultat d’une partie peut contribuer à ce signal.

Si vous lisez que le programme a appris « tout seul », gardez donc en tête ce qui a été fourni : les règles, l’architecture, la procédure d’entraînement et les moyens de calcul. Il ne s’est pas installé spontanément devant un plateau de go.


[^h5s5-alphago]: [Google DeepMind, AlphaGo](https://deepmind.google/research/alphago/).
[^h5s5-gozero]: [Silver et ses collègues, Mastering the game of Go without human knowledge (2017)](https://www.nature.com/articles/nature24270).

Les réseaux deviennent capables de traiter des tâches de plus en plus variées, mais l’histoire ne se résume pas à augmenter leur taille. Les données, l’entraînement, le matériel et la façon de les associer à d’autres méthodes comptent aussi.

Les progrès sur le langage vont maintenant rapprocher ces outils d’un public beaucoup plus large.
