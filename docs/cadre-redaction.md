# Cadre de rédaction

Ces choix reprennent les demandes formulées par Hugo pendant la préparation du billet et du tutoriel. Ce fichier sert à continuer le travail sans lui demander de répéter ces préférences.

## Le projet

Écrire un tutoriel très complet sur l’IA et son utilisation en développement : histoire, fonctionnement des modèles, pratique, auto-hébergement, agents, MCP, skills, adaptation de modèles et création d’une petite IA.

Commencer par l’histoire de l’IA. Relier les parties entre elles et expliquer avec quels outils réaliser les manipulations avant de les demander au lecteur.

Ne pas réduire le tutoriel à Claude Code. Cursor, Codex et les autres assistants font partie du paysage. Employer **MCP**, pas « connecteur ».

## La manière d’écrire

Référence donnée par l’auteur : [le tutoriel Vim de ZdS](https://zestedesavoir.com/tutoriels/3575/vim/), fourni aussi en archive.

Reprendre l’esprit de cette pédagogie : explications vivantes, situations concrètes, illustrations qui aident à comprendre, progression accompagnée et touches d’humour. La référence ne remplace pas la voix personnelle de l’auteur et n’autorise pas à copier les formulations.

- Écrire en français naturel, avec des phrases directes et une voix cohérente.
- Garder les termes que l’auteur emploie lorsqu’ils servent le propos, en expliquant ceux qui sont nécessaires au lecteur.
- Utiliser de vrais smileys Unicode avec mesure.
- Mettre un TL;DR au début des parties et chapitres.
- Préférer de vraies illustrations explicatives aux simples promesses d’illustration.
- Éviter le ton scolaire, les commentaires sur la fabrication du tutoriel et les panneaux d’information condescendants.
- Ne pas diluer une opinion assumée en une formule vague ; distinguer cependant l’opinion d’un fait technique.
- Corriger les titres, accords et ponctuation sans neutraliser le ton.

## Faire et comprendre

Des ateliers guidés et reproductibles, accompagnés de fichiers, de résultats attendus et de corrections consultables. L’auteur ne corrigera pas les exercices des lecteurs ; leur retour ne conditionne pas l’avancement du tutoriel.

Prévoir un parcours sans grosse carte graphique et sans abonnement payant obligatoire. Les variantes GPU enrichissent le parcours ; elles ne le remplacent pas.

Un développeur junior doit pouvoir comprendre pourquoi une solution fonctionne. L’assistant peut aider à structurer des tests ou à traiter des tâches répétitives, mais relire, tester et valider restent nécessaires. Montrer aussi les situations où il vaut mieux travailler sans IA.

## Les questions à ne pas oublier

Éthique, données d’entraînement, création des modèles, licences, confidentialité, dépendance aux fournisseurs, coût environnemental et évolution du métier.

L’auto-hébergement est une possibilité à expérimenter, pas une réponse automatique à toutes ces questions. Les traiter au fil des usages, puis les approfondir dans les parties consacrées à ces choix.

Partir des difficultés réelles du développeur. Adapter l’outil à sa manière de travailler ; ne pas organiser son travail autour d’un framework simplement parce qu’il est populaire.

## Idée à reprendre plus tard : les skills comme recettes

Analogie transmise par Hugo le 16 septembre 2026, proposée par un ami :

> Les skills sont comme une recette de cuisine, on peut enlever du sel ou du sucre pour l’adapter à notre régime.

À garder pour la partie sur les skills : adapter une procédure à ses besoins plutôt que la reprendre telle quelle. Hugo demande de conserver l’idée pour une prochaine passe, sans l’intégrer immédiatement au chapitre.

## Sources et vérifications

- Aucune statistique, mesure ou trace d’exécution inventée.
- Séparer les exemples fictifs des résultats réellement obtenus.
- Vérifier les informations changeantes dans les sources officielles ; dater les comparatifs.
- La comparaison d’outils ajoutée à la partie 4 est une photographie de septembre 2026. Inclure Pi et faire un véritable tour des harness connus, en distinguant agents, éditeurs et services ; vérifier les changements de nom et les projets archivés.
- Distinguer installation documentée et installation réellement rejouée.
- Expliquer les limites utiles sans multiplier les avertissements décoratifs.

## Format et organisation

Suivre [Rédiger sur ZdS](https://zestedesavoir.com/tutoriels/249/rediger-sur-zds/). Les sources sont en Markdown découpé au format ZdS, avec appels de notes, légendes, crédits et images.

GitHub rassemble désormais les fichiers courants. Le sommaire est le point d’entrée. Les versions précédentes se retrouvent dans Git, sans créer des copies concurrentes nommées « finale-v2-v3 ».

Les derniers chapitres peuvent être sur `main` tout en restant à relire. Leur statut doit l’indiquer. La publication sur ZdS reste une étape séparée.

Textes et illustrations originales : CC BY-SA 4.0. Code : licence GPLv3 présente dans le dépôt. Conserver les licences et attributions propres aux éléments tiers.
