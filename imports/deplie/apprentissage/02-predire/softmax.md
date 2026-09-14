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
