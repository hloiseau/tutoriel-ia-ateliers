# 6. Faire apparaître le bug dans un test

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** nous ajoutons d’abord le cas oublié. Son échec nous permet de vérifier que le test distingue bien l’ancien comportement du comportement demandé.

## Écrire le premier test qui échoue

Dans `mon-suivi`, créez `test_ticket.py` :

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

Lancez de nouveau :

```bash
python -m unittest discover -v
```

Cette fois, vous devez obtenir **quatre tests, dont un en échec**. Le programme renvoie vrai, alors que ce cas attend faux. Nous n’avons pas cassé le projet en ajoutant un test : nous avons rendu visible le désaccord avec la nouvelle règle.

Lisez le nom du test en échec. Une erreur d’import ou une faute de syntaxe ne prouvent pas que le comportement du ticket est reproduit. Le programme doit atteindre l’assertion, puis échouer parce que sa décision ne correspond pas à celle attendue.

Si votre test passe déjà, vérifiez que vous travaillez bien dans la copie de `01-depart` et que la fonction n’a pas été corrigée par avance. Il serait dommage de conclure à une démonstration du bug sans avoir exécuté le code qui le contient.

## Ajouter les voisins du cas principal

Le cas principal est maintenant couvert. Ajoutez les autres situations de la table, notamment le retour en stock avec baisse et celui avec hausse. Pour une baisse accompagnant le retour, l’assertion doit être `assertTrue`.

Le dossier `02-test-rouge` contient une version complète de `test_ticket.py`. Vous pouvez comparer votre fichier au sien ou le recopier après avoir essayé. Il ajoute aussi les limites suivantes : une baisse d’un centime, un prix nul et des données invalides.

Avec ce fichier complet, la suite contient **treize tests**. Avant correction, **deux échouent** : le retour en stock sans baisse et le retour en stock avec hausse. Le reste passe.

![Trois états réellement exécutés : trois tests verts, puis deux échecs sur treize, puis treize tests verts](../images/tests.png)
Figure: Les résultats des trois versions fournies dans l’atelier

Les tests de données invalides vérifient notamment qu’un prix négatif, un prix décimal, un booléen utilisé comme prix et une disponibilité écrite sous forme de texte sont refusés. Ils protègent un comportement existant ; ils ne décrivent pas de nouvelles fonctionnalités du ticket.

Lisez le test sur le booléen comme prix avec la validation dans `Etat`. En Python, les booléens sont un cas particulier des entiers. Le contrôle `type(...) is int` utilisé ici exclut délibérément `True`, alors qu’un simple `isinstance(..., int)` l’accepterait.[^p4-bool]

[^p4-bool]: Python, [type booléen et relation avec les entiers](https://docs.python.org/3.12/library/stdtypes.html#boolean-type-bool).

## Faire écrire les tests par l’agent

Si vous voulez lui confier cette étape, repartez de la copie initiale et donnez-lui cette consigne :

```text
À partir de TICKET.md, propose une table de cas puis écris
les tests manquants dans test_ticket.py.
Ne modifie pas suivi.py.
Lance python -m unittest discover -v.
Rapporte les noms des tests en échec et la différence
entre la valeur attendue et la valeur obtenue.
```

La séparation entre les tests et la correction nous permet d’observer le comportement initial. Vérifiez le diff après son intervention : s’il a modifié `suivi.py` en même temps, l’expérience ne montre plus aussi clairement que les nouveaux tests attrapent l’ancien comportement.

Regardez également si ses tests appellent vraiment `notifier`. Un test qui compare deux constantes ou reproduit sa propre version de la condition peut passer sans contrôler notre fonction.

Enfin, les tests sont du code exécuté sur votre ordinateur. Dans cet atelier, ils utilisent seulement nos petites fonctions. Dans un dépôt inconnu, regardez leurs imports, leurs préparatifs et les commandes proposées avant de les lancer. Le mot « test » ne garantit pas à lui seul l’absence d’écriture ou d’appel réseau.


