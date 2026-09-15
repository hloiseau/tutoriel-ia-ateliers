# Développer avec une IA, du problème au changement vérifié

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Nous allons corriger un petit programme avec l’aide d’un agent : observer le problème, écrire un test qui le reproduit, faire la modification et vérifier le résultat. Un seul dossier de travail nous suivra jusqu’au bout.

Les trois tests passent. Pourtant, notre suivi de prix annonce une bonne affaire… alors que le prix n’a pas baissé. Voilà un programme un peu trop enthousiaste. 😅

Nous allons lui retirer cette habitude. La correction sera petite, ce qui nous laissera le temps de comprendre ce que l’agent fait autour : les fichiers qu’il lit, les tests qu’il écrit et les commandes qu’il lance.

Dans la partie précédente, nous faisions tourner un modèle chez nous. Pour cet atelier, nous utiliserons un assistant de développement avec un modèle hébergé. Vous n’avez donc pas besoin d’une grosse carte graphique. Si vous avez déjà un assistant, gardez-le ; sinon, nous décrirons une installation avec VS Code et GitHub Copilot. L’accès gratuit dépend de votre compte et de son quota.

Il vous faut savoir ouvrir un terminal, lancer un programme Python et lire une fonction simple. Le projet utilise Python 3.12 et sa bibliothèque standard. Nous expliquerons les assertions de test et la condition qui nous intéressent.

Les **sept chapitres de cette partie** suivent l’atelier. L’annexe [« Comparer les outils et leurs tarifs »](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/annexes/comparatif/LECTURE.md) rassemble le panorama complet, dont Pi : vous pouvez le consulter dès maintenant pour choisir votre outil, puis revenir à l’installation. L’**expérience locale avec Continue**, dans les annexes, est facultative et reste à vérifier sur machine ; elle ne remplace pas un parcours d’agent validé.

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

Le programme qui organise ces échanges est souvent appelé **harness**. Copilot, Codex, Claude Code, Pi et d’autres proposent leur propre manière de le faire. Nous comparerons leurs possibilités dans l’annexe comparative.

Pour commencer, nous resterons en discussion. Nous passerons au mode agent au moment d’écrire notre premier test. Vous verrez ainsi ce qui change quand l’outil peut agir sur les fichiers.

### Quel outil prendre pour commencer ?

Vous utilisez déjà un assistant capable de lire et modifier un projet ? Gardez-le. Les demandes de l’atelier portent sur des fichiers et des commandes Python ; elles ne dépendent pas d’une marque.

Sinon, nous prendrons **VS Code avec GitHub Copilot** comme exemple d’installation. D’autres possibilités figurent dans le [comparatif complet](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/annexes/comparatif/LECTURE.md) : éditeurs, agents en terminal, choix du modèle, prix et limites des offres. Ce comparatif est daté de septembre 2026.

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

L’atelier s’arrête ici. Dans les annexes, le comparatif sert à choisir d’autres outils et l’expérience locale permet d’explorer une autre installation. Dans la prochaine partie, nous regarderons plus précisément comment les agents choisissent leurs actions et comment encadrer ce travail.

## Conclusion

Vous pouvez conserver le même assistant pour la suite. Nous allons maintenant ouvrir un peu le capot : contexte, outils, permissions et coût d’une session d’agent.
