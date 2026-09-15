Ouvrez `suivi.py`. La fonction `main` lit le fichier JSON ; `lire_etat` construit les deux objets `Etat` ; `notifier` reçoit ces objets et décide du résultat.

![Le fichier JSON est lu, transformé en deux états puis envoyé à la fonction de décision](image:images/projet.png)
Figure: Le chemin de notre scénario

Retrouvez `notifier` dans le fichier. Copiez cette fonction et la définition de `Etat` dans la discussion, puis envoyez :

```text
Explique quand notifier renvoie True.
Pour ancien = Etat(2000, False) et nouveau = Etat(2000, True),
donne la valeur de chaque condition et le résultat final.
Appuie-toi sur ce code. Ne propose pas encore de correction.
```
Code: Demander une explication que l’on peut vérifier

Gardez la fonction sous les yeux pendant la lecture. `nouveau.disponible` vaut vrai ; la comparaison des prix vaut faux ; `not ancien.disponible` vaut vrai. Le `or` suffit donc à rendre vraie la parenthèse, puis la fonction entière.

Si l’explication de l’assistant aboutit à faux, confrontez-la à ces trois valeurs et au résultat que vous avez exécuté. C’est un désaccord précis à lui montrer, sans lui demander vaguement de « mieux réfléchir ».

Nous savons maintenant où intervenir. Ouvrons le ticket pour décider ce qui doit remplacer cette règle.
