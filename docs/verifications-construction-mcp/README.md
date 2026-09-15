# Rejeu du chapitre de construction

[Relecture adverse](../relecture-construction-mcp.md) · [Résultats et limites](../../tutoriel/06-mcp-skills/VERIFICATION.md).

`executions.json` contient l’empreinte de l’archive pratique, les commandes et les codes de sortie. Les journaux JSON proviennent des appels stdio réels. Les fichiers texte conservent les sorties des commandes et des tests. Les deux mutations doivent produire un échec ; les restaurations doivent réussir.

Le script de rejeu lit les blocs Markdown du chapitre et utilise l’environnement Python MCP du lanceur. Aucun modèle n’est appelé. Le contenu de la configuration est vérifié mais ses chemins temporaires ne sont pas publiés.
