# 2. Des pixels à une première réponse

[Sommaire de la partie](../README.md) · [Sources](.)

Pour reconnaître un chiffre, nous allons calculer un score pour chaque possibilité : zéro, un, deux… jusqu’à neuf. Le score le plus élevé donnera notre choix.

Il faut d’abord décider comment calculer ces scores. Nous commencerons avec des multiplications et des additions.

## Ce que fait un poids

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

## Transformer les scores en probabilités

Les scores peuvent être positifs ou négatifs. Nous les passons à une fonction appelée **softmax**, qui produit des nombres positifs dont la somme vaut un.[^p2-2-softmax-softmax]

```python
def softmax(scores):
    decales = scores - scores.max(axis=1, keepdims=True)
    e = np.exp(decales)
    return e / e.sum(axis=1, keepdims=True)
```

`np.exp` calcule l’exponentielle de chaque score. Nous divisons ensuite ces valeurs par leur somme. La soustraction du maximum empêche les exponentielles de devenir inutilement grandes ; elle ne change pas les probabilités obtenues.

`axis=1` signifie « séparément pour chaque ligne », donc pour chaque image. Sans cette précision, nous risquerions de mélanger les résultats de plusieurs images.

Le modèle peut ainsi attribuer `0,60` au trois, `0,25` au huit et répartir les `0,15` restants sur les autres chiffres. Pour choisir une classe, nous prenons la position de la plus grande valeur :

```python
chiffre = probas.argmax()
```

Un score de 60 % est une probabilité **calculée par le modèle**. Ce n’est pas automatiquement la garantie que 60 % des dessins ayant ce score seront bien reconnus. Pour savoir si les scores correspondent aux fréquences de réussite, il faudrait aussi étudier leur calibration.


[^p2-2-softmax-softmax]: [Dive into Deep Learning, Softmax Regression](https://d2l.ai/chapter_linear-classification/softmax-regression.html).

## Lancer le modèle avant l’apprentissage

Exécutez :

```bash
python 02_predire.py
```

```text
Étiquette attendue : 3
Probabilités : [0.099 0.099 0.104 0.099 0.092 0.103 0.102 0.097 0.102 0.102]
Classe choisie : 2
Paramètres : 650
Exactitude avant entraînement : 10.3%
```

Le chiffre attendu est un trois. Le modèle choisit un deux. Ses probabilités sont toutes proches d’un dixième : les poids viennent d’être tirés au hasard, il n’a encore reçu aucune correction.

Les 10,3 % de bonnes réponses ne sont donc pas une panne. Avec dix classes assez équilibrées, une règle naïve ou un choix au hasard peut déjà obtenir un résultat de cet ordre. C’est un point de comparaison, pas un objectif.

Ouvrez `02_predire.py`. Remplacez :

```python
index = train[0]
```

par :

```python
index = train[1]
```

Relancez le programme. Nous avons changé l’image, pas les paramètres. Le score peut bouger, mais le modèle n’apprend rien en exécutant cette prédiction.

Vous pouvez conserver cette modification ou remettre `train[0]` pour retrouver l’exemple du trois. Le script d’entraînement choisit ses propres lots et ne dépend pas de ce changement.

Nous avons une première chaîne complète : une image devient des scores, puis des probabilités, puis un chiffre choisi. Elle fonctionne, mais les réponses sont mauvaises. Il manque un moyen de corriger les paramètres.
