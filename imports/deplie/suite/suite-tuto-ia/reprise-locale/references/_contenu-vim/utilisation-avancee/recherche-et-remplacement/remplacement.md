Une fonctionnalité très commune aux éditeurs est le remplacement. Dans Vim on utilise la commande `:substitute` (ou `:s`).

[[information]]
| L'aide concernant cette fonctionnalité s'ouvre avec la commande `:h substitute`.

La commande s'utilise de la manière suivante:

```
:[range]s/{pattern}/{string}/[flag] [count]
```

[[information]]
| Ici j'utilise le séparateur `/` (c'est la caracrère par défaut). Si l'on travaille avec des `/` dans `{pattern}` ou dans `{string}` il peut être utile d'utiliser un autre séparateur comme par exemple `#`.  
| Cela donnerait :
|
| ```
| :[range]s#{pattern}#{string}#[flag] [count]
| ```
| 
| Le séparateur peut être quelconque, on peut utiliser celui que l'on veut.

Nous allons décortiquer les éléments de la commande.

# Range

`[range]` correspond a l'intervalle sur lequel nous allons appliquer la substitution.  
Par exemple `10,15` correspond à l'intervalle de la ligne 10 à la ligne 15. On peut aussi remplacer `[range]` par `%` pour appliquer l'intervalle sur tout le fichier.

[[information]]
| Le range peut être bien plus complexe. La commande `:h range` vous permettra de consulter sa documentation.

Si aucun intervalle n'est précisé la commande substitute s'applique uniquement sur la ligne du curseur.

# Pattern

Le pattern est le motif que l'on recherche et qui va être remplacé. Il fonctionne de la même manière que lors de la recherche avec `:vimgrep`.

[[information]]
| La documentation complète sur les motifs de recherche peut être obtenue avec la commande `:h pattern`.

# String

`{string}` est le texte qui remplacera `{pattern}`. Le plus souvent on met seulement tu texte simple, et on peut utiliser des expressions bien plus complexes.

[[information]]
| Les détails sur les expressions de remplacement sont dans la documentation, accessible avec `:h sub-replace-special`.

# Flags

Les flags permettent d'ajouter des options à la commande de substitution.

[[information]]
| Une liste exhaustive des flags disponibles dans Vim est disponible dans la documentation (`:h s_flags`).

Voici quelques options:

| Option | Action |
|:------:|:-------|
| `c` | Permet de confirmer chaque substitution |
| `g` | Remplace toutes les occurrences d'une ligne. Sans cette option seulement la première occurrence de la ligne est changée |
| `i` | Ignore la case (ne fait pas de différence entre les majuscules et les minuscules) |

# Count

`[count]` permet de répéter la substitution plusieurs fois. Ce doit être un nombre positif. S'il n'est pas renseigné la substitution n'est faite qu'une seule fois.

[[information]]
| La documentation de `[count]` se fait avec la commande `:h count`.

Lorsque `[count]` est combiné avec `[range]` la commande de substitution est exécutée `[count]` fois depuis la dernière ligne de l'intervalle.  
Par exemple la commande:
```
:15s/toot/pouet/g 3
```
sera équivalente à la commande:
```
:15,17s/toot/pouet/g
```