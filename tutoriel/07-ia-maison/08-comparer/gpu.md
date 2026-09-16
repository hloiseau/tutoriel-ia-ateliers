La machine prévue pour cette expérience dispose d’une RTX 3090 Ti de 24 Go et de 64 Go de RAM. Nous n’avons pas encore identifié son système ni exécuté l’adaptation. Avant de choisir une recette d’entraînement, il faudra vérifier le système, les pilotes et la mémoire réellement disponible.

Le fichier de poids ne représente pas toute la mémoire nécessaire. L’entraînement conserve aussi des informations pour calculer les gradients et mettre à jour les paramètres. La longueur des séquences, la taille des lots, la précision numérique et les couches adaptées changent le budget.[^p7-memoire]

LoRA réduit le nombre de paramètres entraînés, mais le calcul traverse toujours une partie du modèle de base. On ne peut donc pas déduire la consommation totale de mémoire de la seule taille du fichier d’adaptateur.

Le dossier `experience-gpu` contient un protocole de reprise à donner à un agent de code sur cette machine. Il demande de commencer par un essai court, avec un modèle et une révision identifiés, de mesurer la mémoire, puis de sauvegarder et recharger l’adaptateur dans un nouveau processus. Il prévoit aussi la comparaison avec la base et la recherche de régressions. Tant que ce protocole n’a pas été exécuté, il ne constitue ni une procédure validée ni un résultat.

Lors de cet essai, des bibliothèques d’entraînement comme Transformers et PEFT remplaceront notre petit calcul NumPy.[^p7-peft] Le GGUF de la partie 3 ne servira pas de fichier de départ : il faudra récupérer des poids compatibles avec la méthode d’entraînement choisie.

Vous pouvez poursuivre le tutoriel sans cette expérience GPU. Les essais CPU que nous venons de faire suffisent pour distinguer un document ajouté au contexte, un adaptateur et un modèle entraîné depuis zéro.

[^p7-memoire]: Hugging Face, [mémoire et optimisation des LLM](https://huggingface.co/docs/transformers/main/en/llm_tutorial_optimization).
[^p7-peft]: Hugging Face, [prise en main de PEFT](https://huggingface.co/docs/peft/main/en/quicktour).
