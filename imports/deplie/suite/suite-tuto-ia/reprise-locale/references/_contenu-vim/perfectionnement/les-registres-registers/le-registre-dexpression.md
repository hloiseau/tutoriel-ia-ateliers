Ce registre (`"=`) nous permet d'avoir accès à la puissance de VimL, notamment lorsque nous voulons créer du contenu dynamiquement en évaluant des expressions.

[[information]]
| Nous n'avons pas encore abordé le VimL. Nous n'en avons pas besoin pour le moment cependant nous l'aborderons plus tard.

Faisons un exemple simple.  
Nous souhaitons écrire la ligne `5016 / 24 = 209`.

Bon, jusqu'ici rien de particulier pour vous. Enfin pas pour moi. Vous connaissez de tête le résultat de la division de 5016 par 24 ? Ba, moi, pas du tout. Du coup j'ai ouvert une console et tapé l'opération dans python pour avoir le résultat.  
Le but du registre d'expression est de pallier ce type d'inconvenance.

Voici le contenu de notre buffer:

-> ![](/media/galleries/11359/a1b09dff-c460-4f7f-9b36-416b4c0243b1.png) <-

Notre curseur est après le signe `=` et nous sommes en mode insertion.

Je vais maintenant presser la touche `Ctrl` + `r` puis `=`.

-> ![](/media/galleries/11359/41b66c18-cc4e-4244-9f23-a92992c149a8.png) <-

Vim nous a placé un `"` bleu à l'endroit où notre curseur était. Maintenant ce dernier se situe en bas de notre terminal après le `=`. Maintenant c'est à nous de jouer.  
Nous pouvons rentrer une expression VimL, cependant nous avons juste besoin d'une bête opération.  
On entre l'opération et un appui sur `Enter`.

-> ![](/media/galleries/11359/85ae2694-cd7c-4e02-931b-d0079d20d50d.png) <-

Et voilà ! Vim nous a calculé notre expression et remis en mode Insertion juste après notre résultat.

À présent lorsque l'on retourne en mode Normal et que l'on observe ses registres (avec la commande `:reg`) vous devriez voir apparaitre le registre `"=` qui contient l'expression que nous avons précédemment tapée.