Prenons la probabilité attribuée à la bonne réponse. Si l’image représente un trois et que le modèle lui donne une probabilité de `0,9`, nous voulons une petite erreur. S’il lui donne `0,01`, nous voulons une erreur beaucoup plus grande.

Nous utilisons la **perte logarithmique**, ici l’entropie croisée pour une classe attendue :

```python
perte = -np.log(probabilite_de_la_bonne_classe)
```

| Probabilité de la bonne classe | Perte, arrondie |
| ---: | ---: |
| 0,9 | 0,105 |
| 0,1 | 2,303 |
| 0,01 | 4,605 |

Cette perte tient compte de l’assurance de la mauvaise réponse. Deux modèles peuvent choisir le mauvais chiffre tout en n’étant pas aussi éloignés de la bonne réponse.

Dans `perte_gradient`, le code calcule directement les logarithmes à partir des scores décalés. Cela évite de prendre le logarithme d’une probabilité arrondie à zéro par la machine. `np.arange(len(y))` fournit les numéros des lignes, et `y` indique la colonne attendue pour chacune.

```python
perte = -log_p[np.arange(len(y)), y].mean()
```

La moyenne donne une perte pour le lot entier. L’**exactitude**, elle, compte seulement les réponses dont la classe choisie est correcte. Nous conserverons les deux mesures.
