En 1956, Allen Newell et Herbert Simon décrivent la *Logic Theory Machine*, associée au projet Logic Theorist. Le système est conçu pour chercher des démonstrations en logique symbolique.[^h2s1-logic]

Le mot **symbolique** signifie ici que le programme manipule des représentations explicites : des objets, des relations, des propositions. Donnons-lui un fait et une règle :

- le programme sait que **Mina est un chat** ;
- il dispose de la règle **si un animal est un chat, alors c’est un mammifère** ;
- il peut en déduire que **Mina est un mammifère**.

Nous lui avons donné un fait et une règle. Il les a combinés pour obtenir un nouveau fait. Nous pouvons ensuite ajouter d’autres règles et continuer les déductions.

![Un fait sur Mina et une règle sur les chats permettent de déduire que Mina est un mammifère.](image:images/deduction.png)
Figure: À partir du fait et de la règle, le programme déduit que Mina est un mammifère.

La difficulté augmente lorsqu’il existe plusieurs règles applicables et de nombreuses étapes possibles. Le programme doit alors choisir les pistes à explorer. Le projet de Newell et Simon utilise des **heuristiques**, c’est-à-dire des méthodes pour guider cette recherche.

Une heuristique ressemble à un conseil pratique : « commence par les possibilités qui semblent les plus utiles ». Elle évite parfois beaucoup d’essais, mais ne garantit pas à elle seule de trouver la meilleure solution.

Le rapport de 1956 décrit le système et ses méthodes. Il ne fournit cependant pas le journal détaillé d’une exécution sur un ordinateur ; restons-en à ce qu’il documente.


[^h2s1-logic]: [Newell et Simon, The Logic Theory Machine (1956)](https://www.rand.org/pubs/papers/P868.html).
