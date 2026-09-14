La commande `:argdo` exécute la commande donnée sur tous les buffers qui ont donné en argument lors de l'ouverture de Vim. Par exemple si nous ouvrons Vim en faisant `vim fichier.txt text.txt` alors la commande `:agrdo` s'appliquera aux buffers `fichier.txt` et `text.txt`.

[[information]]
| On peut voir la liste des arguments en étant dans Vim avec la commande `:args`

La commande `:argdo` est très similaire à `:bufdo`. La différence entre les deux est que `:argdo` agis **seulement** sur les buffers qui ont donné en argument, là où `:bufdo` va agir sur **tous** les buffers.

[[question]]
| C'est bien d'avoir la liste des buffers ouverts au démarrage de Vim, mais comment faire si je veux modifier cette liste ? Car j'ai pu rouvrir d'autres buffers, ou en fermer certains.

Il est possible de modifier la liste d'argument tout en étant dans Vim. Pour cela nous allons utiliser la commande `:args` (`:h args` pour avoir l'aide).  
Voici comment on l'utilise.

J'ai ouvert Vim en faisant la commande `vim fichier.txt text.txt`. Voici le résultat de la commande `:args`

->![](/media/galleries/11359/58273fad-032f-4bd9-8b8c-36d50d4525f7.png)<-

On observe en bas à gauche la liste des buffers que j'ai donnée en argument. À présent je vais ouvrir le fichier `.zshrc` dans Vim (avec la commande `:e .zshrc`)

Voici donc mes buffers ouverts (`:ls`):

->![](/media/galleries/11359/dd59de5c-2a76-43f3-bcab-e80bbe36f13f.png)<-

J'ai mes 3 buffers ouverts, mais uniquement `fichier.txt` et `text.txt` qui sont présents dans la liste des arguments.

En faisant la commande `:args .zshrc` je vais dire à Vim qu'à présent la liste d'arguments contient **uniquement** le buffer `.zshrc`.

La commande `:args` ne prend pas uniquement des noms de fichier. Nous pouvons composer des commandes plus complexes pour inclure plusieurs fichiers sans écrire le nom de chacun d'eux.

Je peux par exemple faire la commande `:args .*rc` pour inclure tous les fichiers qui commencent par un `.` et qui finissent par `rc` dans la liste d'arguments (cette syntaxe est identique à celle du shell).

Voici la liste des arguments après avoir fait cette commande (en bas à gauche):

->![](/media/galleries/11359/cc012b48-62ee-4417-a261-f9eb3d8c9bcf.png)<-

Notre liste d'arguments contient tous les fichiers de mon répertoire courant qui commencent par un `.` et qui se terminent en `rc`.