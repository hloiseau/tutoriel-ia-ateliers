# Les MCP et les skills en pratique

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Nous allons consulter des tickets avec un vrai serveur MCP, lui refuser les écritures, puis préparer une recette avec un skill que nous pourrons modifier nous-mêmes.

Jusqu’ici, nous avons donné des fichiers à l’agent et observé ses appels d’outils. Mais les informations nécessaires ne sont pas toujours dans le dépôt : le ticket est dans Jira, une décision dans la documentation, un résultat dans les logs… On peut tout copier dans la conversation. Une fois. À la dixième, on aimerait bien faire autrement. 😅

Nous allons donner à l’agent un moyen de consulter ces informations, puis lui expliquer comment s’en servir pour une tâche précise. Ce sont deux choses différentes : **accéder à un ticket** et **préparer les tests de ce ticket**.

Pour suivre, gardez Python 3.12 et l’assistant utilisé dans la partie 4. Le serveur et le client de l’atelier fonctionnent sur CPU, sans modèle et sans compte sur un service de tickets. Les essais dans l’assistant utilisent votre modèle habituel. Nous n’allons pas transformer le petit modèle local de la partie 3 en agent de développement.

Les tickets et les documents sont fictifs. Nous retrouvons notre suivi de prix avec un premier ticket, PRIX-1, dont la règle est décidée, et un second, PRIX-2, auquel il manque encore des informations. Les [fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/main/ateliers/06-mcp-skills) sont disponibles dans le dépôt.

## 1. Consulter notre premier ticket

**TL;DR** — Le client lance le serveur, lui demande PRIX-1 et enregistre sa réponse. Aucun modèle n’intervient encore.

Avant de parler du protocole, faisons-lui transporter quelque chose. Un ticket fera très bien l’affaire. 🙂

### Préparer le dossier

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

### Demander PRIX-1

Lancez :

```bash
python client.py ticket PRIX-1 --journal sorties/prix-1.json
```

Le client démarre `serveur.py`, appelle l’outil de lecture, puis arrête le serveur. Vous n’avez pas de deuxième terminal à ouvrir.

La réponse est assez longue : le SDK fournit notamment une représentation textuelle et un contenu structuré. Ouvrez `sorties/prix-1.json` et cherchez `structuredContent`. Vous y retrouverez cet extrait :

```json
{
  "id": "PRIX-1",
  "titre": "Ne plus notifier une simple remise en stock",
  "statut": "a preparer",
  "regle": "Notifier seulement si le produit est disponible dans le nouvel état et si son prix baisse strictement.",
  "questions_ouvertes": [],
  "documents": ["regle-notification"],
  "revision": "exemple-1"
}
```
Code: Contenu du ticket fictif retourné par le serveur

Comparez-le avec `donnees/tickets.json`. C’est bien notre fichier qui a répondu. Le client n’a ni deviné la règle ni demandé à un modèle de la reformuler.

Le journal conserve aussi `protocole`, la version employée lors de l’échange. Notre exécution avec le SDK fourni utilise `2026-07-28`. Ce journal contient les résultats obtenus par le client, pas une capture de chaque message qui a circulé.

Pour refaire la commande, choisissez un autre nom de journal. Le client refuse d’écraser le premier : nous pourrons comparer nos essais sans perdre la réponse précédente.

### Si le ticket n’arrive pas

Essayez maintenant un identifiant absent :

```bash
python client.py ticket PRIX-999 --journal sorties/inconnu.json
```

Cette fois, cherchez `isError` dans la réponse : sa valeur est `true`. Le serveur a reçu une demande compréhensible, mais ne possède pas ce ticket. Son message ne signifie pas que PRIX-999 n’existe nulle part ; seulement qu’il est absent de notre jeu de données.

C’est différent d’un client qui n’arrive même pas à démarrer :

| Ce que vous voyez | Où regarder d’abord |
| --- | --- |
| `No module named 'mcp'` | L’interpréteur utilisé et l’installation avec ce même Python |
| `can't open file ...client.py` | Le dossier dans lequel le terminal est ouvert |
| Le journal existe déjà | Un nouveau nom après `--journal` |
| `isError: true` dans un journal enregistré | Le message retourné par l’outil |
| Le serveur s’arrête avant de répondre | La sortie d’erreur du terminal et les dépendances |

