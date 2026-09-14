Le fichier de configuration de Vim est le `vimrc`. Il est lu par le logiciel lors de son démarrage.

[[information]]
| Pour obtenir la documentation à propos du `vimrc` on utilise la commande `:help vimrc`.

Ce fichier se nomme `.vimrc` (`_vimrc` sous Windows) et se situe dans votre répertoire home (`$HOME`) ou bien `$HOME/.vim/vimrc` (`$HOME/vimfiles/vimrc` sous Windows).

Si plusieurs fichiers sont présents, Vim prend en compte le premier qu'il rencontre (dans l'ordre ci-dessus).

Dans le cas où aucun de ces fichiers n'est présent, l'éditeur va utiliser le fichier du système (`/etc/vimrc`).