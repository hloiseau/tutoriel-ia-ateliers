Le mode ligne de commande permet l'exécution de commandes par sa propre invite de commande.

Pour activer ce mode on utilise la touche `:`. Pour retourner en mode normal il faut faire `Esc` ou presser `Enter` pour exécuter la commande.

Nous avons déjà utilisé certaines commandes telles que `:w`, `:q` que vous connaissez. On peut aussi utiliser par exemple `:x` qui est l'équivalent de `:wq` qui sauvegarde le fichier et quitte.

Il existe un grand nombre de commandes.

- `:pwd` → Affiche le répertoire dans lequel Vim a été ouvert.
- `:help` → Ouvre un viewport sur l'aide de Vim (essayez la commande `:h vim-modes` et faites `:q` pour quitter).
- `:history` → Ouvre l'historique des commandes, pressez `q` pour quitter.

Je ne vais pas toutes les énumérer ici. J'en présenterai d'autres lorsque nous en aurons besoin.

On peut aussi taper `q:` en mode normal (à ne pas confondre avec `:q` !) qui ouvre une fenêtre avec l'historique des commandes. On peut éditer les commandes déjà faites ainsi qu'exécuter la commande sur la ligne sur laquelle est le curseur en pressant `Enter`. Ceci est particulièrement utile lorsque nous allons écrire de longues commandes. Pour quitter sans exécuter de commande, on quitte simplement la fenêtre avec `:q`.

Nous avons la possibilité d'exécuter des commandes pour notre shell directement dans Vim avec `:!`. Par exemple `:! ls` nous listera les fichiers du répertoire où nous avons ouvert Vim.