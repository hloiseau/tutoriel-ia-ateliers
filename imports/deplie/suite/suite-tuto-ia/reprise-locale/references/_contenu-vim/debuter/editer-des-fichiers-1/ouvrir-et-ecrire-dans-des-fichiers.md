On peut lancer Vim dans un terminal avec la commande `vim`.  
Essayez, dans un terminal tapez:
```console
vim
```

Vous devriez voir quelque chose comme cela:

->
![](/media/galleries/11359/acec40ac-7ff7-47b2-8488-ccd5a18f6101.png)
<-

Avant d'aller plus loin nous allons apprendre à quitter Vim. Cela vous évitera de redémarrer votre pc à chaque fois que vous voulez quitter. :p

Pour cela vous devez taper `:q` (ou `:quit`) sur votre clavier.

[[information]]
| Vous remarquerez qu'en bas à gauche de votre terminal vous verrez ce que vous écrivez.

Ensuite pressez la touche `Entrée`. Vous retournerez dans votre terminal.

Maintenant que nous savons comment quitter Vim, nous allons écrire du texte dans un fichier et le sauvegarder.

Nous allons donc ouvrir vim (avec la commande `vim`).  
Si vous essayez de taper directement du texte, cela ne risque pas de fonctionner correctement.

[[information]]
| En effet, Vim est un éditeur modal. C'est-à-dire que Vim a des modes pour différentes taches.

Pour insérer du texte il faut passer en **mode insertion**, cela se fait en pressant la touche `i`.  
Après avoir pressé la touche `i`, vous devriez voir apparaitre en bas à gauche de votre terminal le texte `-- INSERT --`. Vim nous indique qu'il est en mode insertion et que nous pouvons écrire du texte.

->
![](/media/galleries/11359/c6358170-a486-4312-97f9-3c84e6dadc0a.png)
<-

[[information]]
| Le rectangle gris après le point d'exclamation est notre curseur. On peut le déplacer avec les flèches directionnelles.

À présent, essayons de quitter.  
On presse la touche Échap (`Esc`) pour sortir du mode d'insertion et on tape `:q`.

Vim ne vous laissera pas faire ! Vous devriez avoir ceci:

->
![](/media/galleries/11359/ca1ff61d-5d7b-4421-ab6a-371ce4f6bf4a.png)
<-

Vim nous dit qu'il refuse de quitter puis que nous avons modifié le fichier et que nous n'avons pas sauvegardé.

Pour pallier cela nous avons deux options:

- Quitter sans sauvegarder.
- Sauvegarder, puis quitter.

La commande pour quitter sans sauvegarder est très simple, il s'agit de `:q!` (ou `:quit!`). Le `!` permet d'outrepasser l'avertissement.

Pour sauvegarder nous allons utiliser la commande `:w` (ou `:write`) suivi du nom de fichier dans lequel on veut sauvegarder.

->
![](/media/galleries/11359/7466eb9a-68c0-4b04-a97d-83c199997efe.png)
<-

En appuyant sur la touche `Entrée`, Vim va créer le fichier. Si le fichier existe déjà, vous aurez une erreur. Ce dernier refuse d'écraser le fichier déjà existant. Néanmoins, si vous voulez vraiment écraser le fichier déjà existant, vous pouvez *forcer* l'écriture dans le fichier. Au lieu de faire `:w file.txt` nous devrions faire `:w! file.txt`.

Maintenant, Vim sait dans quel fichier écrire. Si vous ajoutez du texte, pour sauvegarder ne serez plus obligé de préciser le nom du fichier, `:w` suffira.

On peut aussi ouvrir un fichier avec la commande suivante:
```console
vim file.txt
```

Ici, si le fichier existe, Vim l'ouvrira, s'il n'existe pas, Vim le créera lorsque vous le sauvegarderez . (Vous ne serez pas non plus obligé de préciser le nom du fichier lors de la première sauvegarde.)

[[information]]
| On peut aussi enchainer les commandes. Par exemple `:wq` sauvegardera le fichier et quittera.

[[attention | On sait maintenant:]]
| - Ouvrir Vim et ouvrir un fichier avec Vim.
| - Écrire du texte dans un fichier (on passe en mode insertion avec `i`).
| - Quitter le mode insertion (en appuyant sur `Esc`).
| - Sauvegarder notre fichier (avec `:w`).
| - Sauvegarder dans un fichier spécifique (avec `:w nom_du_fichier`).
| - Quitter notre fichier qui a été sauvegardé (avec `:q`).
| - Quitter sans sauvegarder (avec `:q!`).
| - Sauvegarder et quitter (avec `:wq`).