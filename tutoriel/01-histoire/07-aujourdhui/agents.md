Supposons qu’un modèle produise la commande `pytest`. Pour qu’elle soit réellement exécutée, un programme autour de lui doit lire cette proposition, autoriser l’appel, lancer l’outil et lui transmettre le résultat.

Les travaux ReAct, publiés en 2022, étudient notamment l’association entre des étapes de raisonnement formulées par le modèle et des actions dans un environnement. Ils constituent un repère parmi les recherches qui conduisent aux agents fondés sur des modèles de langage.[^h7s1-react]

Voici un scénario fictif de consultation de documentation :

![Une demande est transmise au modèle ; l’application peut exécuter une recherche autorisée, transmettre son résultat au modèle, puis présenter une réponse.](image:images/agent-outils.png)
Figure: Boucle simplifiée d’un agent utilisant un outil. L’application exécute les appels ; le modèle propose les actions et produit la réponse.

Suivez la boucle : le modèle demande une recherche, l’application l’exécute, puis le résultat revient dans les informations disponibles. Le modèle peut alors répondre ou demander autre chose.

Cela change les possibilités du système. Il peut consulter une information récente ou examiner un fichier qui n’était pas présent dans son entraînement. Cela ajoute aussi de nouvelles causes d’erreur : le mauvais outil peut être choisi, ses résultats mal interprétés ou une action proposée hors du périmètre attendu.

Nous appelons ici **agent** cette organisation capable d’enchaîner des décisions et des appels d’outils. Elle ne promet pas la réussite en solitaire : les droits, les limites et les vérifications font partie de son fonctionnement.


[^h7s1-react]: [Yao et ses collègues, ReAct (2022)](https://arxiv.org/abs/2210.03629).
