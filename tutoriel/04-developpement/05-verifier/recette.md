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
