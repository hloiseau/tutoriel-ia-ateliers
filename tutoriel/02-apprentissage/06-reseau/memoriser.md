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

![Le réseau atteint cent pour cent sur quatre-vingts étiquettes arbitraires, tandis que son résultat sur les vrais chiffres de validation reste très mauvais.](image:images/memorisation.png)
Figure: L’entraînement utilise les étiquettes tirées au hasard ; la validation conserve les véritables chiffres.

Le réseau a réussi à reproduire les réponses arbitraires des 80 exemples. Il n’a pas découvert une bonne façon de reconnaître les chiffres. Il a disposé de suffisamment de paramètres et de mises à jour pour mémoriser des associations qui ne l’aident pas sur la validation.

C’est une manière de rendre visible la différence entre **mémoriser les exemples** et **généraliser**. Dans un projet réel, le surapprentissage n’est pas toujours aussi spectaculaire. Il peut apparaître comme une perte d’entraînement qui continue à diminuer alors que la validation se dégrade.

Nous pouvons agir sur la quantité et la qualité des données, la taille du modèle, la durée de l’entraînement ou la régularisation. Mais aucune de ces options ne remplace le besoin de regarder les résultats hors entraînement.

Les exemples et leurs étiquettes font partie du comportement appris. Si la cible est mal définie, le programme peut très bien optimiser ce qu’on lui a demandé tout en produisant quelque chose d’inutile.
