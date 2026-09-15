Téléchargez [l’archive MCP et skills](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-mcp-skills.zip) et décompressez-la. Si vous avez déjà le dépôt, ouvrez `ateliers/06-mcp-skills`. Le terminal doit se trouver à côté de `client.py`.

Créez un environnement Python :

```bash
python -m venv .venv
```

Comme dans les ateliers précédents, remplacez la commande de création par `python3` ou `py -3.12` si c’est celle que vous utilisez. Activez ensuite l’environnement :

| Terminal | Commande |
| --- | --- |
| Bash ou Zsh, Linux/macOS | `source .venv/bin/activate` |
| PowerShell, Windows | `.venv\Scripts\Activate.ps1` |
| Invite de commandes Windows | `.venv\Scripts\activate.bat` |

Si PowerShell refuse l’activation, vous pouvez employer directement `.venv\Scripts\python.exe` à la place de `python` dans la suite. Inutile de changer la politique de votre machine pour cela.

Installez les dépendances :

```bash
python -m pip install -r requirements.txt
```

Nous utilisons le SDK Python officiel de MCP. Les versions de l’atelier sont conservées dans ce fichier ; la dépendance directe est `mcp==2.2.0`. Un exemple trouvé ailleurs peut employer une ancienne API du SDK, même s’il parle du même protocole.[^p6-sdk]

L’installation télécharge des bibliothèques. Le serveur que nous allons lancer lit, lui, les fichiers du dossier `donnees` : aucun accès à Jira ou à un modèle n’est nécessaire.

[^p6-sdk]: [SDK Python officiel de MCP](https://github.com/modelcontextprotocol/python-sdk).
