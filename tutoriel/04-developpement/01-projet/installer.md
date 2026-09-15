Votre dossier `mon-suivi` est déjà ouvert dans l’éditeur depuis l’installation de l’assistant. Gardez cette copie : inutile de télécharger ou de recopier le projet une seconde fois.

Ouvrez un terminal dans ce dossier. Il doit contenir `suivi.py` et `scenarios`. Pour exécuter cet atelier, nous utilisons Python 3.12 ; aucune bibliothèque externe n’est nécessaire.

```bash
python -m unittest discover -v
python suivi.py scenarios/retour-stock.json
```
Code: Lancer les tests existants et le scénario de remise en stock

Si votre installation utilise la commande `python3` ou `py -3.12`, utilisez-la à la place de `python` dans les commandes de l’atelier.

Les trois tests de départ passent. Le scénario affiche pourtant une décision de notification pour une simple remise en stock. Le programme n’envoie rien sur le réseau : il affiche sa décision en JSON.

Nous allons suivre le chemin qui mène à cette décision avant de demander une correction.

Si vous lisez « Ran 0 tests », vous n’avez pas encore vérifié le projet. Regardez le dossier courant et la présence de `test_suivi.py`. Un lancement sans test trouvé peut se terminer sans erreur, ce qui rend la dernière ligne trompeuse si on la lit seule.[^p4-unittest]

[^p4-unittest]: Python, [découverte et exécution des tests avec `unittest`](https://docs.python.org/3.12/library/unittest.html).
