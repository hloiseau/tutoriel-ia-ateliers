# 3. Construire les outils dont on a besoin

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Brancher le serveur à notre assistant](../02-relier/LECTURE.md) · [Suivant : Refuser ce que le serveur ne doit pas faire](../04-controler/LECTURE.md)

**TL;DR** — Un outil annonce ses arguments, valide la demande et retourne un résultat. Nous allons suivre ces trois étapes dans le code fourni.

Ouvrez `serveur.py`. Il est assez court pour qu’on en fasse le tour sans déléguer sa lecture à l’IA. 🙂

## D’une fonction Python à un outil MCP

En haut du fichier, cette ligne crée notre serveur :

```python
mcp = MCPServer("atelier-tickets", version="1.0.0")
```

Le décorateur `@mcp.tool(...)` qui précède `lire_ticket` l’enregistre comme outil. Sa description vient de la chaîne placée au début de la fonction. L’annotation de l’argument indique ce que le client peut lui transmettre.[^p6-serveur]

Dans notre fonction, le travail proprement dit reste très ordinaire : charger le catalogue, chercher l’identifiant, retourner le ticket. Si l’identifiant manque, `ToolError` produit une erreur d’outil explicite. Le SDK se charge de l’exposition par MCP.

Regardez aussi le type de retour : `dict[str, Any]`. Nous retournons un objet dont les clés sont des chaînes et dont les valeurs peuvent différer. Avec cette annotation, notre SDK fournit le contenu structuré que nous avons consulté. Les champs précis de nos tickets restent définis par notre petit jeu de données ; nous n’avons pas encore construit un modèle de validation complet pour chacun.

Pour comprendre ce qui appartient à notre application, changez le titre de PRIX-1 dans une copie de `tickets.json`, puis relancez une lecture avec un nouveau journal. Le titre change, le protocole reste le même. Rétablissez ensuite le fichier : nous gardons les données communes pour les exercices suivants.

[^p6-serveur]: SDK Python MCP, [définir un serveur et ses outils](https://py.sdk.modelcontextprotocol.io/servers/).

## Chercher, puis ouvrir le bon document

Lisez la documentation associée au ticket :

```bash
python client.py document regle-notification --journal sorties/regle.json
```

Cette commande convient quand nous connaissons déjà l’identifiant. Si nous cherchons où l’on parle des notifications, utilisons plutôt :

```bash
python client.py chercher notification --journal sorties/recherche.json
```

La recherche renvoie des **identifiants, des titres et un statut**, pas le texte complet des documents. On peut ensuite ouvrir celui qui nous intéresse. La réponse est limitée à cinq résultats ; `tronque` indique si le serveur en a trouvé davantage.

Notre fonction fait une recherche littérale, sans distinction de casse, dans le titre et le texte. « notification » peut trouver « notifications », mais « alerte » ne trouvera pas automatiquement « notification ». Il n’y a ni embeddings ni recherche sémantique cachés dans ces quelques lignes.

Vous remarquerez deux résultats : la règle en vigueur et une note archivée. Le statut fait partie de la réponse parce qu’il change la façon dont on doit lire le document. Une vieille note peut expliquer l’histoire d’une décision ; elle ne remplace pas automatiquement la règle actuelle.

Dans un vrai serveur, la recherche pourrait appeler l’API documentaire de l’équipe. Nous conserverions la même séparation : **trouver les sources**, puis **lire celles qui servent à la tâche**. Nous remplacerions l’accès aux fichiers, pas nécessairement toute l’interface MCP.

## Et les ressources ?

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

Nous avons trois outils et une ressource, chacun avec un rôle précis. Avant de les faire utiliser par le skill, essayons quelques demandes que le serveur doit rejeter.

---

[Précédent : Brancher le serveur à notre assistant](../02-relier/LECTURE.md) · [Suivant : Refuser ce que le serveur ne doit pas faire](../04-controler/LECTURE.md)
