Nous allons écrire la chanson de la bataille de Reichshoffen.

Nous avons un premier fichier qui contient notre couplet:

```txt
C’était un soir la bataille de Reichshoffen
Il fallait voir les cavaliers charger.
Attention cavaliers, chargez !
```
Code: couplet.txt

Voici ensuite le fichier qui contient notre chanson:

```txt
<couplet>
D’une main…

<couplet>
D’une main, de deux mains…

<couplet>
D’une main, de deux mains, d’un pied…

<couplet>
D’une main, de deux mains, d’un pied, de deux pieds…
```
Code: la_bataille_de_reichshoffen.txt

À présent, votre mission si vous l'acceptez, est de remplacer les `<couplet>` par le contenu du fichier `couplet.txt` en utilisant la commande `:read`.