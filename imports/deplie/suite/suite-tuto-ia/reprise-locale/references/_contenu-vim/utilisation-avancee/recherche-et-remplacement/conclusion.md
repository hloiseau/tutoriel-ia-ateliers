La recherche est dans Vim est très puissante et permet de chercher avec des expressions régulières.  
Vim utilise les listes pour stocker ce dont il a besoin et nous pouvons les réutiliser comme bon nous semble.  
La syntaxe pour le remplacement est proche d'autres outils (comme [sed](https://fr.wikipedia.org/wiki/Sed_(Unix))) et peut utiliser des expressions régulières.

[[attention | On sait maintenant:]]
| - Chercher:
|   - dans un fichier avec `/`
|   - dans plusieurs fichiers avec `vimgrep`, `lvimgrep`, `grep`, ou `lgrep`
| - Les listes:
|   - La `jump list`: qui est la liste des déplacements du curseur
|   - La `quickfix list`: elle est utilisée pour accéder rapidement à des changements *rapides*
|   - La `location list`: est identique à la `quickfix list` mais dépend de la fenêtre
|   - La `change list`: qui est la liste des derniers changements
| - Les remplacements avec la forme `:[range]s/{pattern}/{string}/[flag] [count]`