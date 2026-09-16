Ouvrez un terminal dans l’atelier de cette partie. Python 3.12 suffit, sans dépendance supplémentaire. Prenons une puissance moyenne **hypothétique** de 200 W pendant 30 minutes :

```bash
python energie.py --puissance-w 200 --minutes 30
```

Le résultat vaut 100 Wh, soit 0,1 kWh. C’est le produit d’une puissance moyenne par une durée. Ces valeurs servent à expliquer le calcul ; elles n’ont pas été mesurées sur notre modèle ni sur la machine de l’auteur.

Pour remplacer l’hypothèse par une mesure, il faudrait relever une consommation sur l’intervalle de l’essai, avec un outil dont on connaît le périmètre. Une puissance maximale annoncée pour une carte ne donne pas sa puissance moyenne pendant notre tâche. Et une lecture instantanée ne décrit pas, à elle seule, toute l’exécution.

Si vous disposez déjà d’un compteur d’énergie à la prise, vous pouvez relever le début et la fin d’un essai. Notez ce qui était branché, les autres tâches actives et la durée. La différence inclut alors ce que le compteur a réellement mesuré, y compris le repos éventuel. Pour estimer un supplément par rapport au repos, il faudrait aussi établir une référence comparable, avec son incertitude.

Le script s’arrête aux Wh. Calculer des émissions de CO₂ demanderait notamment un facteur adapté à l’électricité considérée ; évaluer l’eau ou la fabrication de l’ordinateur élargirait encore le périmètre. En leur absence, gardons l’unité obtenue et la description de la mesure.
