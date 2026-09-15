# Corrigés des étapes de construction

Ces fichiers accompagnent le [chapitre de construction](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/06-mcp-skills/03-construire/LECTURE.md).

Le lecteur crée `mon_serveur.py` **à la racine de l’atelier**, à côté de `client.py` et de `donnees`. Pour reprendre une étape, copier le contenu du fichier correspondant dans `mon_serveur.py` à cet emplacement. Les états intermédiaires ne sont pas destinés à être lancés depuis ce sous-dossier.

| État | Contenu acquis |
| --- | --- |
| `00-demarrage.py` | Serveur sans outil |
| `01-premier-outil.py` | Lecture d’un ticket écrit dans le code |
| `02-catalogue.py` | Lecture des tickets dans le fichier JSON |
| `03-documents.py` | Recherche et lecture des documents |
| `04-validation.py` | Contraintes d’entrée et annotations de lecture |
| `../serveur.py` | Corrigé complet, avec la ressource des conventions |

`test_mon_serveur.py` est le corrigé des trois tests à écrire à côté de `mon_serveur.py`. La suite `../test_serveur.py` contrôle séparément le serveur de référence.

```bash
python client.py inventaire --serveur mon_serveur.py --journal sorties/mon-inventaire.json
python -m unittest test_mon_serveur -v
python configuration.py --serveur mon_serveur.py
```

Le champ `serveur` du journal aide à détecter une commande qui aurait appelé le corrigé par erreur. L’option `--serveur` accepte un fichier Python à exécuter : choisissez le fichier que vous venez de créer.

La relecture adverse et le rejeu depuis les blocs du chapitre sont conservés dans le dépôt sous `docs/relecture-construction-mcp.md` et `outils/verifier_construction_mcp.py`.
