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
