Dans `cas/equipe.md`, l’équipe veut repérer des prix négatifs et des identifiants manquants dans un catalogue. Les règles sont explicites. Nous pouvons les vérifier avec un programme déterministe : un LLM n’a pas besoin de réinterpréter chaque ligne.

Pour un texte libre, le choix peut être différent. Il reste utile de comparer une solution spécialisée à un modèle généraliste. L’étude *Power Hungry Processing* mesure justement des consommations d’inférence différentes selon les tâches et les architectures testées ; ses résultats ne fournissent pas un coût universel de « la requête IA ».[^p8-energie]

Avant d’acheter du matériel, essayez ce qui suffit déjà à votre besoin. Notre recherche lexicale fonctionne sans carte graphique. Notre génération documentaire sur CPU a montré ses limites. Ces deux observations sont plus utiles qu’une règle qui recommanderait toujours le local ou toujours le service distant.

Nous pouvons aussi réduire le nombre d’appels, réutiliser un résultat encore valable ou arrêter une boucle qui ne progresse plus. Mais si une réponse plus courte provoque cinq nouvelles tentatives, l’économie annoncée mérite d’être recalculée.

Une facture moins élevée ne démontre pas une empreinte plus faible : les tarifs peuvent changer indépendamment du matériel. Conservez donc séparément le prix payé, les ressources mesurées et ce que vous ne savez pas mesurer.

[^p8-energie]: Luccioni, Jernite et Strubell, [*Power Hungry Processing: Watts Driving the Cost of AI Deployment?*](https://arxiv.org/abs/2311.16863), étude publiée à FAccT 2024.
