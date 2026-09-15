# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
from mcp.server import MCPServer

mcp = MCPServer("atelier-tickets", version="1.0.0")

if __name__ == "__main__":
    mcp.run(transport="stdio")
