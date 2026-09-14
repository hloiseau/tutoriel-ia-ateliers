Nous avons évoqué ce mode précédemment. Il permet d'exécuter plusieurs commandes à la suite (contrairement au mode ligne de commande qui retourne en mode normal après chaque commande).  
Lorsque Vim est ouvert on fait `Q` pour passer en mode Ex (et on fait `:vi` pour quitter).

Bien que ce mode ne soit pas très utilisé fréquemment par une grande partie des utilisateurs de Vim il est néanmoins très puissant.

Le mode Ex peut aussi être utilisé directement depuis la ligne de commande. Imaginons que nous souhaitons remplacer toutes les occurrences d'un mot dans un fichier. On pourrait le faire avec la commande [`sed`](https://en.wikipedia.org/wiki/Sed) mais ici notre sujet est Vim. :D 

Voici la commande que l'on aurait:

```shell
vim -E chat.txt -s <<-EOF
  :%s/chat/chien/g
  :wq
EOF
```

Ici l'option `-E` signifie que nous démarrons Vim en mode Ex. `chat.txt` est le fichier que nous ouvrons. L'option `-s` permet de ne pas démarrer Vim mais d'exécuter les commandes qu'on lui donne en argument. Nous donnons ensuite les commandes au format [heredoc](https://en.wikipedia.org/wiki/Here_document).

[[secret]]
| L'équivalent avec la commende `sed` pour cet exemple serait `sed -i 's/chat/chien/' chat.txt`