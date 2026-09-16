# Comprendre l’IA et développer avec elle

Les textes, les illustrations et les ateliers du tutoriel en cours de rédaction pour **Zeste de Savoir**, par Hugo Loiseau.

**[Ouvrir le sommaire](SOMMAIRE.md)** · **[Voir ce qui est disponible](docs/etat-des-contenus.md)** · **[Lire les derniers chapitres](tutoriel/08-choisir/LECTURE.md)**

Ce dépôt est le point de travail commun. La branche `main` rassemble les versions courantes, y compris les brouillons identifiés comme tels. Être présent ici ne signifie pas être validé pour publication.

Les **huit parties** sont désormais réunies ici : **56 chapitres et deux annexes, 196 sections et 46 illustrations**, avec les ateliers et les documents de reprise. Le [sommaire](SOMMAIRE.md) mène directement aux lectures par chapitre. Les huit parties disposent d’une première rédaction ; les relectures et expériences restantes sont suivies dans l’état des contenus. Le billet d’origine est un contenu séparé.

## Où trouver quoi ?

| Dossier ou fichier | Contenu |
| --- | --- |
| [SOMMAIRE.md](SOMMAIRE.md) | Plan global et liens de lecture |
| [tutoriel/](tutoriel/README.md) | Sources Markdown du tutoriel, organisées par partie |
| [ateliers/](ateliers/) | Code, données d’exercice et résultats de référence |
| [telechargements/](telechargements/) | Archives des ateliers |
| [docs/](docs/README.md) | État des textes, décisions de rédaction et vérifications |
| [billets/](billets/README.md) | Repère vers le billet à l’origine du projet ; sources à récupérer |
| [outils/](outils/) | Scripts de préparation et de vérification |

Pour relire ou corriger, partez du sommaire et modifiez le Markdown de la section concernée. Les vues `LECTURE.md` regroupent les sections pour une lecture continue ; les fichiers séparés sont les sources à modifier. Les ZIP servent aux téléchargements et aux imports ZdS.

## Choisir un atelier

| Partie | Ce que l’on fait | Dossier de départ |
| --- | --- | --- |
| 2 — Comprendre un modèle | Reconnaître des chiffres, entraîner un petit réseau, produire du texte et calculer une attention | [Atelier d’apprentissage](ateliers/02-apprentissage/atelier-ia/README.md) |
| 3 — Modèle local | Charger un petit modèle, lui envoyer des messages et mesurer les appels | [Atelier local](ateliers/03-modele-local/atelier-local/README.md) |
| 4 — Développement | Reproduire un bug, écrire les tests, corriger et vérifier un suivi de prix | [Atelier de développement](ateliers/04-developpement/README.md) |
| 5 — Agents | Observer des appels d’outils, des refus et un budget, puis calculer un coût fictif | [Banc d’essai sans modèle](ateliers/05-agents/README.md) |
| 6 — MCP et skills | Consulter des tickets avec un serveur MCP et préparer une recette | [Atelier MCP et skill](ateliers/06-mcp-skills/README.md) |
| 7 — IA maison | Retrouver des sources, assembler une application et adapter un petit modèle | [Atelier IA maison](ateliers/07-ia-maison/README.md) |
| 8 — Choisir la place de l’IA | Examiner les données, comparer l’effort et décider d’un usage | [Exercices et corrigés](ateliers/08-choisir/README.md) |

Chaque README indique le dossier dans lequel ouvrir le terminal et les commandes à lancer. Python 3.12 est utilisé pour les exécutions de référence.

Les répertoires `resultats-reference` contiennent des résultats réellement obtenus. Les scripts écrivent vos essais dans leurs propres dossiers de sortie. Les réponses et durées peuvent différer sur votre machine.

## Télécharger

Les [archives d’import ZdS](telechargements/zds/README.md) contiennent les parties 1 à 8 et les annexes dans un ZIP séparé.

Vous pouvez cloner ce dépôt ou télécharger son archive ZIP depuis GitHub. Les [archives des sept ateliers](telechargements/) permettent de télécharger un atelier séparément. Le chapitre peut pointer vers une révision précise du dépôt pour conserver les mêmes fichiers au fil des corrections. Les fichiers de poids du modèle local et les exécutables de llama.cpp se téléchargent séparément.

## État des vérifications des ateliers

Les ateliers ont été exécutés sous Linux sur CPU. L’atelier local a été interrogé avec un vrai modèle ; les tests unitaires du client utilisent, eux, des réponses factices. Les scripts de développement et leurs mutations ont été exécutés. Les prompts fournis ne sont pas des traces attribuées à un agent particulier.

La recherche et les entraînements de la partie 7 ont également été rejoués depuis leur archive. Les réponses du modèle documentaire conservent leurs erreurs.

Les exercices de décision de la partie 8 ont été vérifiés depuis leur archive. Les durées de démonstration sont fictives ; aucune mesure de gain de productivité ou d’apprentissage n’en est tirée.

Les essais GPU, Windows, macOS et les interactions dans un vrai navigateur restent à vérifier. Voir [les résultats et leurs limites](docs/verification.md).

## Préparer les lectures et les imports ZdS

```bash
python outils/assembler_tutoriel.py --exports ../exports-zds
```

Cette commande vérifie les fichiers et les images référencés, régénère les lectures GitHub et prépare un ZIP par partie ainsi qu’un ZIP d’annexes, avec leurs manifests à la racine. Sans `--exports`, elle régénère seulement les lectures. Les notes éditoriales et les ateliers ne sont pas inclus dans les imports ZdS.

## Préparer les archives des ateliers

```bash
python outils/assembler_annexes.py
```

Les sept ZIP sont écrits dans `telechargements/`. Ils contiennent le code, les résultats de référence et les mentions de licence.

Pour exécuter les contrôles rapides sans téléchargement de modèle :

```bash
python outils/verifier.py
```

Ces contrôles ne relancent pas les entraînements de la partie 2 ni le serveur de la partie 3. Les tests MCP de la partie 6 se lancent séparément, avec les dépendances de son [atelier](ateliers/06-mcp-skills/README.md).

Les sources des données et du modèle sont recensées dans [CREDITS.md](CREDITS.md).

## Licences

Copyright © 2026 Hugo Loiseau.

- **Code et page de dessin : GPLv3**, voir [LICENSE](LICENSE).
- **Textes de documentation et illustrations originales : CC BY-SA 4.0**, voir [LICENCE-TEXTES.md](LICENCE-TEXTES.md).
- **Éléments tiers :** les licences et attributions précisées dans [CREDITS.md](CREDITS.md) restent applicables.

