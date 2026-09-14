# Débuter

## Éditer des fichiers

### Ouvrir et écrire dans des fichiers

- Écrire du texte dans un fichier (on passe en mode insertion avec `i`).
- Quitter le mode insertion (en appuyant sur `Esc`).
- Sauvegarder notre fichier (avec `:w`).
- Sauvegarder dans un fichier spécifique (avec `:w nom_du_fichier`).
- Quitter notre fichier qui a été sauvegardé (avec `:q`).
- Quitter sans sauvegarder (avec `:q!`).
- Sauvegarder et quitter (avec `:wq`).

### Déplacer le curseur et retour sur l'insertion

- Déplacer le curseur (avec `h`, `j`, `k` et `l` ou `←`, `↓`, `↑` et `→`).
- Déplacer le curseur au début et à la fin du fichier (avec `gg` et `G`).
- Insérer du texte avant et après notre curseur (avec `i` et `a`).
- Insérer du texte au début et à la fin de la ligne (avec `I` et `A`).
- Insérer du texte au-dessus et au-dessous de la ligne (avec `O` et `o`).

### Couper, copier et coller

- Passer en mode visuel (avec `v`) et sélectionner du texte (en déplaçait le curseur).
- Couper le texte sélectionné (avec `d`).
- Copier le texte sélectionné (avec `y`).
- Coller la sélection après le curseur (avec `p`).
- Coller la sélection avant le curseur (avec `P`).
- Couper une ligne (avec `dd`).
- Copier une ligne (avec `Y`).
- Coller la (ou les) ligne(s) sur la ligne suivante au curseur (avec `p`).
- Coller la (ou les) ligne(s) sur la ligne précédente au curseur (avec `P`).
- Couper N lignes (avec `Ndd`, N étant un nombre).
- Copier N lignes (avec `NY`, N étant un nombre).

### Indentation et Ctrl + z

- Décaler la ligne du curseur vers la droite ou la gauche (avec `<<` et `>>`).
- Décaler N lignes à partir du curseur vers la droite ou la gauche (avec `N<<` et `N>>`, N étant un nombre).
- Annuler la dernière action effectué (avec `u`).
- Annuler l'annulation de la dernière action effectuée (avec `Ctrl + r`).

### Chercher dans un fichier et changement rapide

