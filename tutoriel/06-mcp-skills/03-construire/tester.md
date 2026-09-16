Nos commandes montrent que quelques appels fonctionnent. Écrivons maintenant des contrôles que nous pourrons relancer après chaque changement, sans rouvrir les journaux un par un.

Créez `test_mon_serveur.py` à côté de `mon_serveur.py` et écrivez :

```python
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
```

Lancez uniquement ce fichier :

```bash
python -m unittest test_mon_serveur -v
```

Les trois tests doivent passer. Le deuxième cherche aussi `string_pattern_mismatch`, le code de l’erreur de format retournée par notre version du SDK : une simple erreur « document introuvable » ne suffirait pas. Le troisième vérifie l’inventaire, pour distinguer un outil absent d’un outil présent qui aurait refusé cet appel.

`IsolatedAsyncioTestCase` permet d’écrire des tests avec `async` et `await`. Ici, `Client(mcp)` appelle le serveur en mémoire. Les commandes précédentes complètent donc ces tests en exerçant le transport stdio entre deux processus.

Vérifions que le premier test ne passe pas par accident. Commentez temporairement le décorateur de `lire_ticket` dans **`mon_serveur.py`**, puis relancez les tests. La lecture doit échouer : la fonction existe toujours en Python, mais elle n’est plus exposée comme outil. Rétablissez le décorateur et vérifiez que les trois tests repassent au vert.

Le fichier `construction/test_mon_serveur.py` contient le corrigé de ces tests. La suite `test_serveur.py`, à la racine, est plus complète et teste le serveur de référence ; elle ne remplace pas les tests de votre fichier.

Enfin, faites utiliser votre serveur à l’assistant :

```bash
python configuration.py --serveur mon_serveur.py
```

Dans `.vscode/mcp.json`, remplacez l’entrée **`atelier-tickets`** par celle affichée, en gardant vos autres serveurs. Arrêtez puis redémarrez cette entrée depuis **MCP: List Servers** pour charger votre programme. Les chemins absolus affichés concernent votre machine. Avec un autre assistant, modifiez le chemin du programme dans sa configuration MCP.

Demandez de nouveau la lecture de PRIX-1 et inspectez l’appel. Cet essai dépend de votre installation et de votre modèle. Les tests Python ont vérifié le serveur et ses appels ; ils ne prédisent pas ce que l’assistant choisira d’en faire. Pour les chapitres suivants, nous garderons `mon_serveur.py` et cette configuration.
