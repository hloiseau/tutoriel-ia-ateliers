Vim permet de lire depuis un autre fichier et d'injecter dans le fichier courant. Pour cela on utilise la commande `:read`.

[[information]]
| `:h inserting-file` pour obtenir la documentation.

La commande `:read` s'utilise en spécifiant un nom de fichier.

```
:read /path/to/file.txt
```

La commande ci-dessus va lire le fichier `file.txt` dans le répertoire `/path/to/` et ajouter son contenu à partir de la ligne en dessous du curseur.

On peut préciser un numéro de ligne afin que le contenu soit ajouté à partir de la ligne choisie. Par exemple:

```
:10read /path/to/file.txt
```

[[attention]]
| La commande insert le contenu **entier** du fichier spécifier à partir de la ligne 10 **dans le buffer en cours d'édition**.

[[information]]
| On peut aussi utiliser un intervalle (range) avant la commande `read`

`:read` permets aussi d'injecter depuis le résultat de la console. Pour cela, à la place de préciser un nom de fichier on met un `!` suivi de la commande shell que l'on souhaite exécuter.  
Par exemple `:read !ls` insérera le contenu de mon répertoire courant dans le buffer ouvert. Ou encore `:read !env` y insérera toutes les variables d'environnement ainsi que leur valeur.

[[neutre | Insérer une partie d'un fichier]]
| Si l'on souhaite uniquement insérer une partie du fichier on peut utiliser `:read` avec une commande shell comme [`sed`](https://en.wikipedia.org/wiki/Sed "sed - Wikipedia"). On peut par exemple faire `:read !sed -n 10,15p /path/to/file.txt` pour ajouter les lignes 10 à 15 dans notre buffer courant.