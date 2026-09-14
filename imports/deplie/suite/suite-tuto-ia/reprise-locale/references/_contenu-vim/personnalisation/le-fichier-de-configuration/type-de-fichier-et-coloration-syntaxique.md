Vim est capable de détecter quel est le type de fichier que vous éditez. Pour cela il regarde l'extension du nom du fichier ou bien en lis une partie.  
Déterminer le type de fichier permet d'activer l'événement `FileType` qui peut être utilisé pour activer des options, des actions automatiques (à voir dans la section suivante).

Pour activer la reconnaissance de fichier, on utilise la commande `:filetype on` ou bien dans le `.vimrc` ajoutez la ligne `filetype on`.

[[information]]
| Pour avoir l'aide on utilise la commande `:h filetype`.

Pour quoi quel type de fichier Vim a détecté on utilise la commande `:set filetype?`.  
Il est possible que Vim se trompe sur le type de fichier détecter. Pour définir le type de fichier on utilise la commande `:set filetype=<type_du_fichier>`. Par exemple pour définir le type de fichier sur python on ferait `:set filetype=python`.

Vous l'aurez sûrement remarqué, Vim à une fonctionnalité de coloration syntaxique. Cela lui permet dont d'afficher le contenu du fichier sous différentes formes ou couleurs.

[[information]]
| L'aide à se sujet se trouve en faisant `:h syntax`.

Ce sujet est très vaste. Je ne vais pas développer tout son fonctionnement.

Pour activer la coloration syntaxique on utilise la commande `:syntax on` (et `:syntax off`) pour la désactiver. Pour rendre ce choix persistant, dans le `.vimrc` on ajoute `syntax on` (ou `syntax off`).