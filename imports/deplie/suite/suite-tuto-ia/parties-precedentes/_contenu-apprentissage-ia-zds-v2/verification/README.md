# Exécutions et portée des contrôles

Les journaux ont été obtenus dans un environnement virtuel Python neuf, sous Linux. Les scripts d’entraînement ont limité les bibliothèques de calcul à un fil CPU. Les durées et pics mémoire sont ceux des processus mesurés ; ils ne décrivent pas la mémoire totale de la machine. La référence précise du processeur n’était pas exposée par l’environnement.

Chaque commande d’`executions.json` a été lancée dans un processus distinct. La durée est mesurée autour du sous-processus ; le pic mémoire vient de `resource.getrusage(RUSAGE_CHILDREN).ru_maxrss`, converti de Kio en Mio sous Linux. Le temps interne à l’entraînement est enregistré séparément dans `resultats-reference/*.json`.

Le découpage en 1 077 / 360 / 360 images a été vérifié : les groupes sont disjoints et couvrent toutes les images. Les gradients de la version linéaire et de la version à couche cachée ont été comparés à des différences finies (écart absolu maximal d’environ 4,7e-10). Les modèles rechargés donnent les mêmes nombres de bonnes réponses que leurs rapports.

Les appels à des outils non autorisés et les arguments inattendus ont été vérifiés. Les gestionnaires JavaScript de dessin, l’export JSON, l’effacement et le clavier ont été exercés sous Node avec un DOM simulé. Le dessin d’exemple a été exporté par ce code puis soumis au classifieur (3 : 51,4 %, 9 : 33,1 %, 7 : 11,5 %).

Les treize illustrations ont été inspectées. Le rendu et les interactions de la grille dans un véritable navigateur restent à contrôler : l’installation du navigateur de test a échoué par expiration du téléchargement. Aucun test réel Windows, macOS ou import ZdS n’est revendiqué.

Le parcours principal a aussi été rejoué depuis l’archive extraite dans un nouveau dossier, sans modèle préchargé dans sorties : chargement, entraînement linéaire, évaluation, dessin et bigrammes. Le résultat reste de 345 bonnes réponses sur 360. Le journal est dans parcours-archive.json.

Les expériences n’ont pas été optimisées après consultation du jeu de test. Les deux modèles prédéfinis obtiennent chacun 345 bonnes réponses sur 360 ; cette égalité est conservée dans la rédaction.
