Ouvrez `corpus.txt`. Il contient de courtes phrases sur des animaux, des objets et du code. Ce texte est assez petit pour que vous puissiez le lire entièrement, le modifier et comprendre d’où viennent les exemples.

Dans `08_langage.py`, nous construisons un vocabulaire :

```python
vocabulaire = sorted(set(texte))
vers_id = {c: i for i, c in enumerate(vocabulaire)}
```

Chaque caractère distinct reçoit un numéro. L’espace, le point et le retour à la ligne ont eux aussi un numéro. Notre corpus contient 31 caractères distincts : notre vocabulaire comporte donc **31 tokens**.

Un **token** est une unité choisie pour représenter le texte. Ici, nous avons décidé qu’un token serait un caractère. Un modèle de langage plus grand peut utiliser des morceaux de mots, des mots fréquents, des octets ou d’autres unités. Le numéro d’un token ne désigne pas à lui seul son sens.

Dans un réseau, on associe souvent chaque numéro à un vecteur de nombres, appelé **embedding**. Ce vecteur donne au calcul une représentation modifiable pendant l’entraînement. Nous n’en avons pas besoin pour notre première table de fréquences.

Le choix du découpage compte. Avec des caractères, les séquences sont longues mais le vocabulaire est petit. Avec des morceaux de mots, une même phrase peut utiliser moins de positions, mais la table des tokens est plus grande.
