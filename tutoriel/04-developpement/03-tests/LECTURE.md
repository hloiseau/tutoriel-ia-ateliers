# 4. Faire apparaître le bug dans un test

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Décider ce que le ticket veut changer](../02-demande/LECTURE.md) · [Suivant : Faire le changement et lire le diff](../04-corriger/LECTURE.md)

**TL;DR** — Nous allons faire ajouter un premier test à l’agent, puis lire son échec. La correction expliquée juste après permet de contrôler ce qu’il a écrit, ou d’ajouter le test vous-même.

## Demander un premier test à l’agent

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

## Écrire le premier test qui échoue

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

## Ajouter les voisins du cas principal

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

![Trois états réellement exécutés : trois tests verts, puis deux échecs sur treize, puis treize tests verts](../images/tests.png)
Figure: Les résultats des versions de référence fournies

Pour poursuivre avec la même référence que le tutoriel, remplacez votre seul fichier `test_ticket.py` par celui de `02-test-rouge`, après l’avoir lu. Gardez `suivi.py` dans son état initial. Les deux échecs sont maintenant prêts à juger la correction.



---

[Précédent : Décider ce que le ticket veut changer](../02-demande/LECTURE.md) · [Suivant : Faire le changement et lire le diff](../04-corriger/LECTURE.md)
