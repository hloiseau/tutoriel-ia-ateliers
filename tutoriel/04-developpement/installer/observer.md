Dans l’éditeur, ouvrez **Terminal → Nouveau terminal**. Il doit être placé dans `mon-suivi`, le dossier qui contient `suivi.py`. Nous utiliserons Python 3.12 ; aucune bibliothèque supplémentaire n’est nécessaire.

```bash
python --version
python -m unittest discover -v
```
Code: Vérifier Python et lancer les tests de départ

Si votre installation utilise `python3` ou `py -3.12`, remplacez `python` par cette commande dans la suite.

Vous devez obtenir **trois tests réussis**. Si vous voyez `Ran 0 tests`, vérifiez le dossier courant et la présence de `test_suivi.py` : aucune fonction n’a encore été testée[^p4-unittest].

Ouvrez maintenant `scenarios/retour-stock.json`. Le produit passe d’indisponible à disponible, mais son prix reste à 2 000 centimes. Exécutez ce scénario :

```bash
python suivi.py scenarios/retour-stock.json
```

Le programme initial affiche :

```json
{"notifier": true}
```
Code: Une notification décidée sans baisse de prix

Voilà notre point de départ : la suite est verte, tandis que le scénario du ticket produit la mauvaise décision. Les trois tests existants n’exercent donc jamais ce retour en stock. Le programme se contente d’afficher sa décision ; aucun courriel n’est envoyé.

[^p4-unittest]: Python, [découverte et exécution des tests avec unittest](https://docs.python.org/3.12/library/unittest.html).
