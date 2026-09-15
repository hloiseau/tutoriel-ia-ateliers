Dans un agent fondé sur un modèle de langage, le modèle peut proposer un appel. L’application vérifie cet appel, exécute l’outil autorisé et ajoute son résultat au contexte. Le modèle reçoit alors de nouvelles informations et peut continuer.

![Boucle entre la demande, le modèle, l’application qui exécute l’outil et le résultat renvoyé au modèle.](image:images/agent-outils.png)
Figure: L’application effectue les appels ; les résultats alimentent le contexte du modèle.

Nous venons de programmer la partie qui exécute un outil. Pour obtenir un agent complet, il faudrait notamment y associer un modèle capable de proposer les appels, lui décrire les outils et organiser la boucle.

Un **MCP** peut fournir un protocole commun pour présenter et utiliser des outils exposés par un serveur. Il ne remplace pas le modèle, ni les autorisations de l’application.[^p2-8-boucle-mcp]

Un **skill** peut rassembler une procédure, des consignes et des ressources : par exemple, quels fichiers examiner lors d’une revue ou comment interpréter les sorties d’une commande. Lire ce skill fournit des informations à l’agent ; cela n’entraîne pas automatiquement les poids du modèle.

Si une procédure prévoit de lancer les tests, il faut encore un outil pour les exécuter, des droits adaptés et une manière de juger le résultat. Une sortie de commande peut fournir une preuve utile, mais elle peut aussi être incomplète ou mal interprétée.


[^p2-8-boucle-mcp]: [Model Context Protocol, architecture](https://modelcontextprotocol.io/docs/learn/architecture).
