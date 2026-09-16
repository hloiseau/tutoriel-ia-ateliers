# Développer avec une IA, du problème au changement vérifié

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Nous allons suivre un correctif de bout en bout avec l’aide d’un agent : observer le problème, l’enfermer dans un test, modifier le code puis vérifier le résultat. Nous garderons le même dossier de travail jusqu’au compte rendu final.

Les trois tests passent. Pourtant, notre suivi de prix annonce une bonne affaire… alors que le prix n’a pas baissé. Voilà un programme un peu trop enthousiaste. 😅

Nous allons lui retirer cette habitude. La correction tient presque sur un timbre-poste ; tout ce qui permet de lui faire confiance prend un peu plus de place. Nous suivrons les fichiers lus par l’agent, les tests qu’il écrit, les commandes qu’il lance et le diff qu’il nous rend.

Dans la partie précédente, nous faisions tourner un modèle chez nous. Pour cet atelier, nous utiliserons un assistant de développement avec un modèle hébergé. Vous n’avez donc pas besoin d’une grosse carte graphique. Si vous avez déjà un assistant, gardez-le ; sinon, nous décrirons une installation avec VS Code et GitHub Copilot. L’accès gratuit dépend de votre compte et de son quota.

Il vous faut savoir ouvrir un terminal, lancer un programme Python et lire une fonction simple. Le projet utilise Python 3.12 et sa bibliothèque standard. Nous expliquerons les assertions de test et la condition qui nous intéressent.

Les **sept chapitres de cette partie** suivent ce même correctif. Si vous hésitez encore entre plusieurs assistants, l’annexe [« Comparer les outils et leurs tarifs »](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/annexes/comparatif/LECTURE.md) rassemble le panorama complet, dont Pi. L’**expérience locale avec Continue** se trouve également dans les annexes. Elle reste à vérifier sur machine et porte sur une discussion avec un modèle local, pas sur une session complète d’agent de code.

Les fichiers du projet sont publics et le ticket est fictif. Nous pouvons les montrer au service choisi sans utiliser le code de notre entreprise. Si vous préférez travailler sans IA, les tests et les corrections expliquées permettent aussi de suivre l’exercice.

## 1. Choisir de quoi suivre l’atelier

**TL;DR** — Pour l’atelier, il nous faut discuter du code, modifier un fichier et lire le résultat des tests. Gardez un assistant qui sait déjà le faire ; sinon, nous allons préparer VS Code avec Copilot.

Avant d’ouvrir l’éditeur, suivons le trajet de notre code. Cela permettra de savoir ce qui reste sur notre machine, ce qui part vers le fournisseur du modèle et quel logiciel exécutera les commandes.

### Où tournent le code et le modèle ?

Dans la partie précédente, notre client envoyait une question à `llama-server`, puis le modèle calculait une réponse. Un assistant de développement reprend ce principe en y ajoutant du code, des résultats de commandes et parfois le droit de modifier les fichiers.

Il faut distinguer **l’endroit où l’assistant agit** et **l’endroit où le modèle tourne**. Dans l’installation que nous allons utiliser, l’éditeur et les tests tournent sur notre ordinateur. Le modèle, lui, reçoit le contexte et calcule sa réponse chez le fournisseur.

| Élément | Dans l’atelier |
| --- | --- |
| Projet et tests Python | Sur notre ordinateur |
| Assistant | Dans l’éditeur, avec accès à notre copie de travail |
| Modèle et moteur d’inférence | Chez le fournisseur du modèle |
Table: Où se passe le travail ?

Le calcul lourd ayant lieu chez le fournisseur, cette installation ne demande pas de GPU. On peut aussi faire tourner le modèle chez soi, avec des besoins de mémoire et de calcul à évaluer. Obtenir une réponse courte sur CPU ne suffit pas à établir qu’un modèle soutiendra le rythme et le contexte d’une session d’agent de code.

### Discuter, puis laisser agir

La complétion suggère du code pendant que vous tapez. Nous allons surtout utiliser deux autres fonctions :

- **La discussion** : nous montrons une fonction et demandons une explication. Nous lisons la réponse en gardant le code sous les yeux.
- **Le mode agent** : le modèle peut demander au logiciel de lire ou modifier des fichiers et de lancer des commandes. Les résultats lui reviennent, ce qui lui permet de poursuivre.

