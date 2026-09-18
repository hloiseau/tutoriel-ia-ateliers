# Sauvegarde après interruption du transfert

Le 18 septembre 2026, l’environnement de rédaction est déconnecté pendant la publication de la branche `parcours-dev-travail-2026-09-17`. Le commit local `ff0d73b` avait été créé après la rédaction, l’intégration et les contrôles. Son arbre Git attendu est `04fe18090769bbac995251362e639702d4519856`.

Cette branche de sauvegarde rend accessibles les huit archives dont le transfert sur GitHub a été confirmé avant l’interruption. Elle ne remplace pas la publication complète du commit local. Les sources du dépôt hors de ce dossier restent celles du commit de départ `a81cbdc9dc09caf76990a90e93f326742600a05b`.

Les [sept chapitres du parcours de tâches de travail sont aussi lisibles directement](partie-7/README.md). Les sources et les deux images ont été récupérées depuis le ZIP transféré, avec contrôle CRC de chaque entrée ; les empreintes Git des images correspondent aux originaux. Les vues de lecture adaptent seulement les liens de téléchargement et d’images à cette sauvegarde.

## Textes récupérés

- [Partie 2 — repères communs et apprentissage](02-apprentissage.zip) : neuf chapitres, dont le nouveau premier chapitre sans code.
- [Partie 6 — MCP et skills](06-mcp-skills.zip) : conclusion raccordée aux deux parcours.
- [Partie 7 — tâches de travail](07-travail.zip) : sept chapitres complets, vingt-deux sections, deux illustrations et manifest.
- [Partie 8 — IA maison](08-ia-maison.zip) : sources renumérotées et raccordées.
- [Partie 9 — choix d’usage](09-choisir.zip) : conclusion commune, avec exercices accessibles sans Python.

Chaque ZIP de partie contient les petits Markdown canoniques et les illustrations. Les lectures monolithiques ne font pas partie des imports ZdS.

## Ateliers récupérés

- [Dossier fictif et pipeline de tâches de travail](atelier-hors-developpement.zip) : application locale, variante n8n, consignes, procédure, exercices et tests.
- [Atelier IA maison](atelier-ia-maison.zip) : README raccordé ; résultats de référence conservés.
- [Atelier des choix d’usage](atelier-choisir-ia.zip) : README raccordé ; références conservées.

Décompressez les archives avant utilisation. Le parcours local de tâches de travail se suit en ouvrant `pipeline/index.html`. Il n’appelle aucun modèle et reçoit une extraction par copier-coller ou charge un exemple fictif.

## Vérifications déjà exécutées avant l’interruption

Dans l’environnement de rédaction, sous Linux avec Python 3.12.14 et Node.js 24.19.0 : neuf tests sur les données, dix-huit tests du moteur local, quinze tests du code des nœuds n8n hors de son moteur et huit tests des assembleurs réussissaient. Les quarante-deux tests de l’atelier réussissaient aussi depuis son archive extraite.

Le ZIP global avait été reconstruit et contrôlé : neuf parties, soixante-quatre chapitres et deux annexes, deux cent vingt-deux sections et quarante-neuf images. Son transfert n’est pas confirmé et il n’est pas livré dans cette sauvegarde. Son empreinte locale était `f4da501c3b8cb61ac461bb6cbf07b39e59d2f48b7dcbd17604463b1ee2f9a04b`.

L’interface locale dans un vrai navigateur, l’import et l’exécution dans n8n, les sorties d’assistants réels, les expériences sur le PC de Hugo et l’import ZdS restent à vérifier. Aucun import ZdS n’a été réalisé.

## Reprendre la publication

Reconnecter l’environnement contenant `/workspace/scratch/b759e1b5a3b7/tutoriel-ia-ateliers`, puis retrouver le commit `ff0d73b` sur `parcours-dev-travail-2026-09-17`. Le fichier voisin `publication-parcours.json` contient la description complète de l’arbre à publier, et `empreintes-parcours.json` les empreintes des livrables contrôlés.

La publication complète doit notamment conserver l’introduction générale, le sommaire à deux parcours, les lectures générées, les rapports, les assembleurs et le ZIP global. Ne pas présenter cette sauvegarde comme leur publication achevée.
