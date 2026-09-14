Imaginons que nous regardions seulement trois pixels d’une image. Ils valent `1`, `0,5` et `0`. Pour calculer un score, nous leur associons les poids `0,2`, `−0,4` et `0,7`, puis nous ajoutons un nombre de départ, appelé **biais**, égal à `0,1`.

```text
score = 1 × 0,2 + 0,5 × (−0,4) + 0 × 0,7 + 0,1
score = 0,1
```

Le deuxième pixel fait baisser le score : son poids est négatif. Le troisième ne contribue pas ici, puisqu’il vaut zéro. Le biais ajoute une valeur même lorsque tous les pixels sont noirs.

Dans notre véritable modèle, nous faisons ce calcul avec les 64 pixels, et nous le répétons pour chacun des dix chiffres. Nous avons donc 64 × 10 poids et dix biais, soit **650 paramètres**.

Dans `modele.py`, la version sans couche intermédiaire commence ainsi :

```python
return {"W": rng.normal(0, 0.01, (64, 10)), "b": np.zeros(10)}
```

`W` est un tableau de 64 lignes et dix colonnes. Une colonne contient les poids d’un chiffre. `b` contient les dix biais. Les poids sont initialisés avec de petites valeurs aléatoires ; les biais commencent à zéro.

Calculons les scores pour un lot d’images :

```python
scores = X @ p["W"] + p["b"]
```

Le symbole `@` effectue une **multiplication de matrices**. Il condense les produits et les additions que nous venons de faire à la main. Avec 64 images en entrée, les dimensions sont :

```text
X : 64 images × 64 pixels
W : 64 pixels × 10 chiffres
scores : 64 images × 10 chiffres
```

Le premier `64` est la taille du lot ; le second est le nombre de pixels. Ils sont égaux ici par choix, mais ce sont deux choses différentes. Nous pourrions traiter 12 images à la fois sans changer le nombre de poids.
