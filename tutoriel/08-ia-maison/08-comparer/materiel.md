| Expérience | Matériel utilisé ici | Ce que nous avons observé |
| --- | --- | --- |
| Recherche dans les paragraphes | CPU | Une question reformulée échappe à la recherche lexicale |
| Réponses avec SmolLM2-360M-Instruct Q8_0 | CPU, serveur local | Une réponse correcte sur l’horaire, un délai inventé, une réponse confuse sur le prix |
| Entraînement du modèle de caractères | CPU | La perte baisse ; la génération reste mauvaise |
| Adaptation complète et LoRA de ce petit réseau | CPU | Le nouveau format est mieux prédit ; l’ancien se dégrade |
| Adaptation d’un LLM sur RTX 3090 Ti | À faire sur la machine locale | Aucun résultat annoncé pour cet atelier |

Ces usages n’ont pas le même coût. Notre réseau de caractères tient dans de petits tableaux. Le modèle documentaire contient beaucoup plus de paramètres ; nous l’avons seulement utilisé pour trois appels courts, sans longue session ni appels d’outils répétés.

Ces trois réponses sur CPU ne disent donc rien du confort d’un agent de code sur la même machine. Pour travailler sur un dépôt, reprenez les critères pratiques de la partie 4 : qualité des modifications, temps d’attente, contexte utile et vérification du résultat.
