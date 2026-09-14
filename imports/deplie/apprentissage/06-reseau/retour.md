Les poids de la première couche ont influencé `h`, qui a influencé les scores. Il faut donc faire passer le calcul du gradient par ces deux étapes.

Dans `perte_gradient`, les gradients de la sortie utilisent les valeurs de la couche intermédiaire :

```python
"W2": h.T @ d,
"b2": d.sum(axis=0)
```

Pour revenir vers la première couche :

```python
dh = (d @ p["W2"].T) * (h > 0)
```

Le produit par `W2.T` fait revenir les contributions à travers les poids de sortie. Le masque `(h > 0)` conserve les passages où ReLU était positive et coupe ceux qu’elle avait ramenés à zéro.

Nous obtenons ensuite :

```python
"W1": X.T @ dh,
"b1": dh.sum(axis=0)
```

C’est la **rétropropagation** : les dépendances du calcul permettent de retrouver l’influence des paramètres sur la perte. Nous n’avons pas eu à attribuer manuellement une part de responsabilité à chaque unité.

Dans les bibliothèques comme PyTorch, la différentiation automatique réalise ce travail à partir des opérations enregistrées. Ici, les expressions sont assez courtes pour les écrire et les examiner directement.
