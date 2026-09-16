# Passe adverse — partie 7

16 septembre 2026. Relecture effectuée dans la même session de rédaction, sans second agent indépendant.

## Parcours et pédagogie

Le parcours suit deux expériences explicitement séparées. Les chapitres 1 à 4 construisent une application documentaire ; les chapitres 5 à 7 utilisent un autre modèle pour rendre l’adaptation et l’entraînement observables sur CPU. Le chapitre 8 relie les résultats au besoin et prépare l’expérience GPU.

Les deux fichiers du lecteur sont construits depuis les blocs du cours, puis exécutés depuis l’archive extraite. Les fonctions de recherche et d’HTTP réutilisées sont identifiées. Le retour au serveur de la partie 3 précise le dossier dans lequel le relancer et donne un lien vers ses commandes. Aucun téléchargement d’un nouveau modèle n’est demandé pour cette étape.

Chaque chapitre commence par un TL;DR. Les résultats arrivent après les manipulations. Les rapports de vérification et les consignes pour la session locale restent hors des fichiers de cours importés dans ZdS.

## Pièges recherchés

| Risque | Traitement retenu |
| --- | --- |
| Faire passer la recherche pour un apprentissage des poids | Contexte et paramètres distingués dès le premier chapitre |
| Attribuer à la recherche lexicale une compréhension des synonymes | Question « purge des fixtures » conservée comme échec réel |
| Transformer un score de recherche en probabilité de vérité | Signification du score explicitée ; évaluation des sources séparée de celle des réponses |
| Valider une phrase parce que sa citation existe | Contre-exemple avec la temporisation, puis réponse réelle inventée |
| Présenter l’interface qui fonctionne comme un assistant fiable | Les trois réponses documentaires et leurs défauts sont conservés |
| Faire croire que le CPU exécute un agent de code utilisable | Appels documentaires courts, petit réseau et session d’agent distingués |
| Faire croire qu’un adaptateur figé préserve tous les comportements | Régression sur les anciennes phrases mesurée, adaptateur actif/désactivé distingué |
| Confondre taille de l’adaptateur et mémoire totale d’entraînement | Poids, gradients, états d’optimiseur et activations mentionnés ; aucune capacité GPU promise |
| Avoir des fenêtres voisines réparties entre train et test | Séparation par identifiants avant la création des fenêtres ; audit exécuté |
| Surestimer l’indépendance du test synthétique | Gabarits communs explicités ; aucune généralisation linguistique annoncée |
| Confondre baisse de perte et génération cohérente | Vrais préfixes à l’évaluation, sorties propres en génération, exemples défaillants conservés |
| Adapter le GGUF directement avec une recette prévue pour d’autres poids | Reprise GPU demande une base compatible et une révision identifiée |

## Contrôles pratiques supplémentaires

L’adaptateur a été rechargé séparément et comparé au modèle complet. Une base différente est refusée. Les gradients des cinq tableaux du réseau et des deux facteurs LoRA sont comparés par différences finies. Les poids de base de LoRA sont vérifiés inchangés par empreinte.

Le modèle original utilisé pour l’inférence a été téléchargé et son empreinte vérifiée avant les trois appels réels. Les petites réponses en français ne sont pas présentées comme une mesure générale de SmolLM2 ou de tous les modèles locaux.

## Limites ouvertes

Le cours est une première rédaction à relire par Hugo. L’import réel ZdS, Windows et macOS n’ont pas été testés. Le protocole GPU est préparé mais non exécuté. Le modèle de caractères est volontairement faible ; obtenir une génération réellement utile demanderait une autre expérience et de nouveaux critères, pas seulement quelques retouches au commentaire des résultats.
