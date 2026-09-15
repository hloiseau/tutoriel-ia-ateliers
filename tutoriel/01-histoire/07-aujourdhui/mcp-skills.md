En novembre 2024, Anthropic présente le **Model Context Protocol**, ou **MCP**. Le protocole vise à faciliter les échanges entre des applications utilisant des modèles et des serveurs qui exposent des ressources ou des outils.[^h7s2-mcp]

Pour reprendre notre exemple, un serveur peut proposer un outil de recherche documentaire. Le protocole aide l’application à découvrir cet outil et à l’appeler. Il ne garantit pas que le modèle saura quand l’utiliser, ni que toutes les réponses obtenues seront correctes.

Les fichiers de consignes et les procédures réutilisables se développent également autour des agents. En 2025, Anthropic présente notamment les **Agent Skills**, des ensembles organisés de consignes, de ressources et éventuellement de scripts, chargés selon le travail à effectuer.[^h7s2-skills]

Les MCP et les skills permettent d’organiser l’accès aux outils et les informations fournies à un agent. Ils ne constituent pas un nouvel entraînement complet du modèle.

Une procédure de revue de code peut ainsi préciser ce qu’il faut examiner, tandis qu’un outil permet de lire les changements. Ce sont deux rôles différents, qui peuvent être combinés.

Les noms des fichiers, les fonctions disponibles et leur chargement varient selon les applications.


[^h7s2-mcp]: [Anthropic, Introducing the Model Context Protocol (25 novembre 2024)](https://www.anthropic.com/news/model-context-protocol).
[^h7s2-skills]: [Anthropic, Equipping agents for the real world with Agent Skills (2025)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
