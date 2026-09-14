# Résultats de référence et limites

## Partie 2

Exécutions CPU sous Linux, Python 3.12.14. Les 1 797 images sont séparées en 1 077 images d’entraînement, 360 de validation et 360 de test. Les deux modèles prédéfinis obtiennent chacun 345 bonnes réponses sur 360 dans l’exécution de référence. Les gradients ont été comparés à des différences finies. Les programmes ont également été rejoués depuis une archive extraite.

La logique de la grille de dessin a été exercée avec un DOM simulé. Les interactions dans un vrai navigateur restent à vérifier.

## Partie 3

Exécution sous Linux x86-64, Python 3.12.14, llama.cpp b10809, variante CPU générique `libggml-cpu-x64.so`, deux fils CPU et contexte de 2 048 tokens. Les poids ont été vérifiés par SHA-256. Les résultats ne représentent pas le débit optimal de toutes les variantes du moteur.

Les cinq questions ont été envoyées au modèle. Le mardi est correctement donné à 10 heures ; le modèle s’abstient pour le dimanche ; le JSON demandé est valide. L’explication anglaise tient en une phrase au lieu de deux. Le français est maladroit et la réponse atteint la limite de 96 tokens.

La série `cpu-verifie-2048` conserve l’échauffement et trois requêtes. Le rapport tokens/durée inclut la requête complète ; ce n’est pas le débit du seul décodage. Aucun relevé de RAM, de mémoire vidéo ou d’énergie n’est fourni.

Six tests du client utilisent des réponses factices. Ils contrôlent son comportement HTTP et sont distincts des appels réels au modèle.

## Partie 4

Les trois états du projet et les scénarios ont été exécutés. La suite initiale contient trois tests. La suite complétée en contient treize, dont deux échouent avant correction ; les treize passent après. Les mutations `<` en `<=` et la suppression de la condition de disponibilité font échouer la suite.

Les prompts sont proposés pour différents agents. Aucun comportement d’un produit particulier n’est garanti par ces résultats.

## À reprendre sur d’autres environnements

Les commandes Windows et macOS, le GPU et les interactions dans un navigateur réel restent à valider. Gardez vos propres résultats et leurs paramètres, même lorsqu’ils diffèrent de ceux fournis.
