Vim permet de créer ses propres raccourcis clavier avec des actions que nous choisissons.

Pour cela dans le `.vimrc` nous allons utiliser la syntaxe suivante:

```vimrc
map {lhs} {rhs}
```

Lorsque la séquence de touches `{lhs}` sera effectuée au clavier la commande `{rhs}` sera effectuée. Voici un exemple concret:

```vimrc
map <C-w>t :tabnew<CR>
```

Ici, faire `Ctrl+w` suivi de `t` aura pour effet d'exécuter la commande `:tabnew` qui ouvre un nouvel onglet.

> On note le `<CR>` à la fin de la commande. Il a pour effet de valider la commande, s'il n'est pas présent vous vous trouverez en mode `ligne commande` avec `:tabnew` d’écrit. Il vous faudra valider en cliquant sur `Entrée` pour que la commande s'exécute.

N'oublions pas que Vim est un éditeur modal. C'est pourquoi Vim permet de définir des raccourcis clavier seulement pour certains modes. De plus, il existe plusieurs modes pour les raccourcis (ex: `:help noremap`  ;) ).

[[information]]
| Pour accéder à l'aide sur le mapping des touches, il faut utiliser la commande `:h key-mapping`.