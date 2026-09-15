# Développer avec une IA, du problème au changement vérifié

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Nous allons corriger un petit programme avec l’aide d’un agent : observer le problème, écrire un test qui le reproduit, faire la modification et vérifier le résultat. Un seul dossier de travail nous suivra jusqu’au bout.

Les trois tests passent. Pourtant, notre suivi de prix annonce une bonne affaire… alors que le prix n’a pas baissé. Voilà un programme un peu trop enthousiaste. 😅

Nous allons lui retirer cette habitude. La correction sera petite, ce qui nous laissera le temps de comprendre ce que l’agent fait autour : les fichiers qu’il lit, les tests qu’il écrit et les commandes qu’il lance.

Dans la partie précédente, nous faisions tourner un modèle chez nous. Pour cet atelier, nous utiliserons un assistant de développement avec un modèle hébergé. Vous n’avez donc pas besoin d’une grosse carte graphique. Si vous avez déjà un assistant, gardez-le ; sinon, nous décrirons une installation avec VS Code et GitHub Copilot. L’accès gratuit dépend de votre compte et de son quota.

Il vous faut savoir ouvrir un terminal, lancer un programme Python et lire une fonction simple. Le projet utilise Python 3.12 et sa bibliothèque standard. Nous expliquerons les assertions de test et la condition qui nous intéressent.

Les **sept premiers chapitres** suivent l’atelier. Le chapitre [« Référence — comparer les outils et leurs tarifs »](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/04-developpement/comparatif/LECTURE.md) rassemble le panorama complet, dont Pi : vous pouvez le consulter dès maintenant pour choisir votre outil, puis revenir à l’installation. L’**expérience locale avec Continue**, à la fin, est facultative et reste à vérifier sur machine ; elle ne remplace pas un parcours d’agent validé.

Les fichiers du projet sont publics et le ticket est fictif. Nous pouvons les montrer au service choisi sans utiliser le code de notre entreprise. Si vous préférez travailler sans IA, les tests et les corrections expliquées permettent aussi de suivre l’exercice.

## 1. Choisir de quoi suivre l’atelier

**TL;DR** — Pour l’atelier, il nous faut discuter du code, modifier un fichier et lire le résultat des tests. Gardez un assistant qui sait déjà le faire ; sinon, nous allons préparer VS Code avec Copilot.

Avant l’installation, réglons deux questions : à qui allons-nous montrer le code, et qui exécutera les commandes ?

### Où tournent le code et le modèle ?

Notre client de la partie précédente envoyait une question à `llama-server`, qui faisait calculer la réponse par le modèle. Un assistant de développement ajoute notamment les fichiers du projet à cette conversation.

Il faut distinguer **l’endroit où l’assistant agit** et **l’endroit où le modèle tourne**. Dans l’installation que nous allons utiliser, l’éditeur et les tests tournent sur notre ordinateur. Le modèle, lui, reçoit le contexte et calcule sa réponse chez le fournisseur.

| Élément | Dans l’atelier |
| --- | --- |
| Projet et tests Python | Sur notre ordinateur |
| Assistant | Dans l’éditeur, avec accès à notre copie de travail |
| Modèle et moteur d’inférence | Chez le fournisseur du modèle |
Table: Où se passe le travail ?

C’est pour cela que cette installation ne demande pas de GPU. Faire également tourner le modèle chez soi est une autre possibilité, avec des besoins de mémoire et de calcul à évaluer. Un petit modèle qui répond sur CPU ne devient pas un agent de code efficace simplement parce qu’on le branche à l’éditeur.

### Discuter, puis laisser agir

La complétion suggère du code pendant que vous tapez. Nous allons surtout utiliser deux autres fonctions :

- **La discussion** : nous montrons une fonction et demandons une explication. Nous lisons la réponse en gardant le code sous les yeux.
- **Le mode agent** : le modèle peut demander au logiciel de lire ou modifier des fichiers et de lancer des commandes. Les résultats lui reviennent, ce qui lui permet de poursuivre.

Le programme qui organise ces échanges est souvent appelé **harness**. Copilot, Codex, Claude Code, Pi et d’autres proposent leur propre manière de le faire. Nous comparerons leurs possibilités dans le chapitre de référence.

Pour commencer, nous resterons en discussion. Nous passerons au mode agent au moment d’écrire notre premier test. Vous verrez ainsi ce qui change quand l’outil peut agir sur les fichiers.

### Quel outil prendre pour commencer ?

Vous utilisez déjà un assistant capable de lire et modifier un projet ? Gardez-le. Les demandes de l’atelier portent sur des fichiers et des commandes Python ; elles ne dépendent pas d’une marque.

Sinon, nous prendrons **VS Code avec GitHub Copilot** comme exemple d’installation. D’autres possibilités figurent dans le [comparatif complet](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/04-developpement/comparatif/LECTURE.md) : éditeurs, agents en terminal, choix du modèle, prix et limites des offres. Ce comparatif est daté de septembre 2026.

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

Copiez **`01-depart`** dans un nouveau dossier nommé **`mon-suivi`**, en dehors du dossier téléchargé. Gardez les trois versions fournies à leur emplacement d’origine. `mon-suivi` sera notre seule copie de travail ; nous ne repartirons pas de zéro à chaque chapitre.

