Pour qu'un plugin soit automatiquement chargé on place le fichier dans le répertoire `~/.vim/plugin/`.  
Il n'est pas obligatoire de mettre les fichiers directement à la racine de ce répertoire, on peut créé une architecture de fichier pour mieux s'y retrouver (par exemple regrouper les plugins par langage `~/.vim/plugin/python/`, `~/.vim/plugin/go/`, ...)

Le plugins spécifiques se placent dans le répertoire `~/.vim/ftplugin/`. Dans ce répertoire les fichiers doivent suivre un des motifs suivants:

- `~/.vim/ftplugin/<filetype>.vim`
- `~/.vim/ftplugin/<filetype>_<name>.vim`
- `~/.vim/ftplugin/<filetype>/<name>.vim`

Ici, `<name>` peut être le nom qui vous arrange, il permet de mieux s'organiser. Cependant le `<filetype>` doit être un type de fichier qui correspond à celui auquel le plugin sera actif.