# 4. Ouvrir un projet que l’on peut comprendre

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** nous allons lire le programme et vérifier son état de départ. Un agent peut nous aider à nous repérer, mais les fichiers restent notre point de contrôle.

## Lancer les tests du projet

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

## Suivre une entrée jusqu’à la décision

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

![Le fichier JSON est lu, transformé en deux états puis envoyé à la fonction de décision](../images/projet.png)
Figure: Le parcours d’un scénario dans notre programme

Vous n’avez pas besoin de mémoriser tout le fichier. En revanche, vous devez pouvoir montrer la fonction qui décide et expliquer quelles données elle reçoit. Essayez de la retrouver une deuxième fois sans relire ce paragraphe.

## Demander de l’aide pour lire

Si vous utilisez un agent, ouvrez uniquement le dossier `mon-suivi` dans son espace de travail. Commencez par une demande de lecture :

```text
Lis README.md, suivi.py, test_suivi.py et TICKET.md.
Explique le chemin entre le fichier JSON et la décision.
Cite les fonctions concernées.
N’édite aucun fichier pendant cette lecture.
Signale les questions auxquelles les fichiers ne répondent pas.
```
Code: Une consigne pour se repérer dans le projet

Cette consigne peut être utilisée dans différents outils. La manière de choisir le dossier et d’autoriser une lecture dépend de votre application. Vérifiez ce périmètre dans son interface avant de lui demander d’agir.

Comparez ensuite son explication au code. S’il parle d’une file de messages, d’un appel réseau ou d’une base de données, cherchez où cela apparaît. Dans notre projet, aucun de ces éléments n’existe. Une explication plausible n’est pas une preuve de lecture.

Vous pouvez aussi lui demander d’expliquer une ligne précise, puis reformuler vous-même son rôle. C’est particulièrement utile quand on apprend un langage : on garde un passage court, dont on peut vérifier chaque détail.