Installez [Visual Studio Code](https://code.visualstudio.com/download), puis utilisez **Fichier → Ouvrir le dossier** pour ouvrir `mon-suivi`. Si vous avez déjà un éditeur et un assistant, ouvrez cette même copie avec eux et passez à « Observer le problème ».

Dans l’explorateur, vous devez retrouver `suivi.py`, `test_suivi.py`, `TICKET.md` et `scenarios`. Les dossiers de correction restent en dehors de l’espace de travail : autant éviter de laisser la réponse sous le nez de l’agent. 🙂

### Ouvrir la discussion dans VS Code

Dans VS Code, ouvrez le menu de l’icône Copilot dans la barre d’état, choisissez **Use AI Features**, puis suivez la connexion à GitHub. L’offre gratuite peut être proposée à un compte éligible ; le tableau de bord Copilot permet de consulter son usage[^p4-install-copilot].

Ouvrez ensuite la vue **Chat**. Pour la première lecture, utilisez une session **Local** et le rôle **Ask**, avec un modèle accessible par votre compte Copilot. Ici, *Local* désigne l’exécution des outils de VS Code, pas l’hébergement du modèle. Le rôle Ask permet de poser des questions sans modifier le code[^p4-install-roles].

Les interfaces évoluent. Si vous utilisez une autre version ou un autre assistant, cherchez la fonction de discussion sans édition. Nous lui fournirons nous-mêmes le court extrait à expliquer.

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

Les tests passent, et nous venons pourtant de reproduire le comportement à changer. Ils ne couvraient donc pas ce cas. Le programme se contente d’afficher sa décision : aucun courriel n’est envoyé.

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

Si l’explication de l’assistant aboutit à faux, confrontez-la à ces trois valeurs et au résultat que vous avez exécuté. C’est un désaccord précis à lui montrer, sans lui demander vaguement de « mieux réfléchir ».

Nous savons maintenant où intervenir. Ouvrons le ticket pour décider ce qui doit remplacer cette règle.



## 3. Décider ce que le ticket veut changer

**TL;DR :** une phrase de ticket cache parfois plusieurs comportements. Nous allons les mettre à plat avant de toucher à la fonction.

### Une remise en stock n’est pas une baisse de prix

Le ticket PRIX-1 demande de ne plus notifier un produit qui revient simplement en stock. Le fichier `TICKET.md` donne la règle complète : une notification est autorisée seulement si le produit est disponible dans le nouvel état **et** si son prix a strictement baissé par rapport à l’observation précédente.

Les prix sont des entiers en centimes. Nous comparons deux observations consécutives, dans une même devise implicite. Il n’est pas question de retrouver le prix le plus bas des six derniers mois ni de calculer une promotion.

Avant de regarder la suite, répondez à ces deux cas :

- Le produit revient en stock au même prix. Faut-il notifier ?
- Le produit revient en stock avec un prix plus bas. Faut-il notifier ?

Le premier cas doit donner **faux**, le second **vrai**. « Ne plus notifier une remise en stock » ne veut donc pas dire « ignorer tous les produits qui étaient indisponibles ». Une baisse de prix peut accompagner le retour en stock.

C’est exactement le genre de raccourci qu’il faut éclaircir dans un vrai ticket. Si personne n’a décidé comment traiter le second cas, l’agent ne devrait pas choisir discrètement à la place de l’équipe.

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

Vous pouvez demander à l’agent de proposer cette table avant de coder les tests. Relisez alors les **résultats attendus**, pas seulement le nombre de lignes. Une longue suite de tests qui attend la mauvaise réponse reste une longue suite de tests qui attend la mauvaise réponse.

Pour une règle aussi petite, faire la table soi-même prend peu de temps. Dans un projet plus grand, l’aide peut surtout servir à retrouver les cas oubliés ou à traduire une règle déjà décidée en scénarios exécutables.

### Délimiter le changement

Ajoutons quelques limites simples à notre travail : nous conservons la fonction `notifier`, les fichiers JSON et les validations existantes. Nous n’ajoutons pas de base, d’envoi de courriel ou de système de préférences.

Pourquoi le préciser ? Parce qu’une demande d’« amélioration des notifications » pourrait facilement produire une architecture plus ambitieuse que notre besoin. Ici, le programme doit continuer à prendre deux états et à renvoyer une décision.

Les limites ne sont pas seulement des interdictions à adresser à l’agent. Elles nous servent aussi pendant la revue. Si un nouveau fichier de configuration apparaît, nous pourrons demander quel comportement du ticket le rend nécessaire.

Dans votre propre travail, gardez ce périmètre à la taille de la tâche. Un correctif d’une condition n’exige pas automatiquement un document de conception de dix pages. Il exige en revanche que les cas ambigus aient une réponse.



## 4. Faire apparaître le bug dans un test

**TL;DR** — Nous allons faire ajouter un premier test à l’agent, puis lire son échec. La correction expliquée juste après permet de contrôler ce qu’il a écrit, ou d’ajouter le test vous-même.

### Demander un premier test à l’agent

Gardez `mon-suivi` ouvert : il contient encore la fonction initiale et ses trois tests. Nous allons demander à l’agent d’ajouter **un seul test**, celui de la remise en stock au même prix.

Dans la session **Local** de VS Code, passez du rôle **Ask** au rôle **Agent** avec le sélecteur de la discussion. Agent dispose des outils de lecture, d’édition et d’exécution ; Ask nous servait seulement à discuter[^p4-premier-agent]. Avec un autre assistant, activez son mode de modification du projet. Conservez les demandes d’autorisation pour les commandes plutôt que d’activer une approbation générale.

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

Observez les actions : lecture des fichiers, création du test, lancement de la suite. Si l’agent corrige aussi `suivi.py`, arrêtez-le et remettez **ce seul fichier** dans son état initial à partir de `01-depart`. Gardez le nouveau test : nous voulons justement le voir échouer avant de corriger.

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

`unittest.TestCase` fournit les assertions, et les méthodes dont le nom commence par `test_` sont exécutées comme tests. Ici, `assertFalse` vérifie que l’appel à **notre fonction** renvoie une valeur fausse. Si l’agent compare seulement deux constantes, son test ne contrôle pas `notifier`.

Lancez de nouveau :

```bash
python -m unittest discover -v
```

Avec cet unique nouveau test, vous devez obtenir **quatre tests, dont un en échec**. Le programme renvoie vrai, alors que ce cas attend faux. Nous n’avons pas cassé le projet en ajoutant un test : nous avons rendu visible le désaccord avec la nouvelle règle.

Lisez le nom du test en échec. Une erreur d’import ou une faute de syntaxe ne prouvent pas que le comportement du ticket est reproduit. Le programme doit atteindre l’assertion, puis échouer parce que sa décision ne correspond pas à celle attendue.

Si votre test passe déjà, vérifiez que vous travaillez bien dans la copie de `01-depart` et que la fonction n’a pas été corrigée par avance. Il serait dommage de conclure à une démonstration du bug sans avoir exécuté le code qui le contient.

### Ajouter les voisins du cas principal

Nous avons couvert la remise en stock au même prix. Il manque notamment deux voisins : le retour avec une baisse, qui doit notifier, et le retour avec une hausse, qui ne doit pas notifier.

Demandez à l’agent de compléter **le fichier existant**, en lui donnant la table du ticket :

```text
Complète test_ticket.py avec les cas encore absents de cette table.
Conserve les tests déjà écrits et ne modifie pas suivi.py.
Lance la suite et indique quels comportements échouent.
```

Joignez la table à la demande. Vous pouvez aussi écrire ces tests vous-même. Relisez leurs valeurs attendues : `assertTrue` pour une baisse accompagnant le retour, `assertFalse` pour une hausse.

Notre fichier de référence se trouve dans **`02-test-rouge/test_ticket.py`**, parmi les dossiers extraits au début. Ouvrez-le séparément, puis comparez-le au vôtre. Il comporte aussi des cas à un centime, un prix nul et des entrées invalides. Ces derniers protègent les validations déjà présentes dans `Etat`.

Avec ce fichier de référence et les trois tests d’origine, on obtient **treize tests, dont deux échouent avant correction** : le retour en stock sans baisse et celui avec hausse. Votre agent peut avoir produit un autre nombre de tests. Comparez les comportements couverts et les échecs, pas seulement le compteur.

![Trois états réellement exécutés : trois tests verts, puis deux échecs sur treize, puis treize tests verts](images/tests.png)
Figure: Les résultats des versions de référence fournies

Si vous souhaitez retrouver exactement ces treize tests, remplacez votre seul fichier `test_ticket.py` par celui de `02-test-rouge`, après l’avoir lu. Gardez `suivi.py` dans son état initial. Nous avons maintenant les tests qui nous permettront de contrôler la correction.



## 5. Faire le changement et lire le diff

**TL;DR** — L’agent va corriger la fonction sans toucher aux résultats attendus des tests. Nous comparerons ensuite son changement à la règle du ticket.

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

La demande porte sur le comportement du ticket ; elle ne donne pas la ligne de correction. C’est le moment de regarder quelle solution l’agent propose. Si vous faites l’exercice à la main, essayez votre modification avant de lire la section suivante.

Cela reste une consigne au modèle. Pour limiter effectivement son accès aux fichiers, au réseau ou à la publication, utilisez aussi les permissions de votre outil. Une phrase dans un prompt n’a pas le même rôle qu’un droit technique refusant l’opération.

Si l’agent propose une classe de notification, une nouvelle dépendance ou un système de règles pour cette fonction, demandez-lui quel cas du ticket le justifie. Vous pouvez rejeter ces ajouts et demander une modification plus petite. Vous n’êtes pas obligé de conserver du code parce qu’il a déjà été généré.

### Relire les opérateurs

Comparez maintenant sa proposition à la fonction initiale :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
    )
