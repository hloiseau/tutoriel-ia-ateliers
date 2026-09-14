# Chercher dans un fichier

Quelque chose de très utile est de trouver toutes les occurrences d'une chaine de caractère, dans la plupart des navigateurs web cette commande est `Ctrl + f`.  
Dans Vim on fait `/` suivi du texte que l'on cherche.

[[information]]
| Quand on fait une recherche avec `/`, Vim s’attend à une [expression régulière](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re). Vous pouvez donc avoir des résultats qui vous semblent bizarres si vous cherchez des caractères spéciaux.

Voici un fichier nous parlant du chat:

->
![](/media/galleries/11359/e56f070a-3bf9-4fd0-91ff-60d407a49b70.png)
<-

Dans ce fichier on va chercher toutes les occurrences du mot "chat". On tape donc `/chat`. Voici ce que Vim nous donne:

->
![](/media/galleries/11359/d8ee3889-2d9b-4a0a-96a7-dcf560fbe067.png)
<-

Vim a placé notre curseur sur la première chaine de caractère correspondante qu'il a trouvé. Pour se déplacer directement à l'occurrence suivante nous allons utiliser la commande `n` comme next (et `N` pour la précédente).

Je vous laisse essayer ces deux commandes de votre côté.

[[information]]
| Nous verrons dans la partie personnalisation comment rendre la recherche plus visuelle. Voici un exemple de ce que nous pourrions obtenir:
|
| ->
| ![](/media/galleries/11359/6f870f0b-bc6d-4a31-b05d-5afab346db8d.png)
| <-
| Les occurrences ne sont pas sensibles à la case et elles sont surlignées.

# Suppression et remplacement rapide

Je ne suis pas très fort en orthographe mais quand je me relis, j'arrive à voir mes fautes.  
Voici mon texte:

->
![](/media/galleries/11359/54158b6a-637c-465b-9092-5e311d2f136e.png)
<-

Quelle catastrophe ! "Le chat" est singulier et ne prend pas de "s" et le verbe "manjer" n'existe pas, c'est "man**g**er"

Qu'avons-nous à faire ?

- Remplacer le "j" par un "g"
- Supprimer le "s"

Nous pouvons faire ces actions sans entrer en mode insertion.

Premièrement, nous allons placer le curseur sur le "j":

->
![](/media/galleries/11359/ea0f9999-8775-4923-9bb9-d0d46fb39b8d.png)
<-

Maintenant je vais utiliser la commande `r` (comme remplacer ou replace en anglais). Il faut taper `r` suivis d'un caractère. Cela a pour effet de remplacer le caractère sous le curseur par le caractère tapé.

Je vais donc taper sur mon clavier `r` puis `g`. Et voilà le résultat !

->
![](/media/galleries/11359/13de892d-aedd-4949-a51c-08cdc599991e.png)
<-

Le "j" a été remplacé par le "g".

Maintenant nous allons placer notre curseur sur le "s" du mot "chats".

->
![](/media/galleries/11359/f3669ca2-cd17-4013-82fb-7603784a253a.png)
<-

À présent j'utilise la commande `x` et voici le résultat:

->
![](/media/galleries/11359/bda9d9f2-8830-4145-8e91-cdf9b31d5e70.png)
<-

Le "s" a été supprimé.

[[information]]
| On peut taper un nombre avant le `x`, par exemple `5x`. Cela aura pour effet de supprimer 5 caractères.

# Répéter la dernière action

Il est souvent très utile de répéter la dernière commande que nous venons de faire, imaginons le fichier suivant:

->
![](/media/galleries/11359/b4314c2e-bb04-422f-b3d3-d1b06b51c725.png)
<-

Je veux décaler les parties avec des lettres d'un cran vers la gauche.  
Je commence par me placer sur la partie **A** de la partie **1**. Comme vous le savez déjà, pour décaler les 3 lignes vers la gauche on fait la commande `3<<` et voici le résultat:

->
![](/media/galleries/11359/046b66aa-5c33-469b-a280-3067ddfc63e4.png)
<-

Maintenant, on se place sur la partie **A** de ma partie **2**. Au lieu de répéter la commande `3<<` on va simplement faire `.`. Je répète l'opération sur la partie **A** des parties **3** et **4**.

Voilà notre fichier maintenant:

->
![](/media/galleries/11359/e9c394c2-cf5b-4036-9e4a-ce8ada95a065.png)
<-

Comme vous le voyez la commande `.` répète la commande précédente. Son avantage va être de pouvoir répété des commandes complexes (nous verrons les commandes en détail dans un chapitre suivant) sans les retaper entièrement à chaque fois.

[[attention | On sait maintenant:]]
| - Chercher les occurrences dans un fichier (avec `/` suivi de ce qu'on cherche).
| - Passer à l'occurrence suivante ou précédente (avec `n` et `N`).
| - Remplacer le caractère sous le curseur (avec `r` suivi du caractère remplaçait).
| - Supprimer le caractère sous le curseur (avec `x`).
| - Supprimer N caractères à partir du curseur (avec `Nx`, N étant un nombre).
| - Répéter la dernière commande que nous avons faite (avec `.`).