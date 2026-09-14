Les modèles de langage attribuent des probabilités aux suites de texte. Dans un modèle qui génère de gauche à droite, on peut produire une réponse en choisissant un élément, en l’ajoutant au contexte, puis en recommençant.

Ces éléments sont appelés **tokens**. Selon le système utilisé, un token peut correspondre à un mot, un morceau de mot, un signe de ponctuation ou une autre unité de texte.

Prenons la phrase : « Pour ouvrir le fichier, cliquez sur… ». Plusieurs suites sont possibles. Le modèle calcule lesquelles sont plausibles dans ce contexte, puis la méthode de génération en sélectionne une. Le choix peut dépendre de réglages qui rendent les réponses plus ou moins variées.

En 2020, l’article sur GPT-3 montre qu’un grand modèle de langage peut accomplir différentes tâches à partir d’instructions et de quelques exemples placés dans son entrée, sans modifier ses paramètres pour chaque demande.[^h6s2-gpt3]

Par exemple, nous pouvons montrer le format d’une traduction, puis demander d’en produire une nouvelle. Ce travail à partir du contexte ne doit pas être confondu avec un nouvel entraînement du modèle.

Le programme ne consulte pas nécessairement une fiche vérifiée pour chaque phrase qu’il écrit. Il peut produire une suite convaincante qui contient une erreur. La fluidité du texte et son exactitude doivent donc être examinées séparément.


[^h6s2-gpt3]: [Brown et ses collègues, Language Models are Few-Shot Learners (2020)](https://arxiv.org/abs/2005.14165).