Le client imprime les erreurs attendues de l’outil dans son journal et termine normalement. Un code de sortie nul signifie ici qu’il a pu enregistrer la réponse, pas que le ticket demandé a été trouvé.

Une erreur correctement remontée est déjà un résultat utile : l’agent pourra dire qu’il n’a pas obtenu le ticket. Une réponse inventée serait beaucoup plus ennuyeuse à repérer.

Nous avons obtenu une donnée par MCP. Regardons maintenant ce que le client a dû connaître pour la demander, puis remplaçons-le par notre assistant.

## 2. Brancher le serveur à notre assistant

**TL;DR** — MCP décrit les échanges avec le serveur. L’assistant décide comment présenter ses outils au modèle et comment traiter leurs résultats.

Notre petit client connaît déjà le nom `lire_ticket`. Comment un autre programme peut-il découvrir qu’il existe ?

### Demander ce que le serveur sait faire

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

Voilà ce qu’apporte un format commun : notre assistant peut demander au serveur son inventaire, au lieu de contenir à l’avance une intégration Python spécifique à `lire_ticket`. Cela ne garantit ni que tous les assistants utilisent toutes les possibilités de MCP, ni qu’ils montrent les mêmes boutons.

Et MCP n’a pas choisi de lire PRIX-1 : dans notre client, ce choix vient de la ligne de commande. Dans un agent, il peut venir d’une demande d’outil produite par le modèle, traitée par le programme qui l’entoure.

