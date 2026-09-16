Voici deux réponses réellement obtenues avec le modèle de la partie 3, sur CPU. Les journaux complets sont dans `resultats-reference/reponse-staging.json` et `reponse-delai.json`.

À propos de staging :

> Les documents de staging sont réinitialisées chaque mardi à 06 h 00 UTC. Cet horaire concerne uniquement le service fictif de cet atelier.

L’horaire correspond au document. La phrase est maladroite et ne cite aucun identifiant, malgré la consigne. Mais pour la temporisation, nous obtenons ceci :

> Délai de temporisation validé : 10 minutes.

Aïe. Ouvrez `reponse-delai.json` : `temporisation#2` figure bien dans les passages et dit qu’aucune durée chiffrée n’est validée. La recherche a fait son travail ; les dix minutes viennent du modèle. Une troisième question sur la baisse de prix produit également une réponse confuse, qui ne restitue pas correctement les conditions.

Notre application transmet bien les sources, mais ce modèle ne les exploite pas de manière fiable dans cet essai. Sa fiche indique l’anglais comme langue ; notre utilisation en français ne lui facilite pas la tâche.[^p7-smollm] Cela n’explique pas à lui seul chaque erreur. Pour comparer un autre modèle, nous rejouerions les mêmes questions et relirions à nouveau les passages envoyés.

Évitons de corriger la règle de temporisation pour donner raison au modèle. 🙂 Conservons plutôt cet échec dans nos essais, puis comparons une autre formulation ou un modèle plus adapté. Grâce au journal, nous pourrons vérifier si le changement touche la recherche, le contexte ou la génération.

Pour une question très structurée comme un horaire, nous pourrions aussi afficher directement le passage retrouvé. Le modèle ajouterait ici une étape et une occasion de déformer une réponse déjà lisible.

[^p7-smollm]: Hugging Face, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct).
