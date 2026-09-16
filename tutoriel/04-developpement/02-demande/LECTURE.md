# 3. Décider ce que le ticket veut changer

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Installer l’assistant et observer le problème](../installer/LECTURE.md) · [Suivant : Faire apparaître le bug dans un test](../03-tests/LECTURE.md)

**TL;DR** — Le ticket donne une règle courte, mais plusieurs combinaisons de prix et de disponibilité. Nous allons décider leur résultat avant de toucher à la fonction.

## Une remise en stock n’est pas une baisse de prix

Le ticket PRIX-1 demande de ne plus notifier un produit qui revient simplement en stock. Le fichier `TICKET.md` donne la règle complète : une notification est autorisée seulement si le produit est disponible dans le nouvel état **et** si son prix a strictement baissé par rapport à l’observation précédente.

Les prix sont des entiers en centimes. Nous comparons deux observations consécutives, dans une même devise implicite. L’historique des six derniers mois et le calcul d’une promotion restent hors du programme.

Avant de regarder la suite, répondez à ces deux cas :

- Le produit revient en stock au même prix. Faut-il notifier ?
- Le produit revient en stock avec un prix plus bas. Faut-il notifier ?

Le premier cas doit donner **faux**, le second **vrai**. Le titre du ticket, pris tout seul, pourrait faire écarter les deux retours en stock. La règle complète conserve pourtant celui qui s’accompagne d’une baisse.

Ce genre de raccourci arrive vite dans un vrai ticket. Si l’équipe n’a pas décidé comment traiter le second cas, il faut lui poser la question ; laisser l’agent trancher en silence transformerait une supposition en règle métier.

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

Vous pouvez demander à l’agent de proposer cette table avant de coder les tests. Relisez surtout les **résultats attendus**. Dix tests persuadés qu’une hausse mérite une alerte ne rendraient pas cette idée plus juste. 😅

Pour une règle aussi petite, faire la table soi-même prend peu de temps. Dans un projet plus grand, l’aide devient intéressante pour retrouver les voisins d’un cas principal ou traduire une règle déjà décidée en scénarios exécutables.

## Délimiter le changement

Ajoutons quelques limites simples à notre travail : nous conservons la fonction `notifier`, les fichiers JSON et les validations existantes. Nous n’ajoutons pas de base, d’envoi de courriel ou de système de préférences.

Pourquoi le préciser ? Parce qu’une demande d’« amélioration des notifications » pourrait facilement produire une architecture plus ambitieuse que notre besoin. Ici, le programme doit continuer à prendre deux états et à renvoyer une décision.

Ces limites guideront aussi notre revue. Si un nouveau fichier de configuration apparaît dans le diff, nous pourrons demander quel comportement du ticket le rend nécessaire.

Dans votre propre travail, gardez ce périmètre à la taille de la tâche. Une condition à corriger mérite que l’on tranche ses cas ambigus ; elle réclame rarement un document de conception de dix pages.



---

[Précédent : Installer l’assistant et observer le problème](../installer/LECTURE.md) · [Suivant : Faire apparaître le bug dans un test](../03-tests/LECTURE.md)
