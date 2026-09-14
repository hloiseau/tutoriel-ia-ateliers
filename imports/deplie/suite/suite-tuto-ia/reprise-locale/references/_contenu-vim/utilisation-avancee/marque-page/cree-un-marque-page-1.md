Pour créer un marque-page on utilise la commande `m` suivie d'un caractère alphabétique en minuscule ou majuscule.  
On crée donc un marque-page nommé `a` avec la commande `ma`.

En créant notre marque-page, Vim sauvegarde la ligne et la colonne où était notre curseur et le lie au *buffer* dans lequel nous sommes.

On peut aussi utiliser la commande `:mark` néanmoins cette dernière mémorise la colonne à 0 (et non la position du curseur). Pour connaitre la différence complète entre `m` et `:mark` l'aide est à votre disposition (`:h m` et `:h :mark`).

[[information]]
| Vim possède des raccourcis pour les commandes. Par exemple, à la place de la commande `:mark` je peux faire `:m` (la même chose existe avec `:help` et `:h`, faire `:help mark` et `:h m` sera identique).


[[attention]]
| Il y a une différence entre les marque-pages en minuscule et majuscule.  
| Les marque-pages en minuscule sont spécifiques à un fichier contrairement aux marque-pages en majuscules. Cela signifie que les marque-pages en majuscules sont accessibles depuis n'importe quel endroit dans Vim tandis que ceux en minuscule sont accessibles uniquement depuis un *buffer* du fichier dont le marque-page a été créé.

[[information]]
| Vim sauvegarde tous les marque-pages dans le fichier `.viminfo` dans votre répertoire principal.