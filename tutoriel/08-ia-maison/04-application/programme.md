Créez `mon_assistant.py` à côté de `assistant_local.py`. Nous réutilisons les fonctions de recherche et d’appel HTTP pour nous concentrer sur l’enchaînement :

```python
import argparse
from assistant_local import preparer, appeler

parser = argparse.ArgumentParser()
parser.add_argument("question")
parser.add_argument("--generer", action="store_true")
args = parser.parse_args()

contexte = preparer(args.question)
if not contexte["passages"]:
    print("Aucun passage retrouvé. Essayez une autre formulation.")
else:
    for passage in contexte["passages"]:
        print(passage["id"], "—", passage["texte"])

    if args.generer:
        reponse = appeler(contexte["messages"])
        print("\nRéponse à relire :")
        print(reponse["texte"])
```
Code: Notre première application documentaire

Essayez d’abord sans génération :

```bash
python mon_assistant.py "Quand les données de staging sont-elles réinitialisées ?"
```

Vous devez voir les sources sélectionnées. Relancez ensuite le [serveur de la partie 3](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/03-modele-local/02-installer/LECTURE.md), depuis le dossier de cet ancien atelier, avec le modèle SmolLM2-360M-Instruct Q8_0, l’alias `atelier-local` et le port `8080`. Gardez ce serveur ouvert dans un autre terminal, revenez dans le dossier de la partie 8, puis ajoutez `--generer` à la commande.

Dans `assistant_local.py`, ouvrez maintenant `appeler`. L’application envoie les messages à `http://127.0.0.1:8080/v1/chat/completions` et extrait le texte de la réponse. Le modèle reste servi par `llama-server` ; notre programme ne charge pas lui-même ses poids.

Notre premier fichier laisse apparaître une erreur Python si le serveur est absent. C’est un bon prochain problème à traiter : la version fournie intercepte ce cas et conserve un journal, y compris lorsque l’appel échoue.

```bash
python assistant_local.py "Quand les données de staging sont-elles réinitialisées ?" --appeler --sortie sorties/reponse-staging.json
```

Le journal contient le contexte, la requête et la réponse brute. Utilisez un autre nom de sortie pour chaque essai : le programme refuse d’écraser un fichier existant.
