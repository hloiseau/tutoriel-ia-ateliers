Il y a principalement deux manières d'installer Vim, soit depuis le [gestionnaire de paquets](https://fr.wikipedia.org/wiki/Gestionnaire_de_paquets "Page Wikipédia sur les gestionnaires de paquets") de votre distribution ou bien depuis les sources.

# Installation depuis le gestionnaire de paquets

Sous Linux, il est préférable d'installer Vim en utilisant le gestionnaire de paquets.

Pour cela nous allons ouvrir un terminal et taper la commande correspondant à notre gestionnaire de paquets.

[[information]]
| Vous pouvez aussi l'installer via un gestionnaire de paquets graphique.

Exemples:

- `sudo apt-get install vim` pour toutes les distributions basées sur [Debian](https://fr.wikipedia.org/wiki/Debian "Page Wikipédia de Debian") et [Ubuntu](https://fr.wikipedia.org/wiki/Ubuntu_(système_d%27exploitation) "Page Wikipédia d'Ubuntu").
- `pacman -S vim` pour toutes les distributions basées sur [Arch Linux](https://fr.wikipedia.org/wiki/Arch_Linux "Page Wikipedia d'Arch Linux").
- `emerge app-editors/vim` pour le système [Gentoo](https://fr.wikipedia.org/wiki/Gentoo_Linux "Page Wikipédia de Gentoo").
- ...

# Installation depuis les sources

On peut aussi installer Vim depuis ses fichiers sources et le compiler nous-mêmes. Ici je fais le choix de récupérer les sources depuis git. Vous trouverez d'autres moyens depuis [le site officiel](https://www.vim.org/download.php "Page de téléchargement du site officiel de Vim").

Voici les commandes à taper dans un shell ainsi que ce qu'elles font:

```console
git clone https://github.com/vim/vim.git    # On commence par récupérer les fichiers sources via git
cd vim/src    # On va dans le répertoire source du projet vim
make distclean    # On supprime les anciennes versions de vim (cette commande se termine en erreur s'il n'y avait pas de version précédemment installée)
make    # On compile le code source de vim
make install     # On copie les fichiers compilés pour que l'ordinateur puisse les exécuter
```