Vim a pour but de nous rendre toujours plus rapide. Pour y arriver il nous propose un système d'abréviation.  
On définit les abréviations dans le `.vimrc` avec la syntaxe suivante:

```vimrc
abbr ms Microsoft
ab lx GNU/Linux
abbreviate mac MacOS
```

À présent, lorsque vous écrirez `ms` dans Vim suivi d'un espace, cela sera tout de suite remplacé par `Microsoft`.

> Dans Vim, pour voir quelles abréviations existent, on utilise la commande `:abbr` (ou `:ab` ou encore `:abbreviate`). Une liste des abréviations disponible apparaitra alors à l'écran.

Tout comme les raccourcis clavier, il est possible de définir les abréviations seulement pour certains modes.  

[[information]]
| Pour lire l'aide détaillé à ce sujet on utilise la commande `:h abbreviation`.