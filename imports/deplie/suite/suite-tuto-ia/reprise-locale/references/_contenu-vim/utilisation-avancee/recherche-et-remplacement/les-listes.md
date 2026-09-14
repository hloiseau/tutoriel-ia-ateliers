# Jump list

Lorsque l'on déplace le curseur dans Vim, par exemple avec la commande `G`, ce dernier que nous avons réalisé un saut. Vim enregistre les 100 derniers sauts réalisés dans la *jump list*.  
Tous les mouvements (*motions*) sont considérés comme des sauts.

On utilise la commande `Ctrl` + `o` pour sauter en arrière et `Ctrl` + `i` pour sauter en avant.  
Pour lister les sauts réalisés on utilise la commande `:ju`.

[[information]]
| L'aide sur la *jump list* est accessible avec la commande `:h jumplist`.

# Quickfix list

La *quickfix list* est souvent utilisée pour stocker les localisations qui doivent être réparées rapidement. Par exemple les erreurs du compilateur, les warnings, les messages du linter, ...  
Cette liste est globale à l'instance de Vim. Cela veut dire que l'on utilise toujours la même dans toutes les autres fenêtres. 

On utilise la commande `:cw` pour ouvrir ou fermer la fenêtre contenant la *quickfix list*.  
Une fois la fenêtre ouverte, on choisit la localisation où nous allons nous déplacer. En appuyant sur `Enter` on saute à l'endroit indiquer. (Pour revenir en arrière on utilise donc la commande `Ctrl`+`o`)

[[information]]
| L'aide au sujet de la *quickfix list* peut-être obtenus avec la commande `:h quickfix`

# Location list

La *location list* est similaire à la *quickfix list*, cependant la *location list* n'est pas globale à Vim. Elle dépend de la fenêtre.

On utilise la commande `:lw` pour ouvrir ou fermer la fenêtre contenant la *location list* de la fenêtre dans laquelle on se trouve.

[[information]]
| L'aide concernant la *location-list* est obtenue en faisant la commande `:h location-list`.

# Change list

De la même manière que Vim liste les derniers déplacements, il liste aussi les derniers changements. Ils sont stockés dans la *change list*.

On ouvre la *change list* avec la commande `:changes`. Cette liste est reliée à la fenêtre dans laquel se trouve le curseur.  
Pour aller au changement précédent on utilise la commande `g;` et `g,` pour aller au changement suivant. On peut préfixer ces commandes d'un nombre pour remonter ou descendre de plusieurs changements en une fois.

[[information]]
| La documentation de la *change list* s'obtient avec la commande `:h changelist`.