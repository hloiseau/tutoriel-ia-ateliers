Commençons par un seul ticket, écrit dans le code. Ajoutez ces deux imports en haut du fichier :

```python
from typing import Any
from mcp.server.mcpserver.exceptions import ToolError
```

Puis insérez cette fonction avant le bloc final de démarrage :

```python
@mcp.tool()
def lire_ticket(identifiant: str) -> dict[str, Any]:
    """Lire un ticket fictif par son identifiant."""
    if identifiant != "PRIX-1":
        raise ToolError("Ticket introuvable dans le jeu de démonstration.")
    return {
        "id": "PRIX-1",
        "titre": "Ne plus notifier une simple remise en stock",
    }
```

Le décorateur `@mcp.tool()` enregistre la fonction comme outil. Sa chaîne de documentation décrit son rôle ; l’annotation `identifiant: str` indique qu’on attend du texte. `dict[str, Any]` décrit un objet dont les clés sont des chaînes et dont les valeurs peuvent être de types différents. Le SDK en tire un résultat structuré.[^p6-construire-outil]

Appelez votre nouvel outil :

```bash
python client.py ticket PRIX-1 --serveur mon_serveur.py --journal sorties/c01-ticket.json
python client.py ticket PRIX-999 --serveur mon_serveur.py --journal sorties/c01-absent.json
```

Dans le premier journal, `structuredContent` contient les deux champs `id` et `titre`. Dans le second, `isError` vaut `true` : `ToolError` a produit une erreur compréhensible par le client.

Pour vérifier que vous appelez bien votre code, changez momentanément le titre retourné en « Mon premier outil MCP », enregistrez et relancez la première commande avec un **nouveau nom de journal**. Vous devez retrouver ce titre dans la réponse. Rétablissez ensuite le texte initial.

Le client relance le processus à chaque commande : il utilise donc le fichier enregistré. Nous avons écrit un outil MCP et observé sa réponse sans demander à une IA de l’interpréter.

[^p6-construire-outil]: SDK Python MCP, [serveurs et outils](https://py.sdk.modelcontextprotocol.io/servers/).
