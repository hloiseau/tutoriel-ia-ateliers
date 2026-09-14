# Situation initiale

Imaginons que nous avons un fichier `chat.txt` et `chat-v2.txt`. Vous vous en doutez, le fichier `chat-v2.txt` est une version améliorée ou corrigée du fichier `chat.txt` qui a été dupliqué puis modifié.

Nous allons ouvrir les deux fichiers.
On peut faire:
- `vim -d chat.txt chat-v2.txt` (ou `vimdiff chat.txt chat-v2.txt`)
- Ouvrir `chat.txt` puis faire la commande `:diffsplit chat-v2.txt` (ou `:vert diffsplit chat-v2.txt`)
- Ouvrir les fichiers `chat.txt` et `chat-v2.txt` dans deux fenêtres et faire la commande `diffthis` dans chacune d'elles (ou bien faire la commande `:windo diffthis`)

Voici ce que l'on obtient:

->![](/media/galleries/11359/451d0a35-f65d-4afb-ba82-96bb0085f373.png)<-

On peut éditer un fichier ou l'autre et on verra les différences changées entre les deux fichiers.

[[information]]
| Pour arrêter la coloration du texte en fonction des différences on utilise la commande `:diffoff`

On peut naviguer rapidement entre les différences avec les raccourcis clavier `]` + `c` pour aller au changement suivant et `[` + `c` pour aller au changement précédent.

# Intégrer rapidement les différences

Lorsque nous sommes dans un des deux fichiers, sur une différence, plutôt que de passer d'une fenêtre à l'autre et en copiant et collant le texte nous pouvons utiliser des commandes.  
Les commandes `:diffget` et `:diffput` vont récupérer ou donner à l'autre fichier la différence sur laquelle nous sommes. Nous pouvons aussi utiliser les raccourcis clavier `do` et `dp`.

La syntaxe complète de la commande est la suivante:
```
[range]diff{get|put} [bufspec]
```

Comme d'habitude, `[range]` corresponds aux lignes que l'on souhaite ajouter ou écraser. `[bufspec]` est le numéro du buffer depuis lequel nous allons récupérer ou écraser le contenu.

[[neutre|Rappel]]
| On peut voir les buffers et leurs numéros avec la commande `:ls`

Suite à de multiples modifications il est possible que Vim soit perdu et que le surlignage ne soit pas mis à jour. Si cela vous arrive, on peut utiliser la commande `:diffupdate`.

[[information]]
| Toute l'aide sur la comparaison de fichier s'obtient dans Vim avec la commande `:h diff`