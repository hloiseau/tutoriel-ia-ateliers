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

![Courbes d’apprentissage du réseau à une couche intermédiaire de 32 unités.](image:images/reseau-courbes.png)
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
