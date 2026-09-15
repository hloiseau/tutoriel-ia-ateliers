# État des contenus

Mis à jour le **15 septembre 2026**. [Sommaire](../SOMMAIRE.md).

## Textes et illustrations centralisés

| Partie | Chapitres | Sections | Illustrations | État éditorial |
| --- | --- | --- | --- | --- |
| [1 — Histoire](../tutoriel/01-histoire/README.md) | 7 | 29 | 12 | Version V3 validée par l’auteur ; texte préservé |
| [2 — Construire un modèle](../tutoriel/02-apprentissage/README.md) | 8 | 31 | 13 | Version V2 rédigée, à poursuivre en relecture |
| [3 — Modèle local](../tutoriel/03-modele-local/README.md) | 6 | 21 | 4 | Rédigée ; corrections demandées sur la forme conservées ; transition vers la partie 4 ajoutée |
| [4 — Développement](../tutoriel/04-developpement/README.md) | 7 | 23 | 3 | Atelier continu ; interfaces à vérifier |
| [5 — Agents](../tutoriel/05-agents/README.md) | 6 | 18 | 3 | Première rédaction complète ; banc Python exécuté, essais avec un modèle à réaliser |
| [6 — MCP et skills](../tutoriel/06-mcp-skills/README.md) | 7 | 25 | 3 | Construction du MCP pas à pas ; parcours rejoué depuis le Markdown, essais du skill avec un modèle à réaliser |
| [Annexes](../tutoriel/annexes/README.md) | 2 | 4 | 0 | Comparatif des outils et expérience locale facultative |

Les sources sont sous `tutoriel/`. Chaque chapitre possède une lecture avec images. Les ateliers, données et résultats sont sous `ateliers/` ; les archives pratiques sont sous `telechargements/`.

Les parties 7 et 8 disposent d’un [plan détaillé](plan-parties-suivantes.md), pas encore de chapitres complets. Le dernier export du billet d’origine reste distinct et n’a pas été ajouté à cette centralisation du tutoriel.

## Ce qui a été vérifié pendant l’intégration

- Décompression des trois archives fournies, sans exécuter leur contenu.
- Présence des 178 fichiers Markdown référencés par les manifests et des 32 images utilisées.
- Assemblage des 30 lectures de chapitre et des quatre lectures complètes.
- Construction des quatre ZIP ZdS à partir des sources centralisées, avec les manifests et images à la bonne place.
- Raccord de la partie 3 à la partie 4, conservation des trois nouveaux chapitres et suppression de la seconde étape de téléchargement du projet.
- Remplacement des liens locaux d’annexes par les téléchargements GitHub existants, épinglés à leur révision.

Cette intégration ne rejoue pas les expériences sur les modèles, ni les installations d’assistants, ni l’import dans l’interface ZdS.

## Provenance et versions

Les trois ZIP déposés par l’auteur restent dans [imports/](../imports/README.md). Le [relevé de provenance](../imports/provenance.json) conserve les fichiers d’origine et leurs empreintes. Git conserve les versions antérieures.

L’archive fournie des parties 3 et 4 précédait trois corrections explicitement demandées : « environ 386 Mo », une formulation moins scolaire sur la fiche de modèle et « planter tout le bureau ». Ces corrections ont été réappliquées. Les ateliers existants du dépôt, déjà publiés et vérifiés, n’ont pas été écrasés par leurs copies anciennes contenues dans les archives.

## Validations pratiques restantes

[Vérification des ateliers](verification.md) · [Nouvelles installations de la partie 4](../tutoriel/04-developpement/VERIFICATION.md) · [Expériences sur la machine de l’auteur](experiences-a-lancer.md).

Les rapports initiaux récupérés restent sous `docs/verifications-initiales/`. Ils décrivent leurs exécutions d’origine ; leurs chemins se rapportent aux anciens exports.

## Correction après relecture : CPU et agent de code

La cohérence des versions ne validait pas la faisabilité du parcours. Les introductions et raccords des parties 3–4 ont été corrigés : Qwen 1,5B sur CPU est une expérience facultative de discussion, encore non exécutée, et non une solution validée pour mener l’atelier avec un agent. La qualité des réponses et les délais restent à mesurer.

## Réorganisation pédagogique

Sept chapitres suivent désormais un seul atelier ; le comparatif et l’expérience locale sont consultables séparément. Les doublons de lecture et les redémarrages de l’exercice ont été retirés. Les commandes des versions de référence ont été rejouées sous Python 3.12.14, sans agent. Voir la [relecture et ses limites](relecture-partie4.md).

## Déplacement dans les annexes

À la demande de l’auteur, les anciens chapitres 8 et 9 de la partie 4 sont déplacés dans `tutoriel/annexes/`. La partie 4 comporte désormais sept chapitres et son export ne contient plus le comparatif ni l’expérience locale. Ceux-ci disposent d’un manifest et d’un ZIP d’import propres. Les anciens liens de lecture renvoient vers les annexes.

## Partie 5 rédigée

Six chapitres, dix-huit sections, trois schémas et un atelier Python. Le banc rejoue des demandes d’outils fictives sans modèle. Son archive a été extraite et les manipulations exécutées ; les observations avec un assistant réel restent à faire. Voir [les résultats et les limites](../tutoriel/05-agents/VERIFICATION.md).

## Partie 6 rédigée

Sept chapitres, vingt et une sections, trois schémas, un serveur et un client MCP, puis un skill de préparation de recette. Dix appels stdio et dix tests ont été exécutés depuis l’archive extraite. Les fichiers de la recette restent à essayer avec un assistant réel. Voir [les résultats et leurs limites](../tutoriel/06-mcp-skills/VERIFICATION.md).

Une correction de l’assembleur rétablit également les numéros de chapitre dans les lectures complètes des parties 4 et 5 ; leurs sources de cours restent inchangées.

## Reprise du chapitre de construction du MCP

Le chapitre 3 de la partie 6 comporte maintenant sept étapes : fichier vide, premier outil, catalogue, recherche documentaire, validation, ressource et tests. Le client permet de choisir explicitement `mon_serveur.py`. Les chapitres suivants gardent cette cible. Les états intermédiaires, le corrigé complet et les tests sont dans l’archive pratique.

Le parcours a été reconstruit depuis les blocs de code du chapitre, avec les fichiers d’une archive extraite. La [passe adverse](relecture-construction-mcp.md) décrit les défauts corrigés, les mutations essayées et les limites restantes.
