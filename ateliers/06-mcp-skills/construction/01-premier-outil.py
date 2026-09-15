# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
from mcp.server import MCPServer
from typing import Any
from mcp.server.mcpserver.exceptions import ToolError

mcp = MCPServer("atelier-tickets", version="1.0.0")

@mcp.tool()
def lire_ticket(identifiant: str) -> dict[str, Any]:
    """Lire un ticket fictif par son identifiant."""
    if identifiant != "PRIX-1":
        raise ToolError("Ticket introuvable dans le jeu de démonstration.")
    return {
        "id": "PRIX-1",
        "titre": "Ne plus notifier une simple remise en stock",
    }

if __name__ == "__main__":
    mcp.run(transport="stdio")
