Ouvrez `scenarios/retour-stock.json`. Il décrit deux observations du même produit : un prix de 2 000 centimes avant et après, avec un passage d’indisponible à disponible.

Lancez :

```bash
python suivi.py scenarios/retour-stock.json
```

Le programme initial affiche :

```json
{"notifier": true}
```
Code: Décision du programme avant notre modification

Il n’envoie aucun courriel et ne contacte aucun service : il calcule une décision et l’affiche. Nous pouvons donc rejouer le scénario autant de fois que nécessaire.

Ouvrez maintenant `suivi.py` et suivez les appels. `main` charge le fichier JSON. `lire_etat` vérifie les champs de chaque observation et crée un `Etat`. La fonction `notifier` reçoit l’ancien et le nouvel état, puis renvoie un booléen. Enfin, `main` affiche ce résultat en JSON.

![Le fichier JSON est lu, transformé en deux états puis envoyé à la fonction de décision](image:images/projet.png)
Figure: Le parcours d’un scénario dans notre programme

Vous n’avez pas besoin de mémoriser tout le fichier. En revanche, vous devez pouvoir montrer la fonction qui décide et expliquer quelles données elle reçoit. Essayez de la retrouver une deuxième fois sans relire ce paragraphe.