- Chercher les occurrences dans un fichier (avec `/` suivi de ce qu'on cherche).
- Passer à l'occurrence suivante ou précédente (avec `n` et `N`).
- Remplacer le caractère sous le curseur (avec `r` suivi du caractère remplaçait).
- Supprimer le caractère sous le curseur (avec `x`).
- Supprimer N caractères à partir du curseur (avec `Nx`, N étant un nombre).
- Répéter la dernière commande que nous avons faite (avec `.`).

# Perfectionnement

## Les modes

- Le mode `Normal` est celui par défaut
- Le mode `Insertion` permet d'ajouter du texte
- Le mode `Ligne de commande` permet d'écrire et d'exécuter des commandes (avec `:`)
- Le mode `Visuel` permet de faire des sélections (avec `v`), des sélections de bloc (`Ctrl + v`), et des sélections de lignes (`Maj + v`)
- Le mode `Remplacement` qui remplace le texte au fur et à mesure que l'on écrit (`Maj + r`)
- Le mode `Selection` qui s'active en faisant `Ctrl + g` lorsqu'on est en mode `Visuel`
- Le mode `Ex` permet d'enchainer plusieurs commandes (`Maj + q`, on utilise `vi` pour le quitter)

## Les commandes

- Le schéma des commandes: `[nombre] {opérateur} {[nombre] mouvement | objet texte}`
- Les différents opérateurs, mouvements du curseur et de la page
- Les différents objets texte (`Word`, `Sentence`, `Paragraph`, `Tag`, `Quote`, `Block`)
- Exécuter des commandes en mode insertion `Ctrl + o`

#### Opérateurs (Operators)

| Opérateur | Explication |
|:---------:|:-------------|
| `Y` | Copie la ligne du curseur |
| `dd` | Coupe la ligne du curseur |
| `D` | Coupe du curseur à la fin la ligne (équivalent à d$) |
| `p` | Colle après le curseur |
| `P` | Colle avant le curseur |
| `x` | Coupe le caractère sous le curseur |
| `X` | Coupe le caractère avant le curseur |
| `i` | Passer en mode Insertion après le curseur |
| `a` | Passer en mode Insertion avant le curseur |
| `o` | Passer en mode Insertion sur la ligne en dessous le curseur |
| `O` | Passer en mode Insertion sur la ligne au-dessus le curseur |
| `s` | Coupe le caractère sous le curseur et passe en mode Insertion |
| `S` | Coupe la ligne et passe en mode Insertion |
| `c <mouvement>` | Coupe et passe en mode Insertion |
| `v` | Passer en mode Visuel |
| `.` | Reexecute la dernière commande |
| `~` | Inverse la casse du caractère ("a" deviendra "A" et "E" deviendra "e") |

#### Mouvements du curseur (Motions)

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

#### Mouvement de la page

| Mouvement | Explication |
|:---------:|:-------------|
| `zt` | Déplace la page à fin que la ligne du curseur se situe en haut de la fenêtre |
| `zz` | Déplace la page à fin que la ligne du curseur se situe au milieu de la fenêtre |
| `zb` | Déplace la page à fin que la ligne du curseur se situe en bas de la fenêtre |
| `H` | Déplace le curseur en haut de la fenêtre |
| `M` | Déplace le curseur au milieu de la fenêtre |
| `L` | Déplace le curseur en bas de la fenêtre |
| `Ctrl` + `u` | Remonter d'un demi-écran |
| `Ctrl` + `d` | Descendre d'un demi-écran |
| `Ctrl` + `b` | Remonter d'un écran |
| `Ctrl` + `f` | Descendre d'un écran |

### Les objets texte

| Objet | Identifiant |
|:-----:|:------------|
| mot (word) | `w` |
| phrase (sentence) | `s` |
| paragraphes (paragraph) | `p` |
| balises (tag) | `t` |
| citations (quote) | `"`, `'`, `` ` `` |
| blocs (block) | `(`, `)`, `[`, `]`, `{`, `}`, `<`, `>` |

## Les buffers

- Vim ne travaille pas directement sur le fichier mais avec une *copie*, le buffer
- Les différents types de buffers (Le buffer, le [No Name] buffer, le scratch buffer)
- Se déplacer entre les buffers

### Les différents types de buffers

- Le buffer
- Le [No Name] buffer
- Le scratch buffer

### Naviguer entre les buffers

| Commande | Explication |
|:--------:|:-------------|
| `:ls` | Liste les buffers ouverts |
| `:bn` | Passe au buffer suivant |
| `:b<nombre>` | Passe au buffer portant le nombre `<nombre>` |
| `:bp` | Passe au buffer précédent |
| `:b#` | Passe au dernier buffer visité |
| `:bf` | Passe au premier buffer de la liste |
| `:bl` | Passe au dernier buffer de la liste |
| `:bm` | Passe au prochain buffer modifié |
| `:enew` | Ouvre un [No Name] buffer |

## Les fenêtres (window ou viewport)

- Découper le buffer horizontalement et verticalement
- Se déplacer entre les fenêtres
- Déplacer et changer la taille des fenêtres

+------------------------------------------------+-------------------------------------------------------------------------+
| Commande                                       | Explication                                                             |
+================================================+=========================================================================+
| `:sp` ou `:split`                              | Coupe la fenêtre horizontalement                                        |
+------------------------------------------------+-------------------------------------------------------------------------+
| `:vsp` ou `:vsplit`                            | Coupe la fenêtre verticalement                                          |
+------------------------------------------------+-------------------------------------------------------------------------+
| `:new`                                         | Ouvre un nouveau [No Name] buffer en coupant la fenêtre horizontalement |
+------------------------------------------------+-------------------------------------------------------------------------+
| `:vnew`                                        | Ouvre un nouveau [No Name] buffer en coupant la fenêtre verticalement   |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `w`                          | Aller dans la fenêtre suivante                                          |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `W`                          | Aller dans la fenêtre précédente                                        |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `h` ou `Ctrl` + `w` puis `←` | Aller dans la fenêtre de gauche                                         |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `j` ou `Ctrl` + `w` puis `↓` | Aller dans la fenêtre du dessous                                        |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `k` ou `Ctrl` + `w` puis `↑` | Aller dans la fenêtre du dessus                                         |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `l` ou `Ctrl` + `w` puis `→` | Aller dans la fenêtre de droite                                         |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `H`                          | Déplacer la fenêtre à gauche                                            |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `J`                          | Déplacer la fenêtre au-dessous                                          |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `K`                          | Déplacer la fenêtre au-dessus                                           |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `L`                          | Déplacer la fenêtre à droite                                            |
+------------------------------------------------+-------------------------------------------------------------------------+
| `:on` ou `:only`                               | Ferme toutes les fenêtres sauf la courante                              |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `>`                          | Élargis la fenêtre d'une colonne                                        |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `<`                          | Affine la fenêtre d'une colonne                                         |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `-`                          | Rapetisse la fenêtre d'une ligne                                        |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `+`                          | Agrandis la fenêtre d'une ligne                                         |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `=`                          | Réarrange toutes les fenêtres de manière égale                          |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `<n>` puis `>`               | Élargis la fenêtre de `<n>` colonnes                                    |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `<n>` puis `<`               | Affine la fenêtre de `<n>` colonnes                                     |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `<n>` puis `-`               | Rapetisse la fenêtre de `<n>` lignes                                    |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `<n>` puis `+`               | Agrandis la fenêtre de `<n>` lignes                                     |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `|`                          | Maximise la largeur de la fenêtre                                       |
+------------------------------------------------+-------------------------------------------------------------------------+
| `Ctrl` + `w` puis `_`                          | Maximise la hauteur de la fenêtre                                       |
+------------------------------------------------+-------------------------------------------------------------------------+

## Les onglets (tabs)

- Ouvrir et fermer des onglets
- Se déplacer entre les onglets

| Commande | Explication |
|:--------:|:------------|
| `:tabnew` | Ouvre un nouvel onglet |
| `gt` | Passer à l'onglet suivant |
| `gT` | Passer à l'onglet précédent |
| `<nb>gt` | Passer à l'onglet `<nb>` |
| `:tabclose` | Fermer un onglet |
| `:tabmove <nb>` | Déplace l'onglet en position `<nb>`, si `<nb>` est absent l'onglet sera mis en dernier |
| `Ctrl` + `w` puis `T` | Convertis une fenêtre en onglet |

## Les registres (Registers)

- Les 9 différents types de registres de Vim  
  - Sans nom: `""`
  - Numérique
  - Nommés
  - En lecture seuls: `":`, `".`, `"%`, `"#`
  - Trou noir: `"_`
  - Dernière recherche: `"/`
  - Petite suppression `"-`
  - D'expression: `"=`
  - De selection et de dépôt (`"*`, `"+`, `"~`)
- Afficher le contenu des registres (avec la commande `:reg`)

## Le folding

- Les différentes méthodes de pliages (`manual`, `indent`, `syntax`, `expr`, `marker`, `diff`)
- Manipuler les plis

+----------------------------------------+------------------------------------------------------------+
| Commande                               | Explication                                                |
+========================================+============================================================+
| `zo`                                   | Ouvre le pli sur lequel est le curseur                     |
+----------------------------------------+------------------------------------------------------------+
| `zc`                                   | Ferme le pli dans lequel est le curseur                    |
+----------------------------------------+------------------------------------------------------------+
| `za`                                   | Bascule entre l'état ouvert ou fermé                       |
+----------------------------------------+------------------------------------------------------------+
| `zO`                                   | Ouvre tous les plis de la hiérarchie                       |
+----------------------------------------+------------------------------------------------------------+
| `zC`                                   | Ferme tous les plis de la hiérarchie                       |
+----------------------------------------+------------------------------------------------------------+
| `zA`                                   | Ouvre ou ferme tous les plis de la hiérarchie              |
+----------------------------------------+------------------------------------------------------------+
| `zM`                                   | Ferme tous les plis du buffer                              |
+----------------------------------------+------------------------------------------------------------+
| `zR`                                   | Ouvre tous les plis du buffer                              |
+----------------------------------------+------------------------------------------------------------+
| `zm`                                   | Ferme le pli (non ouvert) le plus profond de la hiérarchie |
+----------------------------------------+------------------------------------------------------------+
| `zr`                                   | Ouvre le plus haut pli (non fermé) de la hiérarchie        |
+----------------------------------------+------------------------------------------------------------+
| `zf{[nombre] mouvement | objet texte}` | Crée un pli en méthode `manual`                            |
+----------------------------------------+------------------------------------------------------------+

# Personnalisation

## Le fichier de configuration

- Vim utilise le fichier de configuration `.vimrc`
- On définit des options dans ce fichier pour le configurer
- Comment définir ses propres raccourcis clavier avec `map`
- Créer des abréviations avec `abbr`
- Comment activer et régler la coloration syntaxique (les commandes `filetype` et `syntax`)
- Exécuter automatiquement des commandes avec `autocmd`
- L'utilité des fichiers swap et du fichier viminfo

## Les plugins

- Où placer les fichiers de plugin pour qu'ils soient pris en compte au démarrage de Vim (`~/.vim/plugin/`)
- Les plugins peuvent être spécifiques en fonction des types de fichiers (`~/.vim/ftplugin/<filetype>/file.vim`)

## Les packages

- Que les plugins se placent dans le répertoire `~/.vim/pack/<name>/start/`

## Les templates

- Ouvrir un fichier avec un modèle précis selon le type de fichier ouvert

# Utilisation avancée

## Recherche et remplacement

- Checher:
  - dans un fichier avec `/`
  - dans plusieurs fichiers avec `vimgrep`, `lvimgrep`, `grep`, ou `lgrep`
- Les listes:
  - La `jump list`: qui est la liste des déplacements du curseur
  - La `quickfix list`: elle est utilisée pour accéder rapidement à des changements *rapides*
  - La `location list`: est identique à la `quickfix list` mais dépend de la fenêtre
  - La `change list`: qui est la liste des derniers changements
- Les remplacements avec la forme `:[range]s/{pattern}/{string}/[flag] [count]`

## Naviguer dans les fichiers

- Ouvrir et utiliser l'explorateur de fichiers de Vim `:Explore`
- Ouvrir des fichiers avec la commande `:edit` en précisant le chemin relatif ou absolu vers le fichier
- Dans quel répertoire a été ouvert Vim (`:pwd`) et nous déplacer dans l'arborescence de fichier (`:cd`)

## Injecter dans des fichiers 

- Injecter le contenu d'un fichier ou le résultat d'une commande dans le buffer courant avec `:read`

## Différences entre fichiers

- Afficher les différences entre deux fichiers:
  - avec `vim -d <file_1> <file_2>` ou `vimdiff  <file_1> <file_2>`
  - avec un fichier en faisant `:diffsplit <file_2>`
  - en ouvrant les deux fichiers et en faisant `:diffthis` dans chaque buffer
- Intégrer rapidement les différences:
  - avec `:diffget` ou `:diffput`
  - avec les raccourcis claviers `do` et `dp`
  - avec la commande `[range]diff{get|put} [bufspec]`
- Mettre à jour les différences entre deux fichiers avec `:diffupdate`

## Exécution de commande généralisée

- Exécuter des commandes dans:
  - chaque buffer → `:bufdo`
  - chaque fenêtre → `:windo`
  - chaque onglet → `:tabdo`
  - chaque fichier donné en argument → `:argdo`

## Les sessions

- La différence entre une *view* et une *session*
- Comment créer une view (`:mkview`) et une session (`:mksession`)
- Réouvrir sa view ou sa session avec `:source` (et l'argument `-S` pour les sessions)

## Marque-page

- Crée un marque-page (avec `m` ou `:mark`)
- Afficher ses marque-pages avec `:marks`
- Se déplacer à un marque page (avec `` ` `` ou `'`, suivis de son nom)
- Les marque-pages *sont* des mouvements
- Supprimer des marque-pages avec la commande `:delm`

## Automatisation

- Utiliser le mode Ex en ligne de commande
- Créer des macros (`q{registre}{commandes}q`)
- Exécuter notre macro (`@{registre}`)
- Ajouté des commandes à une macro (en utilisant le registre en majuscule)
- Modifier une macro (on l'écrit dans un buffer pour la modifier puis on la sauvegarde dans un registre)

## L'encodage

- Changer l'encodage que Vim utilise pour lire un fichier (avec `encoding`)
- Changer l'encodage d'un fichier sur le disque (avec `fileencoding`)