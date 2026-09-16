# Vérification de la partie 7

Exécutions du 16 septembre 2026. Cette première rédaction attend la relecture de l’auteur.

## Parcours depuis l’archive

L’archive `telechargements/atelier-ia-maison.zip` a été extraite dans un dossier séparé. Dix-neuf commandes ont été exécutées avec Python 3.12.14, NumPy 2.3.5 et threadpoolctl 3.6.0, sous Linux x86-64 sur CPU. Le [journal complet](../../docs/verifications-partie7/executions.json) contient les commandes, leurs codes de sortie, leurs sorties et l’empreinte de l’archive.

- Onze tests passent : recherche, exclusion des archives, provenance, limites lexicales, gradients du réseau et de LoRA, fenêtres par ligne, initialisation de l’adaptateur, rechargement et refus d’une autre base.
- Les deux programmes écrits par le lecteur ont été reconstruits depuis les blocs Python des chapitres et exécutés sans génération.
- La recherche retrouve une source attendue pour les quatre questions renseignées du lot de validation, puis trois des quatre du test. La question sur la purge des fixtures reste manquée. Les deux questions sans source, une par lot, ne renvoient aucun passage.
- L’application n’appelle pas le serveur en l’absence de passage. Quand des passages existent mais que le serveur est absent, elle conserve le contexte et sort avec le code 2.
- Les trois entraînements — base, adaptation complète, LoRA — ont été rejoués. Les six pertes de test reproduisent les valeurs de référence à `1e-10` près dans cet environnement.
- Le modèle LoRA rechargé depuis la base et le fichier d’adaptateur donne les mêmes probabilités que le fichier complet. Une autre base est refusée. L’empreinte des poids de base reste identique pendant l’adaptation LoRA.

Aucune mesure d’énergie ou de pic mémoire n’a été réalisée. Les durées des rapports sont celles de cet environnement, pas une promesse pour d’autres machines.

## Appels documentaires réels

Trois appels ont été exécutés séparément, avec les mêmes scripts, contre llama.cpp b10809, SmolLM2-360M-Instruct Q8_0 vérifié par SHA-256, deux fils CPU, contexte 2 048, température zéro et plafond de 192 tokens. Le serveur était local, sans GPU. [Configuration](../../docs/verifications-partie7/serveur-configuration.json) et [journal du serveur](../../docs/verifications-partie7/serveur.log).

| Question | Observation |
| --- | --- |
| Horaire de staging | L’horaire fictif du mardi à 06 h 00 UTC est correctement repris ; formulation maladroite et aucune citation |
| Temporisation validée | Dix minutes inventées, alors que les passages disent que la décision reste ouverte |
| Notification et baisse de prix | Réponse confuse qui ne restitue pas les conditions métier |

Les réponses brutes sont dans [les résultats de l’atelier](../../ateliers/07-ia-maison/resultats-reference/). Elles n’ont pas été réécrites pour les rendre correctes. Les trois sorties s’arrêtent avec `finish_reason: stop`. La présence des bonnes sources ne valide pas la réponse produite.

## Relecture et limites

La [passe adverse](../../docs/relecture-partie7.md) examine la progression, les affirmations techniques et les pièges d’interprétation. Les quatre illustrations ont été ouvertes et inspectées ; le graphique reprend les six mesures JSON, sans valeurs inventées.

L’assembleur vérifie la présence des sections et des images référencées. L’archive ZdS contient huit chapitres, vingt-quatre sections et quatre illustrations. Aucun import dans l’interface ZdS n’a été effectué.

Restent à exécuter : Windows, macOS, l’environnement réel de l’auteur et une adaptation de LLM sur GPU. Le [prompt de reprise](../../ateliers/07-ia-maison/experience-gpu/PROMPT-CODEX.md) prépare cette dernière expérience. Le petit réseau entraîné sur CPU ne valide ni cette adaptation d’un LLM ni un usage comme agent de code.
