# 4. Assembler notre assistant documentaire

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Évaluer les sources avant les réponses](../03-evaluer/LECTURE.md) · [Suivant : Préparer ce que notre modèle va apprendre](../05-donnees/LECTURE.md)

**TL;DR** — Nous allons relier la recherche au serveur local, puis comparer les réponses avec les passages transmis. Le modèle peut se tromper même lorsque la bonne source est sous ses yeux.

Nous avons les documents et leur classement. Il manque maintenant le petit programme qui fait circuler tout cela.

## Regarder ce que le modèle va recevoir

Commençons sans lancer le serveur :

```bash
python assistant_local.py "Quel délai de temporisation est validé ?" --sortie sorties/contexte-delai.json
```

Ouvrez le fichier produit. `passages` contient les résultats de recherche avec leur provenance. `messages` contient ce qui serait envoyé au modèle : une consigne, puis les passages et la question.

La consigne demande de répondre avec les sources, de citer leurs identifiants et de signaler une décision encore ouverte. Elle précise aussi que les documents sont des données à lire, pas des ordres à exécuter. Vous retrouvez le problème rencontré avec la documentation piégée de la partie 6.

La préparation n’a fait aucun appel réseau. Vous pouvez donc examiner le contexte avant de lancer quoi que ce soit. Si aucun passage n’est retrouvé, le programme le signale et ne demande pas au modèle de combler le vide.

Cela reste une décision de notre application. D’autres usages peuvent avoir besoin d’une réponse générale malgré l’absence de source locale ; ici, nous cherchons une réponse sur les règles de notre service.

## Relier les deux morceaux

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

Vous devez voir les sources sélectionnées. Relancez ensuite le [serveur de la partie 3](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/03-modele-local/02-installer/LECTURE.md), depuis le dossier de cet ancien atelier, avec le modèle SmolLM2-360M-Instruct Q8_0, l’alias `atelier-local` et le port `8080`. Gardez ce serveur ouvert dans un autre terminal, puis ajoutez `--generer` à la commande.

Dans `assistant_local.py`, ouvrez maintenant `appeler`. L’application envoie les messages à `http://127.0.0.1:8080/v1/chat/completions` et extrait le texte de la réponse. Le modèle reste servi par `llama-server` ; notre programme ne charge pas lui-même ses poids.

Ce premier fichier laisse apparaître une erreur Python si le serveur est absent. La version fournie gère ce cas et conserve un journal, y compris lorsque l’appel échoue :

```bash
python assistant_local.py "Quand les données de staging sont-elles réinitialisées ?" --appeler --sortie sorties/reponse-staging.json
```

Le journal contient le contexte, la requête et la réponse brute. Utilisez un autre nom de sortie pour chaque essai : le programme refuse d’écraser un fichier existant.

## Le bon document, la mauvaise réponse

Voici deux réponses réellement obtenues avec le modèle de la partie 3, sur CPU. Les journaux complets sont dans `resultats-reference/reponse-staging.json` et `reponse-delai.json`.

À propos de staging :

> Les documents de staging sont réinitialisées chaque mardi à 06 h 00 UTC. Cet horaire concerne uniquement le service fictif de cet atelier.

L’horaire correspond au document. La phrase est maladroite et ne cite aucun identifiant, malgré la consigne. Mais pour la temporisation, nous obtenons ceci :

> Délai de temporisation validé : 10 minutes.

Aïe. Le passage transmis dit pourtant qu’aucune durée n’est validée. Le nombre vient du modèle, pas de notre documentation. Une troisième question sur la baisse de prix produit également une réponse confuse, qui ne restitue pas correctement les conditions.

Nous avons donc une application qui transmet les sources, et un modèle qui ne les exploite pas de manière fiable. La fiche de ce petit modèle indique l’anglais comme langue ; notre utilisation en français ne lui facilite pas la tâche.[^p7-smollm] Cela ne suffit pas à expliquer chaque erreur, et passer à un autre modèle demanderait de rejouer les mêmes questions.

Ne modifiez pas la règle de temporisation pour qu’elle corresponde à sa réponse. 🙂 La suite logique est de conserver cet échec dans nos essais, puis de comparer une autre formulation ou un modèle plus adapté. Le journal permet de vérifier si l’amélioration vient de la recherche, du contexte ou de la génération.

Pour une question très structurée comme un horaire, nous pourrions aussi afficher directement le passage retrouvé. Générer une nouvelle phrase n’est pas toujours nécessaire.

[^p7-smollm]: Hugging Face, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct).

Notre assistant fonctionne comme programme, mais ses réponses ne sont pas assez fiables pour lui confier les décisions du service. Gardons cette différence en tête en passant à une autre expérience : modifier les poids d’un modèle.

---

[Précédent : Évaluer les sources avant les réponses](../03-evaluer/LECTURE.md) · [Suivant : Préparer ce que notre modèle va apprendre](../05-donnees/LECTURE.md)
