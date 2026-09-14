Commençons par un exemple. J'exécute Vim sans argument:

->![](/media/galleries/11359/0f8b2e4a-924f-4e88-a2bc-3f17df4b9dd9.png)<-

Maintenant je vais faire la commande `:sp` (ou `:split`) et voici le résultat:

->![](/media/galleries/11359/d2b002af-810f-4681-93c8-283bd8b44e03.png)<-

Mon buffer a été coupé de manière horizontale. Le buffer du haut et celui du bas sont les mêmes, cependant, j'y ai accès depuis deux fenêtres différentes.

Comme dit au chapitre précédent, comme les buffers sont synchronisés, si vous écrivez du texte dans une des deux fenêtres, ce texte sera aussi présent dans l'autre.

Pour fermer une fenêtre, il suffit d'être dedans et de faire la commande `:q`.

On peut aussi couper une fenêtre dans le sens vertical. Pour cela on utilisera la commande `:vsp` (ou `:vs` ou encore `:vsplit` pour "vertical split").

Voici le résultat de `:vsp`:

->![](/media/galleries/11359/6d9ee841-1f45-4bbe-b53c-fa314eb21a32.png)<-

Tout comme `:sp` mon buffer est coupé en deux de manière verticale, j'ai le même buffer à gauche et à droite.

[[question]]
| C'est bien beau de couper sa fenêtre en plus petite fenêtre, mais comment faire pour s'y rendre ?