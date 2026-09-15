**TL;DR** — Nous allons consulter des tickets avec un vrai serveur MCP, développer le nôtre pas à pas, puis préparer une recette avec un skill que nous pourrons modifier nous-mêmes.

Jusqu’ici, nous avons donné des fichiers à l’agent et observé ses appels d’outils. Mais les informations nécessaires ne sont pas toujours dans le dépôt : le ticket est dans Jira, une décision dans la documentation, un résultat dans les logs… On peut tout copier dans la conversation. Une fois. À la dixième, on aimerait bien faire autrement. 😅

Nous allons donner à l’agent un moyen de consulter ces informations, puis lui expliquer comment s’en servir pour une tâche précise. Ce sont deux choses différentes : **accéder à un ticket** et **préparer les tests de ce ticket**.

Pour suivre, gardez Python 3.12 et l’assistant utilisé dans la partie 4. Le serveur et le client de l’atelier fonctionnent sur CPU, sans modèle et sans compte sur un service de tickets. Les essais dans l’assistant utilisent votre modèle habituel. Nous n’allons pas transformer le petit modèle local de la partie 3 en agent de développement.

Les tickets et les documents sont fictifs. Nous retrouvons notre suivi de prix avec un premier ticket, PRIX-1, dont la règle est décidée, et un second, PRIX-2, auquel il manque encore des informations. Les [fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/main/ateliers/06-mcp-skills) sont disponibles dans le dépôt.
