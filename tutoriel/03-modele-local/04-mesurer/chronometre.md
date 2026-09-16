Lancez :

```bash
python mesurer.py --nom cpu-contexte2048
```

Le programme effectue un appel d’échauffement, puis trois appels mesurés. Il conserve les quatre réponses dans `resultats/cpu-contexte2048/` et produit `mesures.csv`. Un dossier existant n’est pas écrasé : donnez un nouveau nom pour une autre série.

Le premier appel sert d’échauffement et reste à part des trois suivants. L’état du système, les autres programmes ou la température de la machine peuvent tout de même faire varier les durées.

Nous désactivons la réutilisation du préfixe entre requêtes avec `cache_prompt: false` dans les appels. Sans ce choix, répéter exactement la même demande pourrait surtout mesurer le bénéfice d’un cache déjà rempli. La réponse brute est conservée pour retrouver les informations que le serveur expose.[^p3-cache]

À côté du CSV, créez `reglages.txt` et copiez votre commande de lancement, la version du moteur et le nom du fichier GGUF. Ajoutez toute activité importante sur la machine pendant l’essai. La semaine suivante, ces quelques lignes éviteront de comparer deux nombres dont les conditions ont disparu.

[^p3-cache]: ggml-org, [paramètre `cache_prompt` et réutilisation du cache](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).
