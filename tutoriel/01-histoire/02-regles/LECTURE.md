# 2. Des règles pour raisonner

[Sommaire de la partie](../README.md) · [Sources](.)

Un ordinateur peut exécuter des instructions. Pourrait-il aussi utiliser des connaissances pour trouver lui-même les étapes d’une solution ? Dans les années 1950 et 1960, cette question occupe une place importante dans les recherches sur l’IA.

## Décrire ce que le programme sait

En 1956, Allen Newell et Herbert Simon décrivent la *Logic Theory Machine*, associée au projet Logic Theorist. Le système est conçu pour chercher des démonstrations en logique symbolique.[^h2s1-logic]

Le mot **symbolique** signifie ici que le programme manipule des représentations explicites : des objets, des relations, des propositions. Donnons-lui un fait et une règle :

- le programme sait que **Mina est un chat** ;
- il dispose de la règle **si un animal est un chat, alors c’est un mammifère** ;
- il peut en déduire que **Mina est un mammifère**.

Nous lui avons donné un fait et une règle. Il les a combinés pour obtenir un nouveau fait. Nous pouvons ensuite ajouter d’autres règles et continuer les déductions.

![Un fait sur Mina et une règle sur les chats permettent de déduire que Mina est un mammifère.](../images/deduction.png)
Figure: À partir du fait et de la règle, le programme déduit que Mina est un mammifère.

La difficulté augmente lorsqu’il existe plusieurs règles applicables et de nombreuses étapes possibles. Le programme doit alors choisir les pistes à explorer. Le projet de Newell et Simon utilise des **heuristiques**, c’est-à-dire des méthodes pour guider cette recherche.

Une heuristique ressemble à un conseil pratique : « commence par les possibilités qui semblent les plus utiles ». Elle évite parfois beaucoup d’essais, mais ne garantit pas à elle seule de trouver la meilleure solution.

Le rapport de 1956 décrit le système et ses méthodes ; il faut distinguer cette description du détail de son exécution sur un ordinateur.


[^h2s1-logic]: [Newell et Simon, The Logic Theory Machine (1956)](https://www.rand.org/pubs/papers/P868.html).

## Les échecs : connaître les règles ne suffit pas

Claude Shannon étudie dès 1950 comment programmer un ordinateur pour jouer aux échecs. Le jeu fournit un terrain bien défini : on connaît les pièces, les coups autorisés et les conditions de fin de partie.[^h2s2-shannon]

Pour choisir un coup, on peut examiner les réponses possibles de l’adversaire, puis nos réponses à ces réponses. Le problème est que les possibilités se multiplient très vite.

Imaginons que chaque position n’offre que trois choix :

![Un arbre de possibilités passe de trois choix à neuf, puis à vingt-sept en trois étapes.](../images/arbre-recherche.png)
Figure: Trois choix à chaque étape donnent 3, puis 9, puis 27 possibilités au niveau suivant. Ce ne sont pas des nombres mesurés sur une partie d’échecs.

Chaque petit cercle en bas peut encore ouvrir de nouvelles branches. Vous voyez pourquoi « il suffit de tout essayer » risque de prendre un peu de temps. 🙂

Shannon propose de limiter la recherche et d’évaluer les positions obtenues. Le programme peut, par exemple, tenir compte des pièces disponibles et de leur disposition. Il cherche ainsi un coup intéressant sans calculer toute la partie à l’avance.

Les recherches sur les jeux vont continuer pendant des décennies. Elles réunissent des questions qui concernent aussi d’autres problèmes : représenter une situation, prévoir les conséquences d’une action et choisir avec des ressources limitées.


[^h2s2-shannon]: [Claude Shannon, Programming a Computer for Playing Chess (1950)](https://www.computerhistory.org/chess/doc-431614f453dde/).

## 1966 : discuter avec ELIZA

Au MIT, Joseph Weizenbaum développe ELIZA, qu’il décrit dans un article de 1966. Le programme utilise des règles pour analyser des fragments de phrases et préparer ses réponses. Son célèbre script DOCTOR reprend la forme d’un entretien où l’interlocuteur est invité à développer ce qu’il vient de dire.[^h2s3-eliza]

Pour imaginer ce fonctionnement, prenons un échange fictif, inspiré de ce principe :

> **Vous :** Je suis inquiet pour mon travail.  
> **Programme :** Depuis quand êtes-vous inquiet pour votre travail ?

Le programme peut repérer une forme de phrase, récupérer une partie du texte et la réutiliser dans un modèle de réponse. Il n’a pas besoin de connaître votre métier pour produire cette relance.

Essayez maintenant de remplacer « mon travail » par « mon grille-pain ». La même transformation reste possible, même si la conversation devient assez étrange. 😅

Cet exemple montre comment quelques règles peuvent donner une impression de dialogue. ELIZA est plus élaboré que notre unique transformation, mais il ne fonctionne pas comme les grands modèles de langage actuels : ses réponses reposent sur des scripts et des mécanismes de traitement du texte.

On peut donc faire apparaître des phrases dans une conversation par des moyens très différents. L’interface ressemble parfois à celle d’un outil récent, alors que le programme derrière elle n’a pas du tout la même organisation.


[^h2s3-eliza]: [Joseph Weizenbaum, ELIZA (1966)](https://cse.buffalo.edu/~rapaport/572/S02/weizenbaum.eliza.1966.pdf).

Les programmes symboliques obtiennent des résultats en s’appuyant sur des connaissances explicites et des règles. Cela permet de suivre certaines de leurs déductions, mais demande aussi de leur décrire le monde dans lequel ils doivent travailler.

Pendant que ces recherches avancent, d’autres équipes cherchent à faire ajuster le comportement des machines à partir d’exemples.