```

Lisez-la à voix haute : le produit doit être disponible maintenant, et il faut soit une baisse de prix, soit une ancienne indisponibilité.

Le second terme du `or` explique notre problème. Pour un retour en stock, `not ancien.disponible` vaut vrai. Le prix peut être identique ou même plus élevé : l’expression entre parenthèses sera tout de même vraie.

Notre ticket exige uniquement une disponibilité actuelle et une baisse stricte. Notre correction de référence est :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes
    )
```
Code: La fonction après correction

Une expression sur une ligne peut être tout aussi correcte. Ce que nous cherchons dans la proposition, c’est la disponibilité actuelle et la baisse stricte, sans condition supplémentaire.

N’ajoutez pas `ancien.disponible` dans la nouvelle condition. Cela empêcherait de notifier une vraie baisse au moment du retour en stock, contrairement à la règle décidée.

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

Cette comparaison ne porte que sur `suivi.py`. Dans la liste des fichiers touchés affichée par l’assistant, ouvrez ensuite chaque autre fichier. Pour un fichier déjà présent au départ, recommencez la comparaison avec son original dans `01-depart`. Lisez entièrement le nouveau `test_ticket.py`, qui n’a pas d’original.

Le test ajouté est attendu. En revanche, changer les données de `retour-stock.json`, supprimer un test ou modifier une validation n’est pas nécessaire pour corriger cette condition. Cherchez la raison de ces changements avant de les garder.

