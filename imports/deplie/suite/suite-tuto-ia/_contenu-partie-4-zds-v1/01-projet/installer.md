[Téléchargez l’atelier de suivi de prix](annexes-developpement-v1.zip) et décompressez-le. Le dossier `atelier-developpement` contient trois états du projet : `01-depart`, `02-test-rouge` et `03-corrige`.

Copiez `01-depart` dans un nouveau dossier nommé `mon-suivi`. C’est dans cette copie que vous allez travailler. Les deux autres dossiers permettent de reprendre à une étape connue ou de comparer votre résultat ; ne les ajoutez pas au contexte de l’agent si vous souhaitez observer comment il résout le problème.

Ouvrez un terminal dans `mon-suivi` et lancez :

```bash
python --version
python -m unittest discover -v
```
Code: Contrôler le point de départ

Nous utilisons Python 3.12 et sa bibliothèque standard. Comme dans l’atelier précédent, remplacez `python` par `python3` ou `py -3.12` selon votre installation. Aucune dépendance n’est à télécharger pour ce projet.

La suite initiale contient **trois tests**, qui passent. La durée affichée dépend de votre machine ; ce qui nous intéresse pour le moment, ce sont leurs noms et leur résultat.

Si vous lisez « Ran 0 tests », vous n’avez pas encore vérifié le projet. Regardez le dossier courant et la présence de `test_suivi.py`. Un lancement sans test trouvé peut se terminer sans erreur, ce qui rend la dernière ligne trompeuse si on la lit seule.[^p4-unittest]

[^p4-unittest]: Python, [découverte et exécution des tests avec `unittest`](https://docs.python.org/3.12/library/unittest.html).
