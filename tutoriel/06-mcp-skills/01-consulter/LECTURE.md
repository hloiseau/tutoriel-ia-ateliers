# 1. Consulter notre premier ticket

[Sommaire de la partie](../README.md) · [Sources](.)

[Suivant : Brancher le serveur à notre assistant](../02-relier/LECTURE.md)

**TL;DR** — Le client lance le serveur, lui demande PRIX-1 et enregistre sa réponse. Aucun modèle n’intervient encore.

Avant de parler du protocole, faisons-lui transporter quelque chose. Un ticket fera très bien l’affaire. 🙂

## Préparer le dossier

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

## Demander PRIX-1

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

## Si le ticket n’arrive pas

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

---

[Suivant : Brancher le serveur à notre assistant](../02-relier/LECTURE.md)
