# L'indentation

Très souvent, en tant que développeurs, nous avons besoin d'indenter notre code.  
Vim nous permet d'indenter le texte très facilement.

Voici un exemple:

->
![](/media/galleries/11359/98d06c22-69c4-4d09-851c-1774d706229e.png)
<-

Mon curseur se situe à la ligne 6. Je vais décaler la ligne jusqu'à la flèche de la ligne en dessous.  
Pour cela on va appuyer deux fois sur la touche `>`, la commande est `>>`.  
Et voici le résultat:

->
![](/media/galleries/11359/a0982e7a-f049-466c-a304-788aeced6e49.png)
<-

Je vous laisse répéter la commande pour décaler la ligne au niveau de la flèche.

->
![](/media/galleries/11359/e57f05f4-3a11-4214-bf0c-05824928bdac.png)
<-

Notre curseur se situe sur la ligne 4.

Si la commande `>>` permet de décaler vers la droite, on peut en déduire que la commande `<<` décale vers la gauche. Ici on pourrait donc naïvement faire `<<` pour décaler la ligne 4 vers la droite, puis `j` pour passer à la ligne 5 et refaire `<<` pour décaler cette dernière.  
Cependant si nous avons plusieurs dizaines de lignes à décaler cela va prendre beaucoup de temps. Souvenez-vous, Vim a pour but de nous rendre de telles actions facile et rapide.  
Dans cet exemple on va faire la commande `2<<`, cela signifie: prends les  2 lignes à partir du curseur et décale les vers la gauche.

Voici le résultat de la commande `2<<`:

->
![](/media/galleries/11359/98e0adf2-e050-4e5c-a560-df913d4859fa.png)
<-

[[information]]
| Notez qu'on a décalé les lignes sans passer par le mode insertion.

# Défaire et refaire

Lorsqu'on édite des fichiers, il arrive que nous fassions des erreurs, cependant on peut annuler ces dernières très facilement dans tous les logiciels. Vous avez sûrement déjà entendu le raccourci `Ctrl + z` qui permet d'annuler la dernière action et peut-être `Ctrl + y` qui permet d'annuler l'annulation. Dans Vim ces commandes sont légèrement différentes.

Voici un fichier:

->
![](/media/galleries/11359/4758bf56-4e6a-404a-9bba-11b7eb025b45.png)
<-

Maintenant je vais mettre seulement 1 point à la fin de la ligne 2 (`a` puis deux fois sur [retour arrière](https://fr.wikipedia.org/wiki/Retour_arrière#:~:text=Retour%20arrière%2C%20espace%20arrière%20ou,pour%20«%20revenir%20en%20arrière%20». "Page Wikipedia de la touche retour arrière") et `Esc` pour quitter le mode insertion).  En plus, je vais décaler la ligne 1 vers la gauche (`k` pour passer le curseur à la ligne du dessus puis `<<` pour décaler).

Voici notre fichier maintenant:

->
![](/media/galleries/11359/696452d9-3526-48fb-b55f-7a2adfa58b44.png)
<-

Finalement on se rend compte qu'on préférait lorsque la première ligne était décalée vers la droite.  
On pourrait la redécaler avec la commande `>>` cependant dans notre cas, on souhaite annuler l'action précédente, on utilise la commande `u` (comme "undo") et voici le résultat:

->
![](/media/galleries/11359/d478a535-ecc1-4bf7-a2ee-246a935e5019.png)
<-

Et en fait, on va aussi remettre les 3 points. Pour cela on a juste à réutiliser la commande `u`.

->
![](/media/galleries/11359/020d7a97-080d-499c-92e9-fd9a0a9aabc5.png)
<-

Mais bon, avec beaucoup d'hésitation on préfère ne laisser qu'un point à la fin de la ligne. On va donc annuler la dernière annulation, on utilise la commande `Ctrl + r` (comme "redo").

Voilà le fichier après la commande `Ctrl + r`:

->
![](/media/galleries/11359/dcc691a8-650d-4820-a01a-3f2215299b56.png)
<-

[[attention | On sait maintenant:]]
| - Décaler la ligne du curseur vers la droite ou la gauche (avec `<<` et `>>`).
| - Décaler N lignes à partir du curseur vers la droite ou la gauche (avec `N<<` et `N>>`, N étant un nombre).
| - Annuler la dernière action effectuée (avec `u`).
| - Annuler l'annulation de la dernière action effectuée (avec `Ctrl + r`).