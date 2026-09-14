Pour nous faciliter le travail, Vim nous permet d'automatiser des actions lors de certains évènements.

Pour cela on utilise la commande `:autocmd` ou bien on ajoute la directive dans le `.vimrc`.

[[information]]
| L'aide à ce sujet s'obtient avec la commande `:h autocmd`.

Ici je vais faire présenter de manière simplifiée comment utiliser la commande `autocmd`. Si vous souhaitez en faire plus, je vous invite à chercher par vous-même ou à lire l'aide de Vim.

La commande s'utilise de la manière suivante:

```.vimrc
autocmd {evenement} {paterne} {commande}
```

Cela signifie que lors de l'événement `{evenement}` arrivera, la commande `{commande}` sera exécutée si le nom du fichier correspond au schéma `{paterne}`.

Voici un exemple:

```.vimrc
autocmd BufWritePre * :%s/\($\n\s*\)\+\%$//e
```

Ici, juste avant l'écriture de mon buffer (`BufWritePre`) la commande `:%s/\($\n\s*\)\+\%$//e` (supprime les espaces inutiles à la fin des lignes) est exécuté sur tous les types de fichiers (`*`).

Le fonctionnement des paternes est assez complexe. Pour avoir la documentation sur le fonctionnement des paternes on utilise la commande `:h autocmd-patterns`.  
Pour faire simple, le paterne représente un nom de fichier (ou un chemin) et on utilise le caractère `*` comme joker. Par exemple le paterne `*.go` matchera tous les fichiers qui finissent en `.go`.

Pour avoir la liste des événements que Vim reconnait on utilise la commande `:h autocommand-events`. Voici une liste de quelques événements:

| Événement | Déclenché par |
|:---------:|:--------------|
| `BufWrite` ou `BufWritePre` | Début de l'écriture du buffer |
| `BufNewFile` | Début de l'édition d'un fichier qui n'existe pas |
| `BufRead` | Début de l'édition d'un fichier qui existe |