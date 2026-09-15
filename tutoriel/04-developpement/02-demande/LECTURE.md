# 5. Décider ce que le ticket veut changer

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** une phrase de ticket cache parfois plusieurs comportements. Nous allons les mettre à plat avant de toucher à la fonction.

## Une remise en stock n’est pas une baisse de prix

Le ticket PRIX-1 demande de ne plus notifier un produit qui revient simplement en stock. Le fichier `TICKET.md` donne la règle complète : une notification est autorisée seulement si le produit est disponible dans le nouvel état **et** si son prix a strictement baissé par rapport à l’observation précédente.

Les prix sont des entiers en centimes. Nous comparons deux observations consécutives, dans une même devise implicite. Il n’est pas question de retrouver le prix le plus bas des six derniers mois ni de calculer une promotion.

Avant de regarder la suite, répondez à ces deux cas :

- Le produit revient en stock au même prix. Faut-il notifier ?
- Le produit revient en stock avec un prix plus bas. Faut-il notifier ?

Le premier cas doit donner **faux**, le second **vrai**. « Ne plus notifier une remise en stock » ne veut donc pas dire « ignorer tous les produits qui étaient indisponibles ». Une baisse de prix peut accompagner le retour en stock.

C’est exactement le genre de raccourci qu’il faut éclaircir dans un vrai ticket. Si personne n’a décidé comment traiter le second cas, l’agent ne devrait pas choisir discrètement à la place de l’équipe.

## Écrire la table avant les tests

Voici les cas que nous voulons distinguer :

| Ancien état | Nouvel état | Notification attendue |
| --- | --- | --- |
| 20 €, disponible | 15 €, disponible | Oui |
| 15 €, disponible | 20 €, disponible | Non |
| 20 €, disponible | 15 €, indisponible | Non |
| 20 €, indisponible | 20 €, disponible | Non |
| 20 €, indisponible | 15 €, disponible | Oui |
| 20 €, indisponible | 25 €, disponible | Non |
| 20 €, disponible | 20 €, disponible | Non |
Table: Les situations que la règle doit départager

Les trois premières correspondent déjà à nos tests de départ. Les suivantes rendent visible ce que ces tests ne contrôlaient pas.

Vous pouvez demander à l’agent de proposer cette table avant de coder les tests. Relisez alors les **résultats attendus**, pas seulement le nombre de lignes. Une longue suite de tests qui attend la mauvaise réponse reste une longue suite de tests qui attend la mauvaise réponse.

Pour une règle aussi petite, faire la table soi-même prend peu de temps. Dans un projet plus grand, l’aide peut surtout servir à retrouver les cas oubliés ou à traduire une règle déjà décidée en scénarios exécutables.

## Délimiter le changement

Ajoutons quelques limites simples à notre travail : nous conservons la fonction `notifier`, les fichiers JSON et les validations existantes. Nous n’ajoutons pas de base, d’envoi de courriel ou de système de préférences.

Pourquoi le préciser ? Parce qu’une demande d’« amélioration des notifications » pourrait facilement produire une architecture plus ambitieuse que notre besoin. Ici, le programme doit continuer à prendre deux états et à renvoyer une décision.

Les limites ne sont pas seulement des interdictions à adresser à l’agent. Elles nous servent aussi pendant la revue. Si un nouveau fichier de configuration apparaît, nous pourrons demander quel comportement du ticket le rend nécessaire.

Dans votre propre travail, gardez ce périmètre à la taille de la tâche. Un correctif d’une condition n’exige pas automatiquement un document de conception de dix pages. Il exige en revanche que les cas ambigus aient une réponse.


