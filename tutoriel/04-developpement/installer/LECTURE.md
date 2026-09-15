# 2. Installer l’assistant et observer le problème

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Choisir de quoi suivre l’atelier](../outils/LECTURE.md) · [Suivant : Décider ce que le ticket veut changer](../02-demande/LECTURE.md)

**TL;DR** — Nous préparons une copie de travail, ouvrons l’assistant et exécutons le programme. À la fin du chapitre, nous aurons observé le problème et retrouvé la fonction qui le provoque.

## Préparer notre seule copie de travail

Téléchargez [les fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/b95165289276a45bc299d0826e3c540727e8e203/telechargements/annexes-developpement-v1.zip), puis décompressez l’archive. Le dossier `atelier-developpement` contient trois états du même projet :

| Dossier fourni | À quoi il nous servira |
| --- | --- |
| `01-depart` | Le programme avant notre modification |
| `02-test-rouge` | Les tests de référence, avant la correction |
| `03-corrige` | La correction à consulter après avoir essayé |
Table: Les fichiers de départ et les corrections

Copiez **`01-depart`** dans un nouveau dossier nommé **`mon-suivi`**, en dehors du dossier téléchargé. Gardez les trois versions fournies à leur emplacement d’origine. `mon-suivi` sera notre seule copie de travail ; nous ne repartirons pas de zéro à chaque chapitre.

Installez [Visual Studio Code](https://code.visualstudio.com/download), puis utilisez **Fichier → Ouvrir le dossier** pour ouvrir `mon-suivi`. Si vous avez déjà un éditeur et un assistant, ouvrez cette même copie avec eux et passez à « Observer le problème ».

Dans l’explorateur, vous devez retrouver `suivi.py`, `test_suivi.py`, `TICKET.md` et `scenarios`. Les dossiers de correction restent en dehors de l’espace de travail : autant éviter de laisser la réponse sous le nez de l’agent. 🙂

## Ouvrir la discussion dans VS Code

Dans VS Code, ouvrez le menu de l’icône Copilot dans la barre d’état, choisissez **Use AI Features**, puis suivez la connexion à GitHub. L’offre gratuite peut être proposée à un compte éligible ; le tableau de bord Copilot permet de consulter son usage[^p4-install-copilot].

Ouvrez ensuite la vue **Chat**. Pour la première lecture, utilisez une session **Local** et le rôle **Ask**, avec un modèle accessible par votre compte Copilot. Ici, *Local* désigne l’exécution des outils de VS Code, pas l’hébergement du modèle. Le rôle Ask permet de poser des questions sans modifier le code[^p4-install-roles].

Les interfaces évoluent. Si vous utilisez une autre version ou un autre assistant, cherchez la fonction de discussion sans édition. Nous lui fournirons nous-mêmes le court extrait à expliquer.

Si l’accès au modèle est bloqué, regardez le compte connecté et le quota disponible avant de relancer la demande. Vous pouvez continuer les manipulations Python pendant que cet accès est indisponible.

Laissez la discussion ouverte. Nous allons d’abord exécuter le programme pour avoir quelque chose de précis à lui montrer.

[^p4-install-copilot]: Microsoft, [configuration de Copilot dans VS Code](https://code.visualstudio.com/docs/setup/copilot).
[^p4-install-roles]: Microsoft, [cibles de session et rôles Ask et Agent](https://code.visualstudio.com/docs/agents/run/agent-harnesses).

## Observer le problème

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

Les tests passent, et nous venons pourtant de reproduire le comportement à changer. Ils ne couvraient donc pas ce cas. Le programme se contente d’afficher sa décision : aucun courriel n’est envoyé.

[^p4-unittest]: Python, [découverte et exécution des tests avec unittest](https://docs.python.org/3.12/library/unittest.html).

## Retrouver la décision et la faire expliquer

Ouvrez `suivi.py`. La fonction `main` lit le fichier JSON ; `lire_etat` construit les deux objets `Etat` ; `notifier` reçoit ces objets et décide du résultat.

![Le fichier JSON est lu, transformé en deux états puis envoyé à la fonction de décision](../images/projet.png)
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



---

[Précédent : Choisir de quoi suivre l’atelier](../outils/LECTURE.md) · [Suivant : Décider ce que le ticket veut changer](../02-demande/LECTURE.md)
