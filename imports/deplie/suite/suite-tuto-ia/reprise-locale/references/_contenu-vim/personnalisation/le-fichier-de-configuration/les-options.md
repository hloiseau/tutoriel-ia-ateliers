Vim possède beaucoup d'options. On accède à la documentation des options avec la commande `:help options`.

Pour définir une option on utilise `set`.  
Dans votre fichier `.vimrc` cela prend la forme suivante:

```vimrc
set number " Display line numbers
```

[[information]]
| Avec Vim, tout ce qui suit un `"` est un commentaire. Il est présent à titre informatif pour la personne qui lit le fichier et est ignorée par l'ordinateur. Pour la documentation complète sur les commentaires, tapez `:h comment`.

On peut supprimer une option en préfixant l'option de `no` comme suit:

```vimrc
set nonumber " Remove line numbers
```

La commande `:set` est bien plus complexe, si vous souhaitez en voir toutes les fonctionnalités je vous invite à lire la documentation de Vim avec la commande `:help set`.

À présent, nous allons voir certaines options et leurs utilisations.

```vimrc
set background=black     " Utilise des couleurs de texte en fonction d'un fond foncé
set expandtab            " Convertis les caractères tabulation en espace
set foldmethod=indent    " Plis sur le niveau d'indentation (`:help foldmethod` pour plus d'informations)
set hlsearch             " Surligne le résultat de la recherche
set incsearch            " Recherche incrémentale
set ignorecase           " Ignore la case pendant la recherche
set smartcase            " Ignore l'option `ignorecase` si la recherche contient une majuscule
set mouse=n              " Active la souris seulement en mode Normal et Terminal
set nocompatible         " Rend Vim non compatible avec Vi
set number               " Affiche les numéraux de ligne
set showmatch            " Surligne la parenthèse, le crochet, ou accolade paire duquel le curseur se situe
set textwidth=140        " Définit la longueur de la ligne à 140 caractèrs
set wildmenu             " Affiche les options disponibles en mode ligne de commande
```

C'est une liste non exhaustive des options disponibles.

Pour avoir des informations à propos d'une option on utilise la commande `:help`. Par exemple, `:help wildmenu` affichera l'aide complète.

[[information]]
| Pour recharger les modifications du fichier `.vimrc` sans quitter puis rouvrir Vim, on peut utiliser la commande `:source ~/.vimrc`