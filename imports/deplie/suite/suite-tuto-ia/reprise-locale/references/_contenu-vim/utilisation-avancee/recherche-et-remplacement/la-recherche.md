# Chercher dans un fichier

Nous avons évoqué la recherche dans un fichier dans un des premiers chapitres avec `/`.

Ce que l'on cherche avec la commande `/` est un motif (*patten* en anglais (`:h pattern`)).  
Les motifs peuvent être très complexes grâce aux [expressions régulière](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re) et permettent des recherches très poussées.

La recherche de base avec `/` est sensible à la casse. Cela signifie que `/chat` ne sera pas égale à `Chat` dans le texte.  
Pour change ce comportement on peut ajouter `set ignorecase` à notre `.vimrc`.  
À présent la commande `/Chat` sera considérée comme égale à `chat`.  
On peut aussi ajouter l'option `set smartcase` (au `.vimrc`) afin de prendre en compte la casse s'il y a des majuscules dans le texte que l'on cherche.  
Avec ces deux options ensemble `/chat` sera égale à `chat`, `Chat` ou encore `CHAT`, mais `/Chat` sera égale uniquement à `Chat`.

Les éléments dans le fichier correspondant au motif cherché peuvent être mis en valeur avec l'option `set showmatch`. Cela aura pour effet de les surligner.

[[information]]
| L'usage de `/` fait une recherche du début vers la fin du fichier. Il est possible de faire l'inverse en utilisant `?` de la même manière que `/`. En utilisant `?` on ira au match précédent avec `n` et au suivant avec `N` (à l’inverse de `/`).

[[information]]
| Si l'on se trouve sur un mot, on peut (en mode normal) utiliser `*` pour parcourir les occurrences de ce dernier du début vers la fin et `#` pour les parcourir dans l'ordre inverse.

# Chercher dans plusieurs fichiers

Lorsque l'on édite des fichiers, il est rare que l'on n'en édite qu'un seul. Il est donc indispensable d'avoir une fonction qui permet de rechercher dans plusieurs fichiers.

[[information]]
| L'aide complète à ce sujet est disponible avec la commande `:h grep`.

Vim possède plusieurs commandes pour faire une telle recherche:

- `:vimgrep`
- `:lvimgrep`
- `:grep`
- `:lgrep`

Ces quatre commandes s'utilisent de la même manière.

```
:<command> {pattern} {file}
```

> Les commandes sont en réalité plus complexes, ici nous n'allons évoquer un usage simple de ces dernières.

`{pattern}` correspond au motif que l'on recherche. Il peut être très simple comme très complexe pour des recherches très poussées avec les expressions régulières.

`{file}` correspond au motif de fichier dans lesquels on va chercher le `{pattern}`. Il peut lui aussi être une expression régulière pour chercher dans certains fichiers très spécifiques.

## Les différentes commandes

### `:vimgrep`

Cette commande fait la recherche au sein de Vim et place les résultats correspondant dans la *quickfix list* qu'il ouvre dans une fenêtre.

### `:lvimgrep`

Cette commande fait la recherche au sein de Vim et place les résultats correspondant dans *location list* qu'il ouvre dans une fenêtre.

### `:grep`

Cette commande fait la recherche en utilisant la commande shell `grep` et place les résultats correspondant dans la *quickfix list* qu'il ouvre dans une fenêtre.

### `:lgrep`

Cette commande fait la recherche en utilisant la commande shell `grep` et place les résultats correspondant dans *location list* qu'il ouvre dans une fenêtre.


[[information]]
| Nous verrons dans la section suivante à quoi correspondent la *location list* et la *quickfix list*.

La liste remplie contiens les résultats qui correspondent au modèle que l'on cherche. Pour ouvrir et fermer la fenêtre contenant la liste on utilise la commande `:cw` pour la *quickfix list* et `:lw` pour la *location list*.