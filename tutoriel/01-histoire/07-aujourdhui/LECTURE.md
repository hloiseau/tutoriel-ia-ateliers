# 7. Où en sommes-nous aujourd’hui ?

[Sommaire de la partie](../README.md) · [Sources](.)

Les modèles génératifs deviennent aussi des composants de logiciels : on les associe à une recherche documentaire, à un éditeur de code ou à des outils capables d’agir sur des fichiers.

En parallèle, des équipes distribuent les paramètres de certains modèles. Il devient possible de les exécuter et parfois de les adapter sur ses propres machines, selon leurs conditions d’utilisation et le matériel disponible.

## Du modèle qui répond à l’agent qui utilise des outils

Supposons qu’un modèle produise la commande `pytest`. Pour qu’elle soit réellement exécutée, un programme autour de lui doit lire cette proposition, autoriser l’appel, lancer l’outil et lui transmettre le résultat.

Les travaux ReAct, publiés en 2022, étudient notamment l’association entre des étapes de raisonnement formulées par le modèle et des actions dans un environnement. Ils constituent un repère parmi les recherches qui conduisent aux agents fondés sur des modèles de langage.[^h7s1-react]

Voici un scénario fictif de consultation de documentation :

![Une demande est transmise au modèle ; l’application peut exécuter une recherche autorisée, transmettre son résultat au modèle, puis présenter une réponse.](../images/agent-outils.png)
Figure: Boucle simplifiée d’un agent utilisant un outil. L’application exécute les appels ; le modèle propose les actions et produit la réponse.

Suivez la boucle : le modèle demande une recherche, l’application l’exécute, puis le résultat revient dans les informations disponibles. Le modèle peut alors répondre ou demander autre chose.

Cela change les possibilités du système. Il peut consulter une information récente ou examiner un fichier qui n’était pas présent dans son entraînement. Cela ajoute aussi de nouvelles causes d’erreur : le mauvais outil peut être choisi, ses résultats mal interprétés ou une action proposée hors du périmètre attendu.

Nous appelons ici **agent** cette organisation capable d’enchaîner des décisions et des appels d’outils. Elle ne promet pas la réussite en solitaire : les droits, les limites et les vérifications font partie de son fonctionnement.


