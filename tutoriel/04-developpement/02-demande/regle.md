Le ticket PRIX-1 demande de ne plus notifier un produit qui revient simplement en stock. Le fichier `TICKET.md` donne la règle complète : une notification est autorisée seulement si le produit est disponible dans le nouvel état **et** si son prix a strictement baissé par rapport à l’observation précédente.

Les prix sont des entiers en centimes. Nous comparons deux observations consécutives, dans une même devise implicite. L’historique des six derniers mois et le calcul d’une promotion restent hors du programme.

Avant de regarder la suite, répondez à ces deux cas :

- Le produit revient en stock au même prix. Faut-il notifier ?
- Le produit revient en stock avec un prix plus bas. Faut-il notifier ?

Le premier cas doit donner **faux**, le second **vrai**. Le titre du ticket, pris tout seul, pourrait faire écarter les deux retours en stock. La règle complète conserve pourtant celui qui s’accompagne d’une baisse.

Ce genre de raccourci arrive vite dans un vrai ticket. Si l’équipe n’a pas décidé comment traiter le second cas, il faut lui poser la question ; laisser l’agent trancher en silence transformerait une supposition en règle métier.
