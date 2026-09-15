Notre client de la partie précédente envoyait une question à `llama-server`, qui faisait calculer la réponse par le modèle. Un assistant de développement ajoute notamment les fichiers du projet à cette conversation.

Il faut distinguer **l’endroit où l’assistant agit** et **l’endroit où le modèle tourne**. Dans l’installation que nous allons utiliser, l’éditeur et les tests tournent sur notre ordinateur. Le modèle, lui, reçoit le contexte et calcule sa réponse chez le fournisseur.

| Élément | Dans l’atelier |
| --- | --- |
| Projet et tests Python | Sur notre ordinateur |
| Assistant | Dans l’éditeur, avec accès à notre copie de travail |
| Modèle et moteur d’inférence | Chez le fournisseur du modèle |
Table: Où se passe le travail ?

C’est pour cela que cette installation ne demande pas de GPU. Faire également tourner le modèle chez soi est une autre possibilité, avec des besoins de mémoire et de calcul à évaluer. Un petit modèle qui répond sur CPU ne devient pas un agent de code efficace simplement parce qu’on le branche à l’éditeur.
