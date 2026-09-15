Le cas principal est maintenant couvert. Ajoutez les autres situations de la table, notamment le retour en stock avec baisse et celui avec hausse. Pour une baisse accompagnant le retour, l’assertion doit être `assertTrue`.

Le dossier `02-test-rouge` contient une version complète de `test_ticket.py`. Vous pouvez comparer votre fichier au sien ou le recopier après avoir essayé. Il ajoute aussi les limites suivantes : une baisse d’un centime, un prix nul et des données invalides.

Avec ce fichier complet, la suite contient **treize tests**. Avant correction, **deux échouent** : le retour en stock sans baisse et le retour en stock avec hausse. Le reste passe.

![Trois états réellement exécutés : trois tests verts, puis deux échecs sur treize, puis treize tests verts](image:images/tests.png)
Figure: Les résultats des trois versions fournies dans l’atelier

Les tests de données invalides vérifient notamment qu’un prix négatif, un prix décimal, un booléen utilisé comme prix et une disponibilité écrite sous forme de texte sont refusés. Ils protègent un comportement existant ; ils ne décrivent pas de nouvelles fonctionnalités du ticket.

Lisez le test sur le booléen comme prix avec la validation dans `Etat`. En Python, les booléens sont un cas particulier des entiers. Le contrôle `type(...) is int` utilisé ici exclut délibérément `True`, alors qu’un simple `isinstance(..., int)` l’accepterait.[^p4-bool]

[^p4-bool]: Python, [type booléen et relation avec les entiers](https://docs.python.org/3.12/library/stdtypes.html#boolean-type-bool).