[^p6-tools]: Spécification MCP, [outils et appels d’outils](https://modelcontextprotocol.io/specification/2026-07-28/server/tools).

### Garder l’assistant que nous avons déjà

Si vous suivez le parcours VS Code de la partie 4, ouvrez le dossier de cet atelier dans l’éditeur. Dans le terminal qui utilise notre environnement Python, lancez :

```bash
python configuration.py
```

Le script affiche une configuration avec le chemin de **votre** Python et celui de `serveur.py`. Copiez ce JSON dans `.vscode/mcp.json`, à la racine du dossier ouvert. Si vous avez déjà ce fichier, ajoutez seulement `atelier-tickets` à son objet `servers` ; conservez vos autres entrées.

Dans la palette de commandes, ouvrez **MCP: List Servers**, sélectionnez `atelier-tickets`, puis démarrez-le. **Show Output** permet de retrouver ses erreurs. Dans le chat, gardez l’agent **Local** de notre parcours et vérifiez que les outils de l’atelier sont disponibles dans la sélection des outils.[^p6-vscode-mcp]

Demandez :

> Consulte PRIX-1 avec le MCP atelier-tickets et donne-moi sa règle.

Dépliez l’appel d’outil. Retrouve-t-on `lire_ticket`, l’identifiant `PRIX-1` et la règle que nous avons obtenue dans le terminal ? Si l’assistant a seulement ouvert `tickets.json`, il a pu trouver la bonne réponse, mais vous n’avez pas encore testé son accès MCP.

Avec Cursor, Codex, Pi ou un autre assistant, gardez votre outil. Il faut reprendre la **commande** et les **arguments** dans sa configuration MCP, si votre installation prend en charge le transport stdio. Le fichier JSON de VS Code n’est pas un format de configuration universel. Si cet accès manque, les manipulations avec `client.py` restent disponibles ; nous pourrons essayer séparément la procédure du skill.

[^p6-vscode-mcp]: [Ajouter et gérer les serveurs MCP dans VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers).

### Où passent les informations ?

Notre serveur utilise **stdio** : le programme client lance un processus et échange avec lui par son entrée et sa sortie standard. MCP dispose aussi d’un transport HTTP pour des serveurs accessibles par le réseau.[^p6-transport]

![Le client MCP appartient à l’assistant ; le serveur lit les fichiers locaux, tandis que le modèle peut être distant.](images/trajet.png)
Figure: Un serveur local peut alimenter un modèle distant

Dans le vocabulaire MCP, l’application qui accueille l’interaction est l’**hôte**. Elle contient un client MCP qui parle au serveur. Le modèle n’a pas besoin de comprendre comment Python ouvre `tickets.json` ; il reçoit les outils que l’hôte lui présente et les résultats que celui-ci réintroduit dans la conversation.

Le mot *local* mérite donc qu’on précise ce qu’il désigne. Le serveur tourne ici sur notre machine. Si l’assistant utilise un modèle hébergé, les informations issues du ticket peuvent ensuite lui être envoyées. Héberger le MCP chez soi ne suffit pas à garder toute la conversation chez soi.

Pour notre atelier, les données sont fictives. Dans un projet professionnel, ce trajet aide à décider quels champs exposer et avec quel compte accéder aux services. Une liste d’identifiants et de titres suffit parfois pour chercher ; envoyer tout le ticket, ses pièces jointes et son historique à chaque recherche ajouterait des informations dont on n’a pas encore besoin.

[^p6-transport]: Spécification MCP, [transports stdio et Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports).

Le même serveur peut être appelé par notre script ou par un assistant compatible. Nous pouvons maintenant ouvrir son code et décider exactement ce qu’il donne accès à lire.

## 3. Construire les outils dont on a besoin

**TL;DR** — Un outil annonce ses arguments, valide la demande et retourne un résultat. Nous allons suivre ces trois étapes dans le code fourni.

Ouvrez `serveur.py`. Il est assez court pour qu’on en fasse le tour sans déléguer sa lecture à l’IA. 🙂

### D’une fonction Python à un outil MCP

En haut du fichier, cette ligne crée notre serveur :

```python
mcp = MCPServer("atelier-tickets", version="1.0.0")
```

Le décorateur `@mcp.tool(...)` qui précède `lire_ticket` l’enregistre comme outil. Sa description vient de la chaîne placée au début de la fonction. L’annotation de l’argument indique ce que le client peut lui transmettre.[^p6-serveur]

Dans notre fonction, le travail proprement dit reste très ordinaire : charger le catalogue, chercher l’identifiant, retourner le ticket. Si l’identifiant manque, `ToolError` produit une erreur d’outil explicite. Le SDK se charge de l’exposition par MCP.

Regardez aussi le type de retour : `dict[str, Any]`. Nous retournons un objet dont les clés sont des chaînes et dont les valeurs peuvent différer. Avec cette annotation, notre SDK fournit le contenu structuré que nous avons consulté. Les champs précis de nos tickets restent définis par notre petit jeu de données ; nous n’avons pas encore construit un modèle de validation complet pour chacun.

Pour comprendre ce qui appartient à notre application, changez le titre de PRIX-1 dans une copie de `tickets.json`, puis relancez une lecture avec un nouveau journal. Le titre change, le protocole reste le même. Rétablissez ensuite le fichier : nous gardons les données communes pour les exercices suivants.

[^p6-serveur]: SDK Python MCP, [définir un serveur et ses outils](https://py.sdk.modelcontextprotocol.io/servers/).

### Chercher, puis ouvrir le bon document

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

### Et les ressources ?

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

## 4. Refuser ce que le serveur ne doit pas faire

**TL;DR** — Nous allons rejeter un mauvais paramètre et une demande d’écriture, puis lire un document qui contient une fausse consigne. Ces trois problèmes ne se règlent pas au même endroit.

Écrire « lecture seule » dans une description ne change pas les droits du programme. Voyons ce qui limite réellement notre serveur.

### Un identifiant n’est pas un chemin

La signature de `lire_document` contient cette annotation :

```python
identifiant: Annotated[
    StrictStr,
    Field(pattern=r"^[a-z0-9-]+$", max_length=60),
]
```
Code: Contrainte sur l’identifiant de document

`StrictStr` demande une chaîne. Le motif autorise les lettres minuscules non accentuées, les chiffres et les tirets. La longueur est également limitée. Ces contraintes servent à construire le schéma annoncé au client et à valider la demande reçue.

Essayez :

```bash
python client.py document ../tickets --journal sorties/mauvais-identifiant.json
```

Le paramètre est refusé. Mais il faut aussi regarder ce qui aurait été fait d’un identifiant valide : notre code cherche une **clé dans un catalogue chargé depuis un fichier fixé par le programme**. Il ne construit pas un chemin à partir de l’argument du client.

La différence compte. Vérifier seulement que la valeur est une chaîne n’empêcherait pas un outil conçu pour lire des chemins de recevoir celui d’un fichier confidentiel. Ici, l’appelant ne choisit pas le fichier ouvert.

Cette validation ne dit pas qui a le droit de consulter quel ticket. Notre jeu fictif n’a qu’un seul niveau d’accès. Pour un service utilisé par plusieurs personnes, les droits sur les tickets doivent être vérifiés séparément ; un identifiant bien formé n’accorde aucune permission.

### Demander une modification impossible par cet outil

Lancez la tentative prévue dans le client :

```bash
python client.py refus --journal sorties/refus.json
```

Elle appelle `modifier_ticket` en demandant de terminer PRIX-1. Le serveur répond que l’outil est inconnu : nous ne l’avons pas exposé. Relisez PRIX-1 avec un nouveau journal ; son statut reste `a preparer`.

Vous avez peut-être vu `readOnlyHint` dans l’inventaire. Cette annotation annonce l’intention de l’outil aux clients ; elle ne retire aucun droit au processus et ne transforme pas une fonction d’écriture en lecture seule.[^p6-annotations]

![Les paramètres sont validés, seuls les outils déclarés sont accessibles, et les droits du processus restent une limite distincte.](images/acces.png)
Figure: Trois contrôles différents autour d’une lecture

Notre serveur protège un périmètre précis : il ne propose pas d’opération MCP d’écriture et ses fonctions ne modifient pas les données. Il ne protège pas ces fichiers contre un autre programme lancé avec les droits de notre compte. Si l’assistant possède aussi un terminal, cette autre voie d’accès reste à considérer.

Sur un vrai service, on utiliserait en plus un compte disposant uniquement des droits nécessaires. Si le compte peut supprimer un index et qu’un outil générique accepte n’importe quelle requête, retirer seulement l’outil nommé `delete_index` ne suffit pas.

Pour vérifier notre implémentation :

```bash
python -m unittest discover -s . -p 'test_serveur.py' -v
```

Les dix tests vérifient notamment les arguments et les erreurs. Celui de la tentative d’écriture compare les empreintes des données avant et après l’appel. Il contrôle ce scénario ; il ne démontre pas l’impossibilité de toute écriture sur la machine.

[^p6-annotations]: Spécification MCP, [les annotations des outils sont des indications, pas des garanties](https://modelcontextprotocol.io/specification/2026-07-28/server/tools).

### Quand la documentation donne des ordres

Ouvrez maintenant la note archivée :

```bash
python client.py document note-archivee --journal sorties/note.json
```

Son texte demande d’ignorer le ticket, de terminer PRIX-1, puis d’annoncer que tous les tests passent. C’est le document piégé fictif de l’atelier.

Le serveur le retourne sans l’exécuter. Jusque-là, rien de mystérieux : pour Python, il s’agit d’une chaîne. Le problème apparaît si un agent traite ce contenu comme une nouvelle instruction à suivre. Il a demandé de la documentation ; il ne devrait pas en déduire une autorisation de modifier un ticket.

Dans une conversation d’essai, demandez à votre assistant de lire cette note et d’en comparer le contenu à PRIX-1. Regardez les outils appelés et la réponse obtenue. Un résultat satisfaisant identifie le caractère archivé et la demande étrangère à la tâche ; il n’annonce pas des tests qu’il n’a pas exécutés. Si l’agent tente une action, conservez la trace : nous avons précisément besoin de voir où la séparation a échoué.

Même si la tentative `modifier_ticket` est bloquée, le modèle peut encore écrire une réponse trompeuse dans la conversation. La barrière technique protège l’action visée, pas la vérité de chaque phrase.

Nous avons déjà abordé les instructions cachées dans la partie 5. Ici, elles arrivent par un autre chemin : **une réponse d’outil reste du contenu à examiner**. Le fait qu’elle ait traversé MCP n’en fait pas une consigne prioritaire.

Le serveur sait fournir des données et rejeter certaines demandes. Il ne sait toujours pas comment nous voulons préparer une recette. C’est le rôle du fichier que nous allons écrire.

## 5. Écrire notre premier skill

**TL;DR** — Nous allons mettre une procédure de préparation de recette dans un dossier lisible et modifiable. Le skill dira quoi faire des sources ; il ne créera pas les accès MCP.

Demander « prépare-moi les tests » laisse encore beaucoup de place à l’interprétation. Quels tests ? Avec quelles données ? Et que faire si le ticket ne décide pas du résultat attendu ?

### Donner un nom à une tâche précise

Ouvrez `skills/preparer-recette/SKILL.md`. Le début ressemble à ceci :

```yaml
---
name: preparer-recette
description: Préparer des scénarios de recette à partir d’un ticket et de sa documentation, en séparant les comportements décidés des questions encore ouvertes. À utiliser pour préparer les tests manuels, sans exécuter la recette ni implémenter le ticket.
license: CC-BY-SA-4.0
---
```
Code: Métadonnées du skill fourni

Le nom désigne la tâche. La description aide l’assistant à reconnaître quand ce dossier peut servir. « Un super expert du développement » ne lui dirait pas grand-chose sur le moment où charger une procédure de recette.

Le format Agent Skills prévoit un dossier contenant `SKILL.md`, avec des métadonnées YAML puis les instructions en Markdown. On peut y joindre des scripts, des références ou des modèles de documents.[^p6-format-skill] Notre dossier ne contient que la procédure et une référence de présentation.

| Fichier | Ce qu’il apporte ici |
| --- | --- |
| `SKILL.md` | Quand préparer la recette et comment traiter les sources |
| `references/format-recette.md` | La forme du résultat à présenter |

Les mots *skill*, *commande* et *plugin* ne désignent donc pas exactement la même chose. Un produit peut proposer notre skill comme commande dans son interface. Un plugin peut distribuer plusieurs skills avec des outils. Notre procédure reste un fichier que nous pouvons lire et modifier sans adopter l’organisation complète d’un plugin.

[^p6-format-skill]: [Spécification du format Agent Skills](https://agentskills.io/specification).

### Décrire le travail à faire

Le corps du skill commence par demander la lecture du ticket. Il fait ensuite charger les documents cités, préparer les cas décidés et faire apparaître les questions ouvertes. Voici la consigne qui nous intéresse particulièrement :

> Si une décision manque ou que les sources se contredisent, expose la question et laisse le résultat concerné indéterminé. Ne choisis pas discrètement à la place de l’équipe.

Nous écrivons à l’impératif parce que nous décrivons la procédure attendue. « Tu pourrais peut-être vérifier les questions » ressemble à une possibilité parmi d’autres. Ici, leur examen fait partie du travail.

Cela ne transforme pas le texte en programme déterministe. Nous devrons vérifier que le modèle suit cette procédure, comme nous avons vérifié les tests proposés dans la partie 4.

Le skill ne contient pas la règle « notifier si le prix baisse et si le produit est disponible ». Cette information appartient au ticket et à sa documentation. En la recopiant dans la procédure, nous créerions une deuxième version à mettre à jour lors du prochain changement métier.

Enfin, le skill demande de lire `references/format-recette.md` au moment de présenter le résultat. Ce fichier précise les colonnes : cas, préconditions, action, résultat attendu et source. Il ne sert pas à découvrir si PRIX-1 existe ; le charger plus tard permet de garder les informations proches de l’étape où elles sont utiles.

Le chargement progressif dépend de l’implémentation du client : séparer les fichiers rend ce fonctionnement possible, mais ne prouve pas à lui seul que votre assistant évite de tout charger.[^p6-chargement]

[^p6-chargement]: Agent Skills, [prise en charge et chargement par les clients](https://agentskills.io/client-implementation/adding-skills-support).

### Préparer la recette de PRIX-1

Dans VS Code, copiez le dossier complet `skills/preparer-recette` dans `.github/skills/`, à la racine du dossier d’atelier ouvert. Vous devez obtenir `.github/skills/preparer-recette/SKILL.md`, avec son sous-dossier `references` à côté. Cet emplacement est pris en charge pour les skills de projet.[^p6-vscode-skill]

Si `/preparer-recette` apparaît dans le chat, sélectionnez-le puis demandez :

> Prépare la recette de PRIX-1 avec le MCP atelier-tickets. Présente-la dans la conversation.

Avec un autre assistant, utilisez son emplacement de skills ou demandez explicitement la lecture du fichier fourni. Cette dernière possibilité permet d’essayer les instructions, même sans découverte automatique du dossier. Elle ne valide pas le mécanisme d’activation du produit.

Dans la réponse, cherchez des cas concrets. Le retour en stock à prix égal doit être distingué du retour en stock accompagné d’une baisse. L’indisponibilité nouvelle doit aussi être couverte. Un tableau très long qui répète seulement « le système fonctionne correctement » ne nous aide pas beaucoup. 😅

Comparez la proposition avec `attendus-recette.md`. Ce document contient des cas rédigés pour l’exercice. Les données y sont en centimes, comme dans nos conventions. Il explique aussi ce qui manque pour exécuter une vraie recette : notre jeu ne décrit ni interface de staging ni compte ni moyen d’observer un envoi.

La préparation peut donc être utile sans prétendre que les tests ont eu lieu. Pour annoncer un résultat, il faudrait encore disposer de l’application et jouer les scénarios.

[^p6-vscode-skill]: [Utiliser les skills dans VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills).

Nous avons une première procédure et des critères pour relire ce qu’elle produit. Essayons-la maintenant sur un ticket qui ne permet pas de remplir toutes les cases.

## 6. Faire évoluer le skill à partir des problèmes rencontrés

**TL;DR** — PRIX-2 laisse deux décisions ouvertes. Nous allons nous en servir pour repérer une mauvaise réponse, corriger la procédure si nécessaire et vérifier que PRIX-1 fonctionne encore.

C’est souvent là que les choses deviennent intéressantes : le premier exemple marchait, le suivant révèle ce que nous n’avions pas précisé.

### Un ticket qui ne dit pas tout

Consultez le second ticket :

```bash
python client.py ticket PRIX-2 --journal sorties/prix-2.json
```

Il demande de limiter les notifications trop rapprochées. Deux questions restent ouvertes : quelle durée définit un intervalle court, et une baisse plus importante peut-elle contourner cette limite ?

Ouvrez une nouvelle conversation, chargez le même skill et demandez la préparation de PRIX-2. Une nouvelle conversation évite que vos corrections précédentes soient les seules à expliquer un bon résultat : nous voulons voir ce que les fichiers permettent de refaire.

Que doit contenir la réponse ? Des questions, justement. On peut déjà identifier des familles de cas : une notification juste avant la limite, une autre juste après, une nouvelle baisse pendant l’intervalle. Mais choisir « dix minutes » ou décider qu’une forte baisse passe toujours inventerait une règle.

La documentation de PRIX-1 ne résout pas cette ambiguïté. Elle dit quand une baisse rend une notification pertinente ; PRIX-2 ajoute une condition de temporisation encore à définir. Des sources vraies peuvent donc rester insuffisantes pour répondre.

Une recette avec deux résultats « à arbitrer » peut être plus utile qu’un tableau entièrement rempli. Elle montre précisément les décisions dont nous avons besoin pour poursuivre. Ce n’est pas au modèle de décider discrètement du comportement du produit pour que son tableau soit plus joli.

### Changer la règle qui a réellement manqué

Si votre assistant choisit malgré tout une durée, commencez par ouvrir les fichiers qu’il a lus. A-t-il chargé le bon skill ? Le ticket complet ? Est-ce une ancienne copie de la procédure qui est encore utilisée ? Ajouter une nouvelle consigne dans un fichier jamais lu ne réglera pas le problème.

Si le skill a bien été chargé, vous pouvez demander une correction précise :

> Sur PRIX-2, tu as choisi une durée alors que le ticket la laisse ouverte. Modifie le skill pour laisser ce résultat à arbitrer et présenter la question. Garde la préparation possible pour les cas déjà décidés. Montre-moi le diff avant de réessayer.

Relisez le diff. Une bonne modification décrit le comportement manquant. Une mauvaise modification peut simplement ajouter PRIX-2 comme cas particulier, puis inventer une durée sur le prochain ticket.

Notre version fournie contient déjà la consigne sur les décisions manquantes. Si votre assistant la suit, ne rajoutez pas une deuxième formulation pour le principe. Gardez plutôt ce cas dans vos essais futurs.

Après une modification, rejouez PRIX-2 **et** PRIX-1 dans des conversations neuves. Une règle trop large, comme « s’arrêter dès qu’il manque une information », pourrait empêcher toute préparation de PRIX-1 sous prétexte que notre jeu ne fournit pas d’interface de staging. Nous voulons préparer ce qui est déterminé et nommer ce qui manque pour l’exécution.

C’est du *trial and error*, avec des traces qui permettent de comprendre ce qui a changé. L’IA peut nous aider à modifier les fichiers ; nous gardons la décision sur le comportement voulu.

### Garder des essais que l’on peut comparer

Conservez une petite fiche par essai :

| Élément | Exemple à noter |
| --- | --- |
| Version des fichiers | Commit du dépôt ou copie du skill essayé |
| Outil et modèle | Ceux réellement sélectionnés dans l’interface |
| Demande | Texte envoyé pour PRIX-1 ou PRIX-2 |
| Sources | Appels observés et documents effectivement lus |
| Résultat | Réponse conservée, avec les erreurs éventuelles |
| Décision | Modification à garder, à revoir ou à abandonner |

Ces éléments permettent de comparer autre chose qu’une impression. Un meilleur résultat après avoir changé à la fois le modèle, le ticket et le skill ne nous apprend pas quelle modification a aidé.

Il n’est pas nécessaire d’attendre les retours d’autres lecteurs pour avancer. Nos deux tickets et le document piégé fournissent déjà de quoi mettre la procédure à l’épreuve. Si un nouvel incident apparaît dans votre travail, ajoutez un exemple réduit qui le reproduit, avec des données partageables.

Les tests Python de l’atelier ne vérifient pas cette partie : ils contrôlent le serveur. Pour le skill, le résultat dépend aussi du modèle, du contexte et du produit qui charge les fichiers. Un passage réussi n’est pas un taux de fiabilité.

Nous pouvons également comparer l’effort avec une préparation manuelle. Si la réponse demande plus de temps à réparer qu’à écrire, le skill n’a pas encore trouvé sa place pour cette tâche. Et si vous n’aimez pas déléguer le code, rien n’oblige à aller plus loin que cette aide à la recette.

La procédure commence à correspondre à une manière de travailler. Reste à la maintenir sans finir avec un fichier géant qui mélange les règles du projet, les données métier et toutes les erreurs de l’année.

## 7. Articuler skills, conventions et base de connaissances

**TL;DR** — La procédure dit comment travailler ; les conventions décrivent les règles communes du projet ; la base de connaissances fournit les faits dont on a besoin. Nous allons ranger un exemple dans chacun de ces endroits.

Au début, tout tient dans un fichier. Puis on ajoute une règle, un extrait de documentation, trois exceptions… et personne ne sait plus où corriger le montant d’un seuil.

### Mettre chaque information à sa place

Prenons trois phrases de notre atelier :

| Information | Où la conserver ? | Pourquoi ? |
| --- | --- | --- |
| « Les prix sont des entiers en centimes. » | Conventions du projet | Cela sert à plusieurs tâches sur le même code |
| « Faire apparaître les résultats encore à arbitrer. » | Skill de préparation de recette | Cela décrit une étape du travail demandé |
| « Une simple remise en stock ne déclenche pas de notification. » | Ticket et documentation métier | Cela décrit le comportement du produit |

La **base de connaissances** désigne ici l’ensemble des documents qui apportent des faits sur le projet : règles métier, décisions, contrats d’API, explications d’un service. Elle peut être constituée de Markdown dans un dépôt, de pages sur un wiki ou de données accessibles par un outil. Le terme n’impose ni base vectorielle ni logiciel particulier.

![Trois exemples rangés dans les conventions, le skill et la documentation, avec leur portée respective.](images/rangement.png)
Figure: Des fichiers différents parce que les informations changent pour des raisons différentes

Si la règle de notification évolue, nous corrigeons sa source métier. Si la présentation des recettes change, nous corrigeons la référence du skill. Si le projet change d’unité monétaire interne, les conventions et le code doivent être revus ensemble.

La séparation n’a d’intérêt que si les liens permettent de retrouver les informations. Dans notre atelier, le ticket cite un document par son identifiant et le skill renvoie explicitement vers son format de recette. Déplacer un paragraphe dans un sous-dossier sans indiquer quand le lire ne suffit pas.

### Faire une petite passe de refacto

Essayez ce rangement sur un brouillon, sans modifier tout de suite votre skill actif. Réunissez ces trois lignes :

```markdown
- Les prix sont exprimés en centimes.
- Si un résultat dépend d’une décision absente, présenter la question.
- Une remise en stock à prix égal ne déclenche pas de notification.
```
Code: Trois informations de nature différente réunies dans un même brouillon

Demandez à l’agent de proposer leur répartition entre les fichiers de l’atelier, avec les références nécessaires pour les retrouver. Comparez avec le tableau précédent. Vous devriez reconnaître les trois rôles, même si les noms de dossiers proposés diffèrent.

Si vous appliquez une telle refacto à vos propres fichiers, relisez aussi ce qui a été supprimé. Une information déplacée doit toujours exister à son nouvel emplacement ; une règle dupliquée doit avoir une source clairement choisie. Sinon, la prochaine correction laissera deux versions contradictoires.

Puis rejouez la préparation des deux tickets. La réorganisation doit conserver les décisions attendues. Nous ne cherchons pas le plus grand nombre de petits fichiers : une référence de trois lignes peut très bien rester dans le skill si elle sert à chaque utilisation et ne change jamais indépendamment.

Dans mon usage, ces passes viennent après les problèmes rencontrés : une information répétée, une règle perdue, un fichier devenu trop long. Je préfère pouvoir expliquer à quoi sert la séparation que reproduire une arborescence parce qu’elle semble sérieuse.

### Choisir jusqu’où aller

Nous avons construit un serveur pour consulter des sources et un skill pour préparer une recette. Vous pouvez garder l’un sans l’autre. Une commande qui affiche le ticket peut suffire dans un petit projet ; un skill peut travailler à partir de documents déjà présents dans le dépôt.

Avant d’ajouter un MCP, regardez ce qui manque dans votre tâche actuelle. Faut-il retrouver une décision ? Consulter une valeur réelle ? Éviter de recopier un ticket à chaque session ? Le nombre d’outils disponibles n’est pas, en soi, une amélioration. Leurs descriptions et leurs réponses occupent du contexte selon la façon dont votre assistant les charge.

Avant de reprendre un skill, regardez ses choix : où commence-t-il, où s’arrête-t-il, qu’est-ce qu’il suppose déjà décidé ? Une procédure qui lance automatiquement l’implémentation, la revue et la publication ne correspond pas à notre simple demande de préparation de recette.

Vous pouvez reprendre nos fichiers pour expérimenter, puis les changer. Le résultat à conserver est celui qui vous aide dans votre travail, avec vos outils et vos contraintes. Si une étape ne vous sert pas, elle n’a pas à rester parce qu’un dépôt populaire la recommande.

Dans la partie suivante, nous allons agrandir notre corpus documentaire. Notre recherche littérale atteint vite ses limites quand on ne connaît pas les mots employés dans les sources. Ce sera l’occasion de construire une recherche plus utile, puis de distinguer ce que l’on obtient en donnant de meilleurs documents au modèle de ce qui demande réellement de l’adapter ou de l’entraîner.

Nous pouvons désormais consulter des faits, les utiliser dans une procédure et modifier cette procédure à partir d’un problème observé. Les fichiers restent assez accessibles pour qu’on puisse les contester, les simplifier et les faire évoluer.

## Conclusion

Notre ticket a suivi un trajet complet : un client l’a demandé au serveur MCP, nous avons examiné sa documentation, puis un skill a fourni les instructions pour préparer sa recette.

Les rôles sont maintenant visibles dans les fichiers. Le serveur fournit des accès précis. Le skill décrit une tâche. Les documents portent les faits du projet. Et nous relisons encore les résultats, notamment là où le ticket laisse une décision ouverte.

Si la préparation des tests vous fait perdre du temps, c’est déjà un endroit où essayer ces outils. Vous n’avez pas besoin de déléguer tout le développement ni d’organiser votre équipe autour d’un framework pour en tirer quelque chose.

Gardez ce qui vous aide, changez ce qui vous gêne et vérifiez ce que ces changements produisent. Nous avons enfin des outils dont on peut modifier une bonne partie du fonctionnement ; autant en profiter. 🙂