Le programme qui organise ces échanges est souvent appelé **harness**. Copilot, Codex, Claude Code, Pi et d’autres ont chacun leur manière d’assembler la conversation, les fichiers et les outils. Le détail de leurs possibilités reste dans l’annexe comparative ; notre correctif, lui, ne dépend d’aucune fonction exotique.

Nous commencerons par une discussion autour d’une fonction copiée dans le chat. Le mode agent n’arrivera qu’avec le premier test : à cet instant, l’assistant devra réellement créer un fichier et exécuter Python.

### Quel outil prendre pour commencer ?

Vous utilisez déjà un assistant capable de lire et modifier un projet ? Gardez-le. Les demandes de l’atelier portent sur des fichiers et des commandes Python ; elles ne dépendent pas d’une marque.

Sinon, nous prendrons **VS Code avec GitHub Copilot** comme exemple d’installation. Ce choix nous donne un parcours concret à décrire ; il ne change pas l’atelier en tutoriel consacré à Copilot. Le [comparatif complet](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/annexes/comparatif/LECTURE.md), daté de septembre 2026, couvre aussi des éditeurs et des agents en terminal, avec leurs modèles, leurs prix et les limites de leurs offres.

Avant de vous connecter, vérifiez deux points :

- Le service peut-il recevoir ces fichiers ? Pour notre petit projet public, oui. Pour votre code professionnel, il faudra connaître les règles de votre équipe.
- Quel accès avez-vous au modèle ? Une offre gratuite peut avoir un quota. Un logiciel libre peut, lui, utiliser une API payante. Le prix du logiciel ne donne donc pas toujours le coût de la tâche.

Copilot propose une offre gratuite sous conditions et avec des limites[^p4-depart-offre]. Si elle n’est pas disponible pour votre compte, vous pouvez utiliser un autre accès que vous possédez ou suivre les corrections expliquées sans agent. Nous n’allons pas vous demander de souscrire pour ouvrir trois fichiers Python. 🙂

