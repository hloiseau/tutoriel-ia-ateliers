L'explorateur de fichier s'ouvre avec la commande `:Explore`

Voici ce que fait la commande (en ouvrant Vim dans mon répertoire personnel):

->![](/media/galleries/11359/9a78f2d4-3d14-44ed-a3db-baa8b0fb4344.png)<-

On voit que notre curseur est sur la ligne avec `../`. Cela correspond au répertoire parent.  
On peut déplacer le curseur et ainsi choisir le fichier ou répertoire que l'on souhaite ouvrir. Pour ouvrir, on appuie sur `Entrée`.

Ouvrir un répertoire nous fera descendre dans celui-ci et nous affichera son contenu.  
Lorsque l'on ouvre un fichier, Vim nous affiche son contenu et nous pouvons l'éditer comme nous en avons l'habitude.

[[information]]
| Si l'on connait le chemin du fichier à éditer, on peut directement utiliser la commande `:edit` (ou `:e`) suivi du chemin vers le fichier à éditer. Pas besoin de passer par l'explorateur à chaque fois !

Les premières lignes que Vim nous affiche nous donnent des informations. Ici on constate que l'on se situe dans le répertoire `/home/alban`, que les répertoires et fichier sont dans l'ordre de leurs noms (avec les répertoires en premier).

L'explorateur nous affiche aussi des raccourcis claviers comme par exemple `s` qui permet de changer l'ordre d'affichage des fichiers et répertoires.

Lorsque l'explorateur de fichier est ouvert on peut faire `F1` pour ouvrir une aide rapide à son sujet.

[[information]]
| L'aide complète peut s'obtenir en faisant `:h Explore`

---

On peut accéder aux fichiers et répertoires par leurs chemins relatifs par rapport au répertoire courant où nous avons ouvert Vim.

Pour savoir dans quel répertoire nous sommes nous utilisons la commande `:pwd` (comme dans votre shell).

->![](/media/galleries/11359/6a1c196b-88fc-4ed9-9163-5636eed8f381.png)<-

Voici le résultat de la commande (en bas à gauche) je suis dans mon répertoire personnel.

[[attention]]
| Lorsque l'on a sélectionné un répertoire depuis l'explorateur de fichier, nous avons seulement ouvert son contenu. Nous ne nous sommes pas déplacés dans celui-ci. Le point de départ pour les chemins relatifs est donc le répertoire depuis lequel nous avons ouvert Vim.

Pour changer de répertoire courant on utilise la commande `:cd` (encore une fois, c'est la même commande que celle du shell).

Je vais faire la commande `:cd prg/` pour me déplacer dans le répertoire `./prg/` depuis Vim. Voici le résultat:

->![](/media/galleries/11359/99d3086a-4b69-4120-8844-69b76c85d3dc.png)<-

Comme on le voit en bas à gauche, Vim nous confirme que nous avons changé de répertoire courant. On peut le confirmer en faisant `:pwd`.

À présent, si nous ouvrons l'explorateur de fichier, nous avons accès directement au contenu de ce répertoire (car c'est le répertoire courant).

->![](/media/galleries/11359/8cc95f5c-f5fb-4ba1-82eb-b3e4b8a9ca60.png)<-