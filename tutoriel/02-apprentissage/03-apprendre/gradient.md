Imaginons maintenant que nous augmentions un poids d’une toute petite quantité. Si la perte augmente aussi, nous avons intérêt à partir dans l’autre sens. Si elle diminue, nous avons trouvé une direction utile, au moins près de notre point de départ.

Le **gradient** rassemble ces indications pour les paramètres. Nous n’allons pas essayer séparément chaque poids à chaque étape : les dérivées du calcul permettent de les obtenir ensemble.

Pour la combinaison softmax et entropie croisée, le point de départ est particulièrement court :

```python
d = np.exp(log_p)
d[np.arange(len(y)), y] -= 1
d /= len(y)
```

`d` commence avec les probabilités. Nous retirons un dans la colonne de la bonne réponse, puis divisons par la taille du lot. Pour une image dont la réponse attendue est trois, cette colonne contient donc `probabilité_du_trois − 1`.

Faisons le calcul pour une seule image et trois classes. Supposons que les probabilités soient `[0.2, 0.5, 0.3]` et que la classe attendue soit la deuxième. Après avoir retiré un à cette deuxième case, nous obtenons :

```text
d = [0.2, -0.5, 0.3]
```

Le lot ne contient qu’une image, donc la division par sa taille ne change rien. Avec trois pixels valant `[1, 0.5, 0]`, chacun multiplie cette ligne pour contribuer aux gradients :

| Pixel | Vers la première classe | Vers la bonne classe | Vers la troisième classe |
| ---: | ---: | ---: | ---: |
| 1 | 0,2 | −0,5 | 0,3 |
| 0,5 | 0,1 | −0,25 | 0,15 |
| 0 | 0 | 0 | 0 |

Prenons le poids qui relie le premier pixel à la bonne classe. Son gradient vaut `−0,5`. Avec un pas de `0,2`, la mise à jour lui ajoute `0,1`, puisque `−0,2 × (−0,5) = 0,1`. Sur cette image, le pixel contribue alors davantage au score de la bonne réponse.

Le troisième pixel, nul, ne fait modifier aucun de ses poids pendant cette mise à jour. Avec plusieurs images, leurs contributions sont moyennées.

Dans le modèle linéaire, les gradients des poids et des biais sont alors :

```python
gradients = {"W": X.T @ d, "b": d.sum(axis=0)}
```

`X.T` échange les lignes et les colonnes de `X`. Chaque pixel contribue à l’ajustement des poids auxquels il participe. Un pixel toujours égal à zéro dans un lot ne fournit aucune contribution au gradient de ces poids.

La mise à jour se fait ensuite dans `03_entrainer.py` :

```python
for nom in p:
    p[nom] -= args.pas * gradients[nom]
```

Le **pas d’apprentissage** règle la taille du déplacement. Nous utilisons `0.2`. Ce nombre est choisi par nous, contrairement aux poids qui sont ajustés par l’entraînement : c’est un **hyperparamètre**.

Un pas trop petit peut demander beaucoup de mises à jour. Un pas trop grand peut faire osciller le modèle ou augmenter la perte. Le signe moins indique que nous cherchons à descendre la perte, mais il ne garantit pas qu’un déplacement immense soit une bonne idée.