[^p4-depart-offre]: GitHub, [offres et limites de Copilot](https://github.com/features/copilot/plans).



## 2. Installer l’assistant et observer le problème

**TL;DR** — Nous préparons une copie de travail, ouvrons l’assistant et exécutons le programme. À la fin du chapitre, nous aurons observé le problème et retrouvé la fonction qui le provoque.

### Préparer notre seule copie de travail

Téléchargez [les fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/b95165289276a45bc299d0826e3c540727e8e203/telechargements/annexes-developpement-v1.zip), puis décompressez l’archive. Le dossier `atelier-developpement` contient trois états du même projet :

| Dossier fourni | À quoi il nous servira |
| --- | --- |
| `01-depart` | Le programme avant notre modification |
| `02-test-rouge` | Les tests de référence, avant la correction |
| `03-corrige` | La correction à consulter après avoir essayé |
Table: Les fichiers de départ et les corrections

Copiez **`01-depart`** dans un nouveau dossier nommé **`mon-suivi`**, en dehors du dossier téléchargé. Gardez les trois versions fournies à leur emplacement d’origine : elles nous serviront de points de comparaison. Toutes nos modifications iront dans `mon-suivi`, sans nouveau départ au chapitre suivant.

Installez [Visual Studio Code](https://code.visualstudio.com/download), puis utilisez **Fichier → Ouvrir le dossier** pour ouvrir `mon-suivi`. Si vous avez déjà un éditeur et un assistant, ouvrez cette même copie avec eux et passez à « Observer le problème ».

Dans l’explorateur, vous devez retrouver `suivi.py`, `test_suivi.py`, `TICKET.md` et `scenarios`. Les dossiers de correction restent en dehors de l’espace de travail : autant éviter de laisser la réponse sous le nez de l’agent. 🙂

À partir d’ici, chaque commande indiquée sans autre précision est à lancer depuis `mon-suivi`.

### Ouvrir la discussion dans VS Code

La documentation de VS Code consultée pour cette partie indique le parcours suivant : ouvrez le menu de l’icône Copilot dans la barre d’état, choisissez **Use AI Features**, puis suivez la connexion à GitHub. L’offre gratuite peut être proposée à un compte éligible ; le tableau de bord Copilot permet de consulter son usage[^p4-install-copilot].

Ouvrez ensuite la vue **Chat**. Pour la première lecture, utilisez une session **Local** et le rôle **Ask**, avec un modèle accessible par votre compte Copilot. Ici, *Local* désigne l’exécution des outils de VS Code, pas l’hébergement du modèle. Le rôle Ask permet de poser des questions sans modifier le code[^p4-install-roles].

Les libellés et leur emplacement peuvent avoir changé depuis ce relevé. Si votre version diffère, cherchez la fonction de discussion sans édition. Avec un autre assistant, ouvrez son mode équivalent : nous lui fournirons nous-mêmes le court extrait à expliquer.

Si l’accès au modèle est bloqué, regardez le compte connecté et le quota disponible avant de relancer la demande. Vous pouvez continuer les manipulations Python pendant que cet accès est indisponible.

Laissez la discussion ouverte. Nous allons d’abord exécuter le programme pour avoir quelque chose de précis à lui montrer.

[^p4-install-copilot]: Microsoft, [configuration de Copilot dans VS Code](https://code.visualstudio.com/docs/setup/copilot).
[^p4-install-roles]: Microsoft, [cibles de session et rôles Ask et Agent](https://code.visualstudio.com/docs/agents/run/agent-harnesses).

### Observer le problème

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

### Retrouver la décision et la faire expliquer

Ouvrez `suivi.py`. La fonction `main` lit le fichier JSON ; `lire_etat` construit les deux objets `Etat` ; `notifier` reçoit ces objets et décide du résultat.

![Le fichier JSON est lu, transformé en deux états puis envoyé à la fonction de décision](images/projet.png)
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

Si l’explication de l’assistant aboutit à faux, renvoyez-lui ces trois valeurs ainsi que le résultat exécuté. Vous aurez un désaccord précis à résoudre, bien plus utile qu’une invitation à « mieux réfléchir ».

Nous avons retrouvé la condition responsable. Le ticket va maintenant nous dire ce qu’elle doit exprimer — et surtout ce qu’elle ne dit pas sur les autres cas.



## 3. Décider ce que le ticket veut changer

**TL;DR** — Le ticket donne une règle courte, mais plusieurs combinaisons de prix et de disponibilité. Nous allons décider leur résultat avant de toucher à la fonction.

### Une remise en stock n’est pas une baisse de prix

Le ticket PRIX-1 demande de ne plus notifier un produit qui revient simplement en stock. Le fichier `TICKET.md` donne la règle complète : une notification est autorisée seulement si le produit est disponible dans le nouvel état **et** si son prix a strictement baissé par rapport à l’observation précédente.

Les prix sont des entiers en centimes. Nous comparons deux observations consécutives, dans une même devise implicite. L’historique des six derniers mois et le calcul d’une promotion restent hors du programme.

Avant de regarder la suite, répondez à ces deux cas :

- Le produit revient en stock au même prix. Faut-il notifier ?
- Le produit revient en stock avec un prix plus bas. Faut-il notifier ?

Le premier cas doit donner **faux**, le second **vrai**. Le titre du ticket, pris tout seul, pourrait faire écarter les deux retours en stock. La règle complète conserve pourtant celui qui s’accompagne d’une baisse.

Ce genre de raccourci arrive vite dans un vrai ticket. Si l’équipe n’a pas décidé comment traiter le second cas, il faut lui poser la question ; laisser l’agent trancher en silence transformerait une supposition en règle métier.

### Écrire la table avant les tests

Voici les cas que nous voulons distinguer :

| Ancien état | Nouvel état | Notification attendue |
| --- | --- | --- |
| 20 €, disponible | 15 €, disponible | Oui |
| 15 €, disponible | 20 €, disponible | Non |
| 20 €, disponible | 15 €, indisponible | Non |
| 20 €, indisponible | 20 €, disponible | Non |
| 20 €, indisponible | 15 €, disponible | Oui |
| 20 €, indisponible | 25 €, disponible | Non |
| 20 €, disponible | 20 €, disponible | Non |
Table: Les situations que la règle doit départager

Les trois premières correspondent déjà à nos tests de départ. Les suivantes rendent visible ce que ces tests ne contrôlaient pas.

Vous pouvez demander à l’agent de proposer cette table avant de coder les tests. Relisez surtout les **résultats attendus**. Dix tests persuadés qu’une hausse mérite une alerte ne rendraient pas cette idée plus juste. 😅

Pour une règle aussi petite, faire la table soi-même prend peu de temps. Dans un projet plus grand, l’aide devient intéressante pour retrouver les voisins d’un cas principal ou traduire une règle déjà décidée en scénarios exécutables.

### Délimiter le changement

Ajoutons quelques limites simples à notre travail : nous conservons la fonction `notifier`, les fichiers JSON et les validations existantes. Nous n’ajoutons pas de base, d’envoi de courriel ou de système de préférences.

Pourquoi le préciser ? Parce qu’une demande d’« amélioration des notifications » pourrait facilement produire une architecture plus ambitieuse que notre besoin. Ici, le programme doit continuer à prendre deux états et à renvoyer une décision.

Ces limites guideront aussi notre revue. Si un nouveau fichier de configuration apparaît dans le diff, nous pourrons demander quel comportement du ticket le rend nécessaire.

Dans votre propre travail, gardez ce périmètre à la taille de la tâche. Une condition à corriger mérite que l’on tranche ses cas ambigus ; elle réclame rarement un document de conception de dix pages.



## 4. Faire apparaître le bug dans un test

**TL;DR** — Nous allons faire ajouter un premier test à l’agent, puis lire son échec. La correction expliquée juste après permet de contrôler ce qu’il a écrit, ou d’ajouter le test vous-même.

### Demander un premier test à l’agent

Gardez `mon-suivi` ouvert : il contient encore la fonction initiale et ses trois tests. Nous allons demander à l’agent d’ajouter **un seul test**, celui de la remise en stock au même prix.

Dans la session **Local** de VS Code, passez du rôle **Ask** au rôle **Agent** avec le sélecteur de la discussion. D’après la documentation consultée, Agent dispose des outils de lecture, d’édition et d’exécution ; Ask nous servait à discuter[^p4-premier-agent]. Avec un autre assistant, activez son mode de modification du projet. Gardez les demandes d’autorisation pour les commandes : nous voulons voir ce qui va réellement être lancé.

Envoyez :

```text
Dans mon-suivi, lis TICKET.md, suivi.py et test_suivi.py.
Crée test_ticket.py avec unittest.
Ajoute uniquement test_retour_en_stock_sans_baisse :
notifier(Etat(2000, False), Etat(2000, True)) doit renvoyer False.
Ne modifie ni suivi.py ni les tests existants.
Lance python -m unittest discover -v depuis mon-suivi.
Rapporte le résultat obtenu et l’assertion en échec.
Ne crée pas de commit et ne publie rien.
```
Code: Notre première demande qui modifie un fichier

Adaptez `python` si vous avez utilisé une autre commande au chapitre précédent. Quand l’outil vous demande d’autoriser une commande, regardez le dossier et la commande affichés. Cet exercice ne demande ni installation de paquet ni accès réseau.

Observez les actions annoncées par l’interface : lecture des fichiers, création du test, lancement de la suite. Si l’agent corrige aussi `suivi.py`, arrêtez-le et remettez **ce seul fichier** dans son état initial à partir de `01-depart`. Gardez le nouveau test : son échec doit précéder la correction.

Si vous travaillez sans agent, créez le test décrit dans la section suivante. Dans les deux cas, nous continuons dans le même dossier.

[^p4-premier-agent]: Microsoft, [rôles disponibles dans une session Local](https://code.visualstudio.com/docs/agents/run/agent-harnesses).

### Écrire le premier test qui échoue

Ouvrez le fichier `test_ticket.py` créé par l’agent. Pour ce premier cas, il peut se réduire à ceci. Si vous faites l’exercice à la main, créez ce fichier maintenant :

```python
import unittest
from suivi import Etat, notifier


class TicketPrix(unittest.TestCase):
    def test_retour_en_stock_sans_baisse(self):
        self.assertFalse(
            notifier(Etat(2000, False), Etat(2000, True))
        )
```
Code: Reproduire le cas du ticket dans un test

`unittest.TestCase` fournit les assertions, et les méthodes dont le nom commence par `test_` sont exécutées comme tests. Ici, `assertFalse` appelle **notre fonction** puis vérifie que sa réponse est fausse. Une comparaison entre deux constantes pourrait donner une jolie coche verte sans jamais exercer `notifier`.

Lancez de nouveau :

```bash
python -m unittest discover -v
```

Avec cet unique nouveau test, vous devez obtenir **quatre tests, dont un en échec**. Le programme renvoie vrai, alors que ce cas attend faux. Cet échec est le résultat recherché : il relie le ticket au comportement fautif avant que nous changions le code.

Lisez le nom du test en échec. Une erreur d’import ou une faute de syntaxe ne prouvent pas que le comportement du ticket est reproduit. Le programme doit atteindre l’assertion, puis échouer parce que sa décision ne correspond pas à celle attendue.

Si votre test passe déjà, vérifiez que vous travaillez bien dans la copie de `01-depart` et que la fonction n’a pas été corrigée par avance. Sans cet échec initial, nous perdrions la preuve que le nouveau test sait reconnaître le bug.

### Ajouter les voisins du cas principal

Nous avons couvert la remise en stock au même prix. Il manque notamment deux voisins : le retour avec une baisse, qui doit notifier, et le retour avec une hausse, qui ne doit pas notifier.

Demandez à l’agent de compléter **le fichier existant**, en lui donnant la table du ticket :

```text
Complète test_ticket.py avec les cas encore absents de cette table.
Conserve les tests déjà écrits et ne modifie pas suivi.py.
Lance la suite et indique quels comportements échouent.
```

Joignez la table à la demande. Vous pouvez aussi écrire ces tests vous-même. Relisez leurs valeurs attendues : `assertTrue` pour une baisse accompagnant le retour, `assertFalse` pour une hausse.

Notre fichier de référence se trouve dans **`02-test-rouge/test_ticket.py`**, parmi les dossiers extraits au début. Ouvrez-le séparément, puis comparez-le au vôtre. Il ajoute une baisse d’un centime, un prix nul et des entrées invalides. Ces derniers cas vérifient que la correction ne détériore pas les validations déjà présentes dans `Etat`.

Avec ce fichier de référence et les trois tests d’origine, on obtient **treize tests, dont deux échouent avant correction** : le retour en stock sans baisse et celui avec hausse. Votre agent peut avoir produit un autre nombre de tests. Comparez les comportements couverts et les échecs, pas seulement le compteur.

![Trois états réellement exécutés : trois tests verts, puis deux échecs sur treize, puis treize tests verts](images/tests.png)
Figure: Les résultats des versions de référence fournies

Pour poursuivre avec la même référence que le tutoriel, remplacez votre seul fichier `test_ticket.py` par celui de `02-test-rouge`, après l’avoir lu. Gardez `suivi.py` dans son état initial. Les deux échecs sont maintenant prêts à juger la correction.



## 5. Faire le changement et lire le diff

**TL;DR** — Les tests rouges fixent le comportement attendu. Nous allons laisser l’agent corriger la fonction, puis confronter son diff au ticket et à ces tests.

### Une demande de modification précise

Les tests reproduisent le problème ; la fonction est encore dans son état initial. Dans la même session, demandez maintenant :

```text
Applique le comportement décrit dans TICKET.md.
Conserve les interfaces existantes et limite la modification
au code nécessaire.
Ne change pas les réponses attendues des tests pour les faire passer.
Lance la suite avec python -m unittest discover -v.
Montre le diff et explique la condition modifiée.
Ne crée pas de commit et ne publie rien.
```
Code: Confier la correction en gardant un résultat relisible

La demande décrit le comportement sans souffler la ligne de correction. Regardez la solution proposée et les fichiers touchés. Si vous faites l’exercice à la main, essayez votre modification avant de lire la section suivante.

Cela reste une consigne au modèle. Pour limiter effectivement son accès aux fichiers, au réseau ou à la publication, utilisez aussi les permissions de votre outil. Une phrase dans un prompt n’a pas le même rôle qu’un droit technique refusant l’opération.

Si l’agent propose une classe de notification, une nouvelle dépendance ou un système de règles pour cette fonction, demandez-lui quel cas du ticket le justifie. En l’absence de réponse concrète, revenez à une modification plus petite. Le temps déjà passé à générer du code ne lui donne aucune valeur particulière.

### Relire les opérateurs

Comparez maintenant sa proposition à la fonction initiale :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
    )
```

Lisez-la à voix haute : le produit doit être disponible maintenant ; ensuite, une baisse de prix **ou** une ancienne indisponibilité suffit.

Le second terme du `or` explique notre problème. Pour un retour en stock, `not ancien.disponible` vaut vrai. Le prix peut être identique ou même plus élevé : l’expression entre parenthèses sera tout de même vraie.

Le ticket exige les deux conditions : une disponibilité actuelle **et** une baisse stricte. Notre correction de référence est :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes
    )
```
Code: La fonction après correction

Une expression sur une ligne peut être tout aussi correcte. Ce que nous cherchons dans la proposition, c’est la disponibilité actuelle et la baisse stricte, sans condition supplémentaire.

Résistez à la tentation d’ajouter `ancien.disponible` dans la nouvelle condition. Une vraie baisse au moment du retour en stock serait alors ignorée, contrairement à la règle décidée.

![Seul le cas disponible maintenant avec baisse de prix autorise une notification](images/decision.png)
Figure: La règle complète tient dans ces quatre combinaisons

### Lire ce qui a vraiment changé

Ouvrez la comparaison des fichiers dans votre éditeur. Dans VS Code, ouvrez la version originale `01-depart/suivi.py` et copiez tout son contenu. Revenez dans `mon-suivi/suivi.py`, ouvrez la palette de commandes et lancez **File: Compare Active File with Clipboard**[^p4-diff-vscode]. Les libellés peuvent être traduits dans votre installation.

Notre correction de référence montre :

```diff
-        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
+        nouveau.prix_centimes < ancien.prix_centimes
```
Code: La règle retirée par notre correction

Si Git est installé, vous pouvez faire la même comparaison depuis un terminal, sans créer de dépôt :

```bash
git diff --no-index "/chemin/vers/atelier-developpement/01-depart/suivi.py" "/chemin/vers/mon-suivi/suivi.py"
```

Remplacez les deux chemins par ceux de vos fichiers. Cette commande ne suppose pas que les dossiers sont voisins. Avec `--no-index`, le code de sortie 1 signifie que les fichiers diffèrent[^p4-diff].

Cette première comparaison ne porte que sur `suivi.py`. Reprenez ensuite la liste des fichiers touchés affichée par l’assistant. Comparez chaque fichier qui existait déjà à son original dans `01-depart`, puis lisez entièrement le nouveau `test_ticket.py`.

Le test ajouté est attendu. Changer les données de `retour-stock.json`, supprimer un test ou modifier une validation sortirait en revanche du correctif demandé. Si vous trouvez l’un de ces changements, demandez sa raison puis retirez-le s’il ne sert aucun cas du ticket.

[^p4-diff-vscode]: Microsoft, [comparaison des fichiers dans VS Code](https://code.visualstudio.com/docs/editing/codebasics#_compare-files).
[^p4-diff]: Git, [comparaison avec git diff --no-index](https://git-scm.com/docs/git-diff).



## 6. Vérifier au-delà de la dernière ligne verte

**TL;DR** — Une suite verte couvre la fonction avec les cas que nous avons écrits. Les scénarios JSON feront ensuite parcourir au programme tout le chemin observé au début.

### Rejouer les tests et contrôler leur nombre

Après correction, lancez :

```bash
python -m unittest discover -v
```

Avec le fichier complet de `02-test-rouge`, les **treize tests passent**. Si vous avez conservé les tests de l’agent, le nombre peut être différent. Vérifiez que les cas décidés dans la table sont couverts et que ceux qui échouaient passent désormais, avec les mêmes valeurs attendues.

Les noms des tests donnent un premier inventaire des situations contrôlées. Retrouvez surtout les deux qui échouaient avant la correction : ils doivent encore être présents, avec les mêmes valeurs attendues.

Dans le rapport de l’agent, cherchez la commande, son dossier d’exécution et son résultat. La formule « tests vérifiés » est trop floue : l’agent a pu lire leur code, en lancer un seul ou exécuter la suite complète.

Une dépendance manquante ou une commande interrompue doit rester visible dans le rapport. Un fichier de test bien écrit ne nous apprend rien sur le résultat d’une exécution qui n’a pas eu lieu.

### Passer par les fichiers JSON

Exécutez maintenant nos trois scénarios :

```bash
python suivi.py scenarios/retour-stock.json
python suivi.py scenarios/baisse.json
python suivi.py scenarios/rupture.json
```

Voici les décisions attendues après correction :

| Fichier | Résultat |
| --- | --- |
| `retour-stock.json` | `{"notifier": false}` |
| `baisse.json` | `{"notifier": true}` |
| `rupture.json` | `{"notifier": false}` |
Table: Les trois scénarios de recette

Cette fois, les données traversent la lecture du fichier, la construction des états, la décision puis l’affichage. Les tests précédents appelaient surtout les fonctions directement. Ensemble, ces deux niveaux couvrent la règle et son chemin d’entrée principal.

Créez ensuite une copie de `retour-stock.json`, nommée `retour-stock-baisse.json`, et changez seulement le nouveau prix : 1 500 au lieu de 2 000. Lancez ce nouveau scénario. Le résultat doit être vrai.

Si un cas produit une réponse inattendue, conservez le fichier qui le reproduit. Modifier ensuite ses données pour obtenir du vert effacerait précisément l’information dont nous avons besoin. Un scénario complet vaut mieux qu’une capture privée de ses entrées.

### Vérifier qu’un test sait encore protester

Cette expérience est facultative. Copiez le dossier corrigé `mon-suivi` dans un dossier voisin nommé **`mon-suivi-mutations`**. Depuis le terminal placé dans `mon-suivi`, entrez dans cette nouvelle copie :

```bash
cd ../mon-suivi-mutations
```

Ouvrez **le fichier `suivi.py` de cette copie**. Dans la fonction `notifier` uniquement, remplacez la comparaison `nouveau.prix_centimes < ancien.prix_centimes` par `nouveau.prix_centimes <= ancien.prix_centimes`. Enregistrez, puis relancez `python -m unittest discover -v` dans ce terminal.

Le prix identique autorise maintenant une notification. Les tests qui attendent l’absence de notification à prix inchangé doivent échouer. S’ils ne le font pas, vérifiez la copie exécutée et la présence de ces cas.

Rétablissez ensuite `<`, puis retirez temporairement la condition `nouveau.disponible and`. Le test de baisse sur un produit indisponible doit cette fois protester.

Ces modifications volontaires sont de petites **mutations** : nous introduisons une erreur précise pour voir si les tests la remarquent. Nous vérifions ainsi que les cas importants savent protester. D’autres bugs restent évidemment possibles ; deux mutations ne dressent pas un bouclier magique autour de la fonction.

Rétablissez la condition dans `mon-suivi-mutations`, puis revenez à notre copie de travail restée intacte :

```bash
cd ../mon-suivi
python -m unittest discover -v
```

Le but est de tester nos tests, pas de préparer discrètement le prochain ticket. 🙂

### Demander une seconde lecture utile

Pour un second avis, vous pouvez faire relire le changement par un agent. C’est facultatif pour terminer l’atelier. Fournissez-lui le diff obtenu dans la comparaison, le contenu de `TICKET.md` et la table des cas attendus :

```text
Relis le diff par rapport à TICKET.md et aux scénarios.
Pour chaque problème trouvé, donne un cas reproductible,
le comportement obtenu et celui attendu.
Ne modifie pas les fichiers pendant cette revue.
Si tu ne trouves pas de problème, indique ce que tu as vérifié
et les limites de cette vérification.
```

Cette demande ramène la revue aux comportements. Une remarque devient utile lorsqu’elle s’accompagne d’un scénario que l’on peut lancer.

Le second passage peut manquer la même erreur que le premier. Une nouvelle session, même avec un autre modèle, peut retrouver les mêmes habitudes et les mêmes angles morts. Les scénarios, le code et les sorties observées restent nos pièces les plus solides.

Pour notre petit changement, une revue efficace peut tenir en quelques lignes. Inutile d’inventer trois problèmes pour donner du volume au rapport.



## 7. Garder un changement que l’on sait expliquer

**TL;DR** — Gardez une trace courte du problème, du diff et des vérifications réellement exécutées. Vous pourrez ensuite décider à quelles étapes l’aide vous a servi.

### Écrire un compte rendu exploitable

Créez un fichier `COMPTE-RENDU.md` dans `mon-suivi` et renseignez-le avec votre propre exécution :

```markdown
# PRIX-1 — Ne plus notifier une simple remise en stock

## Problème

Le retour en stock autorisait une notification même sans baisse de prix.

## Changement

La décision exige une disponibilité actuelle et une baisse stricte.
Les interfaces et les validations des entrées sont conservées.

## Vérifications effectuées

- Commande de tests, dossier d’exécution, nombre de tests et résultat :
- Scénario retour en stock, résultat observé :
- Scénario baisse de prix, résultat observé :
- Scénario indisponible, résultat observé :

## Limites

Le programme calcule une décision. Il n’envoie pas de notification.
Il compare deux observations dans une même devise implicite.
```
Code: Une trame à compléter avec vos résultats

Indiquez « non exécuté » pour les scénarios que vous n’avez pas lancés.

Ce texte peut servir de base à une description de pull request dans un vrai projet. Avant de publier, relisez les fichiers et les traces jointes : un rapport de test peut lui aussi contenir des données qu’on ne souhaite pas diffuser.

L’agent peut rédiger ce compte rendu à partir des sorties conservées. Comparez ensuite chaque affirmation aux commandes effectivement réalisées ; « treize tests passent » réclame une sortie de treize tests, pas un souvenir de la consigne.

### Quand on apprend encore à développer

Si vous découvrez Python, la version finale donnée tout de suite est tentante. Fermez-la un instant : pourriez-vous expliquer pourquoi le `or` autorisait une alerte lorsque le prix montait ?

Fermez la correction et essayez de prédire le résultat de deux cas : un retour en stock avec hausse, puis une baisse d’un centime sur un produit disponible. Vérifiez vos réponses en exécutant le programme.

En cas d’erreur, demandez une explication de l’expression booléenne, construisez une table de valeurs ou réduisez l’exemple à deux booléens. Le modèle peut proposer un autre angle sans recevoir aussitôt la modification entière.

Pour apprendre, une bonne utilisation consiste souvent à demander un indice, un contre-exemple ou une question de vérification. Une solution complète trop tôt peut vous faire sauter exactement l’effort dont vous aviez besoin pour comprendre.

Et certains jours, le plus efficace sera de fermer l’agent et de lire la fonction tranquillement. Vous n’avez rien à rentabiliser à chaque ligne.

### Trouver ses propres points de friction

Reprenez les étapes de cet atelier et demandez-vous lesquelles vous ont posé problème. Comprendre la règle ? Retrouver la fonction ? Penser aux cas limites ? Écrire la syntaxe de `unittest` ? Relire le diff ?

L’aide n’a pas le même intérêt partout. Vous pouvez aimer écrire le code et détester préparer une recette : dans ce cas, gardez l’implémentation et demandez une première liste de scénarios. Si vous connaissez les tests mais découvrez le langage, une explication ciblée vous apprendra souvent davantage qu’une implémentation complète.

Pour comparer deux façons de travailler, notez le temps total, y compris les corrections de demandes, la lecture des résultats et la validation. Le temps pendant lequel l’agent produit du texte n’est qu’une partie du travail.

N’ajoutez pas automatiquement un framework ou une série de commandes pour reproduire cet atelier. Nous avons séparé des étapes afin de voir ce qu’elles vérifient. Dans votre quotidien, regroupez ou simplifiez ce qui peut l’être, tout en conservant les contrôles nécessaires au changement.

Vous pouvez aussi conclure que l’outil ne vous aide pas sur ce type de tâche. S’en passer est encore une manière parfaitement valable d’adapter sa méthode.

Notre correction tient en peu de caractères. Nous pouvons pourtant expliquer le bug, montrer le test qui l’a fait apparaître, lire le diff et citer les vérifications exécutées. Gardez `mon-suivi` et son compte rendu : la partie suivante repartira de ce projet.

Les annexes restent disponibles pour comparer d’autres outils ou préparer l’expérience locale. Dans la prochaine partie, nous reprendrons l’agent au moment où il demande à lire un fichier ou lancer une commande. Nous pourrons alors séparer sa demande, l’autorisation du logiciel et le résultat renvoyé au modèle.

## Conclusion

Vous pouvez conserver le même assistant et votre dossier `mon-suivi`. Nous allons maintenant ouvrir le capot : quels fichiers entrent dans le contexte, qui exécute les outils, ce que les permissions arrêtent réellement et ce qu’il faut compter pour estimer le coût d’une session.
