Dans la partie précédente, notre client envoyait une question à `llama-server`, puis le modèle calculait une réponse. Un assistant de développement reprend ce principe en y ajoutant du code, des résultats de commandes et parfois le droit de modifier les fichiers.

Il faut distinguer **l’endroit où l’assistant agit** et **l’endroit où le modèle tourne**. Dans l’installation que nous allons utiliser, l’éditeur et les tests tournent sur notre ordinateur. Le modèle, lui, reçoit le contexte et calcule sa réponse chez le fournisseur.

| Élément | Dans l’atelier |
| --- | --- |
| Projet et tests Python | Sur notre ordinateur |
| Assistant | Dans l’éditeur, avec accès à notre copie de travail |
| Modèle et moteur d’inférence | Chez le fournisseur du modèle |
Table: Où se passe le travail ?

Le calcul lourd ayant lieu chez le fournisseur, cette installation ne demande pas de GPU. On peut aussi faire tourner le modèle chez soi, avec des besoins de mémoire et de calcul à évaluer. Obtenir une réponse courte sur CPU ne suffit pas à établir qu’un modèle soutiendra le rythme et le contexte d’une session d’agent de code.
