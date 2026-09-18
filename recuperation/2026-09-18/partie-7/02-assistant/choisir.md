Pour cet exercice, cherchez trois fonctions : joindre des fichiers texte, obtenir un document récupérable et revoir ce document après une correction. Une conversation avec pièces jointes peut déjà convenir. Un espace de travail capable de lire plusieurs fichiers et d’en créer d’autres permet de conserver plus facilement les résultats.

Le **modèle** est le système qui produit le texte. L’**assistant** est l’application avec laquelle vous échangez ; elle lui prépare un **contexte**, composé notamment de vos consignes, des messages et des passages des fichiers qu’elle lui transmet. Joindre un document rend son contenu accessible au système, sans prouver que chaque ligne sera utilisée dans la réponse. Nous demanderons donc des références vérifiables.

Quand l’application laisse le modèle choisir des opérations — ouvrir un fichier, rechercher un passage, créer un document, examiner le résultat — et enchaîne ces opérations, nous parlons d’un **agent**. Ici, sa marge de manœuvre restera modeste : lire un dossier d’exercice et produire des fichiers de travail. Cela suffit largement pour oublier un doublon. 😅

### Avec ChatGPT Work

La documentation de ChatGPT Work décrit le choix du mode **Work**, l’ajout de fichiers sources et la création de documents à relire. Sur le Web, les fichiers produits peuvent être ouverts ou téléchargés depuis la conversation.[^p7-work-fichiers] Pour notre essai, démarrez une nouvelle tâche dans ce mode si votre compte le propose. Joignez les huit fichiers d’`entrees/`, puis `regles-equipe.md` et `modele-point.md`. Les huit entrées sont les cinq courriels, les deux notes de réunion et le CSV.

Vous n’avez aucun plugin à installer pour travailler avec ces pièces jointes. Si l’interface propose d’accéder à votre messagerie ou à un espace partagé, laissez cet accès de côté : tous les documents utiles sont déjà dans le dossier. L’option de travail local d’une application de bureau décrit l’endroit où elle utilise les fichiers et les outils ; elle ne suffit pas à établir que le modèle s’exécute sur votre ordinateur.

### Avec Claude, notamment Cowork

La page d’Anthropic présente Cowork comme un moyen de confier une tâche portant sur les dossiers et outils choisis par l’utilisateur. Au 17 septembre 2026, elle annonce son intégration sous le nom Claude, en déploiement sur Pro et Max ; le nom visible dépend donc de l’accès proposé à votre compte.[^p7-claude-cowork]

Préparez un dossier de travail qui contient uniquement `entrees/`, les règles et le modèle de point. Dans le parcours de travail sur fichiers proposé par votre application, sélectionnez ce dossier. Gardez le corrigé ailleurs. Si votre version accepte seulement des pièces jointes, transmettez les mêmes dix fichiers dans une nouvelle conversation. Nous voulons retrouver les documents produits et les sources utilisées ; le nom du mode n’a aucune valeur dans notre grille de vérification.

Ces gestes suivent les documentations consultées le 17 septembre 2026 ; les parcours d’interface restent à essayer dans votre version. Avant l’essai, vérifiez les fonctions accessibles et le compteur d’usage de votre compte. ChatGPT Work documente un usage de crédits pour le travail effectué ; Anthropic rattache Cowork à ses offres payantes. Aucun abonnement n’est nécessaire pour poursuivre le parcours local du tutoriel. Si vous possédez déjà un outil qui remplit nos trois conditions, commencez avec lui.

[^p7-work-fichiers]: OpenAI, [Get started with ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work) et [Work with files](https://learn.chatgpt.com/docs/artifacts-viewer), documentations consultées le 17 septembre 2026.
[^p7-claude-cowork]: Anthropic, [Claude Cowork](https://claude.com/product/cowork), présentation, accès et changement de nom consultés le 17 septembre 2026.
