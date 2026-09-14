-> [![](/media/galleries/11359/218d493b-34ec-471e-8818-473aa3311f20.png)](https://fr.wikipedia.org/wiki/Macro-commande) <-

Les macros sont souvent vu comme quelque chose de complexe. Une macro c'est *simplement* une suite de commandes que l'on met dans une boîte pour réutiliser ces commandes quand on le souhaite.  
On peut voir une macro comme une *métafonction* que l'on a définie.

# Créer une macro

Le principe est d'enregistrer les commandes dans la macro lors des premières modifications que nous souhaitons répéter.

Pour créer une macro on commence par se placer à l'endroit où nous voulons effectuer les modifications.  
Ensuite nous faisons `q` (en mode Normal) suivi d'un registre (une lettre en minuscule ou un chiffre). À ce moment, en bas à gauche vous verrez `recording @{r}` (`{r}` est le registre dans lequel nous enregistrons les commandes de la macro), cela signifie que les commandes que nous faisons à présent seront enregistrées. Lorsque nous avons fini nos modifications on represse `q` pour arrêter l'enregistrement de la macro.

Voici la structure de la syntaxe pour enregistrer une macro:
```
q{registre}{commandes}q
```

[[information]]
| Les registres dans lesquels nous enregistrons les macros sont les mêmes que les 26 registres nommés.  
| (cf. Perfectionnement → Les registres (Registers) → Les 26 registres nommés)

# Exécuter une macro

Maintenant que nous avons créé notre macro il ne nous reste plus qu'à l'utiliser.  
Pour cela on fait `@{r}` (`{r}` étant le registre dans lequel notre macro a été enregistrée).

On peut précéder l'appel à la macro par un nombre. Ce sera le nombre de fois que la macro sera exécutée.  
Par exemple faire `4@g` exécutera 4 fois la macro dans le registre `g`.

[[information]]
| On peut faire `@@` pour réexécuter la dernière macro exécutée.

[[information | Le caractère @]]
| Vim nous permet de réexécuter la dernière commande en faisant `@:`.  
| Par exemple si on fait `:tabnew` on ouvre un nouvel onglet. Faire `3@:` est équivalent à faire `:tabnew` 3 fois.

# Modifier une macro

Il y a deux manières principales de modifier une macro, soit en ajoutant des commandes à la fin d'une macro ou bien en modifiant certaines parties de cette dernière.

## Ajout à la fin

Pour ajouter des commandes à la fin d'une macro il nous suffit simplement d'utiliser le même nom de registre mais en utilisant une majuscule.  
`qH{commandes}q` va ajouter les commandes `{commandes}` au registre `h`.

[[information]]
| Si nous avions utilisé un `h` à la place d'un `H` cela aurait remplacé le contenu du registre.

## Modification

Voici comment nous allons procéder pour modifier une macro.  
Nous allons commencer par ouvrir la macro dans un *buffer*, éditer les commandes puis copier ces dernières dans le registre que nous voulions modifier.

1. Ouvrir un nouveau *buffer* vide: `:new`
2. Écrire le contenu du registre `{r}`: `:put {r}`
3. Modifier la macro
4. Copier la ligne dans le registre `{r}`: `"{r}Y`
5. Fermer le buffer: `:q!`

Et voilà ! :D   
En quatre commandes nous avons modifié notre macro. On peut en avoir la confirmation en la réécrivant dans un buffer ou en affichant les registres avec la commande `:reg`.