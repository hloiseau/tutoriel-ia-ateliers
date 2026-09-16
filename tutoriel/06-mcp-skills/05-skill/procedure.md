Le corps du skill commence par demander la lecture du ticket. Il fait ensuite charger les documents cités, préparer les cas décidés et faire apparaître les questions ouvertes. Voici la consigne qui nous intéresse particulièrement :

> Si une décision manque ou que les sources se contredisent, expose la question et laisse le résultat concerné indéterminé. Ne choisis pas discrètement à la place de l’équipe.

Nous écrivons à l’impératif parce que nous décrivons la procédure attendue. « Tu pourrais peut-être vérifier les questions » ressemble à une possibilité parmi d’autres. Ici, leur examen fait partie du travail.

L’impératif rend notre attente claire ; il ne transforme pas le texte en programme déterministe. Nous devrons vérifier ce que le modèle en fait, comme nous avons relu les tests proposés dans la partie 4.

Le skill ne contient pas la règle « notifier si le prix baisse et si le produit est disponible ». Cette information appartient au ticket et à sa documentation. En la recopiant dans la procédure, nous créerions une deuxième version à mettre à jour lors du prochain changement métier.

Enfin, le skill demande de lire `references/format-recette.md` au moment de présenter le résultat. Ce fichier précise les colonnes : cas, préconditions, action, résultat attendu et source. L’assistant peut ainsi charger ce format au moment de rédiger, après avoir découvert PRIX-1 et examiné ses sources.

Le chargement progressif dépend de l’implémentation du client. Cette séparation le rend possible ; vérifiez dans votre outil quels fichiers sont réellement chargés et à quel moment.[^p6-chargement]

[^p6-chargement]: Agent Skills, [prise en charge et chargement par les clients](https://agentskills.io/client-implementation/adding-skills-support).
