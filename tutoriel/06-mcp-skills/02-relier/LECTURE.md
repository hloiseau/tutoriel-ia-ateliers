# 2. Brancher le serveur à notre assistant

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Consulter notre premier ticket](../01-consulter/LECTURE.md) · [Suivant : Développer notre serveur MCP, pas à pas](../03-construire/LECTURE.md)

**TL;DR** — MCP décrit les échanges avec le serveur. L’assistant décide comment présenter ses outils au modèle et comment traiter leurs résultats.

Notre petit client connaît déjà le nom `lire_ticket`. Comment un autre programme peut-il découvrir qu’il existe ?

## Demander ce que le serveur sait faire

Exécutez :

```bash
python client.py inventaire --journal sorties/inventaire.json
```

Le serveur annonce trois outils : `lire_ticket`, `chercher_documentation` et `lire_document`. Pour chacun, le journal contient un nom, une description et un `inputSchema`, c’est-à-dire la forme des arguments acceptés. Un identifiant de ticket et un terme de recherche ne sont pas interchangeables.

Dans `client.py`, les deux opérations principales tiennent à ceci :

```python
resultat = await client.list_tools()
resultat = await client.call_tool("lire_ticket", {"identifiant": "PRIX-1"})
```
Code: Deux appels du SDK, à l’intérieur d’un client ouvert

MCP, pour *Model Context Protocol*, définit notamment la découverte et l’appel des outils ; le SDK construit les messages nécessaires.[^p6-tools] Nous n’avons pas à écrire nous-mêmes l’enveloppe du protocole.

Voilà ce qu’apporte un format commun : notre assistant peut demander au serveur son inventaire, au lieu d’embarquer une intégration Python écrite spécialement pour `lire_ticket`. Chaque assistant choisit ensuite les possibilités qu’il prend en charge et la manière de les présenter dans son interface.

Dans notre client, la ligne de commande choisit de lire PRIX-1. Avec un agent, le modèle peut demander cet outil ; le programme qui l’entoure décide alors comment traiter cette demande et son résultat. MCP décrit l’échange entre les programmes, il ne décide pas quel ticket consulter.

[^p6-tools]: Spécification MCP, [outils et appels d’outils](https://modelcontextprotocol.io/specification/2026-07-28/server/tools).

## Garder l’assistant que nous avons déjà

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

## Où passent les informations ?

Notre serveur utilise **stdio** : le programme client lance un processus et échange avec lui par son entrée et sa sortie standard. MCP dispose aussi d’un transport HTTP pour des serveurs accessibles par le réseau.[^p6-transport]

![Le client MCP appartient à l’assistant ; le serveur lit les fichiers locaux, tandis que le modèle peut être distant.](../images/trajet.png)
Figure: Un serveur local peut alimenter un modèle distant

Dans le vocabulaire MCP, l’application qui accueille l’interaction est l’**hôte**. Elle contient un client MCP qui parle au serveur. Le modèle n’a pas besoin de comprendre comment Python ouvre `tickets.json` ; il reçoit les outils que l’hôte lui présente et les résultats que celui-ci réintroduit dans la conversation.

Le mot *local* désigne ici le serveur, qui tourne sur notre machine. Avec un modèle hébergé, les informations issues du ticket peuvent ensuite quitter cette machine pour rejoindre la conversation. Il faut suivre tout le trajet avant de conclure où vivent les données.

Pour notre atelier, les données sont fictives. Dans un projet professionnel, ce trajet aide à décider quels champs exposer et avec quel compte accéder aux services. Une liste d’identifiants et de titres suffit parfois pour chercher ; envoyer tout le ticket, ses pièces jointes et son historique à chaque recherche ajouterait des informations dont on n’a pas encore besoin.

[^p6-transport]: Spécification MCP, [transports stdio et Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports).

Notre script sait appeler le serveur, et un assistant compatible peut faire le même échange. Nous connaissons maintenant le résultat à obtenir ; construisons notre propre serveur depuis un fichier vide.

---

[Précédent : Consulter notre premier ticket](../01-consulter/LECTURE.md) · [Suivant : Développer notre serveur MCP, pas à pas](../03-construire/LECTURE.md)
