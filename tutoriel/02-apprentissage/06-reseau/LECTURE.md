# 6. Ajouter une couche… et voir ce que cela change

[Sommaire de la partie](../README.md) · [Sources](.)

Notre modèle linéaire additionne les contributions des pixels. Il n’a pas de couche intermédiaire capable de transformer leur combinaison avant de calculer les dix scores.

Ajoutons-en une. Nous pourrons comparer le résultat, mais aussi vérifier si davantage de paramètres suffit à mieux reconnaître les chiffres.

## Une transformation entre l’image et les scores

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

## Faire revenir l’erreur à travers la couche

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

## Entraîner puis comparer

Lancez le réseau avec un nom différent :

```bash
python 03_entrainer.py --cachee 32 --nom reseau
```

```text
0 | perte 2.4407 / 2.4398 | exactitude 3.5% / 3.9%
 20 | perte 0.1352 / 0.1843 | exactitude 96.9% / 95.0%
 40 | perte 0.0750 / 0.1365 | exactitude 98.7% / 96.4%
 60 | perte 0.0499 / 0.1169 | exactitude 99.4% / 96.7%
 80 | perte 0.0365 / 0.1102 | exactitude 99.5% / 96.4%
Calcul : 0.211 s ; modèle : sorties/reseau.npz
```

Ouvrez `sorties/reseau-courbes.png` :

![Courbes d’apprentissage du réseau à une couche intermédiaire de 32 unités.](../images/reseau-courbes.png)
Figure: Même découpage de données, mêmes 80 epochs et même pas que pour le modèle linéaire.

Le réseau atteint 99,5 % sur l’entraînement, contre 97,2 % pour le modèle linéaire. Sur la validation, il finit à 96,4 %. La progression sur les données d’entraînement est donc plus forte que sur les données restées à part.

Nous conservons ces réglages et faisons son bilan :

```bash
python 04_evaluer.py --nom reseau
```

```text
Test : 345/360 réponses correctes (95.8%)
```

Eh oui : sur ce test, nous obtenons le même nombre de bonnes réponses qu’avec le modèle linéaire. 😅 Les erreurs ne sont pas nécessairement les mêmes, mais les deux modèles en font quinze.

Nous avons fixé cette comparaison à deux configurations. Continuer à essayer des tailles de couche jusqu’à dépasser 95,8 % sur ce test reviendrait à choisir nos paramètres en fonction de lui.

Vous pouvez utiliser le réseau pour votre dessin :

```bash
python 05_lire_dessin.py dessin.json --nom reseau
```

Comparez les réponses et les scores. Un modèle plus gros peut aider sur certains dessins, se tromper sur d’autres, et demander davantage de calcul. La taille seule ne tranche pas la question.

## Apprendre les mauvaises réponses

Faisons une expérience un peu désagréable pour le modèle : nous prenons 80 images d’entraînement et nous leur attribuons des étiquettes au hasard. Un trois pourra être déclaré sept, puis un autre trois sera déclaré deux.

```bash
python 07_memoriser.py
```

Ce script crée son propre réseau de 64 unités intermédiaires. Il ne remplace aucun des modèles sauvegardés.

```text
0 | étiquettes arbitraires apprises : 8.8% | vrais chiffres de validation : 11.1%
200 | étiquettes arbitraires apprises : 100.0% | vrais chiffres de validation : 3.9%
400 | étiquettes arbitraires apprises : 100.0% | vrais chiffres de validation : 3.3%
600 | étiquettes arbitraires apprises : 100.0% | vrais chiffres de validation : 3.3%
800 | étiquettes arbitraires apprises : 100.0% | vrais chiffres de validation : 3.3%
```

Ouvrez `sorties/memorisation.png` :

![Le réseau atteint cent pour cent sur quatre-vingts étiquettes arbitraires, tandis que son résultat sur les vrais chiffres de validation reste très mauvais.](../images/memorisation.png)
Figure: L’entraînement utilise les étiquettes tirées au hasard ; la validation conserve les véritables chiffres.

Le réseau a réussi à reproduire les réponses arbitraires des 80 exemples. Il n’a pas découvert une bonne façon de reconnaître les chiffres. Il a disposé de suffisamment de paramètres et de mises à jour pour mémoriser des associations qui ne l’aident pas sur la validation.

C’est une manière de rendre visible la différence entre **mémoriser les exemples** et **généraliser**. Dans un projet réel, le surapprentissage n’est pas toujours aussi spectaculaire. Il peut apparaître comme une perte d’entraînement qui continue à diminuer alors que la validation se dégrade.

Nous pouvons agir sur la quantité et la qualité des données, la taille du modèle, la durée de l’entraînement ou la régularisation. Mais aucune de ces options ne remplace le besoin de regarder les résultats hors entraînement.

Les exemples et leurs étiquettes font partie du comportement appris. Si la cible est mal définie, le programme peut très bien optimiser ce qu’on lui a demandé tout en produisant quelque chose d’inutile.

Nous avons construit un réseau à plusieurs couches et fait circuler le gradient à travers ses calculs. Il sait apprendre davantage de détails ; certains sont utiles, d’autres permettent seulement de mémoriser. Les données à part servent à voir la différence.
