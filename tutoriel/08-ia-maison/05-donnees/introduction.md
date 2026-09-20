**TL;DR** — Nous quittons SmolLM2 pour un réseau de caractères assez petit pour être entraîné sur CPU. Avant de toucher à ses poids, nous séparons les données d’entraînement, de validation et de test.

Les réponses précédentes venaient du modèle local de la partie 3. Pour observer un entraînement sans carte graphique, nous passons maintenant à un autre réseau, beaucoup plus petit : son code tient dans un fichier et nous pourrons recommencer les essais autant que nécessaire.
