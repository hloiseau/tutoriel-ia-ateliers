Le modèle produit une demande ou une réponse. L’application qui l’entoure peut aussi lui donner des **outils** : lire un fichier, chercher dans une base, exécuter des tests ou préparer un événement d’agenda. C’est cette application qui exécute les appels autorisés et en renvoie les résultats au modèle.

Lorsque l’assistant enchaîne ces appels, observe leurs résultats et décide de la suite, nous parlons d’un **agent**. Une demande comme « prépare le point de l’équipe » peut l’amener à lire le tableau, ouvrir les notes, puis créer un document. Les accès disponibles déterminent aussi jusqu’où il peut aller. Un accès en lecture à un dossier et un droit d’envoi dans une messagerie ne rendent pas les mêmes actions possibles.

Un **pipeline** fixe davantage l’enchaînement : recevoir un lot, retirer les copies exactes, extraire les demandes, contrôler le résultat, préparer un point. Une étape peut utiliser un modèle ou un agent. D’autres se contentent d’appliquer une règle, par exemple comparer deux identifiants. Nous pouvons placer une attente au moment où une personne doit décider.

| Besoin | Exemple en développement | Exemple dans les tâches de travail |
| --- | --- | --- |
| Donner le contexte | Ticket et code de la fonction | Courriels et notes de réunion |
| Utiliser un outil | Lancer les tests | Lire le tableau de suivi |
| Appliquer une règle | Refuser une valeur négative | Écarter la seconde copie d’un message |
| Vérifier une proposition | Relire la modification | Comparer la synthèse aux documents |
| Prendre une décision | Accepter le changement | Confirmer une date avec l’équipe |
Table: Des gestes communs, appliqués à deux familles de tâches

Vous rencontrerez aussi **MCP**, un protocole qui permet à des applications de dialoguer avec des serveurs donnant accès à des outils et à des ressources. Il ne décide pas à votre place quels accès sont acceptables. Un **skill** rassemble une procédure et, selon l’outil, des ressources pour accomplir une tâche. Nous verrons comment adapter ces procédures à nos besoins, comme une recette que l’on modifie selon ce que l’on veut cuisiner.

Pour commencer, nous n’avons pas besoin de tout brancher. Un dossier délimité, une tâche compréhensible et un résultat que l’on sait relire donnent déjà de quoi essayer. Les accès supplémentaires viendront lorsqu’ils serviront à résoudre une difficulté précise.
