# 3. Faire apprendre le modèle

[Sommaire de la partie](../README.md) · [Sources](.)

Le modèle se trompe sur un trois. Nous pourrions lui dire « non, c’est un trois », mais il faut traduire cette correction en calculs. Quels poids faut-il changer ? Et de combien ?

## Mesurer ce qui ne va pas

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

## Trouver dans quel sens déplacer les poids

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

## Lancer les mises à jour

Lancez :

```bash
python 03_entrainer.py
```

Le programme mélange les indices d’entraînement, traite les images par lots de 64, puis recommence. Un passage sur toutes les images d’entraînement s’appelle une **epoch**. Nous en effectuons 80.

Voici les lignes obtenues. De chaque côté de la barre oblique, vous retrouvez l’entraînement puis la validation :

```text
0 | perte 2.2987 / 2.2985 | exactitude 10.3% / 10.3%
 20 | perte 0.3363 / 0.3716 | exactitude 94.6% / 95.0%
 40 | perte 0.2290 / 0.2651 | exactitude 95.7% / 95.0%
 60 | perte 0.1853 / 0.2213 | exactitude 96.4% / 95.0%
 80 | perte 0.1600 / 0.1973 | exactitude 97.2% / 95.0%
Calcul : 0.107 s ; modèle : sorties/lineaire.npz
```

La ligne zéro montre l’état avant les mises à jour. À la ligne 80, la perte d’entraînement a beaucoup diminué et 97,2 % des images d’entraînement sont bien classées. La validation est à 95,0 %.

Ouvrez `sorties/lineaire-courbes.png` :

![Courbes mesurées de perte et d’exactitude pour l’entraînement et la validation du modèle linéaire.](../images/lineaire-courbes.png)
Figure: Les courbes sont calculées sur les mêmes groupes après chaque passage d’entraînement.

Regardez le graphique de droite : le résultat de validation reste souvent à 95 %, alors que sa perte continue à diminuer. Certaines probabilités s’améliorent sans changer le chiffre choisi. C’est pourquoi les deux mesures racontent des choses différentes.

Le programme a écrit `sorties/lineaire.npz`. Ce fichier contient les poids et les biais. `sorties/lineaire.json` contient les réglages, la durée du calcul et les valeurs des courbes.

Essayez maintenant un entraînement plus court, en conservant le premier modèle :

```bash
python 03_entrainer.py --epochs 20 --nom court
```

Vous obtenez `court.npz` et ses propres courbes. Comparez-les à celles de `lineaire`. Le nom différent empêche d’écraser notre premier résultat.

Chaque lancement repart de l’initialisation. Cette commande ne prolonge pas l’entraînement du modèle précédent.

## Regarder ce qui a changé

L’image du trois qui était mal reconnue avant l’entraînement reçoit maintenant une probabilité de 99,4 % pour la classe trois.

![La même image de trois, avec les probabilités avant et après entraînement.](../images/avant-apres.png)
Figure: Comparaison sur une image appartenant à l’entraînement.

Pour écrire les graphiques de comparaison et les cartes des poids, lancez :

```bash
python 11_figures.py
```

Ouvrez `sorties/poids.png`. Les 64 poids de chaque chiffre y sont rangés en une grille de 8 × 8 :

![Dix cartes de poids appris, une pour chaque score de chiffre. Les valeurs positives sont bleues et les négatives rouges.](../images/poids.png)
Figure: Poids du modèle linéaire. Un pixel clair placé sur une zone bleue augmente le score correspondant ; sur une zone rouge, il le diminue.

Ce ne sont pas dix photographies mémorisées. Ce sont les coefficients utilisés dans nos multiplications. Certaines positions favorisent un chiffre, d’autres le défavorisent.

Le modèle a maintenant une manière de séparer les classes à partir de ces positions. Il n’a pas pour autant appris que « deux boucles superposées font un huit », ni que déplacer un chiffre devrait conserver son identité.

Les paramètres ont été ajustés à partir des images et des réponses attendues. Nous pouvons mesurer la progression, sauvegarder le résultat et le regarder. Il reste à vérifier ce que cette progression vaut sur d’autres images.
