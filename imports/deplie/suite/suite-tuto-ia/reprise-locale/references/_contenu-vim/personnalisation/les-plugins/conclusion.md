Les plugins sont un vaste sujet et permettent une grande extensibilité du logiciel.  
Ici nous n'avons vu qu'une partie de la surface du sujet.

Il est possible que vos besoins de fonctionnalité soient conséquents. Cependant, un plugin étant généralement un fichier, il peut être difficile à maintenir et à partager avec le temps, s'il devient trop gros en ajoutant de multiples fonctionnalités. Pour pallier ce problème viennent les packages.

[[attention | On sait maintenant:]]
| - Où placer les fichiers de plugin pour qu'ils soient pris en compte au démarrage de Vim (`~/.vim/plugin/`)
| - Les plugins peuvent être spécifiques en fonction des types de fichiers (`~/.vim/ftplugin/<filetype>/file.vim`)