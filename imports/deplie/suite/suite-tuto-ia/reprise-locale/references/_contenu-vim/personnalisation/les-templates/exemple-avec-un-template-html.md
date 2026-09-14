La première étape est de créer notre template.

Voici le mien:

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <link rel="stylesheet" href="/style.css" >
    </head>
    <body>
    </body>
</html>
```

Je sauvegarde ce fichier sous `~/tpl.html`.

À présent je dis à Vim de copier ce fichier dans mon buffer lorsque j'ouvre un fichier `.html`. Pour cela on ajoute à notre `.vimrc` la ligne suivante:

```vimrc
autocmd BufNewFile *.html 0r ~/tpl.html
```

[[information]]
| La commande ci-dessus est une commande d'automatisation (`autocmd`). Elle signifie qu'à l'ouverture d'un nouveau fichier (`BufNewFile`), si ce fichier a une extension en `.html` (`*.html`) alors on exécute la commande `0r ~/tpl.html`.  
| `0r ~/tpl.html` est la commande `read` (que nous verrons plus tard). Ici cela signifie d'insérer à partir de la ligne 0 de notre fichier le contenu de `~/tpl.html`.

Maintenant, lorsque l'on ouvre Vim avec par exemple:

```bash
vim home_page.html
```

ou bien que dans Vim on crée le fichier avec `:e home_page.html` ou `:new home_page.html` nous n'avons plus un fichier vide mais un buffer préremplis avec notre template.