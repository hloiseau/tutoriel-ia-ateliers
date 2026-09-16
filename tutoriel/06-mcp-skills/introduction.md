**TL;DR** — Nous allons consulter des tickets avec un serveur utilisant le protocole MCP, développer le nôtre pas à pas, puis préparer une recette avec un skill que nous pourrons modifier nous-mêmes.

Jusqu’ici, nous avons donné des fichiers à l’agent et observé ses appels d’outils. Seulement, les informations nécessaires ne vivent pas toujours dans le dépôt : le ticket est dans Jira, une décision dans la documentation, un résultat dans les logs… On peut tout copier dans la conversation. Une fois. À la dixième, on aimerait bien faire autrement. 😅

Nous allons donc lui donner un accès précis à ces informations, puis écrire la procédure qui permet de s’en servir pour préparer des tests. Le serveur MCP s’occupera du premier travail ; le skill décrira le second.

Pour suivre, gardez Python 3.12 et l’assistant utilisé dans la partie 4. Le serveur et le client de l’atelier fonctionnent sur CPU, sans modèle et sans compte sur un service de tickets. Les essais dans l’assistant réutilisent votre modèle habituel : le petit modèle local de la partie 3 n’a pas été validé pour mener une session d’agent de développement.

Les tickets et les documents sont fictifs. Nous retrouvons notre suivi de prix avec un premier ticket, PRIX-1, dont la règle est décidée, et un second, PRIX-2, auquel il manque encore des informations. Les [fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/main/ateliers/06-mcp-skills) sont disponibles dans le dépôt.
