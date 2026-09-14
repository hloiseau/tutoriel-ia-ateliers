Il existe trois types de mode visuel:

- Visuel (Visual)
- Bloc Visuel (Visual Block)
- Ligne Visuelle (Visual Line)

Les modes visuels permettent de surligner du texte. Dans ces modes, les commandes de mouvement étendent une zone surlignée, tandis que les commandes affectent seulement cette zone.

[[information]]
| Les différences entre ces modes se font de la manière dont Vim surligne le texte.

À tout moment vous pouvez faire `Esc` pour quitter le mode et retourner en mode normal.

# Mode Visuel

> En mode Visuel, le texte est surligné de la même manière que dans un logiciel de traitement de texte.

Voici le code suivant:

->
![](/media/galleries/11359/8195be91-e6b2-423b-b3d5-e8440980330b.png)
<-

À présent j'appuie sur la touche `v` pour passer en mode visuel, vous devriez voir afficher `-- VISUAL --` en bas à gauche de votre terminal.  
Je vais maintenant déplacer le curseur vers la droite (en utilisant `l` ou `→`) puis vers le bas (en utilisant `j` ou `↓`).

Voici le résultat:

->
![](/media/galleries/11359/5363adcd-2987-4357-8866-d7591fbfcb08.png)
<-

Notre curseur se trouve à la fin de la sélection. Vous pouvez mettre le curseur au début de la sélection (pour sélectionner du texte en début de sélection) avec `o`. Ceci permet de sélectionner le texte précédent sans refaire la sélection existante.

Pour effectuer une action sur la sélection, on fait une commande. Si nous souhaitons la supprimer, on peut faire `x`. Et voici le résultat:

->
![](/media/galleries/11359/eb9cc31a-8abb-44e1-919b-ff0605d1292b.png)
<-

Une fois la commande exécuté, Vim retourne en mode normal.

# Mode Bloc Visuel

> En mode Bloc Visuel, le texte est surligné à la manière d'un bloc.

Je reprends le même code que pour l'exemple précédent, cependant, au lieu de faire `v` je vais faire `Ctrl + v`.

->
![](/media/galleries/11359/3d08e949-beea-4ea8-85fa-5b3e84c1ef4b.png)
<-

De la même manière, je peux déplacer mon curseur.

->
![](/media/galleries/11359/e9ec26f3-51dc-41b3-80a1-7a482cb4078a.png)
<-

Cependant mon curseur se situe en bas à droite de mon bloc sélectionné.  
Pour ne pas avoir à refaire la sélection de zéro, on utilise `o` pour déplacer le curseur en diagonale du bloc (dans le cas de l'image ci-dessus, `o` déplacera le curseur en haut à gauche du bloc) et `O` (`Maj + o`) pour déplacer le curseur de l'autre côté du bloc sur la ligne du curseur (dans le cas de l'image ci-dessus `O` déplacera le curseur en bas à gauche du bloc).

Ces commandes, `o` et `O`, permettent de se déplacer dans les 4 coins du bloc de sélection pour la peaufiner sans recommencer une sélection de zéro (car le but de Vim est de nous rendre plus rapide !  ;) ).

Maintenant notre sélection faite, nous pouvons exécuter une commande (essayer par exemple `y` pour couper puis `p` quelque part coller la sélection).

# Mode Ligne Visuel

> En mode Ligne Visuel, le texte est surligné par ligne.

Voici le même code, cette fois-ci je fais `Maj + v`.

->
![](/media/galleries/11359/a4919748-d67a-4fe1-ba32-2af65d3aae24.png)
<-

Tout de suite, la ligne du curseur est sélectionnée.

Maintenant je fais déplacer mon curseur vers le bas pour sélectionner la ligne du dessous.  
Je fais ensuite `o` pour mettre le curseur au début de la sélection et déplace le curseur vers le haut afin d'ajouter la ligne du dessus.

->
![](/media/galleries/11359/782b7ebc-4a01-4f99-b251-795c47105048.png)
<-

Maintenant que la sélection me convient, je peux faire une commande pour modifier la sélection ou appuyer sur `Esc` pour ne rien faire.

---

[[information]]
| Il existe 3 modes visuels dans Vim qui ont chacun leur propre utilité. Ils permettent de faire des sélections rapides pour ensuite modifier ou supprimer la sélection faite.

Les modes visuels sont souvent utilisés pour indenter du code. Pour cela on utilise `>` et `<` pour décaler la sélection d'un niveau vers la droite ou la gauche. On peut utiliser `=` pour indenter automatiquement la sélection.  
Il est aussi possible de faire des insertions en colonne sur plusieurs lignes. Pour cela on fait `I` lors d'une sélection en bloc.

Il est possible de passer d'un mode visuel à l'autre sans repasser par le mode insertion. Cela se fait simplement en utilisant les mêmes commandes que depuis le mode normal.