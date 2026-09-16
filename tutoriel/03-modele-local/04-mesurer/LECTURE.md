# 4. Mesurer sans mélanger les résultats

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** conservez les réglages, répétez les appels et séparez la vitesse de la qualité. Les chiffres qui nous intéressent sont ceux de notre installation.

## Le fichier, la RAM et la mémoire du GPU

Le fichier téléchargé occupe environ 386 Mo. Une fois le serveur lancé, surveiller ce seul nombre nous ferait manquer les zones de calcul et le cache utilisés pendant les réponses.

Pour un calcul grossier, 360 millions de paramètres stockés chacun sur 16 bits représentent 720 millions d’octets. Sur 8 bits, ce serait 360 millions ; sur 4 bits, 180 millions. Ces nombres décrivent **les paramètres seuls**, en supposant ce nombre rond et une même précision partout.

![Volume théorique de 360 millions de paramètres pour trois précisions](../images/poids.png)
Figure: Volume théorique des paramètres seuls, en Mo décimaux

Pour voir l’effet d’une précision réduite, prenons quelques nombres et arrondissons-les au quart le plus proche. Les déplacements sont visibles : nous gagnons une représentation plus grossière, mais nous perdons une partie de l’information.

![Des nombres sont ramenés au quart le plus proche](../images/quantifier.png)
Figure: Une quantification uniforme au quart, pour observer les arrondis

Les formats de quantification des modèles emploient des méthodes plus élaborées, notamment des paramètres par blocs de valeurs. Cet arrondi montre seulement le principe de l’approximation ; le format Q8_0 effectue d’autres calculs.

Notre fichier Q8_0 fait environ 386 Mo. Il contient les éléments nécessaires à son interprétation, tandis que le stockage quantifié possède ses propres informations. Le fichier final dépasse donc le calcul rond d’un octet par paramètre.

Pendant l’exécution, le moteur a également besoin de zones de calcul et d’un cache pour certaines représentations des tokens. La taille de ce cache dépend notamment de l’architecture, du contexte et de la précision utilisée. Charger plusieurs requêtes en parallèle peut encore changer la consommation.

Enfin, le moteur peut garder des données en RAM, en placer en mémoire vidéo ou les répartir entre les deux. Relevez ces mémoires séparément : 64 Go de RAM ajoutés à une carte de 8 Go ne donnent pas une carte de 72 Go.

Ouvrez l’outil de surveillance de votre système et relevez la mémoire du processus avant puis pendant une réponse. Notez ce que vous lisez : mémoire résidente du processus, mémoire totale utilisée ou mémoire vidéo ne désignent pas la même mesure. Sans le nom de la mesure, deux nombres risquent de ne pas être comparables.

## Répéter la même demande

Lancez :

```bash
python mesurer.py --nom cpu-contexte2048
```

Le programme effectue un appel d’échauffement, puis trois appels mesurés. Il conserve les quatre réponses dans `resultats/cpu-contexte2048/` et produit `mesures.csv`. Un dossier existant n’est pas écrasé : donnez un nouveau nom pour une autre série.

Le premier appel sert d’échauffement et reste à part des trois suivants. L’état du système, les autres programmes ou la température de la machine peuvent tout de même faire varier les durées.

Nous désactivons la réutilisation du préfixe entre requêtes avec `cache_prompt: false` dans les appels. Sans ce choix, répéter exactement la même demande pourrait surtout mesurer le bénéfice d’un cache déjà rempli. La réponse brute est conservée pour retrouver les informations que le serveur expose.[^p3-cache]

À côté du CSV, créez `reglages.txt` et copiez votre commande de lancement, la version du moteur et le nom du fichier GGUF. Ajoutez toute activité importante sur la machine pendant l’essai. La semaine suivante, ces quelques lignes éviteront de comparer deux nombres dont les conditions ont disparu.

[^p3-cache]: ggml-org, [paramètre `cache_prompt` et réutilisation du cache](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).

## Que mesure notre chronomètre ?

La durée commence juste avant l’envoi de la requête et s’arrête après la réception de sa réponse complète. Elle inclut donc le traitement de l’entrée, la génération et les échanges avec le serveur local. Elle n’inclut pas le téléchargement ni le démarrage du moteur.

Quand le serveur fournit le nombre de tokens produits, le script le divise par cette durée. La colonne s’appelle `tokens_sortie_par_seconde_globale` parce qu’elle couvre l’appel complet. Certains journaux affichent à la place le débit du seul décodage ; comparez des colonnes qui portent bien sur la même étape.

Prenons un calcul indépendant de notre machine : si un appel produit 60 tokens en 3 secondes, ce rapport vaut 20 tokens par seconde. Cela ne nous apprend pas combien de temps s’est écoulé avant le premier token. Deux installations peuvent avoir le même rapport global et donner une impression différente dans une interface qui affiche progressivement le texte.

Regardez aussi la longueur et la raison d’arrêt. Une réponse plus courte peut arriver plus vite sans que le moteur calcule plus vite. Une réponse vide serait même redoutablement efficace au chronomètre… et assez peu utile. 😅

Le programme affiche la médiane des trois durées. Cette petite série permet de repérer un écart grossier sur notre installation. Gardez aussi les valeurs individuelles : une seule durée bien choisie pourrait raconter à peu près n’importe quoi.

## Changer une seule chose

Arrêtez le serveur avec `Ctrl+C`, puis relancez exactement la même commande en remplaçant `-t 2` par `-t 4`, si votre machine dispose d’au moins quatre processeurs logiques. Ne modifiez pas le modèle, le contexte ou la question en même temps.

Lancez ensuite :

```bash
python mesurer.py --nom cpu-quatre-fils
```

Comparez les médianes, puis les réponses et l’activité de la machine. Doubler le nombre de fils ne divise pas forcément la durée par deux : les échanges de mémoire et le travail déjà présent sur le système interviennent aussi.

Vous pouvez refaire l’expérience avec un contexte maximal de 1 024 tokens au lieu de 2 048, en gardant notre courte question. Relevez surtout les allocations annoncées par le moteur et la mémoire observée. Ici, nous changeons la capacité réservée. Ajouter davantage de texte dans la requête étudierait un autre effet.

Pour étudier une entrée plus longue, créez un autre fichier de messages et conservez-le. N’attribuez pas au seul réglage du contexte un changement qui vient aussi d’une nouvelle question.


