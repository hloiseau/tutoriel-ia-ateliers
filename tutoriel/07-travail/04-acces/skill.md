Notre équipe a aussi des habitudes qui ne figurent pas dans les messages reçus. Elle conserve les pièces originales, rapproche les identifiants, prépare des brouillons et fait apparaître les décisions manquantes. Nous pouvons écrire cette méthode une fois, puis l’ajuster lorsque le travail évolue.

Ouvrez `procedures/preparer-point.md` dans le dossier de l’atelier. La recette reprend le travail réalisé depuis le premier chapitre : lire les règles, relever les demandes, garder les absences, citer les pièces et préparer le point. Elle dit aussi quoi faire si deux contenus différents portent le même identifiant : demander une vérification. Ce cas aurait été facile à oublier dans une consigne improvisée le vendredi à 18 heures.

Vous pouvez suivre cette recette vous-même ou la fournir explicitement à votre assistant avec les entrées. Gardez `corrige/` à part. Le fichier est un document ordinaire ; l’ouvrir ne l’installe dans aucun logiciel. Pour vérifier son effet lors d’un nouvel essai, conservez la recette utilisée et la réponse brute, puis comparez avec votre point précédent. Une version qui paraît mieux formulée ne mérite pas de perdre au passage la question de Nora sur Cartographie.

Un **skill** rassemble ce genre de procédure avec les ressources utiles à son exécution. Dans le format Agent Skills, un dossier contient un fichier `SKILL.md` qui décrit la tâche et ses instructions ; il peut aussi contenir des références, des modèles de documents ou des scripts. Les assistants compatibles peuvent découvrir les skills disponibles et charger leurs instructions lorsqu’ils en ont besoin.[^p7acces-skills]

L’analogie de la recette de cuisine fonctionne bien ici : notre méthode explique comment préparer le point avec les ingrédients disponibles. Elle peut préciser où chercher le suivi initial et comment servir les questions encore ouvertes. Elle n’ajoute aucun droit à notre compte et ne fournit pas l’information que Léo a oublié d’écrire.

Pour reprendre cette recette dans un système de skills, vérifiez le format, le lieu d’installation et le mode de déclenchement de votre outil. Essayez ensuite une demande qui doit l’utiliser et examinez ce qui a effectivement été chargé. Le simple nom `preparer-point` dans un dossier ne prouve aucune activation.

Vous pouvez aussi vous arrêter au document partagé. Si trois collègues arrivent à suivre la procédure et à reprendre le point sans retrouver votre conversation avec l’assistant, nous avons déjà gagné quelque chose.

[^p7acces-skills]: Agent Skills, [présentation du format](https://agentskills.io/home) et [spécification](https://agentskills.io/specification), consultées le 17 septembre 2026.
