# État des contenus

Mis à jour le **15 septembre 2026**. [Sommaire](../SOMMAIRE.md).

## Textes et illustrations centralisés

| Partie | Chapitres | Sections | Illustrations | État éditorial |
| --- | --- | --- | --- | --- |
| [1 — Histoire](../tutoriel/01-histoire/README.md) | 7 | 29 | 12 | Version V3 validée par l’auteur ; texte préservé |
| [2 — Construire un modèle](../tutoriel/02-apprentissage/README.md) | 8 | 31 | 13 | Version V2 rédigée, à poursuivre en relecture |
| [3 — Modèle local](../tutoriel/03-modele-local/README.md) | 6 | 21 | 4 | Rédigée ; corrections demandées sur la forme conservées ; transition vers la partie 4 ajoutée |
| [4 — Développement](../tutoriel/04-developpement/README.md) | 9 | 29 | 3 | Six chapitres récupérés, précédés des trois chapitres sur les outils et l’installation ; ensemble à relire |

Les sources sont sous `tutoriel/`. Chaque chapitre possède une lecture avec images. Les ateliers, données et résultats sont sous `ateliers/` ; les archives pratiques sont sous `telechargements/`.

Les parties 5 à 8 disposent d’un [plan détaillé](plan-parties-suivantes.md), pas encore de chapitres complets. Le dernier export du billet d’origine reste distinct et n’a pas été ajouté à cette centralisation du tutoriel.

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
