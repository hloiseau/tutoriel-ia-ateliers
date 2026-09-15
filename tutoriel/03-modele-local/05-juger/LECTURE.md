# 5. Décider si le résultat nous sert

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** un modèle peut fonctionner correctement comme logiciel et mal répondre à nos questions. Nous allons garder ces deux constats séparés.

## Une petite grille qui vous appartient

Complétez nos premiers essais avec deux autres demandes :

```bash
python client.py --fichier questions/format.json --sortie resultats/format.json
python client.py --fichier questions/francais.json --sortie resultats/francais.json
```

Le premier demande un objet JSON très précis. Le second reprend l’explication d’une variable, en français. Ouvrez les réponses et remplissez une table dans un fichier `evaluation.md` :

| Cas | Vérification | Votre observation |
| --- | --- | --- |
| Variable en anglais | Explication juste, deux phrases | À relever |
| Horaire présent | Mardi à 10 heures | À relever |
| Horaire absent | Pas d’horaire inventé pour dimanche | À relever |
| JSON demandé | Objet valide avec la seule clé `colors` et la liste attendue | À relever |
| Variable en français | Explication juste, français compréhensible, deux phrases | À relever |
Table: Cinq cas à examiner séparément

Pour vérifier le JSON, commencez par copier **le texte produit**, sans le corriger, dans `resultats/format-produit.json`, puis lancez :

```bash
python -m json.tool resultats/format-produit.json
```

Cette commande contrôle la syntaxe JSON. Elle ne vérifie pas que les clés et les valeurs répondent à la demande : ouvrez aussi le résultat et comparez-le à l’attendu.

Si vous retirez vous-même des balises Markdown ou réparez une virgule, notez cette intervention. Le résultat brut et le résultat obtenu après votre correction ne racontent pas la même histoire.

Dans l’exécution de référence sous Linux, le modèle a trouvé 10 heures pour le mardi et répondu « I do not know. » pour le dimanche. Le JSON demandé était valide et contenait la bonne liste. En revanche, l’explication anglaise tenait en une phrase au lieu des deux demandées. La réponse française était maladroite et a atteint la limite de 96 tokens avant de se terminer.

Ce mélange est intéressant : le même modèle respecte certaines consignes et en manque d’autres sur cinq demandes très courtes. Les réponses brutes sont dans `resultats-reference` dans l’archive. Comparez-les aux vôtres, mais conservez aussi vos propres observations si elles diffèrent.

## Partir du travail à faire

Une erreur sur l’horaire du dimanche suffit-elle à jeter le modèle ? Cela dépend du rôle que vous comptiez lui donner. Pour un outil qui renseigne automatiquement des lecteurs, inventer des horaires est un vrai problème. Pour produire des variantes de formulation que vous relisez, ce test ne tranche pas à lui seul.

Écrivez une tâche que vous faites réellement, puis trois exemples dont vous savez juger le résultat. Ajoutez au moins un cas où il faut s’abstenir ou demander une précision. Commencez avec des données inventées ou publiques.

Vous pourrez comparer un autre modèle sur ces mêmes exemples. Changer la question à chaque changement de modèle empêche de savoir d’où vient l’amélioration. Un modèle plus grand, une autre langue d’entraînement ou une autre adaptation peuvent aider, mais c’est votre tâche qui doit décider de l’intérêt.

Si aucun résultat n’est exploitable sans tout refaire, vous avez aussi obtenu une information utile. Vous n’avez aucune obligation de trouver un usage à un outil parce que vous avez réussi à l’installer.

## Ce que « local » change vraiment

Avec notre client et un modèle déjà téléchargé, les demandes vont vers `127.0.0.1`. Le calcul n’a pas besoin d’une API distante. Vous pouvez couper la connexion réseau après l’installation et rejouer les appels pour le constater.

Cela vous donne la possibilité de conserver le fichier choisi, de décider quand le processus tourne et de garder vos demandes sur cette machine. En revanche, les réponses enregistrées restent des fichiers : sauvegardes automatiques, synchronisation de dossiers et autres utilisateurs de l’ordinateur peuvent encore compter dans votre organisation.

L’autohébergement ne répond pas non plus à toutes les questions sur le modèle lui-même. Ses poids ont été produits ailleurs, à partir de données et de travail humain. Sa fiche et sa licence donnent des informations ; elles ne rendent pas nécessairement l’ensemble de son entraînement reproductible ou ses données consultables.

Pour un projet professionnel, examinez séparément ce que vous avez le droit de charger dans l’outil, ce que la licence du modèle autorise et ce que votre organisation accepte. Nous pouvons apprendre les mécanismes avec nos documents fictifs sans résoudre ces questions en copiant des données de l’entreprise dans l’atelier.


