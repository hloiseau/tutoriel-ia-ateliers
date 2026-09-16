Notre serveur utilise **stdio** : le programme client lance un processus et échange avec lui par son entrée et sa sortie standard. MCP dispose aussi d’un transport HTTP pour des serveurs accessibles par le réseau.[^p6-transport]

![Le client MCP appartient à l’assistant ; le serveur lit les fichiers locaux, tandis que le modèle peut être distant.](image:images/trajet.png)
Figure: Un serveur local peut alimenter un modèle distant

Dans le vocabulaire MCP, l’application qui accueille l’interaction est l’**hôte**. Elle contient un client MCP qui parle au serveur. Le modèle n’a pas besoin de comprendre comment Python ouvre `tickets.json` ; il reçoit les outils que l’hôte lui présente et les résultats que celui-ci réintroduit dans la conversation.

Le mot *local* désigne ici le serveur, qui tourne sur notre machine. Avec un modèle hébergé, les informations issues du ticket peuvent ensuite quitter cette machine pour rejoindre la conversation. Il faut suivre tout le trajet avant de conclure où vivent les données.

Pour notre atelier, les données sont fictives. Dans un projet professionnel, ce trajet aide à décider quels champs exposer et avec quel compte accéder aux services. Une liste d’identifiants et de titres suffit parfois pour chercher ; envoyer tout le ticket, ses pièces jointes et son historique à chaque recherche ajouterait des informations dont on n’a pas encore besoin.

[^p6-transport]: Spécification MCP, [transports stdio et Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports).
