Arrêtez le serveur avec `Ctrl+C`, puis relancez exactement la même commande en remplaçant `-t 2` par `-t 4`, si votre machine dispose d’au moins quatre processeurs logiques. Ne modifiez pas le modèle, le contexte ou la question en même temps.

Lancez ensuite :

```bash
python mesurer.py --nom cpu-quatre-fils
```

Comparez les médianes, mais regardez également les réponses et l’activité de la machine. Ajouter des fils n’assure pas une amélioration proportionnelle : le calcul dépend aussi des échanges de mémoire et du travail déjà présent sur le système.

Vous pouvez refaire l’expérience avec un contexte maximal de 1 024 tokens au lieu de 2 048, en gardant notre courte question. Relevez surtout les allocations annoncées par le moteur et la mémoire observée. **Réserver un contexte plus grand et remplir ce contexte avec davantage de texte sont deux expériences différentes.**

Pour étudier une entrée plus longue, créez un autre fichier de messages et conservez-le. N’attribuez pas au seul réglage du contexte un changement qui vient aussi d’une nouvelle question.
