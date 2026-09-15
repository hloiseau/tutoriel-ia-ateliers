Ouvrez `usage-exemple.csv`. Nous y avons placé deux appels fictifs pour comprendre le calcul, avec trois catégories **qui ne se recouvrent pas** :

| Appel | Entrée hors cache | Entrée lue en cache | Sortie |
| --- | --- | --- | --- |
| 1 | 1 000 | 0 | 100 |
| 2 | 200 | 1 000 | 100 |
Table: Un exemple inventé de compteurs, pas les mesures d’un modèle

Dans cet exemple, le second appel réutilise une partie du contexte. Pour chaque catégorie, le calcul est `tokens × prix par million / 1 000 000`. Nous additionnons ensuite les catégories et les appels.

Avec des tarifs eux aussi fictifs, lancez :

```bash
python mesurer.py usage-exemple.csv --prix-entree 2 --prix-cache 0.2 --prix-sortie 8
```

Le résultat est `0.004200` unités monétaires. Passez ensuite `--prix-cache` à `2` : le coût devient `0.006000`. Vous venez de changer la tarification d’une catégorie, pas le nombre de tokens ni la qualité de la réponse.

Ce calcul simplifié ne couvre pas une écriture de cache facturée séparément, un outil payant ou un abonnement. Pour l’utiliser sur vos données, adaptez les colonnes à la facture concernée. Il n’est pas nécessaire d’avoir une précision au millionième pour décider si l’outil vous sert ; elle nous permet ici de vérifier une petite formule sans arrondir trop tôt.
