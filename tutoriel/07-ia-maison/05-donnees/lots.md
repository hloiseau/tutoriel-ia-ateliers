Lancez l’audit :

```bash
python auditer_donnees.py
```

Pour chacun des deux formats, nous avons 180 lignes d’entraînement, 30 de validation et 30 de test. Les identifiants sont répartis avant de fabriquer les fenêtres de caractères : les groupes 10 à 69 servent à l’entraînement, 70 à 79 à la validation et 80 à 89 au test.

Pourquoi cet ordre ? Si nous découpions d’abord une phrase en fenêtres presque identiques, puis les répartissions au hasard, le test pourrait présenter au modèle des morceaux qu’il a déjà vus à un caractère près. Ce serait un examen un peu arrangeant.

L’audit vérifie l’absence de lignes et d’identifiants communs entre les lots. Il ne rend pas pour autant notre test difficile : les mêmes gabarits restent présents dans les trois lots. Nous mesurons donc un apprentissage très limité, sur des formes proches.

L’entraînement lit le lot `train`. La validation sert à observer l’évolution et à choisir les réglages lors du développement. Le test est lu séparément, une fois l’essai fixé. Si vous adaptez vos réglages après avoir étudié ses erreurs, prévoyez ensuite de nouveaux exemples pour l’évaluation finale.
