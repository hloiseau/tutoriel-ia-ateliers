# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
import json
from pathlib import Path
from mcp.server import MCPServer
from typing import Any
from mcp.server.mcpserver.exceptions import ToolError

mcp = MCPServer("atelier-tickets", version="1.0.0")

ROOT = Path(__file__).resolve().parent


def catalogue(nom):
    # Le nom vient du programme, jamais d’un argument du client.
    return json.loads((ROOT / "donnees" / nom).read_text(encoding="utf-8"))

@mcp.tool()
def lire_ticket(identifiant: str) -> dict[str, Any]:
    """Lire un ticket fictif, ses questions ouvertes et ses sources."""
    tickets = catalogue("tickets.json")
    if identifiant not in tickets:
        raise ToolError("Ticket introuvable dans le jeu de démonstration.")
    return tickets[identifiant]

if __name__ == "__main__":
    mcp.run(transport="stdio")
