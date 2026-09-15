Notre table oublie tout sauf le dernier caractère. Les transformers disposent d’un mécanisme qui permet de combiner des informations venant de plusieurs positions : l’**attention**.

Nous pouvons effectuer ce calcul avec de petits tableaux. Dans `09_attention.py`, nous donnons à quatre positions des vecteurs choisis à la main :

```python
Q = np.array([[1., 0.], [0., 1.], [1., 1.], [1., -1.]])
K = Q.copy()
V = np.array([[1., 0.], [0., 1.], [2., 1.], [1., 2.]])
```

`Q` contient les **requêtes**, `K` les **clés** et `V` les **valeurs**. Une requête est comparée aux clés pour calculer des coefficients ; ces coefficients servent ensuite à combiner les valeurs.[^p2-7-attention-attention]

```python
scores = Q @ K.T / np.sqrt(K.shape[1])
```

Nous masquons les positions futures, puis appliquons une softmax par ligne. Enfin :

```python
resultat = attention @ V
```

Lancez :

```bash
python 09_attention.py
```

```text
Poids d'attention :
[[1.    0.    0.    0.   ]
 [0.33  0.67  0.    0.   ]
 [0.248 0.248 0.503 0.   ]
 [0.266 0.065 0.131 0.539]]
Valeurs combinées :
[[1.    0.   ]
 [0.33  0.67 ]
 [1.255 0.752]
 [1.066 1.273]]
```

Ouvrez `sorties/attention.png` :

![Matrice de quatre lignes et quatre colonnes : chaque position combine seulement sa propre valeur et les valeurs précédentes.](image:images/attention.png)
Figure: Poids calculés à partir des tableaux Q, K et V du programme.

Les zéros au-dessus de la diagonale correspondent aux positions futures. La première position ne peut consulter qu’elle-même. La dernière peut combiner les quatre valeurs. Chaque ligne a une somme égale à un, à l’arrondi près.

Sur la deuxième ligne, les coefficients sont environ `0,330` et `0,670`. Les deux valeurs accessibles sont `[1, 0]` et `[0, 1]`. Leur combinaison donne :

```text
0,330 × [1, 0] + 0,670 × [0, 1] = [0,330, 0,670]
```

C’est la deuxième ligne du tableau « Valeurs combinées ». Les coefficients d’attention indiquent comment mélanger les valeurs ; ils ne sont pas eux-mêmes les valeurs à transmettre.

Essayez maintenant une autre requête. **Après la définition de `V`**, ajoutez cette ligne, avant le calcul de `scores` :

```python
Q[3] = [0., 1.]
```

Nous la plaçons après `K = Q.copy()` pour conserver les clés d’origine. Relancez le programme : la dernière ligne d’attention devient environ `[0.180, 0.365, 0.365, 0.089]`. Les trois autres lignes restent identiques.

Vous venez de changer ce que recherche la dernière position, en conservant les informations qu’elle peut consulter. Retirez ensuite cette ligne pour retrouver le calcul de départ.

Ces vecteurs ne proviennent pas d’un entraînement : nous les avons définis pour faire le calcul. Dans un transformer, des projections apprises produisent notamment les requêtes, clés et valeurs à partir des représentations disponibles. Plusieurs têtes d’attention, des transformations supplémentaires et des informations de position sont combinées dans les couches du modèle.[^p2-7-attention-transformer]

Le masque utilisé ici est **causal** : pour prédire la suite, on ne donne pas au modèle les caractères futurs. D’autres usages, comme l’analyse d’un texte déjà entièrement disponible, peuvent employer une attention sans ce masque.


[^p2-7-attention-attention]: [Dive into Deep Learning, Queries, Keys, and Values](https://d2l.ai/chapter_attention-mechanisms-and-transformers/queries-keys-values.html).

[^p2-7-attention-transformer]: [Vaswani et ses collègues, Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762).
