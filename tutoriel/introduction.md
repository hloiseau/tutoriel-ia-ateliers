**TL;DR** — Nous allons découvrir comment l’IA s’est construite, faire fonctionner de petits modèles, développer avec un assistant et apprendre à adapter ces outils à nos besoins. Les premiers ateliers se suivent sur CPU ; les expériences avec une carte graphique viennent ensuite.

Salut !

Vous avez probablement déjà vu un assistant écrire une fonction, expliquer une erreur ou proposer une correction. Parfois, le résultat est utile tout de suite. D’autres fois, on se retrouve avec beaucoup de code et quelques bonnes raisons de tout relire. 😅

J’utilise un agent pour développer sur une flotte de microservices en Go. Avec le temps, j’ai adapté ses consignes et ses outils à notre manière de travailler. Cela m’a aussi donné envie de comprendre ce qui se passe derrière ses réponses : d’où viennent ces modèles, comment ils apprennent et ce qu’on peut réellement en faire chez soi.

C’est ce que je vous propose d’explorer dans ce tutoriel. Nous allons commencer par l’histoire de l’IA, puis construire et utiliser des modèles assez petits pour pouvoir regarder leur fonctionnement. Nous passerons ensuite au développement avec un assistant, aux MCP, aux skills et à l’adaptation d’un modèle.

Nous parlerons aussi des personnes qui participent à leur création, des données utilisées, des ressources consommées et des entreprises dont nous dépendons en les utilisant. Comprendre un outil permet de mieux décider quelle place lui donner, y compris lorsqu’on préfère s’en passer.

# Ce que nous allons faire

Le tutoriel suit huit parties :

| Partie | Ce que nous allons explorer |
| --- | --- |
| 1. Une histoire de l’IA | Les idées, les réussites et les difficultés qui nous ont amenés jusqu’aux outils actuels |
| 2. Comprendre un modèle en le construisant | Reconnaître des chiffres, entraîner un petit réseau et produire du texte |
| 3. Faire tourner un modèle chez soi | Installer un moteur, envoyer des questions et examiner les résultats |
| 4. Développer avec une IA | Suivre un ticket, écrire des tests, corriger le code et vérifier le changement |
| 5. Comprendre les agents | Observer leurs outils, leur contexte, leurs permissions et leurs coûts |
| 6. Les MCP et les skills | Construire un serveur MCP et adapter une procédure de travail |
| 7. Construire son IA maison | Rechercher dans ses documents, adapter un modèle et entraîner un petit réseau |
| 8. Choisir la place de l’IA | Examiner les conséquences de nos usages et construire nos propres critères de choix |
Table: Le parcours du tutoriel

Pour le développement, nous utiliserons un service fictif de suivi de prix. Un ticket nous accompagnera de la demande initiale jusqu’aux tests et à la recette. Cela nous permettra de voir pourquoi une consigne devient utile, et ce qui se passe lorsqu’il manque une décision dans le ticket.

Les fichiers des ateliers et leurs corrigés sont disponibles dans [le dépôt du tutoriel](https://github.com/hloiseau/tutoriel-ia-ateliers). Chaque partie indique où ouvrir le terminal et quels fichiers utiliser. Vous pourrez comparer vos résultats aux exemples fournis sans avoir à envoyer vos exercices à quelqu’un.

# De quoi avez-vous besoin ?

Pour les ateliers, je pars du principe que vous avez déjà écrit un peu de code : variables, conditions, boucles et fonctions doivent vous être familières. Le code des exercices est principalement en Python. Connaître Go n’est pas nécessaire. Les notions de calcul et de représentation des données seront expliquées lorsqu’elles serviront.

Un ordinateur capable de lancer Python et un terminal suffisent pour commencer. Les environnements de référence utilisent Python 3.12. Les chapitres d’installation vous guideront pour préparer les dépendances ; inutile de tout installer avant d’avoir commencé.

Les petits modèles et les exercices de base tournent sur CPU. Si vous avez une carte graphique compatible, vous pourrez ensuite explorer les variantes correspondantes. La machine que je prévois d’utiliser possède une RTX 3090 Ti de 24 Go et 64 Go de RAM, mais vous pourrez suivre les premiers ateliers avec un matériel beaucoup plus modeste.

Le développement avec un agent demande aussi un outil capable de mener les tâches proposées. La partie 4 présente les possibilités avant de commencer l’exercice. Vous pourrez également suivre les modifications à la main. Pour choisir un service, consultez ses conditions au moment de l’utiliser : le comparatif des annexes décrit les offres relevées en septembre 2026.

# Comment avancer ?

Si vous découvrez le sujet, suivez les parties dans l’ordre. L’histoire pose les premières questions ; les ateliers suivants donnent progressivement les moyens d’y répondre. Si vous connaissez déjà une notion, le TL;DR placé au début de chaque partie et de chaque chapitre vous aidera à retrouver la suite.

Prenez le temps de lancer les exemples et de regarder ce qui se produit. Une réponse différente de celle du tutoriel peut être intéressante : gardez la question, la version du modèle et le résultat. Nous verrons comment comparer ces essais.

Si vous débutez en développement, essayez aussi de refaire certains changements sans assistant. Comprendre une correction, savoir la tester et pouvoir expliquer pourquoi elle fonctionne vous servira bien au-delà de cet exercice.

Nous pouvons maintenant remonter un peu dans le temps. Avant les agents capables de modifier un dépôt, il y a eu beaucoup d’autres façons d’essayer de faire raisonner une machine.
