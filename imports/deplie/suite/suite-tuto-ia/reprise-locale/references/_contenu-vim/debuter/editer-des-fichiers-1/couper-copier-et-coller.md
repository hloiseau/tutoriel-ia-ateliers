Quand on fait un copier coller dans les logiciels graphiques on utilise la souris. On commence par faire une sélection (on place le curseur au début de notre sélection, maintient le clic gauche et on déplace pour sélectionner). Ensuite on fait `Ctrl + c` pour copier le texte (ou `Ctrl + x` pour couper). On déplace le curseur à l'endroit où l'on veut puis on fait `Ctrl + v` pour coller le texte.

Dans Vim les étapes pour copier coller sont similaires.

Voici notre texte:

->
![](/media/galleries/11359/3a273d37-54b5-4508-9628-cdbd08700b7c.png)
<-

Déjà, il y a un chiffre dans notre alphabet, pour le supprimer on se place sur le "5" et on fait `3x`.

->
![](/media/galleries/11359/e19e7788-dc71-4ea1-bb24-70ac815ee176.png)
<-

On vois que les lettres "d" et "e" ne sont pas à la bonne place, je vais positionner mon curseur sur le "d", appuyer sur `v` et déplacer le curseur juste avant le "h".

[[information]]
| La commande `v` permet de passer en **mode visuel**, ce mode nous permet de faire une sélection.

Le texte sélectionné est surligné en gris.

->
![](/media/galleries/11359/00004ddb-274b-4fe3-a3e0-3292a3982158.png)
<-

Pour couper, on appuie sur `d` (comme "delete") (si on veut copier on utilisera `y` (comme "yank")).

->
![](/media/galleries/11359/ae55f005-89e6-4efa-a9be-24b97a9fa86c.png)
<-

Maintenant on va déplacer notre curseur juste avant le "f" et utiliser la commande `p` (comme "paste") pour coller.

->
![](/media/galleries/11359/9a250413-05bd-4a87-865b-a111a70da145.png)
<-

Voilà, notre alphabet est dans l'ordre !

[[information]]
| Pour coller du texte il y a deux commandes, `p` pour coller après le curseur et `P` pour avant.
| 
| Voici notre situation initiale avec du texte déjà coupé et le curseur sur le caractère "↑"
|
| ->
| ![](/media/galleries/11359/c7a468d7-c1a8-4258-88ae-6aed0ea478b6.png)
| <-
|
| Je colle le texte avec `p`:
|
| ->
| ![](/media/galleries/11359/abaa0113-5b4c-4f1d-8a00-18f78cacec39.png)
| <-
|
| Je colle avec `P`:
|
| ->
| ![](/media/galleries/11359/a000185b-e20e-4fbd-bd86-8a15d08de351.png)
| <-

Passer par le mode visuel pour sélectionner son texte est bien pratique, cependant le déplacement du curseur est plutôt long car on le déplace caractère par caractère. Il y a des commandes pour le déplacer rapidement mais nous verrons ça dans un autre chapitre. Ici je voudrais introduire des nouvelles commandes pour couper, copier et coller mais des lignes entières sans passer par le mode visuel.

Considérons le fichier suivant:

->
![](/media/galleries/11359/b0792b88-e3e4-4a45-8057-f5741bf69ed4.png)
<-

On va commencer par supprimer la ligne 42, pour cela on place notre curseur sur la ligne et on va la couper avec la commande `dd`.

->
![](/media/galleries/11359/ea875612-3572-482b-9fda-6812e0a8e4f7.png)
<-

Les lignes 3 et 4 sont inversées. Je vais placer le curseur sur la quatrième ligne (ligne avec "Ligne 3") et je vais la couper avec la commande `dd`. Je me place ensuite sur la ligne 2 et je fais `p` pour coller la ligne sous celle du curseur.  
Voici le résultat:

->
![](/media/galleries/11359/5cde7a78-633f-4930-8c06-ea33f432fddd.png)
<-

[[information]]
| On peut tout aussi bien coller la ligne au-dessus de celle du curseur avec la commande `P` (au lieu de `p`). Je vous laisse expérimenter cette commande.

Pour le moment nous avons seulement coupé les lignes. Pour les copier c'est la commande `Y` (à la place de `dd`). Ensuite pour les coller on utilise les commandes `p` ou `P`.

Vim permet de couper et copier plusieurs lignes d'un coup. Imaginons le fichier suivant:

->
![](/media/galleries/11359/c90d1704-1913-43a2-8a47-7c4f843bfd06.png)
<-

Je vais déplacer les lignes 4, 5 et 6 dans la partie B, pour cela je les coupe les 3 lignes en faisant `3dd` à partir de la "Ligne 4". Je déplace le curseur à la fin du fichier avec `G` (car "Partie B" est la dernière ligne du fichier). Et je vais coller sous la ligne du curseur avec `p`.  
Voilà le résultat:

->
![](/media/galleries/11359/6d685af7-e02f-4e09-9e13-50205c05b974.png)
<-

Maintenant je vais copier les lignes 1 à 3 de la partie A dans la partie B.  
Je me place le curseur sur la ligne avec "Ligne 1". Je vais ensuite faire `3Y` pour copier les 3 lignes. Je mets le curseur sur la ligne "Partie B" et je fais `p` pour coller le texte copier.  
Et voilà ce que nous avons à présent:

->
![](/media/galleries/11359/64ed3483-fb0b-4966-b2b2-032758b81811.png)
<-

[[attention | On sait maintenant:]]
| - Passer en mode visuel (avec `v`) et sélectionner du texte (en déplaçait le curseur).
| - Couper le texte sélectionné (avec `d`).
| - Copier le texte sélectionné (avec `y`).
| - Coller la sélection après le curseur (avec `p`).
| - Coller la sélection avant le curseur (avec `P`).
| - Couper une ligne (avec `dd`).
| - Copier une ligne (avec `Y`).
| - Coller la (ou les) ligne(s) sur la ligne suivante au curseur (avec `p`).
| - Coller la (ou les) ligne(s) sur la ligne précédente au curseur (avec `P`).
| - Couper N lignes (avec `Ndd`, N étant un nombre).
| - Copier N lignes (avec `NY`, N étant un nombre).