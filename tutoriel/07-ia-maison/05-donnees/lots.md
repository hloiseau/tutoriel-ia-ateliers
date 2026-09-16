Lancez l’audit :

```bash
python auditer_donnees.py
```

Pour chacun des deux formats, nous avons 180 lignes d’entraînement, 30 de validation et 30 de test. Les identifiants sont répartis avant de fabriquer les fenêtres de caractères : les groupes 10 à 69 servent à l’entraînement, 70 à 79 à la validation et 80 à 89 au test.

Pourquoi cet ordre ? Si nous découpions d’abord une phrase en fenêtres presque identiques, puis les répartissions au hasard, le test pourrait présenter au modèle des morceaux qu’il a déjà vus à un caractère près. Ce serait un examen un peu arrangeant.

L’audit vérifie l’absence de lignes et d’identifiants communs entre les lots. Regardez néanmoins les trois fichiers : ils reprennent les mêmes gabarits. Notre test mesure donc un apprentissage très limité, sur des formes proches.

L’entraînement lit le lot `train`. Pendant le développement, la validation permet d’observer l’évolution et de choisir les réglages. Nous n’ouvrons le test qu’une fois l’essai fixé. Si ses erreurs vous conduisent ensuite à modifier les réglages, il rejoint de fait vos données de développement : prévoyez de nouveaux exemples pour l’évaluation finale.
