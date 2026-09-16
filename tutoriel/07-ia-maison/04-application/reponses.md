Voici deux réponses réellement obtenues avec le modèle de la partie 3, sur CPU. Les journaux complets sont dans `resultats-reference/reponse-staging.json` et `reponse-delai.json`.

À propos de staging :

> Les documents de staging sont réinitialisées chaque mardi à 06 h 00 UTC. Cet horaire concerne uniquement le service fictif de cet atelier.

L’horaire correspond au document. La phrase est maladroite et ne cite aucun identifiant, malgré la consigne. Mais pour la temporisation, nous obtenons ceci :

> Délai de temporisation validé : 10 minutes.

Aïe. Le passage transmis dit pourtant qu’aucune durée n’est validée. Le nombre vient du modèle, pas de notre documentation. Une troisième question sur la baisse de prix produit également une réponse confuse, qui ne restitue pas correctement les conditions.

Nous avons donc une application qui transmet les sources, et un modèle qui ne les exploite pas de manière fiable. La fiche de ce petit modèle indique l’anglais comme langue ; notre utilisation en français ne lui facilite pas la tâche.[^p7-smollm] Cela ne suffit pas à expliquer chaque erreur, et passer à un autre modèle demanderait de rejouer les mêmes questions.

Ne modifiez pas la règle de temporisation pour qu’elle corresponde à sa réponse. 🙂 La suite logique est de conserver cet échec dans nos essais, puis de comparer une autre formulation ou un modèle plus adapté. Le journal permet de vérifier si l’amélioration vient de la recherche, du contexte ou de la génération.

Pour une question très structurée comme un horaire, nous pourrions aussi afficher directement le passage retrouvé. Générer une nouvelle phrase n’est pas toujours nécessaire.

[^p7-smollm]: Hugging Face, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct).
