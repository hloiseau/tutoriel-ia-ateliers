# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
import hashlib
import unittest
from pathlib import Path
from mcp import Client
from serveur import mcp, ROOT


class ContratMCP(unittest.IsolatedAsyncioTestCase):
    async def test_inventaire_lecture_seule(self):
        async with Client(mcp) as c:
            result=await c.list_tools()
            self.assertEqual({t.name for t in result.tools}, {'lire_ticket','chercher_documentation','lire_document'})
            self.assertTrue(all(t.annotations.read_only_hint for t in result.tools))

    async def test_ticket_retourne_les_questions(self):
        async with Client(mcp) as c:
            result=await c.call_tool('lire_ticket',{'identifiant':'PRIX-2'})
            self.assertFalse(result.is_error)
            self.assertTrue(result.structured_content['questions_ouvertes'])

    async def test_identifiant_inconnu(self):
        async with Client(mcp) as c:
            result=await c.call_tool('lire_ticket',{'identifiant':'PRIX-999'})
            self.assertTrue(result.is_error)

    async def test_chemin_interdit(self):
        async with Client(mcp) as c:
            result=await c.call_tool('lire_document',{'identifiant':'../tickets.json'})
            self.assertTrue(result.is_error)

    async def test_type_incorrect(self):
        async with Client(mcp) as c:
            result=await c.call_tool('lire_ticket',{'identifiant':1})
            self.assertTrue(result.is_error)

    async def test_recherche_vide(self):
        async with Client(mcp) as c:
            result=await c.call_tool('chercher_documentation',{'terme':'   '})
            self.assertTrue(result.is_error)

    async def test_recherche_et_lecture(self):
        async with Client(mcp) as c:
            result=await c.call_tool('chercher_documentation',{'terme':'NOTIFICATION'})
            ids={x['id'] for x in result.structured_content['resultats']}
            self.assertIn('regle-notification',ids)
            doc=await c.call_tool('lire_document',{'identifiant':'regle-notification'})
            self.assertEqual(doc.structured_content['statut'],'en vigueur')

    async def test_aucune_ecriture(self):
        def empreintes():
            return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'donnees').iterdir()}
        avant=empreintes()
        async with Client(mcp) as c:
            result=await c.call_tool('modifier_ticket',{'identifiant':'PRIX-1','statut':'termine'})
            self.assertTrue(result.is_error)
        self.assertEqual(avant,empreintes())

    async def test_document_piege_reste_du_contenu(self):
        async with Client(mcp) as c:
            result=await c.call_tool('lire_document',{'identifiant':'note-archivee'})
            self.assertIn('ignore',result.structured_content['texte'])
            ticket=await c.call_tool('lire_ticket',{'identifiant':'PRIX-1'})
            self.assertEqual(ticket.structured_content['statut'],'a preparer')

    async def test_ressource(self):
        async with Client(mcp) as c:
            result=await c.read_resource('atelier://conventions')
            self.assertIn('centimes',result.contents[0].text)


if __name__=='__main__':
    unittest.main()
