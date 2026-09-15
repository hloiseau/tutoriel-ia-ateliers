# 1. Les origines de l’intelligence artificielle

[Sommaire de la partie](../README.md) · [Sources](.)

Avant les premiers ordinateurs, on cherche déjà à confier des calculs à des machines. Le projet est alors très matériel : il faut concevoir les pièces, transmettre les mouvements et trouver comment donner les opérations à effectuer.

Au XIXe siècle, Charles Babbage et Ada Lovelace envisagent déjà une machine dont on pourrait changer les instructions.

## Une machine à laquelle on donne des instructions

Charles Babbage imagine une **machine analytique** capable d’exécuter différentes suites de calculs. Pour lui transmettre les instructions, pas de clavier : il prévoit d’utiliser des cartes perforées, c’est-à-dire des cartes avec des trous que le mécanisme doit lire.[^h1s1-babbage]

![Partie construite de la machine analytique de Babbage, avec ses colonnes de roues et ses axes.](../images/babbage-mecanisme.jpg)
Figure: Modèle d’essai de la machine analytique. © The Board of Trustees of the Science Museum, [Science Museum Group](https://collection.sciencemuseumgroup.org.uk/objects/co62245/babbages-analytical-engine-1834-1871-trial-model), [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Regardez les roues et les axes de ce mécanisme. Les opérations doivent être réalisées par le mouvement de ces pièces. La photographie montre seulement une partie de la machine : l’ensemble ne sera pas achevé du vivant de Babbage.

Pour effectuer un autre calcul, on change les instructions. Pas besoin de reconstruire tous les engrenages à chaque fois, heureusement. 🙂 Les cartes permettent aussi de répéter une suite d’opérations. Si vous avez déjà écrit une boucle dans un programme, vous connaissez le principe.

![Cartes perforées destinées à la machine analytique, avec des trous disposés en lignes et des annotations manuscrites.](../images/babbage-cartes.jpg)
Figure: Cartes pour la machine analytique. © The Board of Trustees of the Science Museum, [Science Museum Group](https://collection.sciencemuseumgroup.org.uk/objects/co62248/punched-cards-for-babbages-analytical-engine), [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

En 1843, Ada Lovelace publie une traduction d’un texte décrivant cette machine, accompagnée de ses propres notes. Elle envisage des usages qui dépassent les calculs habituels, notamment la manipulation de notes de musique.[^h1s1-love]

Imaginons que nous décidions d’associer les nombres de 0 à 6 aux notes do, ré, mi, fa, sol, la et si. La suite `0, 2, 4` représente alors **do, mi, sol**. En ajoutant 1 à chaque nombre, nous obtenons `1, 3, 5`, soit **ré, fa, la**.

Nous avons transformé une suite de notes en effectuant des opérations sur des nombres. En représentant les notes par des nombres, une machine à calculer peut donc manipuler autre chose que des quantités.

Nous sommes encore dans les antécédents de l’informatique. Il faudra d’autres machines et d’autres travaux pour arriver à l’IA.


[^h1s1-babbage]: [Bodleian Libraries, Ada Lovelace and the Analytical Engine](https://blogs.bodleian.ox.ac.uk/adalovelace/2018/07/26/ada-lovelace-and-the-analytical-engine/).
[^h1s1-love]: [Science Museum, Charles Babbage’s Difference Engines and the Science Museum](https://www.sciencemuseum.org.uk/objects-and-stories/charles-babbages-difference-engines-and-science-museum).

## 1943 : des neurones sur le papier

En 1943, Warren McCulloch et Walter Pitts cherchent à décrire des réseaux de neurones avec des mathématiques. Leur modèle simplifie fortement le fonctionnement nerveux : un neurone reçoit des signaux et peut, à son tour, en transmettre un.[^h1s2-mp]

Regardons un exemple. Nous donnons deux entrées à notre neurone et nous fixons son **seuil d’activation** à deux. Il faut donc que les deux entrées lui transmettent un signal pour qu’il s’active.

![À gauche, un seul signal arrive et le neurone reste inactif ; à droite, les deux signaux arrivent et le neurone s’active.](../images/neurone-deux-signaux.png)
Figure: Avec un seuil de deux, une seule entrée active ne suffit pas.

Les `0` et les `1` indiquent l’absence ou la présence d’un signal. Si vous avez utilisé des booléens, vous reconnaîtrez une opération **ET** : la première entrée **et** la deuxième doivent être actives pour obtenir une sortie active.

Le modèle prévoit aussi des entrées **inhibitrices** : lorsqu’elles sont actives, elles bloquent l’activation du neurone.

Ce neurone ne fait pas grand-chose tout seul. Nous sommes encore assez loin de lui demander de faire nos devoirs. 😅 Mais nous pouvons relier sa sortie à d’autres neurones et construire des réseaux qui réalisent plusieurs opérations logiques.

Dans ce modèle, les connexions sont fixées. Le réseau ne découvre pas lui-même comment les modifier à partir d’exemples.


[^h1s2-mp]: [McCulloch et Pitts, A Logical Calculus of the Ideas Immanent in Nervous Activity (1943 ; réédition de 1990)](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf).

## 1950 : peut-on faire passer une machine pour un humain ?

Alan Turing publie en 1950 *Computing Machinery and Intelligence*. Il y examine la question de savoir si les machines peuvent penser, notamment à travers un jeu d’imitation.[^h1s3-turing]

Dans sa présentation courante, le **test de Turing** place une personne face à des interlocuteurs cachés. Elle échange avec eux par écrit et cherche à distinguer la machine de l’humain. Elle ne peut donc pas se fier à une voix ou à un visage.

Imaginez que vous discutiez dans deux fenêtres, sans savoir qui vous répond. Vous pouvez poser des questions et comparer les réponses. Toute la difficulté consiste à décider ce qui vous ferait reconnaître la machine.

Dans le texte original, Turing part d’un jeu où il faut distinguer un homme d’une femme, puis envisage de remplacer l’un des participants par une machine.

Turing s’intéresse aussi à l’apprentissage : il envisage une machine que l’on éduquerait plutôt que de programmer directement toutes les capacités d’un adulte. La question de faire apprendre les machines est donc présente dès cette période.


[^h1s3-turing]: [Alan Turing, Computing Machinery and Intelligence (1950)](https://www.csee.umbc.edu/courses/471/papers/turing.pdf).

## 1956 : le domaine prend un nom

En 1955, John McCarthy, Marvin Minsky, Nathaniel Rochester et Claude Shannon proposent de réunir des chercheurs durant l’été suivant, au Dartmouth College, aux États-Unis. Leur document emploie l’expression *artificial intelligence*, que nous traduisons par **intelligence artificielle**.[^h1s4-dartmouth]

Ils veulent étudier comment faire utiliser le langage à des machines, leur faire résoudre des problèmes et leur permettre de s’améliorer. Les réseaux de neurones figurent aussi dans les pistes proposées.

La rencontre de 1956 devient un événement fondateur du domaine. Les recherches n’ont pas toutes commencé cet été-là, mais elles sont réunies sous un nom et un projet commun.

Le programme est ambitieux : les auteurs espèrent obtenir des avancées en réunissant un petit groupe pendant l’été. Certains de ces problèmes leur résisteront pourtant pendant des décennies.

Il existe déjà plusieurs façons d’aborder ces questions. On peut chercher à représenter des neurones, mais aussi décrire des connaissances et des règles qu’un programme devra appliquer.


[^h1s4-dartmouth]: [McCarthy, Minsky, Rochester et Shannon, proposition du projet de Dartmouth (1955, pour la rencontre de 1956)](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904).

Nous avons rencontré des machines programmables, des neurones décrits par des mathématiques et une proposition pour étudier l’intelligence avec des ordinateurs. À partir des années 1950, ces idées vont donner lieu à des programmes qui jouent, cherchent des démonstrations et dialoguent.
