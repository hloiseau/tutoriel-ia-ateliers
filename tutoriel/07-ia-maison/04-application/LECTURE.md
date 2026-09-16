# 4. Assembler notre assistant documentaire

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Évaluer les sources avant les réponses](../03-evaluer/LECTURE.md) · [Suivant : Préparer ce que notre modèle va apprendre](../05-donnees/LECTURE.md)

**TL;DR** — Nous allons relier la recherche au serveur local, puis comparer les réponses avec les passages transmis. Le modèle peut se tromper même lorsque la bonne source est sous ses yeux.

Nous savons quels passages ont été sélectionnés. Il reste à voir exactement ce que le modèle recevra, puis à comparer sa réponse aux sources placées sous ses yeux.

## Regarder ce que le modèle va recevoir

Commençons sans lancer le serveur :

```bash
python assistant_local.py "Quel délai de temporisation est validé ?" --sortie sorties/contexte-delai.json
```

Ouvrez le fichier produit. `passages` contient les résultats de recherche avec leur provenance. `messages` contient ce qui serait envoyé au modèle : une consigne, puis les passages et la question.

La consigne demande de répondre avec les sources, de citer leurs identifiants et de signaler une décision encore ouverte. Elle précise aussi que les documents sont des données à lire, pas des ordres à exécuter. Vous retrouvez le problème rencontré avec la documentation piégée de la partie 6.

À ce stade, aucun appel réseau n’a eu lieu. Vous pouvez lire tranquillement le contexte avant de lancer le serveur. Si la recherche ne ramène aucun passage, le programme s’arrête là au lieu de demander au modèle de combler le vide.

Ce comportement correspond à notre besoin : nous interrogeons les règles du service. Une application chargée de répondre à des questions générales pourrait faire un autre choix, à condition de l’annoncer clairement au lecteur de la réponse.

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

Vous devez voir les sources sélectionnées. Relancez ensuite le [serveur de la partie 3](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/03-modele-local/02-installer/LECTURE.md), depuis le dossier de cet ancien atelier, avec le modèle SmolLM2-360M-Instruct Q8_0, l’alias `atelier-local` et le port `8080`. Gardez ce serveur ouvert dans un autre terminal, revenez dans le dossier de la partie 7, puis ajoutez `--generer` à la commande.

Dans `assistant_local.py`, ouvrez maintenant `appeler`. L’application envoie les messages à `http://127.0.0.1:8080/v1/chat/completions` et extrait le texte de la réponse. Le modèle reste servi par `llama-server` ; notre programme ne charge pas lui-même ses poids.

Notre premier fichier laisse apparaître une erreur Python si le serveur est absent. C’est un bon prochain problème à traiter : la version fournie intercepte ce cas et conserve un journal, y compris lorsque l’appel échoue.

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

Aïe. Ouvrez `reponse-delai.json` : `temporisation#2` figure bien dans les passages et dit qu’aucune durée chiffrée n’est validée. La recherche a fait son travail ; les dix minutes viennent du modèle. Une troisième question sur la baisse de prix produit également une réponse confuse, qui ne restitue pas correctement les conditions.

Notre application transmet bien les sources, mais ce modèle ne les exploite pas de manière fiable dans cet essai. Sa fiche indique l’anglais comme langue ; notre utilisation en français ne lui facilite pas la tâche.[^p7-smollm] Cela n’explique pas à lui seul chaque erreur. Pour comparer un autre modèle, nous rejouerions les mêmes questions et relirions à nouveau les passages envoyés.

Évitons de corriger la règle de temporisation pour donner raison au modèle. 🙂 Conservons plutôt cet échec dans nos essais, puis comparons une autre formulation ou un modèle plus adapté. Grâce au journal, nous pourrons vérifier si le changement touche la recherche, le contexte ou la génération.

Pour une question très structurée comme un horaire, nous pourrions aussi afficher directement le passage retrouvé. Le modèle ajouterait ici une étape et une occasion de déformer une réponse déjà lisible.

[^p7-smollm]: Hugging Face, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct).

Notre programme retrouve des sources et interroge un modèle, mais ses réponses restent trop fragiles pour décider à la place de l’équipe. Nous allons maintenant changer complètement d’échelle et de modèle afin d’observer ce qui se passe lorsque l’on modifie les poids eux-mêmes.

---

[Précédent : Évaluer les sources avant les réponses](../03-evaluer/LECTURE.md) · [Suivant : Préparer ce que notre modèle va apprendre](../05-donnees/LECTURE.md)
