Ouvrez `usage-exemple.csv`. Il contient deux appels fictifs répartis dans trois catégories disjointes :

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

Le résultat est `0.004200` unités monétaires. Passez ensuite `--prix-cache` à `2` : le coût devient `0.006000`. Seul le tarif de la lecture du cache a changé ; le CSV contient toujours les mêmes tokens et ne dit rien de la qualité des réponses.

Une écriture de cache facturée séparément, un outil payant ou un abonnement demanderait d’autres colonnes. Adaptez-les à la facture concernée avant d’utiliser vos propres données. L’affichage à six décimales sert ici à vérifier la formule sans arrondir trop tôt ; dans un bilan réel, choisissez une précision adaptée à la décision.
