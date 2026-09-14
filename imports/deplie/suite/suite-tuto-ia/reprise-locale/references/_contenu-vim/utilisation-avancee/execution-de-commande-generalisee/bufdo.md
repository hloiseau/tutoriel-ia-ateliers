Nous avons vu dans le chapitre sur les buffers que quand Vim *ouvre* un fichier, il ne l'ouvre pas vraiment. Vim nous montre une copie du fichier que l'on écrit sur le disque lors de la sauvegarde.

En interne de son fonctionnement, Vim garde une liste des buffers que sont ouverts.  
C'est la commande `:bufdo` (qui est suivi d'une autre commande) qui permet d'exécuter la commande donnée en argument dans chaque buffer de la liste.  
Cela permet de faire `:bufdo <command>`, plutôt que de faire `:<command>` puis `:bn` pour passer au buffer suivant, on réexécuter notre commande `:<command>, puis on passe au buffer suivant `:bn`, ...

Par exemple, on peut faire `:bufdo w` pour écrire tous les buffers dans leurs fichiers respectifs.

[[information]]
| Nous l'avons vu dans un chapitre précédent, mais nous pouvons accomplir le même résultat avec la commande `:wa`

Ici notre exemple est très simple. Nous voulons simplement écrire les buffers. Mais cette commande (`:bufdo`) peut-être aussi utilisée pour exécuter des commandes bien plus complexes.