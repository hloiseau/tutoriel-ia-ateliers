# Relecture pédagogique de la partie 4

Révision du 15 septembre 2026, à partir de `299e4198c20e5fee27c22531991425e06f37f860`.

## Le problème relevé

Une première relecture par un second agent a confirmé que le comparatif, l’installation locale et l’atelier se superposaient. Les trois chapitres préparatoires représentaient environ 5 600 mots avant le chapitre de découverte du projet. La lecture de la fonction était répétée et le lecteur écrivait les tests avant de devoir repartir du début pour les demander à l’agent.

La relecture de l’archive Vim a servi à retrouver une progression par manipulations : agir, observer un résultat, comprendre, puis poursuivre.

## Organisation retenue

| Avant | Maintenant |
| --- | --- |
| Panorama et tarifs imposés avant toute manipulation | Choix court, avec accès au comparatif complet depuis le départ |
| Installation et découverte du projet séparées, première lecture en double | Un chapitre pour ouvrir la copie, lancer le scénario et faire expliquer la fonction |
| Tests écrits à la main puis recommencés avec l’agent | Demande à l’agent, lecture du test et correction expliquée dans le même dossier |
| Correction fournie avant la demande à l’agent | Essai d’abord, solution de référence ensuite |
| Continue et deux modèles dans le chemin de l’atelier | Expérience locale facultative après l’atelier et le comparatif |

Les sept chapitres de l’atelier sont suivis de deux compléments : le comparatif intégral, incluant Pi et les tarifs de septembre 2026, puis l’expérience locale. Les trois illustrations de la partie sont conservées. Les sommaires distinguent ces usages ; les lectures de chapitre disposent de liens précédent/suivant. Les anciens points d’entrée `choisir/LECTURE.md` et `01-projet/LECTURE.md` renvoient aux nouveaux chapitres.

## Seconde relecture

Le second agent a relu la version réorganisée. Il a jugé la progression principale cohérente et signalé quatre défauts corrigés ensuite :

- étendre explicitement la revue aux fichiers autres que `suivi.py` ;
- préciser la copie et le terminal utilisés pour les mutations ;
- expliquer `TestCase`, les noms `test_` et `assertFalse` au premier test ;
- retirer la promesse d’un comparatif des MCP, qui appartient à la suite du tutoriel.

Le passage Ask → Agent est décrit pour la cible de session **Local** de VS Code, avec les modèles Copilot. Le terme Local est distingué de l’hébergement du modèle. La comparaison des fichiers utilise une fonction documentée qui ne demande pas d’initialiser Git.

## Vérification réalisée

Les commandes de l’atelier ont été rejouées sous **Python 3.12.14**, dans une copie temporaire, à partir des fichiers fournis. Le premier test a été extrait du bloc Python du chapitre. Résultats : trois tests réussis au départ ; quatre tests avec un échec après ce premier ajout ; treize tests avec deux échecs pour le fichier de référence complet ; treize tests réussis après correction. Les trois scénarios renvoient les décisions prévues. Les deux mutations provoquent des échecs et la copie de travail reste correcte.

[Commandes et sorties conservées](relecture-partie4-execution.json).

Les manifests, les images, les notes et les liens locaux des lectures ont été contrôlés. Les exports des parties 3 et 4 sont reconstruits depuis leurs sources courantes ; chaque membre des ZIP a été comparé au fichier source.

Ces contrôles n’exécutent pas un agent de développement. Ils ne valident ni les interfaces VS Code/Continue à l’écran, ni la réussite des prompts avec un modèle donné, ni les performances CPU/GPU, ni l’import dans ZdS. Le comparatif tarifaire est déplacé, sans nouveau relevé de prix dans cette révision. La validation finale de la pédagogie appartient à la relecture de l’auteur.
