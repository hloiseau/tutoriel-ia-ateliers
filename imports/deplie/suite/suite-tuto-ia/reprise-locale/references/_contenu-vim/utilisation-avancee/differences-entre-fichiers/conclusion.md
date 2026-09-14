Ici nous avons vu comment comparer deux fichiers. Mais Vim peut nous mettre en évidence jusqu'à 4 fichiers en même temps.

[[attention | On sait maintenant:]]
| - Afficher les différences entre deux fichiers:
|   - avec `vim -d <file_1> <file_2>` ou `vimdiff  <file_1> <file_2>`
|   - avec un fichier en faisant `:diffsplit <file_2>`
|   - en ouvrant les deux fichiers et en faisant `:diffthis` dans chaque buffer
| - Intégrer rapidement les différences:
|   - avec `:diffget` ou `:diffput`
|   - avec les raccourcis clavier `do` et `dp`
|   - avec la commande `[range]diff{get|put} [bufspec]`
| - Mettre à jour les différences entre deux fichiers avec `:diffupdate`