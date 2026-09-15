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
