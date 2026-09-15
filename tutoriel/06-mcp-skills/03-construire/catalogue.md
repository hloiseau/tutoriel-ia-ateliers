Notre outil ne connaît qu’un ticket. Branchons-le sur les données de l’atelier.

Ajoutez ces imports :

```python
import json
from pathlib import Path
```

Après la création de `mcp`, insérez :

```python
ROOT = Path(__file__).resolve().parent


def catalogue(nom):
    # Le nom vient du programme, jamais d’un argument du client.
    return json.loads((ROOT / "donnees" / nom).read_text(encoding="utf-8"))
```

`ROOT` désigne le dossier du fichier serveur. Le catalogue reste donc accessible même si un assistant démarre ce programme depuis un autre dossier. Ici, `nom` viendra uniquement de chaînes écrites dans nos fonctions : le client ne pourra pas choisir un chemin de fichier.

Remplacez ensuite **toute la fonction `lire_ticket`, décorateur compris**, par :

```python
@mcp.tool()
def lire_ticket(identifiant: str) -> dict[str, Any]:
    """Lire un ticket fictif, ses questions ouvertes et ses sources."""
    tickets = catalogue("tickets.json")
    if identifiant not in tickets:
        raise ToolError("Ticket introuvable dans le jeu de démonstration.")
    return tickets[identifiant]
```

Essayez maintenant :

```bash
python client.py ticket PRIX-2 --serveur mon_serveur.py --journal sorties/c02-ticket.json
```

Le résultat contient les deux questions ouvertes de PRIX-2. Comparez-le avec `donnees/tickets.json` : la fonction a trouvé l’identifiant dans le catalogue et renvoyé son contenu. Elle n’a plus besoin d’embarquer les données de chaque ticket dans son code.

Nous relisons le petit fichier à chaque appel. Cela rend les changements immédiatement visibles et suffit pour ce jeu de données. Un service réel appellerait peut-être une API, gérerait ses erreurs et contrôlerait les droits du compte utilisé ; nous avons isolé l’accès aux données pour pouvoir le faire évoluer.
