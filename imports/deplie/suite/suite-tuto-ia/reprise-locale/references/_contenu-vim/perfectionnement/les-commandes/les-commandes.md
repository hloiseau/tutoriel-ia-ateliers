[[attention]]
| Il ne faut pas confondre les commandes du mode Normal et les commandes du mode Ligne de commande.  
| Elles peuvent avoir la même syntaxe mais des actions complètement différentes.

Les commandes suivent toutes le même schéma:

->`[nombre] {opérateur} {[nombre] mouvement | objet texte}`<-

- Le nombre, entre crochets, est optionnel. Il donne le nombre de répétitions (de l'opérateur ou du mouvement).
- Les opérateurs sont les opérations, actions que nous allons exécuter.
- Un (ou plusieurs) mouvement, **ou bien**, un objet texte suit l'opérateur. C'est ce sur quoi l'opération sera appliquée.

[[information]]
| Certains opérateurs n'ont pas besoin de mouvement ou d'objet texte les suivants car ils se suffisent à eux-mêmes.

Pour comprendre les commandes et pouvoir composer les vôtres, il est très important d'avoir en tête le patron de conception de ces dernières.

# Opérateurs (Operators)

Les opérateurs sont les actions qui vont être effectué.

Voici une liste non exhaustive des opérateurs:

+-----------------+------------------------------------------------------------------------+
| Opérateur       | Explication                                                            |
+=================+========================================================================+
| `Y`             | Copie la ligne du curseur                                              |
+-----------------+------------------------------------------------------------------------+
| `dd`            | Coupe la ligne du curseur                                              |
+-----------------+------------------------------------------------------------------------+
| `D`             | Coupe du curseur à la fin la ligne (équivalent à `d$`)                  |
+-----------------+------------------------------------------------------------------------+
| `p`             | Colle après le curseur                                                 |
+-----------------+------------------------------------------------------------------------+
| `P`             | Colle avant le curseur                                                 |
+-----------------+------------------------------------------------------------------------+
| `x`             | Coupe le caractère sous le curseur                                     |
+-----------------+------------------------------------------------------------------------+
| `X`             | Coupe le caractère avant le curseur                                    |
+-----------------+------------------------------------------------------------------------+
| `i`             | Passer en mode Insertion après le curseur                              |
+-----------------+------------------------------------------------------------------------+
| `a`             | Passer en mode Insertion avant le curseur                              |
+-----------------+------------------------------------------------------------------------+
| `o`             | Passer en mode Insertion sur la ligne en dessous le curseur            |
+-----------------+------------------------------------------------------------------------+
| `O`             | Passer en mode Insertion sur la ligne au-dessus le curseur             |
+-----------------+------------------------------------------------------------------------+
| `s`             | Coupe le caractère sous le curseur et passe en mode Insertion          |
+-----------------+------------------------------------------------------------------------+
| `S`             | Coupe la ligne et passe en mode Insertion                              |
+-----------------+------------------------------------------------------------------------+
| `c <mouvement>` | Coupe et passe en mode Insertion                                       |
+-----------------+------------------------------------------------------------------------+
| `v`             | Passer en mode Visuel                                                  |
+-----------------+------------------------------------------------------------------------+
| `.`             | Reexécute la dernière commande                                         |
+-----------------+------------------------------------------------------------------------+
| `~`             | Inverse la casse du caractère ("a" deviendra "A" et "E" deviendra "e") |
+-----------------+------------------------------------------------------------------------+

# Mouvements du curseur (Motions)

Les mouvements peuvent aussi bien servir à déplacer le curseur qu'à définir le mouvement d'une commande.

Tout comme les opérateurs, en voici une liste non exhaustive:

| Mouvement | Explication |
|:---------:|:-------------|
| `h` | Déplace sur la gauche |
| `j` | Déplace sur la ligne du dessous |
| `k` | Déplace sur la ligne du dessus |
| `l` | Déplace sur la droite |
| `0` | Déplace au début de la ligne |
| `$` | Déplace à la fin de la ligne (en incluant le caractère de retour à la ligne) |
| `g_` | Déplace à la fin de la ligne (sans inclure le caractère de retour à la ligne) |
| `^` | Déplace au premier caractère visible de la ligne |
| `t<caractère>` | Déplace vers la droite avant le `<caractère>` |
| `T<caractère>` | Déplace vers la gauche avant le `<caractère>` |
| `f<caractère>` | Déplace vers la droite sur le `<caractère>` |
| `F<caractère>` | Déplace vers la gauche sur le `<caractère>` |
| `b` | Déplace au début du mot (précédent) |
| `w` | Déplace au début du mot suivant |
| `ge` | Déplace à la fin du mot précédent |
| `e` | Déplace à la fin du mot (suivant) |
| `gg` | Déplace au début du buffer |
| `G` | Déplace à la fin du buffer |
| `%` | Déplace à l'autre accolade, parenthèse, crocher ou chevron de la paire |
| `(` | Déplace au précédent objet text phrase |
| `)` | Déplace à l'objet text phrase suivant |
| `{` | Déplace au précédent objet text paragraphe |
| `}` | Déplace à l'objet text paragraphe suivant |
| `[(` | Déplace à la prochaine parenthèse sans correspondance |
| `])` | Déplace à la parenthèse précédente sans correspondance |
| `[{` | Déplace à la prochaine accolade sans correspondance |
| `]}` | Déplace à l'accolade précédente sans correspondance |

# Mouvement de la page

Le but de Vim est de vous faire gagner du temps, toujours plus. C'est pour cela qu'il nous offre certaines fonctionnalités, telles que les mouvements de la page.

Imaginons que nous éditions un fichier, il a des chances pour que notre curseur se situe tout en bas de la fenêtre. Cependant nous souhaitons voir le code qui se situe en dessous de notre ligne et qui n'est pas affiché. Pour cela, Vim nous met à disposition la commande `zt`.

| Mouvement | Explication |
|:---------:|:-------------|
| `zt` | Déplace la page à fin que la ligne du curseur se situe en haut de la fenêtre |
| `zz` | Déplace la page à fin que la ligne du curseur se situe au milieu de la fenêtre |
| `zb` | Déplace la page à fin que la ligne du curseur se situe en bas de la fenêtre |

Réciproquement, il nous est possible de déplacer le curseur par rapport à la fenêtre.

| Mouvement | Explication |
|:---------:|:-------------|
| `H` | Déplace le curseur en haut de la fenêtre |
| `M` | Déplace le curseur au milieu de la fenêtre |
| `L` | Déplace le curseur en bas de la fenêtre |

Toujours dans le but de gagner en rapidité, il nous est possible de faire défiler la fenêtre écran par écran ou demi-écran par demi-écran plutôt que ligne par ligne.

| Mouvement | Explication |
|:---------:|:-------------|
| `Ctrl` + `u` | Remonter d'un demi-écran |
| `Ctrl` + `d` | Descendre d'un demi-écran |
| `Ctrl` + `b` | Remonter d'un écran |
| `Ctrl` + `f` | Descendre d'un écran |

---

Il est inutile de tout apprendre par cœur. C'est avec le temps et l'habitude que vous allez les retenir.

Sachez que si vous souhaitez réaliser une action qui n'est pas listée précédemment il existe sûrement un moyen simple de réaliser ce que vous souhaitez. Le mieux est de demander à votre moteur de recherche favoris.  ^^