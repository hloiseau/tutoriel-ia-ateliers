# Mission locale — partie 3, serveur CPU puis GPU

Applique le [prompt coordinateur](../LOCAL-COORDINATEUR.md). Lis `ateliers/03-modele-local/atelier-local/README.md`, les chapitres de `tutoriel/03-modele-local/` et les rapports de vérification existants.

## Référence et installation

Un vrai serveur CPU a déjà été interrogé sous Linux avec la version b10809 du moteur et les poids vérifiés par empreinte. Ce sont les conditions de cette exécution antérieure, pas une preuve de compatibilité avec le système de Hugo.

Choisis un binaire adapté au système et au matériel réellement observés. Inspecte son aide et sa version. Sur Linux, vérifie les bibliothèques et le backend chargé ; ne copie pas mécaniquement un réglage `LD_LIBRARY_PATH` ou `GGML_BACKEND_PATH` prévu pour un autre dossier. Sur Windows ou macOS, adapte les commandes et conserve l’équivalent exact utilisé.

Télécharge le modèle avec le script prévu et vérifie son empreinte. Réutilise un fichier existant seulement après contrôle. Lance le serveur en écoute locale, sur un port libre. Préserve la correspondance entre son alias de modèle et celui utilisé par le client. Attends que le contrôle de santé réussisse avant les requêtes.

## Refaire le parcours CPU

Suis les chapitres depuis le début : préparation, lancement, premier appel, cinq questions, puis mesures. Pars des paramètres de la référence, notamment deux fils CPU et une capacité de contexte de 2 048 quand ils sont applicables à la version utilisée.

Conserve les réponses complètes, leur exactitude et les causes d’arrêt. Distingue chargement initial, échauffement et série d’au moins trois appels identiques. Enregistre chaque mesure individuelle. Vérifie ce que mesure réellement le client : durée globale, débit calculé ou débit interne du moteur.

Si tu changes un paramètre, change-le seul avant une nouvelle série. Une augmentation de la capacité du contexte n’est pas la même expérience qu’un prompt plus long. Note la consommation mémoire et sa méthode de collecte.

Vérifie le fonctionnement après téléchargement sans dépendance à un appel distant. Utilise une méthode limitée à l’expérience : inspection des appels et, si possible, isolement réseau du processus. Ne modifie pas le pare-feu global ni la connexion de toute la machine. Si tu ne peux pas établir le fonctionnement hors ligne, dis précisément ce qui manque.

## Comparaison avec la 3090 Ti

Arrête proprement le serveur que tu as lancé avant de démarrer sa variante GPU. Garde les mêmes poids, questions, limites de génération et conditions d’échantillonnage. Confirme le périphérique et les couches réellement affectées au GPU dans les journaux du moteur ; une option passée en ligne de commande ne suffit pas.

Mesure durée totale et VRAM avec une méthode déclarée. Le temps avant le premier token n’est disponible que si l’instrumentation le permet. Note les autres charges connues. N’extrapole pas les résultats de ce petit modèle à un grand modèle de code.

Une éventuelle variante plus grande répondra à un besoin précis identifié après ces essais. Vérifie taille, licence et marge mémoire avant son téléchargement. Ne transforme pas cette mission en collection de modèles.

## Livrable

Rapport reproductible, journaux CPU/GPU, tableau des essais individuels, réponses conservées et corrections propres au système. Indique séparément « fonctionne », « répond correctement à ces questions » et « délai utile pour cet usage ». La réussite de cet atelier ne valide pas un agent de code sur CPU.
