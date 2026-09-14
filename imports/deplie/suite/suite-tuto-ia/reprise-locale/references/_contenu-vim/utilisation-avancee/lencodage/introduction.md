En informatique les fichiers texte ont un [encodage pour les caractères](https://fr.wikipedia.org/wiki/Codage_des_caractères). On peut voir ça comme le *langage* que l'ordinateur doit utiliser pour lire le fichier texte et nous l'afficher correctement sur l'écran.

Vim permet d'ouvrir des fichiers de multiples encodages. Quand tout se passe bien, nous n'avons pas besoin de préciser à Vim quel encodage utiliser.

Dans le cas où votre fichier n'est pas affiché correctement c'est que l'encodage qu'il a choisi n'est probablement pas celui avec lequel le fichier a été écrit.  
Pour connaître quel est l'encodage que Vim utilise pour lire le fichier on utilise la commande: `:set encoding`

Dans le cas où on veut choisir l'encodage que Vim doit utiliser pour lire le fichier on utilise la commande `:set encoding="utf-8"` (pour choisir de lire le fichier avec l'encodage UTF-8).

[[attention]]
| Il ne faut pas confondre `encoding` et `fileencoding`. `fileencoding` correspond à l'encodage du fichier sur le disque, tandis `encoding` est l'encodage que Vim utilise pour lire le fichier et l'utiliser.  
| Si les deux variables ont une valeur différente Vim fera la conversion lui-même.

Si l'on veut changer l'encodage du fichier, on utilisa la commande `:set fileencoding="utf-8"` (pour écrire le fichier sur le disque avec l'encodage UTF-8) puis on sauvegarde (avec la commande `:w`).

[[information]]
| L'aide de ces commandes s'obtient avec `:h fileencoding` et `:h encoding`