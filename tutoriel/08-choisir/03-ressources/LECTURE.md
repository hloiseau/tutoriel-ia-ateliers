# 3. Coûts, énergie, matériel et environnement

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Licences, transparence et possibilités de vérification](../02-ouverture/LECTURE.md) · [Suivant : Dépendances techniques et économiques](../04-dependances/LECTURE.md)

**TL;DR** — Le prix, l’électricité et l’impact environnemental ne mesurent pas la même chose. Nous allons faire un calcul simple en annonçant son périmètre, puis regarder ce qu’il laisse de côté.

Un appel gratuit peut mobiliser des machines. Un modèle local peut éviter un abonnement tout en occupant notre carte graphique. Le mot « gratuit » n’arrête pas le compteur électrique.

## Que mettons-nous dans le calcul ?

Pour notre atelier, nous pouvons compter le temps consacré à préparer la demande, à attendre, à relire et à corriger. Pour l’électricité, il faut aussi choisir ce que l’on mesure : la carte graphique seule, l’ordinateur à la prise ou l’ensemble du service ?

![Quatre périmètres à distinguer : calcul ciblé, électricité du service, cycle de vie et évolution des usages.](../images/perimetre.png)
Figure: Des périmètres différents, à annoncer avant de comparer

Dans son avis de juillet 2026, l’ADEME demande de considérer le cycle de vie ainsi que les effets indirects, notamment les effets rebonds. La fabrication du matériel, l’eau et les infrastructures ne disparaissent pas parce que l’on a mesuré l’électricité d’une requête.[^p8-ademe]

Un effet rebond peut se comprendre avec notre service : une réponse devient moins coûteuse, nous décidons alors d’en générer pour chaque ligne du catalogue, au lieu de seulement traiter les anomalies. Le coût unitaire baisse, mais le volume change. Il faut regarder les deux avant de conclure que nous avons réduit l’impact.

Cela ne veut pas dire que tout calcul est inutile. Un périmètre étroit, correctement annoncé, peut aider à comparer deux essais. Il faut simplement éviter de le présenter comme le bilan complet de l’IA.

[^p8-ademe]: ADEME, [*IA générative, comment quantifier les impacts ?*](https://www.ademe.fr/presse/communique-national/ia-generative-comment-quantifier-les-impacts/), 22 juillet 2026.

## Un calcul que nous pouvons refaire

Ouvrez un terminal dans l’atelier de cette partie. Python 3.12 suffit, sans dépendance supplémentaire. Prenons une puissance moyenne **hypothétique** de 200 W pendant 30 minutes :

```bash
python energie.py --puissance-w 200 --minutes 30
```

Le résultat vaut 100 Wh, soit 0,1 kWh. C’est le produit d’une puissance moyenne par une durée. Ces valeurs servent à expliquer le calcul ; elles n’ont pas été mesurées sur notre modèle ni sur la machine de l’auteur.

Pour remplacer l’hypothèse par une mesure, il faudrait relever une consommation sur l’intervalle de l’essai, avec un outil dont on connaît le périmètre. Une puissance maximale annoncée pour une carte ne donne pas sa puissance moyenne pendant notre tâche. Et une lecture instantanée ne décrit pas, à elle seule, toute l’exécution.

Si vous disposez déjà d’un compteur d’énergie à la prise, vous pouvez relever le début et la fin d’un essai. Notez ce qui était branché, les autres tâches actives et la durée. La différence inclut alors ce que le compteur a réellement mesuré, y compris le repos éventuel. Pour estimer un supplément par rapport au repos, il faudrait aussi établir une référence comparable, avec son incertitude.

Le script ne calcule ni eau ni émissions de CO₂. Transformer une énergie en émissions nécessite notamment un facteur adapté à l’électricité considérée. Cela ne reconstitue toujours pas la fabrication de l’ordinateur. Sans ces informations, gardons des Wh et une description honnête de la mesure.

## Éviter une dépense qui ne sert pas la tâche

Dans `cas/equipe.md`, l’équipe veut repérer des prix négatifs et des identifiants manquants dans un catalogue. Les règles sont explicites. Nous pouvons les vérifier avec un programme déterministe : un LLM n’a pas besoin de réinterpréter chaque ligne.

Pour un texte libre, le choix peut être différent. Il reste utile de comparer une solution spécialisée à un modèle généraliste. L’étude *Power Hungry Processing* mesure justement des consommations d’inférence différentes selon les tâches et les architectures testées ; ses résultats ne fournissent pas un coût universel de « la requête IA ».[^p8-energie]

Avant d’acheter du matériel, essayez ce qui suffit déjà à votre besoin. Notre recherche lexicale fonctionne sans carte graphique. Notre génération documentaire sur CPU a montré ses limites. Ces deux observations sont plus utiles qu’une règle qui recommanderait toujours le local ou toujours le service distant.

Nous pouvons aussi réduire le nombre d’appels, réutiliser un résultat encore valable ou arrêter une boucle qui ne progresse plus. Mais si une réponse plus courte provoque cinq nouvelles tentatives, l’économie annoncée mérite d’être recalculée.

Une facture moins élevée ne démontre pas une empreinte plus faible : les tarifs peuvent changer indépendamment du matériel. Conservez donc séparément le prix payé, les ressources mesurées et ce que vous ne savez pas mesurer.

[^p8-energie]: Luccioni, Jernite et Strubell, [*Power Hungry Processing: Watts Driving the Cost of AI Deployment?*](https://arxiv.org/abs/2311.16863), étude publiée à FAccT 2024.

Nous savons faire un calcul limité sans lui faire dire plus que ce qu’il mesure. Passons à ce qui arriverait si notre fournisseur, notre réseau ou notre machine devenait indisponible.

---

[Précédent : Licences, transparence et possibilités de vérification](../02-ouverture/LECTURE.md) · [Suivant : Dépendances techniques et économiques](../04-dependances/LECTURE.md)
