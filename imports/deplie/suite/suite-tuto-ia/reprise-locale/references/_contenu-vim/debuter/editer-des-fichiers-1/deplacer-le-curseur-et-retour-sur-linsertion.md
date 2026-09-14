# Déplacer le curseur

Nous avons déjà vu comment déplacer le curseur lorsque nous étions en mode insertion. Notez qu'on peut le déplacer très rapidement grâce à des commandes. Ici nous n'en verrons seulement quelques-unes, un chapitre entier est dédié aux commandes.

Avant d'être en mode insertion on peut déplacer le curseur avec les flèches directionnelles, cependant, cette méthode ne fonctionne pas dans [vi](https://fr.wikipedia.org/wiki/Vi). L'autre moyen de déplacer le curseur est avec les touches du clavier `h`, `j`, `k`, et `l`.

- `h` permet d'aller vers la gauche (équivalant à la touche `←`)
- `j` permet d'aller vers le bas (équivalant à la touche `↓`)
- `k` permet d'aller vers le haut (équivalant à la touche `↑`)
- `l` permet d'aller vers la droite (équivalant à la touche `→`)

[[information]]
| Les touches `h`, `j`, `k`, et `l` sont placées telles quelles sur le clavier. On peut facilement retenir quel mouvement va faire le curseur car `h` est à gauche, `j` peut faire penser à une flèche vers le bas, et `l` est tout à droite.

L'intérêt d'utiliser ces touches est de ne pas avoir à déplacer sa main entre les lettres et les flèches du clavier entre les moments de déplacement du curseur et d'écriture. Cela vous permettra d'être plus rapide quand vous serez à l'aise avec Vim.

[[information]]
| Certainer personnes pensent qu'il ne faut pas utiliser les flèches directionnelles pour se déplacer dans Vim. Pour ma part j'utilise les lettres et les flèches.

Deux autres raccourcis pratiques sont `gg` et `G`. Ils permettent respectivement de se rendre sur **la première**, et sur  **la dernière** ligne du fichier.

[[information]]
| Il existe **beaucoup** d'autres manières de déplacer le curseur avec les commandes, nous les verrons dans le chapitre dédié aux commandes.

# Retour sur l'insertion

Nous savons déjà ajouter du texte avant le curseur, on utilise la touche `i`. Néanmoins, on peut aussi utiliser la touche `a` pour insérer du texte **après** le curseur.  
Voici un exemple:

->
![](/media/galleries/11359/a9f88519-779b-4f69-a5b6-fd3465c4f448.png)
<-

Mon curseur se situe sur le "o" de "pour", c'est le rectangle gris.  
Maintenant, je presse `i` pour insérer **avant** le curseur et je vais mettre un "B". Voici le résultat:

->
![](/media/galleries/11359/3875aabe-2171-4401-be88-f56d1332d9e7.png)
<-

À présent, je vais effectuer la même démarche, cependant le vais utiliser `a` à la place de `i` pour insérer **après** le curseur.

->
![](/media/galleries/11359/819ebabd-ef4e-4baa-b848-93ab99d1ba6d.png)
<-

Comme précédemment, je vais faire `a` suivi de "B", pour insérer avant le curseur un "B". Voici le résultat:

->
![](/media/galleries/11359/743b6860-15f5-4aff-8dbf-aebd38913a8f.png)
<-

Le "B" a été ajouté après le "o".

La différence entre les commandes `a` et `i` peut, pour le moment vous sembler insignifiante. Car pourquoi faire `a` quand on peut faire `i` puis déplacer le curseur ? Et bien parce que ça fait appuyer sur deux touches au lieu d'une seule, de ce fait, selon les cas, l'un est beaucoup plus rapide que l'autre.  :D 

Deux autres actions que nous faisons très souvent c'est d'ajouter du texte au début ou à la fin d'une ligne.  
Pour cela on pourrait presser `h` ou `l` pour aller au début ou à la fin de la ligne puis presser `i` ou `a` pour ajouter notre texte.  
Cependant faire cela est long, c'est pourquoi Vim met à notre disposition une commande pour chacune de ces actions. C'est `I` pour insérer du texte au début de la ligne et `A` pour insérer à la fin de la ligne.

Essayons, je commence par la commande `I`:

->
![](/media/galleries/11359/74df34f3-d22f-4d8d-8d9c-a5c2da7fa43d.png)
<-

Mon curseur se situe sur le "o" de "pour". Je presse `I` pour insérer au début de la ligne puis "B". Voici le résultat:

->
![](/media/galleries/11359/797c5c87-5259-4827-9c6b-e3eaf1467669.png)
<-

Mon curseur est allé au début de la ligne et j'ai inséré le "B".

Maintenant voyons ce que cela donne avec la commande `A`.

->
![](/media/galleries/11359/8457e099-ce73-46fc-9384-59210c62486a.png)
<-

Je presse `A` et ensuite "B", voici le résultat:

->
![](/media/galleries/11359/da589970-f62e-414f-9aa5-3132fe659558.png)
<-

En pressant seulement deux touches, j'ai pu insérer le "B" à la fin de la ligne.

Tout comme insérer du texte au début et à la fin d'une ligne, on a souvent besoin d'insérer au-dessus ou au-dessous de la ligne sur laquelle se trouve notre curseur.  
Pour cela, Vim met à notre disposition deux commandes `O` et `o`.

Voici la démonstration de la commande `O`:

->
![](/media/galleries/11359/20881a19-9c68-446d-8a58-f30fb0fdf413.png)
<-

Mince, j'ai oublié la ligne 3 et mon curseur est sur le "t". Je vais ajouter la ligne au-dessus de celle où se situe mon curseur.  
Je presse la touche `O` et j'écris mon texte. Voici le résultat:

->
![](/media/galleries/11359/32a33414-e0ac-45bc-bb8d-a8e673f459fb.png)
<-

Maintenant voici la même situation à la différence que je suis sur le "g" de la ligne 2.

->
![](/media/galleries/11359/bdb33cda-c28d-48c9-a879-677ccef6ec80.png)
<-

J'ai ici aussi oublié la ligne 3, je vais l'ajouter avec la commande `o`. Voici le résultat:

->
![](/media/galleries/11359/69905eb0-ecf6-448f-89ae-7c8b7f6b564e.png)
<-

J'ai ajouté la ligne en dessous de mon curseur.


[[attention | On sait maintenant:]]
| - Déplacer le curseur (avec `h`, `j`, `k` et `l` ou `←`, `↓`, `↑` et `→`).
| - Déplacer le curseur au début et à la fin du fichier (avec `gg` et `G`).
| - Insérer du texte avant et après notre curseur (avec `i` et `a`).
| - Insérer du texte au début et à la fin de la ligne (avec `I` et `A`).
| - Insérer du texte au-dessus et au-dessous de la ligne (avec `O` et `o`).