[^p4-diff-vscode]: Microsoft, [comparaison des fichiers dans VS Code](https://code.visualstudio.com/docs/editing/codebasics#_compare-files).
[^p4-diff]: Git, [comparaison avec git diff --no-index](https://git-scm.com/docs/git-diff).



## 6. Vérifier au-delà de la dernière ligne verte

**TL;DR :** la suite teste la fonction ; les scénarios font aussi passer les données par le chargement JSON. Nous allons examiner les deux.

### Rejouer les tests et contrôler leur nombre

Après correction, lancez :

```bash
python -m unittest discover -v
```

Avec le fichier complet de `02-test-rouge`, les **treize tests passent**. Si vous avez conservé les tests de l’agent, le nombre peut être différent. Vérifiez que les cas décidés dans la table sont couverts et que ceux qui échouaient passent désormais, avec les mêmes valeurs attendues.

Les noms des tests vous permettent de voir les situations réellement contrôlées. Regardez en particulier les deux qui échouaient avant la correction. Ils doivent toujours être présents et conserver leurs valeurs attendues.

Dans un rapport d’agent, cherchez la commande, son dossier d’exécution et son résultat. « Tests vérifiés » peut cacher plusieurs choses : une lecture du code des tests, une exécution partielle, ou une suite complète. Nous voulons savoir laquelle a eu lieu.

Si une dépendance manque ou qu’une commande échoue, le rapport doit le dire. Réussir à écrire les tests n’est pas la même chose que réussir à les exécuter.

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

Nous passons cette fois par la lecture du fichier, la construction des états, la décision et l’affichage. Les tests précédents appelaient surtout les fonctions directement. Les deux vérifications se complètent.

Créez ensuite une copie de `retour-stock.json`, nommée `retour-stock-baisse.json`, et changez seulement le nouveau prix : 1 500 au lieu de 2 000. Lancez ce nouveau scénario. Le résultat doit être vrai.

Ne modifiez pas les scénarios pour les faire coïncider avec une réponse inattendue. Si un cas ne produit pas ce que la règle prévoit, conservez le fichier qui le reproduit. C’est une meilleure base de discussion qu’une capture sans ses données d’entrée.

### Vérifier qu’un test sait encore protester

Cette expérience est facultative. Copiez le dossier corrigé `mon-suivi` dans un dossier voisin nommé **`mon-suivi-mutations`**. Depuis le terminal placé dans `mon-suivi`, entrez dans cette nouvelle copie :

```bash
cd ../mon-suivi-mutations
```

Ouvrez **le fichier `suivi.py` de cette copie**, remplacez `<` par `<=`, enregistrez, puis relancez `python -m unittest discover -v` dans ce terminal.

Le prix identique autorise maintenant une notification. Les tests qui attendent l’absence de notification à prix inchangé doivent échouer. S’ils ne le font pas, vérifiez que vous avez exécuté la bonne copie et que ces cas sont présents.

Rétablissez ensuite `<`, puis retirez temporairement la condition `nouveau.disponible and`. Le test de baisse sur un produit indisponible doit cette fois protester.

Ces modifications volontaires sont de petites **mutations** : nous introduisons une erreur précise pour voir si les tests la remarquent. Cela ne prouve pas qu’ils détecteront tous les bugs. Cela permet de vérifier que les cas importants ne sont pas seulement décoratifs.

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

Cette demande évite de réduire la revue à des préférences de style. Une remarque devient plus utile lorsqu’on peut lancer le scénario qui la justifie.

Le second passage peut tout de même manquer la même erreur que le premier. Changer de session ou de modèle n’en fait pas une preuve indépendante au sens fort : les outils peuvent partager des habitudes et des angles morts. Appuyez-vous sur les scénarios, le code et les sorties observées.

Pour notre petit changement, une revue efficace peut être courte. Il n’y a aucune raison d’inventer trois problèmes pour remplir une section de rapport.



## 7. Garder un changement que l’on sait expliquer

**TL;DR :** préparez une trace courte du problème, de la correction et des vérifications. Puis choisissez où l’aide vous a réellement été utile.

### Écrire un compte rendu exploitable

Créez un fichier `COMPTE-RENDU.md` et renseignez-le avec votre propre exécution :

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

Ce texte peut ensuite servir de base à une description de pull request dans un vrai projet. Avant de publier, relisez les fichiers et les traces jointes : un rapport de test peut lui aussi contenir des données qu’on ne souhaite pas diffuser.

L’agent peut rédiger ce compte rendu à partir des sorties conservées. Vous gardez à vérifier que les phrases correspondent aux commandes effectivement réalisées.

### Quand on apprend encore à développer

Si vous découvrez Python, vous avez peut-être eu envie de demander directement la version finale. Mais pourriez-vous ensuite expliquer pourquoi le `or` posait problème ?

Fermez la correction et essayez de prédire le résultat de deux cas : un retour en stock avec hausse, puis une baisse d’un centime sur un produit disponible. Vérifiez vos réponses en exécutant le programme.

Si vous vous trompez, ce n’est pas une raison de renoncer à l’aide. Demandez une explication de l’expression booléenne, construisez une table de valeurs ou réduisez l’exemple à deux booléens. Vous pouvez vous servir du modèle pour trouver une autre explication sans lui confier immédiatement toute la modification.

Pour apprendre, une bonne utilisation consiste souvent à demander un indice, un contre-exemple ou une question de vérification. Une solution complète trop tôt peut vous faire sauter exactement l’effort dont vous aviez besoin pour comprendre.

Et certains jours, le plus efficace sera de fermer l’agent et de lire la fonction tranquillement. Il n’y a rien à rentabiliser à chaque ligne.

### Trouver ses propres points de friction

Reprenez les étapes de cet atelier et demandez-vous lesquelles vous ont posé problème. Comprendre la règle ? Retrouver la fonction ? Penser aux cas limites ? Écrire la syntaxe de `unittest` ? Relire le diff ?

L’aide n’a pas le même intérêt partout. Si vous aimez écrire le code mais que préparer une recette vous prend un temps fou, vous pouvez garder le code et demander une première liste de scénarios. Si vous connaissez bien les tests mais découvrez un langage, une explication ciblée peut être plus utile qu’une implémentation complète.

Pour comparer deux façons de travailler, notez le temps total, y compris les corrections de demandes, la lecture des résultats et la validation. Le temps pendant lequel l’agent produit du texte n’est qu’une partie du travail.

N’ajoutez pas automatiquement un framework ou une série de commandes pour reproduire cet atelier. Nous avons séparé des étapes afin de voir ce qu’elles vérifient. Dans votre quotidien, regroupez ou simplifiez ce qui peut l’être, tout en conservant les contrôles nécessaires au changement.

Vous pouvez aussi conclure que l’outil ne vous aide pas sur ce type de tâche. Adapter un outil à son besoin comprend cette possibilité.

Notre correction tient en peu de caractères, mais nous savons maintenant quel cas elle change et comment le vérifier. Gardez votre copie de travail et votre compte rendu.

L’atelier s’arrête ici. Le comparatif qui suit sert à choisir d’autres outils ; l’expérience locale permet d’explorer une autre installation. Dans la prochaine partie, nous regarderons plus précisément comment les agents choisissent leurs actions et comment encadrer ce travail.

## 8. Référence — comparer les outils et leurs tarifs

**TL;DR** — Cette référence compare les interfaces, les possibilités et les coûts des outils. Vous pouvez y revenir pour changer d’assistant sans recommencer l’atelier.

Le relevé est une photographie de septembre 2026. Un éditeur, un harness et un abonnement à un modèle ne désignent pas la même chose ; regardez surtout ce que chaque offre vous permet de faire avec votre projet.

### Les éditeurs et les agents

Commençons par les outils que vous pouvez rencontrer dans un éditeur, un terminal ou un service distant. Nous compléterons ce panorama avec les harness extensibles, dont Pi, dans la section suivante. Ce n’est pas la liste de tous les produits existants, ni un classement de leurs modèles.

Les offres et les fonctions décrites correspondent aux pages officielles consultées le **14 septembre 2026**. Si vous lisez ce chapitre plus tard, les liens en notes permettront de retrouver leur état actuel.

| Solution | Où l’utiliser | Ce qu’il faut regarder pour notre usage |
| --- | --- | --- |
| GitHub Copilot | Dans plusieurs éditeurs, en CLI et sur GitHub | Complétion, discussion, agent et revue ; fonctions et quotas selon l’offre[^p4-out-copilot] |
| Cursor | Éditeur dédié | Complétion et travail avec un agent dans le projet ; offre gratuite limitée[^p4-out-cursor] |
| Claude Code | Terminal et intégrations dans les éditeurs | Travail avec un agent ; accès par abonnement compatible ou API[^p4-out-claude] |
| Codex | Terminal, extension d’éditeur et interfaces hébergées | Tâches de développement, commandes et revue ; exécution locale ou distante selon l’interface[^p4-out-codex] |
| Devin | Desktop, CLI et Cloud | Complétion et agents ; vérifier quelle interface et quel quota couvre le forfait[^p4-out-devin] |
| JetBrains AI Assistant et Junie | Environnement JetBrains | Aide dans l’IDE et travail avec un agent ; quota cloud partagé selon l’offre[^p4-out-jetbrains] |
| Google Antigravity | Éditeur et CLI | Complétion et agents ; accès gratuit limité et offres Google AI[^p4-out-google] |
| Zed | Éditeur | Prédictions d’édition, modèles hébergés ou API personnelle, agents externes[^p4-out-zed] |
| Continue | Extension d’éditeur | Discussion, édition et complétion configurables ; serveur local possible[^p4-out-continue] |
| Cline | Extension VS Code et CLI | Agent avec plusieurs fournisseurs possibles, dont des solutions auto-hébergées[^p4-out-cline] |
| Aider | Terminal | Modifications du code et intégration Git ; API distante ou serveur compatible local[^p4-out-aider] |
| OpenCode | Terminal, application et extension d’éditeur | Agent avec plusieurs fournisseurs ; configuration de modèles locaux possible[^p4-out-opencode] |
Table: Quelques portes d’entrée pour développer avec une IA

Deux changements peuvent vous éviter de suivre une ancienne procédure d’installation. Google a annoncé le passage des utilisateurs individuels de Gemini CLI et Gemini Code Assist vers Antigravity CLI à compter du 18 juin 2026[^p4-out-migration]. De son côté, l’adresse de tarification de Windsurf redirige, lors de cette consultation, vers celle de Devin[^p4-out-windsurf]. Si vous reconnaissez un ancien nom, vérifiez donc aussi le parcours d’accès actuel.

Pour commencer l’atelier, revenez au chapitre « Installer l’assistant et observer le problème ». L’expérience Continue avec notre serveur local se trouve séparément à la fin de cette partie.

[^p4-out-copilot]: GitHub, [offres et fonctions de Copilot](https://github.com/features/copilot/plans).
[^p4-out-cursor]: Cursor, [offres et fonctions](https://cursor.com/pricing).
[^p4-out-claude]: Anthropic, [offres Claude](https://claude.com/pricing) ; Microsoft, [intégration des agents dans VS Code](https://code.visualstudio.com/docs/agents/run/agent-harnesses).
[^p4-out-codex]: OpenAI, [offres Codex](https://learn.chatgpt.com/docs/pricing).
[^p4-out-devin]: Devin, [offres et interfaces](https://devin.ai/pricing).
[^p4-out-jetbrains]: JetBrains, [abonnements et usage de JetBrains AI](https://www.jetbrains.com/help/ai-assistant/licensing-and-subscriptions.html).
[^p4-out-google]: Google, [offres Antigravity](https://antigravity.google/pricing/).
[^p4-out-zed]: Zed, [offres](https://zed.dev/pricing).
[^p4-out-continue]: Continue, [projet](https://github.com/continuedev/continue) et [configuration d’un serveur compatible](https://docs.continue.dev/customize/model-providers/top-level/openai).
[^p4-out-cline]: Cline, [offres](https://cline.bot/pricing).
[^p4-out-aider]: Aider, [présentation](https://aider.chat/) et [serveurs compatibles](https://aider.chat/docs/llms/openai-compat.html).
[^p4-out-opencode]: OpenCode, [présentation](https://opencode.ai/) et [fournisseurs](https://opencode.ai/docs/providers/).
[^p4-out-migration]: Google, [annonce de la transition vers Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), 19 mai 2026.
[^p4-out-windsurf]: [Page de tarification de Windsurf](https://windsurf.com/pricing), redirection constatée le 14 septembre 2026.

### Pi et les autres harness

Vous croiserez souvent le mot **harness** dans les discussions sur les agents. Il désigne le programme qui organise leur fonctionnement : préparer le contexte, appeler le modèle, exécuter ses demandes d’outils et poursuivre la conversation avec les résultats.

Dans notre premier client Python, nous envoyions une question et recevions du texte. Un harness peut ajouter la boucle suivante : le modèle demande à lire un fichier, le programme le lit et lui renvoie le contenu, puis le modèle choisit la prochaine action. La gestion des sessions, des permissions et des modifications appartient aussi à cet entourage logiciel.

Deux agents utilisant le même modèle peuvent donc se comporter différemment. Ils ne préparent pas forcément le même contexte et ne lui donnent pas les mêmes outils.

###### Pi, et les autres possibilités à connaître

**Pi** mérite qu’on s’y arrête. Il propose un agent en terminal que l’on peut étendre et intégrer à ses propres outils. Sa conception laisse une grande place aux extensions et aux modèles de consignes, plutôt que de fournir par défaut toutes les étapes d’une méthode de développement. Il dispose aussi d’interfaces permettant de le piloter depuis un programme[^p4-h-pi].

Cela rejoint une question qui nous suivra dans le tutoriel : est-ce l’outil qui décide de notre manière de travailler, ou pouvons-nous le modifier pour qu’il nous aide là où nous en avons besoin ?

| Outil | Interface et approche | Choix du modèle et usage local |
| --- | --- | --- |
| **Pi** | Agent en terminal, extensible ; API et interfaces d’intégration | Plusieurs fournisseurs et configuration de serveurs locaux[^p4-h-pi-models] |
| **Kilo Code** | Agent dans VS Code, JetBrains et en CLI | Choix de modèles et de fournisseurs ; distinguer l’agent des services de calcul Kilo[^p4-h-kilo] |
| **goose** | Application de bureau, CLI et API ; usages au-delà du code | Plusieurs fournisseurs, dont Ollama pour l’inférence locale[^p4-h-goose] |
| **Amp** | Agent et environnements de travail appelés *orbs* ; exécution hébergée ou sur ses propres runners | API personnelle ou abonnements compatibles selon l’offre ; son propre runner ne signifie pas que le modèle tourne dessus[^p4-h-amp] |
| **Mistral Vibe** | Agent en CLI, avec une offre intégrée de développement | Fournisseurs configurables ; vérifier le format d’API et le modèle utilisés[^p4-h-vibe][^p4-h-vibe-config] |
| **Kiro** | IDE et CLI, avec une place importante donnée aux spécifications et aux règles du projet | Modèles et crédits proposés par le service ; modèle à poids ouverts ne signifie pas inférence locale[^p4-h-kiro] |
| **OpenHands** | Agent et environnement de travail ; Agent Canvas peut aussi accueillir d’autres agents | Exécution locale ou distante ; documentation pour les modèles locaux[^p4-h-openhands][^p4-h-openhands-local] |
Table: Compléter le panorama des harness et des environnements d’agents

Pour Pi, la documentation permet par exemple de déclarer l’adresse d’un serveur compatible dans un fichier de configuration. Nous retrouvons ainsi la séparation entre modèle et assistant, sans devoir adopter un fournisseur unique[^p4-h-pi-models].

Cette liberté n’implique pas que toutes les protections soient installées d’avance. Le dépôt de Pi précise que le programme s’exécute avec les droits du processus qui le lance, sans système intégré de restriction des accès aux fichiers, aux processus ou au réseau. Une isolation supplémentaire relève donc de l’environnement dans lequel on l’exécute[^p4-h-pi-droits]. C’est une différence concrète à connaître lorsqu’on compare deux harness.

###### Les noms que vous trouverez dans d’anciens comparatifs

**Roo Code** a sa place dans l’histoire de ces outils, mais son dépôt officiel est archivé depuis le **15 mai 2026**. Nous ne le présenterons donc pas comme une installation maintenue au même titre que les projets actifs de cette liste[^p4-h-roo].

**Gemini CLI** mérite aussi d’être nommé explicitement. Le changement annoncé par Google concerne notamment les parcours gratuits et les abonnements individuels transférés vers Antigravity ; il ne faut pas en déduire que tous les usages professionnels ou toutes les modalités d’accès ont disparu[^p4-h-gemini].

Les noms, les offres et parfois les dépôts changent. Le comparatif est une photographie de septembre 2026, pas une liste à apprendre par cœur. Les étoiles GitHub peuvent aider à repérer un projet connu ; elles ne disent pas si sa manière de travailler convient à votre équipe.

[^p4-h-pi]: Pi, [présentation du harness et de ses extensions](https://pi.dev/).
[^p4-h-pi-models]: Pi, [modèles et fournisseurs personnalisés](https://pi.dev/docs/latest/models).
[^p4-h-kilo]: Kilo, [interfaces et fournisseurs](https://github.com/Kilo-Org/kilocode).
[^p4-h-goose]: goose, [présentation et fournisseurs](https://github.com/aaif-goose/goose).
[^p4-h-amp]: Amp, [documentation](https://ampcode.com/docs) et [offres, runners et modèles](https://ampcode.com/pricing).
[^p4-h-vibe]: Mistral, [Vibe CLI](https://github.com/mistralai/mistral-vibe).
[^p4-h-vibe-config]: Mistral, [configuration des fournisseurs et des permissions](https://docs.mistral.ai/vibe/code/cli/configuration-reference).
[^p4-h-kiro]: Kiro, [CLI](https://kiro.dev/docs/cli/) et [offres](https://kiro.dev/pricing/).
[^p4-h-openhands]: OpenHands, [Agent Canvas et ses modes d’exécution](https://github.com/OpenHands/OpenHands).
[^p4-h-openhands-local]: OpenHands, [utiliser un modèle local](https://docs.openhands.dev/openhands/usage/llms/local-llms).
[^p4-h-pi-droits]: Pi, [permissions et conteneurisation](https://github.com/earendil-works/pi#permissions--containerization).
[^p4-h-roo]: [Dépôt officiel Roo Code, archivé](https://github.com/RooCodeInc/Roo-Code).
[^p4-h-gemini]: Google, [transition de Gemini CLI vers Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/).

### Les prix et les limites des offres

Les montants ci-dessous sont les tarifs individuels affichés en **dollars américains, par mois avec facturation mensuelle**, relevés le **14 septembre 2026**. Les offres annuelles, promotions et contrats d’entreprise ne sont pas comparés ici. Le prix finalement facturé dépend aussi du pays, des taxes et du canal d’achat.

| Solution | Accès gratuit ou coût du logiciel | Offres payantes et limite à comprendre |
| --- | --- | --- |
| GitHub Copilot | Free : 2 000 complétions mensuelles et accès limité à la discussion et aux agents | Pro : 10 $ ; Pro+ : 39 $ ; Max : 100 $. Les usages IA reposent sur des crédits, distincts du nombre de complétions[^p4-prix-copilot] |
| Cursor | Hobby, avec usage limité | Pro : 20 $ ; Pro+ : 60 $ ; Ultra : 200 $. Usage supplémentaire possible au-delà de l’enveloppe incluse[^p4-prix-cursor] |
| Claude Code | Le forfait Claude Free ne l’inclut pas | Inclus dans Pro à 20 $ ; Max à partir de 100 $. Des limites d’usage s’appliquent[^p4-prix-claude] |
| Codex | L’accès gratuit dépend de l’offre en vigueur ; ne pas compter dessus pour une capacité fixe | Plus : 20 $ ; Pro à partir de 100 $ ; API facturée séparément. Le palier Pro à 200 $ existe, mais les nouvelles souscriptions sont temporairement suspendues à la date du relevé[^p4-prix-codex][^p4-prix-pro] |
| Devin | Free, avec quota limité | Pro : 20 $ ; Max : 200 $. Quotas et usage supplémentaire à vérifier selon l’interface[^p4-prix-devin] |
| JetBrains AI | Free : 3 crédits par période de 30 jours | Pour les particuliers : Pro à 10 $, Ultimate à 30 $. Respectivement 10 et 35 crédits par période de 30 jours ; licence de l’IDE à considérer séparément[^p4-prix-jb] |
| Google Antigravity | Offre individuelle gratuite, limitée | Google AI Pro : 19,99 $ sur la page américaine ; donne accès à des limites plus élevées. D’autres paliers existent[^p4-prix-google][^p4-prix-google-pro] |
| Zed | Personal gratuit, utilisable avec ses propres API ou des agents externes | Pro : 10 $, dont 5 $ d’usage de modèles ; facturation supplémentaire au-delà[^p4-prix-zed] |
| Continue | Extension libre utilisable avec son modèle local | Avec un fournisseur distant, l’inférence reste à financer selon le fournisseur[^p4-prix-continue] |
| Cline | Logiciel gratuit pour un usage individuel | Inférence à l’usage via le service proposé ou son propre fournisseur ; auto-hébergement possible[^p4-prix-cline] |
| Aider | Logiciel libre | API à financer séparément ou calcul local[^p4-prix-aider] |
| OpenCode | Logiciel libre | Modèles accessibles selon le fournisseur choisi : offre hébergée, API personnelle ou modèle local[^p4-prix-opencode] |
Table: Prix d’accès et origine des dépenses

###### Prix des autres harness et environnements

Pour les logiciels libres, le prix du programme est souvent le point le plus simple. Il faut ensuite compter l’inférence et, si vous utilisez une machine distante, son exécution.

| Solution | Logiciel ou accès de départ | Ce qui peut être facturé |
| --- | --- | --- |
| Pi | Logiciel libre, sans abonnement Pi requis | Fournisseur du modèle ou ressources de votre machine[^p4-prix-pi] |
| goose | Logiciel libre | Modèle choisi et éventuelle infrastructure[^p4-prix-goose] |
| Kilo Code | Offre individuelle du logiciel gratuite | Inférence séparée ; achat de crédits avec frais annoncés de 5 % ; Kilo Pass facultatif à partir de 19 $/mois ; calcul cloud séparé[^p4-prix-kilo] |
| Amp | Hobby gratuit, avec ses propres runners ou exécution à l’usage | Offre individuelle affichée à 20 $/mois ; modèles apportés par API ou abonnement compatible et ressources d’exécution à distinguer[^p4-prix-amp] |
| Mistral Vibe | Offre gratuite avec sessions de code limitées ; CLI disponible en source | Pro affiché à 14,99 $/mois hors taxes ; limites d’usage ; API selon son propre tarif[^p4-prix-vibe] |
| Kiro | Free : 50 crédits | Pro : 20 $ ; Pro+ : 40 $ ; Pro Max : 100 $ ; Power : 200 $ par mois. Crédits supplémentaires selon l’offre[^p4-prix-kiro] |
| OpenHands | Logiciel local libre et accès individuel hébergé gratuit | API personnelle ou modèles à l’usage ; conditions distinctes pour l’entreprise[^p4-prix-openhands] |
Table: Tarifs complémentaires, relevés le 14 septembre 2026 en USD

Un abonnement au modèle, un abonnement au logiciel et une machine qui exécute l’agent peuvent donc représenter trois dépenses distinctes. Avant de comparer les totaux, regardez qui fournit chacun de ces éléments.

« Gratuit » peut donc désigner deux choses : un service qui vous accorde un petit quota, ou un logiciel que vous installez sans payer, mais auquel il faut fournir un modèle. Dans le second cas, brancher une API payante ne rend pas ses réponses gratuites.

De même, une complétion et une tâche d’agent ne représentent pas la même quantité de travail. Un agent peut lire plusieurs fichiers, produire du code, recevoir une sortie de tests et recommencer. Selon la tarification, cela consomme des tokens, des crédits ou une partie d’un quota. Les crédits de deux fournisseurs ne sont pas une unité commune.

Avant d’acheter un abonnement, essayez quelques tâches que vous faites réellement. Regardez le temps consacré à obtenir **et vérifier** le résultat. Si vous avez gagné cinq minutes de saisie et ajouté vingt minutes de réparation, l’offre la moins chère ne résout pas votre problème. 😅

[^p4-prix-copilot]: [Tarifs GitHub Copilot](https://github.com/features/copilot/plans).
[^p4-prix-cursor]: [Tarifs Cursor](https://cursor.com/pricing).
[^p4-prix-claude]: [Tarifs Claude](https://claude.com/pricing).
[^p4-prix-codex]: [Tarifs Codex](https://learn.chatgpt.com/docs/pricing) ; [séparation entre abonnement ChatGPT Plus et API](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus).
[^p4-prix-pro]: OpenAI, [paliers Pro et suspension temporaire des nouvelles souscriptions Pro à 200 $](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers).
[^p4-prix-devin]: [Tarifs Devin](https://devin.ai/pricing).
[^p4-prix-jb]: JetBrains, [tarifs individuels, quotas et offres d’organisation](https://www.jetbrains.com/help/ai-assistant/licensing-and-subscriptions.html).
[^p4-prix-google]: [Offres Antigravity](https://antigravity.google/pricing/).
[^p4-prix-google-pro]: Google, [tarifs Google AI aux États-Unis](https://one.google.com/intl/en_us/about/google-ai-plans/).
[^p4-prix-zed]: [Tarifs Zed](https://zed.dev/pricing).
[^p4-prix-continue]: [Projet Continue](https://github.com/continuedev/continue) et [fonctionnement sans Internet](https://docs.continue.dev/guides/running-continue-without-internet).
[^p4-prix-cline]: [Tarifs Cline](https://cline.bot/pricing).
[^p4-prix-aider]: [Aider](https://aider.chat/).
[^p4-prix-opencode]: [OpenCode](https://opencode.ai/) et [ses fournisseurs](https://opencode.ai/docs/providers/).

[^p4-prix-pi]: [Pi, logiciel sous licence MIT](https://github.com/earendil-works/pi) et [configuration des modèles](https://pi.dev/docs/latest/models).
[^p4-prix-goose]: [goose, logiciel sous licence Apache 2.0](https://github.com/aaif-goose/goose).
[^p4-prix-kilo]: [Tarifs Kilo, inférence, frais et calcul](https://kilo.ai/pricing).
[^p4-prix-amp]: [Tarifs Amp](https://ampcode.com/pricing).
[^p4-prix-vibe]: [Tarifs Mistral](https://mistral.ai/pricing/).
[^p4-prix-kiro]: [Tarifs Kiro](https://kiro.dev/pricing/).
[^p4-prix-openhands]: [Tarifs OpenHands](https://www.openhands.dev/pricing).



## 9. Expérience facultative — discuter avec un modèle local

**TL;DR** — Expérience facultative : relier Continue au serveur de la partie 3, puis examiner la réponse d’un petit modèle de code. Cette configuration reste à exécuter et à mesurer ; nous ne la présentons pas comme un agent capable de mener l’atelier.

### Relier Continue à notre serveur

Vous voulez essayer de discuter avec notre modèle depuis l’éditeur ? Nous allons conserver le serveur de la partie 3 et remplacer notre client Python par **Continue**. Gardez sous la main la commande de lancement du serveur qui fonctionnait en partie 3.

###### Retrouver le serveur

Relancez `llama-server` avec la commande qui fonctionnait sur votre machine dans la partie précédente. Pour cette première connexion, conservez le port `8080`, l’adresse `127.0.0.1`, l’alias `atelier-local` et le contexte de `2048` tokens.

Ouvrez <http://127.0.0.1:8080/health> dans le navigateur. Lorsque le modèle est chargé, ce point d’accès doit indiquer que le serveur est prêt. Vous pouvez également ouvrir <http://127.0.0.1:8080/v1/models> pour retrouver le nom exposé par le serveur[^p4-install-server].

Si rien ne répond, regardez d’abord le terminal du serveur. Installer une extension ne réparera pas un modèle qui n’a pas fini de charger.

###### Ajouter Continue

Dans les extensions de VS Code, recherchez **Continue**, ou ouvrez directement [sa page officielle](https://marketplace.visualstudio.com/items?itemName=Continue.continue), puis installez l’extension[^p4-install-continue].

Ouvrez son panneau et choisissez la configuration locale. La roue dentée associée à **Local Config** permet d’ouvrir le fichier YAML. Il se trouve dans `~/.continue/config.yaml` sous Linux et macOS, ou `%USERPROFILE%\.continue\config.yaml` sous Windows[^p4-install-config].

Si vous utilisez déjà Continue, conservez une copie de votre configuration avant cet essai. Pour notre installation, utilisez ce contenu :

```yaml
name: Atelier local
version: 1.0.0
schema: v1

models:
  - name: SmolLM2 - connexion locale
    provider: openai
    model: atelier-local
    apiBase: http://127.0.0.1:8080/v1
    apiKey: local
    roles:
      - chat
    defaultCompletionOptions:
      contextLength: 2048
      maxTokens: 128
      temperature: 0
```
Code: Configuration de Continue pour le serveur de la partie 3

Ici, `provider: openai` indique le format d’API utilisé. **La destination est l’adresse de `apiBase`**, donc notre ordinateur. La valeur `local` est un remplissage pour le champ de clé ; notre serveur d’atelier n’a pas d’authentification configurée. Ce n’est pas une clé de compte OpenAI[^p4-install-compatible].

La longueur de contexte correspond à celle de notre serveur. Nous limitons aussi la réponse à 128 tokens pour ce premier essai. Nous déclarons le rôle `chat`, puis nous sélectionnerons le mode **Chat** dans l’interface. Ce rôle de configuration ne constitue pas à lui seul une interdiction d’utiliser des outils[^p4-install-yaml].

Enregistrez, sélectionnez la configuration et le modèle locaux, puis choisissez le mode **Chat**. Envoyez une question très courte, par exemple :

> Reply with the word hello.

Ce n’est pas un test d’intelligence. Nous cherchons une réponse, même imparfaite, et une requête correspondante dans le terminal de `llama-server`. Si une erreur mentionne une clé de service distant, vérifiez le modèle sélectionné et `apiBase`.

Continue propose un réglage **Allow Anonymous Telemetry** dans les paramètres de l’extension : désactivez-le pour cet usage local[^p4-install-offline]. Les réglages réseau de VS Code et des autres extensions restent séparés. Pour vérifier que cette conversation n’a pas besoin d’Internet, vous pouvez couper la connexion après les téléchargements, ouvrir une nouvelle discussion et envoyer une autre question.

###### Passer à un modèle de code

La connexion fonctionne ? Nous pouvons changer ce que le serveur charge.

Pour un premier essai sur CPU, prenons **Qwen2.5-Coder-1.5B-Instruct**, dans sa version GGUF `Q4_K_M`. C’est un petit modèle destiné au code. Nous allons lui soumettre un extrait court pour examiner sa réponse ; sa fiche ne permet pas de conclure qu’il sera utile sur notre exercice[^p4-install-qwen].

Dans [le dépôt officiel du modèle](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/tree/main), téléchargez **`qwen2.5-coder-1.5b-instruct-q4_k_m.gguf`**, puis placez-le dans le dossier `modeles` utilisé en partie 3. Ce fichier pèse environ **1,1 Go** ; prévoyez aussi de la mémoire pour le contexte et les programmes ouverts[^p4-install-qwen-fichier].

Arrêtez le serveur précédent avec **Ctrl+C**. Dans sa commande de lancement, remplacez le chemin après `-m` par celui de ce fichier, passez le contexte de `2048` à `4096` et l’alias à `atelier-code`. Gardez les réglages de chargement des bibliothèques qui fonctionnaient déjà sur votre système.

Avec l’arborescence Linux de la partie 3, la commande devient :

```bash
./moteur/llama-server -m modeles/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf --host 127.0.0.1 --port 8080 -c 4096 -t 2 -ngl 0 --device none --parallel 1 --alias atelier-code
```
Code: Lancement du modèle de code sur CPU

Sous Windows ou macOS, reprenez votre chemin d’exécutable de la partie 3 avec ces mêmes changements. Le but est de remplacer le modèle dans une installation qui fonctionne déjà.

Remplacez ensuite la configuration Continue par :

```yaml
name: Atelier code local
version: 1.0.0
schema: v1

models:
  - name: Qwen Coder - CPU
    provider: openai
    model: atelier-code
    apiBase: http://127.0.0.1:8080/v1
    apiKey: local
    roles:
      - chat
    defaultCompletionOptions:
      contextLength: 4096
      maxTokens: 512
      temperature: 0
```
Code: Configuration de discussion avec le modèle de code

Ouvrez une nouvelle conversation après le changement de modèle. Copiez la définition de `Etat` et la fonction `notifier` depuis **la version initiale** `01-depart/suivi.py`. Posez la même question que dans le chapitre de lecture : pour `Etat(2000, False)` puis `Etat(2000, True)`, quelles valeurs prennent les conditions et que renvoie la fonction ?

Chronométrez le temps avant le début de la réponse et sa durée totale. Conservez le texte obtenu, puis vérifiez-le contre le code : le résultat initial est vrai. Une réponse rapide mais fausse ne nous aide pas davantage qu’une réponse juste qui arrive trop tard pour notre usage.

Si la réponse est lente, commencez par raccourcir la demande et la sortie attendue. Si la machine manque de mémoire, revenez au contexte précédent ou au petit modèle pour finir le diagnostic de connexion. Pour l’atelier, vous pouvez toujours effectuer les modifications vous-même : il n’est pas nécessaire de laisser un modèle en difficulté multiplier les tentatives.

[^p4-install-server]: llama.cpp, [documentation du serveur et des points d’accès HTTP](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).
[^p4-install-continue]: Continue, [installation de l’extension](https://docs.continue.dev/ide-extensions/install).
[^p4-install-config]: Continue, [configuration locale](https://docs.continue.dev/customize/deep-dives/configuration).
[^p4-install-compatible]: Continue, [serveurs compatibles avec l’API OpenAI](https://docs.continue.dev/customize/model-providers/top-level/openai).
[^p4-install-yaml]: Continue, [référence du fichier YAML](https://docs.continue.dev/reference).
[^p4-install-offline]: Continue, [fonctionnement sans Internet](https://docs.continue.dev/guides/running-continue-without-internet).
[^p4-install-qwen]: Qwen, [Qwen2.5-Coder-1.5B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF).
[^p4-install-qwen-fichier]: Qwen, [fichiers GGUF proposés](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/tree/main).

Une connexion réussie montre que l’éditeur peut parler au serveur. Pour savoir si cette installation vous aide à développer, il reste à examiner ses réponses et ses délais sur vos propres tâches. Nous n’avons pas configuré ni validé ici un parcours d’agent sur CPU.

## Conclusion

Vous pouvez conserver le même assistant pour la suite. Nous allons maintenant ouvrir un peu le capot : contexte, outils, permissions et coût d’une session d’agent.
