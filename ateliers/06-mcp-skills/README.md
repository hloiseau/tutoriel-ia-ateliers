# Tickets, documentation et recette avec MCP

Cet atelier accompagne la [partie 6](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/06-mcp-skills/README.md). Les tickets et documents sont fictifs. Le client utilise réellement MCP, sans appeler de modèle. Pour essayer ensuite le skill, gardez votre assistant habituel et son accès au modèle ; le serveur n’en fournit pas un.

## Installer

Téléchargez [l’archive](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-mcp-skills.zip) et décompressez-la, ou utilisez ce dossier du dépôt. Ouvrez le terminal dans le dossier contenant `client.py`.

Python **3.12** est la version utilisée pour les vérifications. Si votre commande habituelle est `python3` ou `py -3.12`, utilisez-la pour créer l’environnement.

```bash
python -m venv .venv
```

Activez-le avec la commande de votre terminal :

| Terminal | Commande |
| --- | --- |
| Bash ou Zsh, Linux/macOS | `source .venv/bin/activate` |
| PowerShell, Windows | `.venv\Scripts\Activate.ps1` |
| Invite de commandes Windows | `.venv\Scripts\activate.bat` |

Si PowerShell refuse le script d’activation, remplacez simplement `python` dans les commandes suivantes par `.venv\Scripts\python.exe`. L’activation ne fait que sélectionner cet interpréteur.

```bash
python -m pip install -r requirements.txt
```

`requirements.in` indique la dépendance directe, **mcp 2.2.0**. `requirements.txt` conserve aussi les versions de ses dépendances utilisées pour vérifier l’atelier. L’installation demande Internet ; les appels du client ci-dessous lisent uniquement les fichiers locaux.

## Consulter

```bash
python client.py inventaire --journal sorties/inventaire.json
python client.py ticket PRIX-1 --journal sorties/prix-1.json
python client.py chercher notification --journal sorties/recherche.json
python client.py document regle-notification --journal sorties/document.json
python client.py conventions --journal sorties/conventions.json
python client.py ticket PRIX-2 --journal sorties/prix-2.json
python client.py refus --journal sorties/refus.json
```

Le client lance et arrête lui-même `serveur.py`. Ne lancez pas un serveur dans un deuxième terminal. Chaque journal contient l’opération, la version du protocole et la réponse du SDK ; ce n’est pas une capture brute du transport. Changez le nom du journal pour recommencer : un fichier existant n’est pas écrasé.

Dans `prix-1.json`, `reponse.structuredContent` contient le ticket. Pour `refus`, `reponse.isError` vaut `true` : `modifier_ticket` n’existe pas. Le processus client termine normalement après avoir enregistré cette erreur attendue.

## Utiliser depuis VS Code

Ouvrez ce dossier d’atelier comme dossier de travail de VS Code. Dans son terminal, avec le même Python que ci-dessus :

```bash
python configuration.py
```

Copiez le JSON affiché dans `.vscode/mcp.json`. Si ce fichier existe, ajoutez uniquement l’entrée `atelier-tickets` dans son objet `servers`, en conservant les autres entrées. Les chemins sont propres à votre machine : ne publiez pas cette configuration telle quelle.

Dans la palette de commandes, utilisez **MCP: List Servers**, sélectionnez `atelier-tickets`, puis son démarrage. Consultez **Show Output** si nécessaire. Dans le chat, utilisez l’agent **Local** du parcours VS Code, et vérifiez dans la sélection des outils que les trois outils de l’atelier sont disponibles. Essayez : « Consulte PRIX-1 avec le MCP atelier-tickets et donne-moi sa règle. »

Ces étapes suivent la [documentation VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers). L’interface et l’échange avec un modèle restent à vérifier sur une installation interactive. Avec un autre assistant compatible MCP, reprenez le programme et ses arguments dans son format de configuration ; les clés JSON ne sont pas universelles.

## Installer et essayer le skill

Pour VS Code, copiez le dossier complet `skills/preparer-recette` dans `.github/skills/` à la racine du dossier ouvert. On obtient `.github/skills/preparer-recette/SKILL.md` et son sous-dossier `references`. Aucun fichier n’est installé automatiquement par les scripts de l’atelier.

Le format et l’emplacement suivent la [documentation des skills VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills). Sélectionnez `/preparer-recette` dans le chat si le skill est proposé, puis demandez la préparation de PRIX-1. Pour un assistant qui ne découvre pas ce dossier, demandez explicitement la lecture du `SKILL.md` et de sa référence ; cela permet d’essayer la procédure, sans valider le mécanisme de découverte du produit.

Recommencez dans une nouvelle conversation avec PRIX-2. Comparez le résultat à [attendus-recette.md](attendus-recette.md). Conservez le modèle, la demande, la réponse et les appels visibles : nous ne fournissons pas de fausse conversation « de référence ».

## Vérifier le serveur

```bash
python -m unittest discover -s . -p 'test_serveur.py' -v
```

Dix tests contrôlent le contrat des outils, les entrées invalides, les documents et l’absence de modification des données pendant une tentative d’appel d’écriture. Ils utilisent le transport en mémoire du SDK. Les commandes `client.py` vérifient, elles, le transport **stdio** entre deux processus.

Le serveur expose uniquement des lectures. Son processus dispose néanmoins des droits du compte qui le lance : ce petit programme n’est pas un bac à sable. Un assistant doté d’un terminal ou d’un outil d’écriture peut également modifier le dossier par une autre voie.

[Résultats et limites des vérifications](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/06-mcp-skills/VERIFICATION.md).

Code : GPL-3.0-only. Textes, données fictives et skill : CC BY-SA 4.0. Copyright © 2026 Hugo Loiseau. Voir les licences et crédits à la racine du dépôt ou de l’archive.
