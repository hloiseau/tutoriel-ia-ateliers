Le ticket PRIX-1 demande de ne plus notifier un produit qui revient simplement en stock. Le fichier `TICKET.md` donne la règle complète : une notification est autorisée seulement si le produit est disponible dans le nouvel état **et** si son prix a strictement baissé par rapport à l’observation précédente.

Les prix sont des entiers en centimes. Nous comparons deux observations consécutives, dans une même devise implicite. Il n’est pas question de retrouver le prix le plus bas des six derniers mois ni de calculer une promotion.

Avant de regarder la suite, répondez à ces deux cas :

- Le produit revient en stock au même prix. Faut-il notifier ?
- Le produit revient en stock avec un prix plus bas. Faut-il notifier ?

Le premier cas doit donner **faux**, le second **vrai**. « Ne plus notifier une remise en stock » ne veut donc pas dire « ignorer tous les produits qui étaient indisponibles ». Une baisse de prix peut accompagner le retour en stock.

C’est exactement le genre de raccourci qu’il faut éclaircir dans un vrai ticket. Si personne n’a décidé comment traiter le second cas, l’agent ne devrait pas choisir discrètement à la place de l’équipe.
