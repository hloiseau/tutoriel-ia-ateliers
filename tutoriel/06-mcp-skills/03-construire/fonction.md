En haut du fichier, cette ligne crée notre serveur :

```python
mcp = MCPServer("atelier-tickets", version="1.0.0")
```

Le décorateur `@mcp.tool(...)` qui précède `lire_ticket` l’enregistre comme outil. Sa description vient de la chaîne placée au début de la fonction. L’annotation de l’argument indique ce que le client peut lui transmettre.[^p6-serveur]

Dans notre fonction, le travail proprement dit reste très ordinaire : charger le catalogue, chercher l’identifiant, retourner le ticket. Si l’identifiant manque, `ToolError` produit une erreur d’outil explicite. Le SDK se charge de l’exposition par MCP.

Regardez aussi le type de retour : `dict[str, Any]`. Nous retournons un objet dont les clés sont des chaînes et dont les valeurs peuvent différer. Avec cette annotation, notre SDK fournit le contenu structuré que nous avons consulté. Les champs précis de nos tickets restent définis par notre petit jeu de données ; nous n’avons pas encore construit un modèle de validation complet pour chacun.

Pour comprendre ce qui appartient à notre application, changez le titre de PRIX-1 dans une copie de `tickets.json`, puis relancez une lecture avec un nouveau journal. Le titre change, le protocole reste le même. Rétablissez ensuite le fichier : nous gardons les données communes pour les exercices suivants.

[^p6-serveur]: SDK Python MCP, [définir un serveur et ses outils](https://py.sdk.modelcontextprotocol.io/servers/).
