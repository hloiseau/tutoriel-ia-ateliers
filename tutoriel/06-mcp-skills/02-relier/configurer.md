Si vous suivez le parcours VS Code de la partie 4, ouvrez le dossier de cet atelier dans l’éditeur. Dans le terminal qui utilise notre environnement Python, lancez :

```bash
python configuration.py
```

Le script affiche une configuration avec le chemin de **votre** Python et celui de `serveur.py`. Copiez ce JSON dans `.vscode/mcp.json`, à la racine du dossier ouvert. Si vous avez déjà ce fichier, ajoutez seulement `atelier-tickets` à son objet `servers` ; conservez vos autres entrées.

Dans la palette de commandes, ouvrez **MCP: List Servers**, sélectionnez `atelier-tickets`, puis démarrez-le. **Show Output** permet de retrouver ses erreurs. Dans le chat, gardez l’agent **Local** de notre parcours et vérifiez que les outils de l’atelier sont disponibles dans la sélection des outils.[^p6-vscode-mcp]

Demandez :

> Consulte PRIX-1 avec le MCP atelier-tickets et donne-moi sa règle.

Dépliez l’appel d’outil. Retrouve-t-on `lire_ticket`, l’identifiant `PRIX-1` et la règle obtenue dans le terminal ? Si l’assistant a simplement ouvert `tickets.json`, sa réponse peut être juste, mais cet essai ne nous apprend encore rien sur son accès MCP.

Avec Cursor, Codex, Pi ou un autre assistant, gardez votre outil. S’il prend en charge le transport stdio, reprenez la **commande** et les **arguments** dans son propre format de configuration MCP : le JSON de VS Code ne se copie pas tel quel partout. Sans cet accès, poursuivez les manipulations avec `client.py` ; la procédure du skill pourra être essayée séparément.

[^p6-vscode-mcp]: [Ajouter et gérer les serveurs MCP dans VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
