# Expériences restant à vérifier

Les protocoles complets sont dans les [missions locales](prompts/local/README.md), à utiliser avec le [prompt coordinateur](prompts/LOCAL-COORDINATEUR.md). Les prompts sont prêts ; les essais ci-dessous ne sont pas annoncés comme exécutés sur le PC de Hugo.

| Partie | Référence déjà disponible | Travail restant sur la machine de Hugo |
| --- | --- | --- |
| 2 — Apprentissage | Entraînements et évaluations CPU, parcours depuis l’archive, page sous DOM simulé | Reprise sur son système, vrais gestes et rendu dans le navigateur, export du dessin et classification |
| 3 — Modèle local | Serveur réel sur CPU Linux, poids vérifiés, cinq questions et série de mesures | Installation adaptée au système, reproduction CPU, même modèle sur GPU, mesures et fonctionnement hors ligne |
| 4 — Développement | États du code, tests, mutations et cas JSON exécutés | Résolution par un assistant réel, interfaces VS Code/Copilot ; discussion locale facultative évaluée séparément |
| 5 — Agents | Banc déterministe sans modèle et ses tests | Observations avec un assistant réel : outils, contexte, refus, états de tests, reprise, compteurs disponibles |
| 6 — MCP et skills | Construction progressive, client/serveur stdio et tests exécutés | Intégration dans un produit, découverte du skill, recettes réellement produites pour PRIX-1 et PRIX-2 |
| 8 — IA maison | Recherche, réponses documentaires réelles et entraînements NumPy CPU | Reproduction locale, adaptation LoRA d’un LLM sur GPU, comparaison et rechargement de l’adaptateur |
| 9 — Choix d’usage | Exercices de décision et calculs sur données fictives | Comparaison humaine facultative ; aucune mesure de productivité ou d’apprentissage à inventer |

Les rapports existants, réunis dans [les vérifications](verification.md) et les `VERIFICATION.md` des parties, donnent les versions et les limites de chaque référence. Une validation de prose par l’auteur ne remplace pas une exécution manquante.

Les nouveaux rapports utiliseront le [modèle de preuve](prompts/local/RAPPORT-TYPE.md), avec commandes, versions, résultats, erreurs et limites. Les résultats de référence actuels restent conservés. Les données privées et les poids lourds ne vont pas dans Git.

L’import du [ZIP global](../telechargements/zds/tutoriel-ia-complet.zip) dans un brouillon ZdS reste aussi à essayer : images, notes, tableaux, coloration et légendes. Le contrôle structurel automatique ne valide pas le rendu du site.
