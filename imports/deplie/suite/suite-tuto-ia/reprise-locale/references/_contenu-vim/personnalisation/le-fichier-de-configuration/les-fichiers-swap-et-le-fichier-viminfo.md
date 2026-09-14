# Les fichiers swap

Vous avez peut-être remarqué que lorsque vous éditez des fichiers avec Vim, ce dernier créé un fichier caché au même nom avec l'extension `.swp`. Par exemple si je suis en train d'éditer le fichier `file.txt` Vim crée le fichier `.file.txt.swp` à côté du fichier édité. Ce fichier swap est celui dans lequel Vim enregistre les changements que nous faisons.

[[information]]
| On utilise la commande `:h swap-file` pour obtenir l'aide à ce sujet.

Il est possible de définir un répertoire dans lequel Vim stockera les fichiers swap. Cela permet de ne pas polluer le répertoire courant. Pour cela on définit la variable `dir` dans le `.vimrc`.

```vimrc
set dir=~/.tmp
```

À présent vous constaterez que les fichiers swap se situeront dans le répertoire `.tmp` dans votre home.  
Je vous invite à essayer et à utiliser la commande `:sw` (ou `:swapname`) pour voir où se situe le fichier swap du fichier en cours d'édition.

---

Vous avez peut-être déjà vu ce message:

->![](/media/galleries/11359/c7f5a785-2a36-4f28-b0aa-7f749256ba16.png)<-

Ici Vim nous indique que le fichier qu'on essaye d'ouvrir possède déjà un fichier swap. Cela peut vouloir dire que quelqu'un est déjà en train d'éditer le fichier ou bien que le fichier a été fermé de manière inattendue. Il nous propose donc les actions à faire selon notre choix.

[[information]]
| Si vous éditez un fichier dont le fichier `.swp` existe déjà alors vim en créera un nouveau avec l'extension `.swo` (puis `.swn`, `.swm`...)

Dans le cas d'un fichier corrompu par une fermeture du programme non voulu on préférera utiliser l'option `Recover` (il faudra possiblement supprimer le fichier swap manuellement après avoir édité le fichier). Pour plus d'informations sur le fonctionnement de la restauration des fichiers je vous invite à taper la commande `:h recover`.

Si vous ne voulez pas de fichier swap, il est possible de mettre l'option `set noswapfile` dans votre `.vimrc`.

# Le fichier viminfo

Ce fichier permet de sauvegarder des informations lorsque vous redémarrez Vim. Il permet notamment de sauvegarder l'historique des commandes, les dernières recherches faites, les buffers, ...

Pour retrouver la documentation sur le sujet, la commande est `:h viminfo`.

Il se trouve par défaut sous `$HOME/.viminfo` sous Linux et macOS et sous `$HOME\_viminfo` sous windows.