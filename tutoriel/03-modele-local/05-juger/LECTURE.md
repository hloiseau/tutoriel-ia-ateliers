# 5. Décider si le résultat nous sert

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** le serveur fonctionne ; il reste à voir ce que ses réponses valent pour nos usages. Cinq cas courts nous aideront à séparer ces deux constats.

## Une petite grille qui vous appartient

Complétez nos premiers essais avec deux autres demandes :

```bash
python client.py --fichier questions/format.json --sortie resultats/format.json
python client.py --fichier questions/francais.json --sortie resultats/francais.json
```

Le premier demande un objet JSON très précis. Le second reprend l’explication d’une variable, en français. Ouvrez les réponses : le serveur a-t-il renvoyé du texte, le modèle a-t-il suivi la forme demandée, et le contenu tient-il debout ? Pour ne pas mélanger ces questions, rassemblez vos observations dans un fichier `evaluation.md` :

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

Dans l’exécution de référence sous Linux, le modèle a trouvé 10 heures pour le mardi et répondu « I do not know. » pour le dimanche. Le JSON demandé était valide et contenait la bonne liste. L’explication anglaise tenait toutefois en une phrase au lieu des deux demandées. En français, le texte était maladroit et s’est interrompu après avoir atteint la limite de 96 tokens.

Sur cinq demandes très courtes, le même modèle respecte donc certaines consignes et en manque d’autres. Les réponses brutes sont dans `resultats-reference` dans l’archive. Comparez-les aux vôtres et conservez vos propres observations si elles diffèrent : ce sont elles qui décrivent votre installation.

## Partir du travail à faire

Une erreur sur l’horaire du dimanche n’a pas les mêmes conséquences selon le rôle prévu. Un outil qui renseigne automatiquement des lecteurs diffuserait une fausse information. Pour produire des variantes de formulation que vous relisez, ce seul test tranche beaucoup moins de choses.

Écrivez une tâche que vous faites réellement, puis trois exemples dont vous savez juger le résultat. Ajoutez au moins un cas où il faut s’abstenir ou demander une précision. Commencez avec des données inventées ou publiques.

Vous pourrez comparer un autre modèle sur ces mêmes exemples. Gardez les questions identiques pour attribuer plus facilement un changement au modèle. Une taille supérieure, une autre langue d’entraînement ou une autre adaptation peuvent aider ; votre tâche dira si le résultat mérite le temps et les ressources supplémentaires.

Si aucun résultat n’est exploitable sans tout refaire, vous avez aussi obtenu une information utile. Vous n’avez aucune obligation de trouver un usage à un outil parce que vous avez réussi à l’installer.

## Ce que « local » change vraiment

Avec notre client et un modèle déjà téléchargé, les demandes vont vers `127.0.0.1`. Vous pouvez couper la connexion réseau après l’installation et rejouer les appels : le calcul continuera sans API distante.

Cela vous donne la possibilité de conserver le fichier choisi, de décider quand le processus tourne et de garder vos demandes sur cette machine. En revanche, les réponses enregistrées restent des fichiers : sauvegardes automatiques, synchronisation de dossiers et autres utilisateurs de l’ordinateur peuvent encore compter dans votre organisation.

Les poids, eux, ont été produits ailleurs, à partir de données et de travail humain. La fiche et la licence nous renseignent sur le modèle sans rendre nécessairement l’ensemble de son entraînement reproductible ni ses données consultables.

Pour un projet professionnel, examinez séparément ce que vous avez le droit de charger dans l’outil, ce que la licence du modèle autorise et ce que votre organisation accepte. Les documents fictifs de l’atelier suffisent pour apprendre les mécanismes ; inutile d’y copier des données de l’entreprise avant d’avoir répondu à ces questions.


