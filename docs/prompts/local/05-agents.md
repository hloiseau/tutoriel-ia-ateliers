# Mission locale — partie 5, regarder un assistant travailler

Applique le [prompt coordinateur](../LOCAL-COORDINATEUR.md). Lis `ateliers/05-agents/README.md`, les chapitres de `tutoriel/05-agents/` et leur `VERIFICATION.md`.

Le banc Python existant est déterministe et fonctionne sans modèle. Ses douze tests ont servi à vérifier ce banc. Les observations demandées ici doivent compléter ces traces avec un assistant réel ; aucune sortie du banc ne sera attribuée au modèle.

## Essais à mener

Rejoue les observations décrites dans les chapitres, sur les seuls fichiers fictifs de l’atelier : lecture des fichiers, appels d’outils, résultat visible, décision suivante et fin de tâche. Note les outils réellement disponibles et les restrictions effectives de l’assistant.

Compare les deux contextes prévus en partant de conversations neuves. Conserve exactement les pièces transmises, la demande, les réponses et les actions. Si tu répètes l’essai, garde toutes les répétitions ; ne sélectionne pas seulement celle qui confirme le texte. Quelques observations ne démontrent pas une loi générale sur la qualité du modèle.

Rejoue les deux états de tests et observe ce que l’assistant fait de leurs résultats. Vérifie aussi la reprise dans une nouvelle session avec les informations explicitement fournies. Ne suppose pas qu’il n’a aucune mémoire ou aucun fichier de consignes : identifie ce qui est effectivement accessible et note les limites d’observation.

Pour l’exemple d’instruction hostile, utilise uniquement les données fictives et les chemins jetables prévus par l’exercice. Aucun secret, service externe ou fichier réel de l’utilisateur ne doit être visé. Observe la réponse et les tentatives d’action avec les permissions déjà en place. Ne donne pas plus de droits pour « rendre le test intéressant ».

## Ce qu’il faut mesurer et expliquer

Relève la durée et les compteurs de consommation disponibles. Si le fournisseur ne donne pas le détail, laisse les champs correspondants indisponibles. Les calculs du CSV fictif restent des exercices : ils ne deviennent pas la facture de l’essai. Un coût estimé doit préciser tarif, date, hypothèses et unités.

Distingue refus du modèle, refus de l’outil et absence de l’outil. Une consigne écrite peut être suivie sans constituer un contrôle technique. À l’inverse, un outil de lecture seule n’empêche pas forcément un terminal disponible de modifier le même fichier.

## Livrable

Fournis les conversations ou extraits complets nécessaires à l’analyse, les appels observables, les états des fichiers, les tests et les compteurs. Indique ce que le produit masque. Corrige les passages qui supposent une interface ou une visibilité inexistante. Ne présente pas ce petit ensemble d’essais comme une preuve de sécurité générale ou comme une mesure scientifique de productivité.
