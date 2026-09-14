Reprenons notre installation de la partie précédente.

Le fichier GGUF contient les paramètres du **modèle**. **llama.cpp** fournit le moteur qui les utilise pour calculer une réponse. Notre petit client Python envoie la question au serveur et affiche le résultat.

Pour travailler dans un éditeur, nous pouvons remplacer ce client par un **assistant de développement**. C’est lui qui prépare la requête avec notre question et les extraits de code, affiche la réponse et, selon ses fonctions, propose une modification ou exécute une commande.

| Élément | Dans notre installation locale | Ce qu’il fait |
| --- | --- | --- |
| Modèle | Un fichier GGUF | Fournit les paramètres utilisés pour produire la réponse |
| Moteur et serveur | `llama-server` | Charge le modèle, effectue les calculs et reçoit les requêtes |
| Assistant | Continue dans l’éditeur | Prépare la conversation et permet de travailler avec le code |
Table: Les trois éléments que nous allons relier

Changer d’assistant ne signifie donc pas forcément changer de modèle. Et changer de modèle ne demande pas forcément de quitter son éditeur.

Il faut aussi distinguer **l’endroit où l’assistant agit** et **l’endroit où le modèle tourne**. Un agent lancé dans votre terminal peut lire des fichiers et exécuter les tests sur votre ordinateur, tout en envoyant le contexte à un service distant pour obtenir ses réponses.

À l’inverse, une extension peut envoyer ses requêtes à `127.0.0.1`, comme notre client Python. Dans ce cas, c’est notre serveur qui calcule les réponses. Le mot « local » mérite donc une petite question supplémentaire : *qu’est-ce qui tourne localement, exactement ?*
