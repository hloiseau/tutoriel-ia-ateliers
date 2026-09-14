Nous choisissons une couche intermédiaire de 32 unités. Dans `modele.py`, le calcul devient :

```python
h = np.maximum(0, X @ p["W1"] + p["b1"])
scores = h @ p["W2"] + p["b2"]
```

La première multiplication transforme les 64 pixels en 32 valeurs. `np.maximum(0, ...)` remplace les valeurs négatives par zéro et conserve les autres. Cette fonction d’activation est appelée **ReLU**.

Les 32 valeurs obtenues servent ensuite d’entrée au calcul des dix scores. La softmax finale reste la même.

| Tableau | Dimensions | Paramètres |
| --- | --- | ---: |
| `W1` | 64 × 32 | 2 048 |
| `b1` | 32 | 32 |
| `W2` | 32 × 10 | 320 |
| `b2` | 10 | 10 |
| Total | | 2 410 |

Pourquoi ajouter ReLU ? Si nous enchaînions seulement deux transformations linéaires avec leurs biais, nous pourrions les regrouper en une seule transformation du même type. La non-linéarité permet au réseau de construire d’autres séparations.[^p2-6-couche-mlp]

La couche est dite **cachée** parce que ses valeurs ne sont ni nos pixels d’entrée ni nos réponses attendues. Elle n’est pas inaccessible : `h` est un tableau que nous pouvons afficher, enregistrer et examiner comme les autres.


[^p2-6-couche-mlp]: [scikit-learn, réseaux de neurones supervisés](https://scikit-learn.org/1.8/modules/neural_networks_supervised.html).
