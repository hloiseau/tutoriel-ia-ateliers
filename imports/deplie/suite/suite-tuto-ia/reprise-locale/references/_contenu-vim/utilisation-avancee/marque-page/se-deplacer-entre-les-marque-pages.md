# Se déplacer à un marque-page spécifique

Pour se déplacer à un marque-page spécifique on utilise une des commandes suivantes:

- `'{marque-page}` (ex: `'E`)
- `` `{marque-page} `` (ex: `` `E ``)

En utilisant la commande avec `'` on se déplace au début de la ligne de notre marque-page. Si l'on veut aller directement à la colonne de notre marque-page on utilise à la place `` ` ``.

# Se déplacer entre les marque-pages du buffer

On utilise les commandes `]'` et `['` pour aller au marque-page suivant et précédent de notre buffer. Ici aussi, on peut remplacer `'` par `` ` `` pour se déplacer directement à la colonne du marque-page.  
Ces commandes peuvent être précédées d'un opérateur. Par exemple `5]'` sera l'équivalent de faire 5 fois la commande `]'`.