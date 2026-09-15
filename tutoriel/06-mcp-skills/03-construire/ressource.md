Notre serveur expose aussi une ressource :

```bash
python client.py conventions --journal sorties/conventions.json
```

Elle porte l’URI `atelier://conventions`. C’est un identifiant compris par le serveur, pas l’adresse d’un site à ouvrir dans le navigateur. La fonction correspondante lit `donnees/conventions.md` et retourne son texte : les prix de notre exemple sont exprimés en centimes, dans la même devise, et une recette préparée n’est pas une recette exécutée.

Une ressource permet d’exposer un contenu identifié ; un outil propose une opération avec des arguments. Pour consulter un ticket, nous avons choisi un outil, mais un autre serveur pourrait aussi représenter des tickets comme ressources. L’usage dépend de l’application cliente et de ce qu’elle sait afficher ou charger.[^p6-ressources]

Enfin, regardez la dernière ligne de `serveur.py` :

```python
mcp.run(transport="stdio")
```

C’est elle qui attend les demandes. Si vous lancez ce fichier seul, il peut sembler ne rien faire : personne ne lui a encore envoyé de message. Utilisez `client.py`, qui s’occupe de ce dialogue.

Évitez d’ajouter un `print("ça passe ici")` dans les outils : la sortie standard transporte déjà le protocole. Pour un diagnostic, écrivez sur la sortie d’erreur ou utilisez le système de logs. Sinon, votre message de débogage risque de devenir le message que le client essaie de décoder.

[^p6-ressources]: Spécification MCP, [exposer et consulter des ressources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources).
