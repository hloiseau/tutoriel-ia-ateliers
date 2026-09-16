Que se passe-t-il si l’on envoie un terme de recherche énorme ou un chemin à la place d’un identifiant ? Précisons le contrat de nos outils.

Remplacez la ligne `from typing import Any` par ces trois imports :

```python
from typing import Annotated, Any
from pydantic import Field, StrictStr
from mcp.types import ToolAnnotations
```

Après la création de `mcp` et avant les fonctions, ajoutez :

```python
IdentifiantTicket = Annotated[
    StrictStr, Field(pattern=r"^PRIX-[0-9]+$", max_length=24)
]
IdentifiantDocument = Annotated[
    StrictStr, Field(pattern=r"^[a-z0-9-]+$", max_length=60)
]
TermeRecherche = Annotated[
    StrictStr, Field(min_length=2, max_length=80)
]

LECTURE = ToolAnnotations(
    readOnlyHint=True,
    destructiveHint=False,
    idempotentHint=True,
    openWorldHint=False,
)
```

`Annotated` associe un type à des contraintes. `StrictStr` demande une chaîne ; `Field` fixe les longueurs et les caractères acceptés. Les noms `IdentifiantTicket`, `IdentifiantDocument` et `TermeRecherche` nous évitent de répéter ces définitions dans les signatures.

Dans les trois fonctions, remplacez **seulement la ligne qui commence par `def`** par la ligne correspondante ci-dessous. Conservez leur corps indenté ; ces trois lignes ne forment pas un programme à coller ensemble :

```python
def lire_ticket(identifiant: IdentifiantTicket) -> dict[str, Any]:
def chercher_documentation(terme: TermeRecherche) -> dict[str, Any]:
def lire_document(identifiant: IdentifiantDocument) -> dict[str, Any]:
```

Remplacez également les trois décorateurs `@mcp.tool()` par `@mcp.tool(annotations=LECTURE)`.

Les annotations présentent nos outils comme des lectures non destructives que l’on peut répéter sans ajouter d’effet d’écriture. `openWorldHint=False` indique qu’ils travaillent dans notre jeu fermé de données. Le client peut utiliser ces indications pour présenter ou choisir les outils. Les droits du processus, eux, restent inchangés : notre code doit réellement tenir ce qu’il annonce.[^p6-construire-annotations]

Vérifiez l’inventaire et une demande invalide :

```bash
python client.py inventaire --serveur mon_serveur.py --journal sorties/c04-inventaire.json
python client.py document ../tickets --serveur mon_serveur.py --journal sorties/c04-invalide.json
```

L’inventaire décrit les contraintes dans `inputSchema` et expose `readOnlyHint`. L’appel invalide retourne une erreur de validation. Un identifiant bien formé mais absent produira, lui, l’erreur « Document introuvable » écrite dans notre fonction. Ce sont deux échecs différents.

La fonction de recherche conserve son contrôle après `strip()` : une chaîne de trois espaces satisfait la longueur minimale annoncée, mais ne contient aucun terme utile.

[^p6-construire-annotations]: Spécification MCP, [annotations des outils](https://modelcontextprotocol.io/specification/2026-07-28/server/tools).
