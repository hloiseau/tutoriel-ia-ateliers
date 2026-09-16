# État des contenus

Mis à jour le **16 septembre 2026**. [Sommaire](../SOMMAIRE.md).

## Textes et illustrations centralisés

| Partie | Chapitres | Sections | Illustrations | État éditorial |
| --- | --- | --- | --- | --- |
| [1 — Histoire](../tutoriel/01-histoire/README.md) | 7 | 29 | 12 | Fond V3 validé ; réécriture globale effectuée, à relire par l’auteur |
| [2 — Construire un modèle](../tutoriel/02-apprentissage/README.md) | 8 | 31 | 13 | Réécriture globale effectuée ; résultats CPU préservés, à relire par l’auteur |
| [3 — Modèle local](../tutoriel/03-modele-local/README.md) | 6 | 21 | 4 | Réécriture globale effectuée ; références CPU préservées, essais sur la machine de l’auteur à faire |
| [4 — Développement](../tutoriel/04-developpement/README.md) | 7 | 23 | 3 | Réécriture globale effectuée ; atelier continu, interfaces à vérifier |
| [5 — Agents](../tutoriel/05-agents/README.md) | 6 | 18 | 3 | Réécriture globale effectuée ; banc Python exécuté, essais avec un modèle à réaliser |
| [6 — MCP et skills](../tutoriel/06-mcp-skills/README.md) | 7 | 25 | 3 | Fond validé ; réécriture globale effectuée, essais du skill avec un modèle à réaliser |
| [7 — IA maison](../tutoriel/07-ia-maison/README.md) | 8 | 24 | 4 | Accord global conservé ; réécriture effectuée, expérience GPU à faire |
| [8 — Choisir la place de l’IA](../tutoriel/08-choisir/README.md) | 7 | 21 | 4 | Réécriture globale effectuée ; exercices vérifiés, à relire par l’auteur |
| [Annexes](../tutoriel/annexes/README.md) | 2 | 4 | 0 | Formulations harmonisées ; comparatif daté et expérience locale facultative à exécuter |

Les sources sont sous `tutoriel/`. Chaque chapitre possède une lecture avec images. Les ateliers, données et résultats sont sous `ateliers/` ; les archives pratiques sont sous `telechargements/`.

Les huit parties disposent maintenant d’une première rédaction. Le [suivi de fin de rédaction](plan-parties-suivantes.md) renvoie aux relectures et aux expériences restantes. Le dernier export du billet d’origine reste distinct et n’a pas été ajouté à cette centralisation du tutoriel.

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

## Partie 6 validée par l’auteur

Hugo valide la partie 6 le **16 septembre 2026**, après la reprise de la construction du MCP et sa passe adverse. Cette validation porte sur la version des chapitres au commit `aa79bbe51ff9fe2379604339b88057d3fe34719f`. Les essais pratiques restants sont suivis dans le rapport de vérification. À la demande de Hugo, l’analogie des recettes a ensuite été intégrée à l’introduction du chapitre 6, consacré à l’adaptation du skill.

## Partie 7 rédigée

Huit chapitres, vingt-quatre sections et quatre illustrations. L’archive pratique a été extraite et dix-neuf commandes ont été exécutées, dont onze tests. Les trois entraînements et les six pertes de test ont été reproduits. Trois appels réels au modèle documentaire conservent notamment une durée inventée malgré une source qui la laisse ouverte.

La [vérification](../tutoriel/07-ia-maison/VERIFICATION.md) distingue ces exécutions de l’adaptation d’un LLM sur GPU, qui reste à réaliser. Hugo a donné son accord global sur la partie 7 ; les validations pratiques restantes ne sont pas levées par cet accord.

## Partie 8 rédigée

Sept chapitres, vingt et une sections, quatre illustrations et un atelier sans dépendance supplémentaire. Neuf commandes ont été exécutées depuis l’archive extraite, dont huit tests unitaires. Le bug volontaire et les deux corrigés de lecture de code donnent les résultats attendus.

Les sources distinguent travail humain, droits, ouverture, impacts environnementaux, dépendances et apprentissage. Les durées du bilan et les paramètres du calcul énergétique sont fictifs et étiquetés comme tels. Aucune comparaison réelle avec et sans IA, ni mesure pédagogique sur des lecteurs, n’a été réalisée. Voir [le rapport](../tutoriel/08-choisir/VERIFICATION.md) et la [passe adverse](relecture-partie8.md).

Cette partie attend la relecture de l’auteur. Les huit parties sont rédigées ; cela ne vaut ni validation générale ni publication sur ZdS.

## Préparation de la reprise et de la relecture globale

L’auteur a donné un avis globalement positif sur la partie 8, en demandant de reprendre plus tard son ton et les oppositions rhétoriques répétées. Une nouvelle [introduction générale](../tutoriel/introduction.md) est rédigée et attend sa relecture. Le [ZIP global](../telechargements/zds/tutoriel-ia-complet.zip) réunit les huit parties et les annexes ; sa structure est vérifiée, son import interactif dans ZdS reste à faire.

Les [prompts locaux](prompts/LOCAL-COORDINATEUR.md) couvrent les expériences sur le PC de Hugo. Le [prompt de réécriture](prompts/RELECTURE-COORDINATEUR.md) demande une flotte de huit sous-agents et renvoie au guide détaillé de sa voix. Ces documents n’attestent d’aucune nouvelle expérience GPU ; la passe éditoriale effectuée ensuite est décrite ci-dessous.

## Réécriture globale du 16 septembre 2026

Huit missions distinctes ont relu et réécrit les sources canoniques, une par partie, puis deux passes adverses ont contrôlé les raccords. Le [bilan de coordination](relecture/2026-09-16-globale/bilan-coordinateur.md) rassemble les changements, les contrôles et les endroits où concentrer la relecture de l’auteur.

La passe a réduit les oppositions rhétoriques et les transitions automatiques, rendu les manipulations plus concrètes et conservé les distinctions techniques utiles. Le schéma de recherche documentaire de la partie 7 a également été reformulé depuis son générateur. L’introduction générale, déjà naturelle, a été relue sans changement de fond.

Cette réécriture n’ajoute aucune expérience sur le PC de Hugo. Son système reste à identifier ; l’adaptation de LLM sur la RTX 3090 Ti, les interfaces réelles, les essais de skills et d’agents ainsi que l’import interactif dans ZdS restent à effectuer. Le [projet d’extension aux usages hors développement](relecture/2026-09-16-globale/extension-hors-developpement.md) est une proposition de structure, pas une neuvième partie déjà rédigée.
