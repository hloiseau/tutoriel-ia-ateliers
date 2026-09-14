# Le buffer

Le buffer est celui qui est le plus utilisé. Il est relié à un nom de fichier qui est celui utiliser lorsque l'on écrit ce dernier

# Le [No Name] buffer

Ce [No Name] buffer est présent lorsque vous exécutez Vim sans argument. Si vous apportez des modifications à ce buffer et essayez de quitter ou de sauvegarder vous aurez une erreur. Il faut soit quitter sans sauvegarder (`:q!`) ou sauvegarder le fichier en lui donnant un nom (`:w <nom_du_fichier>`).

# Le scratch buffer

Le scratch buffer ressemble fortement au [No Name] buffer. Sa vocation est d'être jeté. C'est pourquoi si vous modifiez ce buffer et que vous quittez, Vim ne vous préviendra pas qu'il y a des modifications non sauvegardé. Il quittera et les modifications seront perdu.  
Néanmoins, il est possible de sauvegarder les contenus de ce buffer avec la commande `:w <nom_du_fichier>`.