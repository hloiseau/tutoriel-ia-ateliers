# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from mcp import Client
from mon_serveur import mcp


class MonServeurMCP(unittest.IsolatedAsyncioTestCase):
    async def test_lire_un_ticket(self):
        async with Client(mcp) as client:
            reponse = await client.call_tool("lire_ticket", {"identifiant": "PRIX-1"})
        self.assertFalse(reponse.is_error)
        self.assertEqual(reponse.structured_content["id"], "PRIX-1")

    async def test_refuser_un_chemin(self):
        async with Client(mcp) as client:
            reponse = await client.call_tool("lire_document", {"identifiant": "../tickets"})
        self.assertTrue(reponse.is_error)
        self.assertIn("string_pattern_mismatch", reponse.content[0].text)

    async def test_aucun_outil_ecriture(self):
        async with Client(mcp) as client:
            inventaire = await client.list_tools()
            reponse = await client.call_tool(
                "modifier_ticket", {"identifiant": "PRIX-1", "statut": "termine"}
            )
        self.assertTrue(reponse.is_error)
        self.assertNotIn("modifier_ticket", {t.name for t in inventaire.tools})


if __name__ == "__main__":
    unittest.main()