[^h7s1-react]: [Yao et ses collègues, ReAct (2022)](https://arxiv.org/abs/2210.03629).

## Les MCP et les skills trouvent leur place

En novembre 2024, Anthropic présente le **Model Context Protocol**, ou **MCP**. Le protocole vise à faciliter les échanges entre des applications utilisant des modèles et des serveurs qui exposent des ressources ou des outils.[^h7s2-mcp]

Pour reprendre notre exemple, un serveur peut proposer un outil de recherche documentaire. Le protocole aide l’application à le découvrir et à l’appeler. Le choix du bon moment et l’interprétation du résultat restent à la charge de l’agent — avec les erreurs que cela peut entraîner.

Les fichiers de consignes et les procédures réutilisables se développent également autour des agents. En 2025, Anthropic présente notamment les **Agent Skills**, des ensembles organisés de consignes, de ressources et éventuellement de scripts, chargés selon le travail à effectuer.[^h7s2-skills]

Les MCP et les skills organisent l’accès aux outils et les informations fournies à un agent. Ils agissent autour du modèle, sans reprendre son entraînement complet.

Une procédure de revue de code peut ainsi préciser ce qu’il faut examiner, tandis qu’un outil permet de lire les changements. Ce sont deux rôles différents, qui peuvent être combinés.

Les noms des fichiers, les fonctions disponibles et leur chargement varient selon les applications.


[^h7s2-mcp]: [Anthropic, Introducing the Model Context Protocol (25 novembre 2024)](https://www.anthropic.com/news/model-context-protocol).
[^h7s2-skills]: [Anthropic, Equipping agents for the real world with Agent Skills (2025)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

## Des modèles que l’on peut récupérer

En 2023, Meta présente LLaMA, puis Llama 2. Ces publications participent au développement d’un écosystème où les paramètres de modèles sont distribués, avec des conditions qui diffèrent selon les versions.[^h7s3-llama][^h7s3-llama2]

Les **poids** sont les nombres ajustés pendant l’entraînement. Les récupérer permet d’exécuter le modèle avec un logiciel compatible, si l’on dispose des ressources nécessaires. Cela donne plus de prise sur son fonctionnement que le seul accès à une interface distante.

Regardons précisément ce que l’on peut récupérer :

| Ce qui est disponible | Ce que cela permet d’examiner ou de faire |
| --- | --- |
| Une interface ou une API | Envoyer des demandes au service proposé |
| Les poids du modèle | Exécuter le modèle dans un environnement compatible |
| Le code d’entraînement | Examiner la procédure et éventuellement la réutiliser |
| Les données et leur documentation | Étudier les exemples utilisés et leurs conditions de collecte |
Table: Ces éléments peuvent être publiés séparément. Leur disponibilité ne donne pas automatiquement les mêmes droits d’utilisation.

Le mot « ouvert » mérite donc qu’on regarde ce qui est effectivement fourni. Avec des poids téléchargeables, les données peuvent rester inaccessibles et la licence peut encore limiter certains usages.

Des méthodes comme **LoRA**, présentée en 2021, permettent aussi d’adapter un modèle en entraînant un ensemble limité de paramètres supplémentaires. On peut ainsi réduire les ressources nécessaires à certaines adaptations, par rapport à la modification de tous les poids.[^h7s3-lora]

Faire tourner un modèle existant, l’adapter et en entraîner un depuis zéro sont trois travaux différents. Lorsqu’un programme de conversation répond avec un modèle déjà fourni, nous accomplissons le premier ; nous n’avons pas entraîné le modèle qui lui répond.

Le local peut nous donner davantage de maîtrise sur les données envoyées et sur la disponibilité de l’outil. Il ne règle pas, à lui seul, les questions sur l’origine des données d’entraînement ou les conditions de fabrication du matériel.


[^h7s3-llama]: [Touvron et ses collègues, LLaMA (2023)](https://arxiv.org/abs/2302.13971).
[^h7s3-llama2]: [Touvron et ses collègues, Llama 2 (2023)](https://arxiv.org/abs/2307.09288).
[^h7s3-lora]: [Hu et ses collègues, LoRA (2021)](https://arxiv.org/abs/2106.09685).

## 2025–2026 : davantage de calcul, davantage d’autonomie ?

En 2025, DeepSeek-R1 illustre l’importance prise par l’apprentissage par renforcement pour améliorer les performances de modèles de langage sur des tâches de raisonnement. Le rapport décrit aussi la diffusion de modèles adaptés et de versions plus petites issues de distillation.[^h7s4-r1model]

La **distillation** consiste à utiliser un modèle pour aider à en entraîner un autre, par exemple au moyen de réponses qu’il a produites. Réduire la précision des nombres stockés dans les poids porte un autre nom : la quantification.

Dans cette période, les systèmes peuvent consacrer davantage de calcul à une réponse, effectuer plusieurs étapes et utiliser des outils pour vérifier certains résultats. L’expérience ressemble moins à une simple complétion de phrase, même si la génération de texte reste un composant important.

Le rapport **AI Index 2026** de Stanford décrit des progrès sur différentes évaluations, mais aussi des capacités très inégales selon les tâches. Il souligne également la place de l’industrie, les questions de ressources et les difficultés à mesurer certains effets sociaux.[^h7s4-index]

Un score sur une épreuve ne résume donc pas tous les usages. Un système peut réussir une question difficile et échouer sur une manipulation qui nous semble banale. Dans votre projet, vos fichiers et vos contraintes constituent encore une autre épreuve.

Le rapport AI Index 2026 rassemble surtout des observations sur l’année précédente et des données disponibles au moment de sa publication.


[^h7s4-r1model]: [DeepSeek-AI, DeepSeek-R1 (2025)](https://arxiv.org/abs/2501.12948).
[^h7s4-index]: [Stanford HAI, AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report).

## Ce que cette histoire change pour nous

Les modèles dits **de fondation** sont entraînés sur de grandes quantités de données, puis adaptés à de nombreux usages. Un rapport de Stanford de 2021 examine les possibilités de cette organisation, mais aussi le risque de propager les mêmes défauts à de nombreuses applications et la concentration des moyens nécessaires.[^h7s5-foundation]

Pour un développeur, cette concentration a des conséquences concrètes. Une application peut dépendre d’un service dont les conditions, les prix ou les fonctionnalités changent. Pour une équipe, la question devient aussi celle du choix : peut-on changer de fournisseur, conserver ses données, exécuter une partie du travail ailleurs ?

Les logiciels libres et l’auto-hébergement offrent d’autres possibilités. Ils ont aussi leurs contraintes : du matériel à acheter, des mises à jour à gérer, des licences à examiner. À nous de choisir les dépendances que nous acceptons.

Si vous débutez en développement, une autre question est tout aussi importante : que voulez-vous apprendre vous-même ? Un programme terminé ne nous dit pas si vous savez expliquer le code, retrouver une erreur ou modifier son comportement.

Vous pouvez demander de l’aide pour comprendre un message d’erreur, puis essayer de résoudre le problème. Vous pouvez aussi confier toute la modification à un agent. Dans le second cas, il faut déjà savoir comment juger ce qu’il produit. Sinon, on risque de conserver une grosse réécriture là où une ligne aurait suffi, ou de laisser passer un bug parce que les tests produits semblent rassurants.

Les skills et les procédures peuvent organiser ce travail. Le temps passé à comprendre, relire, tester et valider reste dans la boucle.

Développer avec une IA reste un choix. Vous pouvez vouloir comprendre le sujet, expérimenter chez vous ou chercher une aide limitée à une tâche pénible, comme préparer des cas de test. Vous pouvez aussi vous en passer : c’est à l’outil de trouver sa place dans vos besoins.


[^h7s5-foundation]: [Bommasani et ses collègues, On the Opportunities and Risks of Foundation Models (2021)](https://arxiv.org/abs/2108.07258).

Les agents actuels associent des modèles entraînés, des règles et des outils. Derrière une même fenêtre de conversation, plusieurs approches issues de cette histoire continuent donc de cohabiter.
