# 8. Vérifier au-delà de la dernière ligne verte

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** la suite teste la fonction ; les scénarios font aussi passer les données par le chargement JSON. Nous allons examiner les deux.

## Rejouer les tests et contrôler leur nombre

Après correction, lancez :

```bash
python -m unittest discover -v
```

Avec le fichier complet de `02-test-rouge`, les **treize tests passent**. Si vous avez seulement écrit le premier nouveau test, vous en aurez quatre : ce n’est pas la même couverture, même si la dernière ligne est également `OK`.

Les noms des tests vous permettent de voir les situations réellement contrôlées. Regardez en particulier les deux qui échouaient avant la correction. Ils doivent toujours être présents et conserver leurs valeurs attendues.

Dans un rapport d’agent, cherchez la commande, son dossier d’exécution et son résultat. « Tests vérifiés » peut cacher plusieurs choses : une lecture du code des tests, une exécution partielle, ou une suite complète. Nous voulons savoir laquelle a eu lieu.

Si une dépendance manque ou qu’une commande échoue, le rapport doit le dire. Réussir à écrire les tests n’est pas la même chose que réussir à les exécuter.

## Passer par les fichiers JSON

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

## Vérifier qu’un test sait encore protester

Faisons une petite expérience, dans une **copie du projet corrigé**. Remplacez `<` par `<=` dans `notifier`, puis relancez la suite.

Le prix identique autorise maintenant une notification. Les tests qui attendent l’absence de notification à prix inchangé doivent échouer. S’ils ne le font pas, vérifiez que vous avez exécuté la bonne copie et que ces cas sont présents.

Rétablissez ensuite `<`, puis retirez temporairement la condition `nouveau.disponible and`. Le test de baisse sur un produit indisponible doit cette fois protester.

Ces modifications volontaires sont de petites **mutations** : nous introduisons une erreur précise pour voir si les tests la remarquent. Cela ne prouve pas qu’ils détecteront tous les bugs. Cela permet de vérifier que les cas importants ne sont pas seulement décoratifs.

Revenez enfin à la version corrigée et relancez la suite. Ne gardez pas une mutation dans votre copie de travail ; le but est de tester nos tests, pas de préparer discrètement le prochain ticket. 🙂

## Demander une seconde lecture utile

Vous pouvez maintenant faire relire le diff par un agent, en lui donnant aussi le ticket et les cas attendus :

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


