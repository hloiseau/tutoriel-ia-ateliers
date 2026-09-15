Dans le dossier qui contient `client.py` et `donnees`, créez un fichier **vide** nommé `mon_serveur.py`. Le fichier `serveur.py` reste notre corrigé ; pour l’instant, nous écrivons dans le nouveau fichier.

Ajoutez ces lignes :

```python
from mcp.server import MCPServer

mcp = MCPServer("atelier-tickets", version="1.0.0")

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

`MCPServer` vient du SDK installé au premier chapitre. Nous lui donnons un nom et une version, puis `run` attend les demandes sur le transport stdio. La condition finale permet de démarrer le serveur lorsque nous exécutons ce fichier ; l’importer depuis un test ne le démarrera pas.[^p6-construire-sdk]

Enregistrez le fichier, puis lancez, toujours depuis le dossier de l’atelier :

```bash
python client.py inventaire --serveur mon_serveur.py --journal sorties/c00-inventaire.json
```

Le journal doit indiquer `"serveur": "mon_serveur.py"` et une liste `tools` vide. C’est normal : notre serveur sait répondre, mais nous ne lui avons encore rien donné à faire. 🙂

L’option `--serveur` choisit le fichier Python que le client démarre. Sans elle, il lancerait `serveur.py`, le corrigé. Gardons-la dans les commandes de construction pour observer notre propre travail.

Pour la suite, placez les nouvelles définitions **avant** le bloc `if __name__ == "__main__":`, qui doit rester à la fin du fichier. Une fonction définie après `run` ne serait pas enregistrée pendant que le serveur attend les demandes.

Si vous êtes perdu à une étape, le dossier `construction` contient les états intermédiaires. Copiez le contenu de l’état concerné dans `mon_serveur.py`, à côté de `donnees` ; les chemins sont prévus pour cet emplacement.

[^p6-construire-sdk]: [SDK Python officiel de MCP](https://github.com/modelcontextprotocol/python-sdk), version 2.2.0 utilisée dans cet atelier.
