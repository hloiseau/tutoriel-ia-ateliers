# 6. Des transformers à l’IA générative

[Sommaire de la partie](../README.md) · [Sources](.)

Reconnaître une image et produire une image sont deux tâches différentes. De même, classer un texte ne suffit pas à savoir rédiger une réponse.

Dans les années 2010 et 2020, les modèles génératifs prennent une place de plus en plus importante. Ils deviennent capables de produire du texte, des images ou du code à partir d’une demande.

## 2017 : les transformers

En 2017, une équipe de chercheurs publie *Attention Is All You Need*. L’article présente une architecture appelée **transformer**, étudiée notamment pour la traduction automatique.[^h6s1-attention]

L’un de ses mécanismes essentiels est l’**attention** : il permet de combiner des informations venant de différentes positions d’une séquence. Prenons cette phrase :

> Le chat poursuit la souris parce qu’elle a volé son fromage.

Pour interpréter « elle », le contexte est utile. Un mécanisme d’attention permet au calcul effectué à une position de tenir compte d’autres éléments de la phrase. Les paramètres qui organisent ces calculs sont appris ; personne n’a écrit une règle « elle désigne toujours la souris ».

![Le mot « elle » est relié à plusieurs éléments de la phrase ; les liens illustrent l’accès au contexte et ne représentent pas des poids mesurés.](../images/attention.png)
Figure: Illustration du rôle du contexte. Les liens ne proviennent pas de l’analyse d’un modèle réel.

Les transformers permettent notamment de paralléliser une partie des calculs d’entraînement qui étaient séquentiels dans les réseaux récurrents. Leur architecture va être reprise et adaptée à de nombreuses tâches.


[^h6s1-attention]: [Vaswani et ses collègues, Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762).

## Prédire la suite d’un texte

Les modèles de langage attribuent des probabilités aux suites de texte. Dans un modèle qui génère de gauche à droite, on peut produire une réponse en choisissant un élément, en l’ajoutant au contexte, puis en recommençant.

Ces éléments sont appelés **tokens**. Selon le système utilisé, un token peut correspondre à un mot, un morceau de mot, un signe de ponctuation ou une autre unité de texte.

Prenons la phrase : « Pour ouvrir le fichier, cliquez sur… ». Plusieurs suites sont possibles. Le modèle calcule lesquelles sont plausibles dans ce contexte, puis la méthode de génération en sélectionne une. Le choix peut dépendre de réglages qui rendent les réponses plus ou moins variées.

En 2020, l’article sur GPT-3 montre qu’un grand modèle de langage peut accomplir différentes tâches à partir d’instructions et de quelques exemples placés dans son entrée, sans modifier ses paramètres pour chaque demande.[^h6s2-gpt3]

Par exemple, nous pouvons montrer le format d’une traduction, puis demander d’en produire une nouvelle. Ce travail à partir du contexte ne doit pas être confondu avec un nouvel entraînement du modèle.

Une suite convaincante peut contenir une erreur : le programme ne consulte pas nécessairement une fiche vérifiée pour chaque phrase qu’il écrit. Lisons donc la fluidité du texte et son exactitude comme deux propriétés séparées.


[^h6s2-gpt3]: [Brown et ses collègues, Language Models are Few-Shot Learners (2020)](https://arxiv.org/abs/2005.14165).

## 2022 : rendre ces modèles plus faciles à utiliser

Un modèle entraîné à poursuivre du texte ne répond pas forcément comme un assistant. Il peut continuer une question, changer de sujet ou produire un format inattendu.

Des étapes supplémentaires d’entraînement servent à orienter son comportement. L’article sur InstructGPT décrit notamment l’utilisation de démonstrations humaines, de comparaisons entre réponses et d’apprentissage à partir de ces préférences. On rencontre souvent le sigle **RLHF**, pour *Reinforcement Learning from Human Feedback*.[^h6s3-rlhf]

Le travail humain intervient donc à plusieurs moments. Certaines personnes écrivent des exemples ; d’autres comparent ou évaluent des réponses. Le choix de ce qui est considéré comme utile, acceptable ou correct influence le résultat.

Le 30 novembre 2022, OpenAI rend ChatGPT accessible sous la forme d’une conversation. Cette interface permet d’essayer le système en écrivant une demande, puis en poursuivant l’échange.[^h6s3-chatgpt]

Il devient plus facile d’explorer ses possibilités sans préparer soi-même un programme autour du modèle. On peut demander une reformulation, préciser un point ou proposer une correction. Cela contribue à faire connaître les modèles génératifs bien au-delà des équipes qui les développaient.

L’interface masque toutefois une partie du fonctionnement. Un utilisateur voit une zone de texte et une réponse ; il ne voit pas directement les données d’entraînement, les étapes d’adaptation ni les règles de l’application.


[^h6s3-rlhf]: [Ouyang et ses collègues, Training language models to follow instructions with human feedback (2022)](https://arxiv.org/abs/2203.02155).
[^h6s3-chatgpt]: [OpenAI, Introducing ChatGPT (30 novembre 2022)](https://openai.com/index/chatgpt/).

## Générer aussi des images

La génération d’images suit également plusieurs pistes. En 2014, les **GAN**, ou réseaux antagonistes génératifs, proposent d’entraîner deux modèles ensemble : l’un produit des exemples, l’autre cherche à distinguer ces productions des données utilisées pour l’entraînement.[^h6s4-gan]

Vous pouvez imaginer un dessinateur et un examinateur, à condition de garder en tête qu’il s’agit de calculs. Le générateur est ajusté pour produire des exemples qui trompent davantage l’autre modèle ; celui-ci est ajusté pour mieux les distinguer.

Les **modèles de diffusion** suivent une autre idée. Une famille de méthodes apprend à inverser progressivement un processus d’ajout de bruit. Les travaux de Ho, Jain et Abbeel en 2020 constituent un repère important de cette approche.[^h6s4-diffusion]

![Une forme devient progressivement bruitée ; une flèche inverse illustre le principe d’un débruitage appris.](../images/diffusion.png)
Figure: Illustration du bruit ajouté à une forme. La rangée ne représente pas les sorties d’un modèle entraîné ; elle sert à expliquer le principe.

Sur l’image, la forme devient de moins en moins visible quand on ajoute du bruit. Pendant l’apprentissage, le modèle est entraîné à estimer comment revenir vers des données moins bruitées. Lors de la génération, des méthodes utilisent cette capacité pour construire progressivement une image à partir de bruit.

Les versions guidées par du texte ajoutent des informations sur ce que l’on souhaite obtenir. On ne peut donc pas résumer toute la génération d’images à un modèle qui choisit le prochain mot.


[^h6s4-gan]: [Goodfellow et ses collègues, Generative Adversarial Networks (2014)](https://arxiv.org/abs/1406.2661).
[^h6s4-diffusion]: [Ho, Jain et Abbeel, Denoising Diffusion Probabilistic Models (2020)](https://arxiv.org/abs/2006.11239).

## Des données à grande échelle, avec leurs problèmes

Pour entraîner les modèles de langage, les équipes rassemblent de grandes quantités de textes. Les choix de collecte, de filtrage et de langues influencent ce que le modèle rencontre.

Une étude de 2021 consacrée au corpus C4 montre l’importance de documenter ces choix. Les auteurs examinent notamment les sources du texte et les effets de certains filtres, qui peuvent écarter des contenus de manière inégale.[^h6s5-c4]

Cela pose des questions qui ne sont pas seulement techniques. Qui a écrit les textes ? Dans quel contexte étaient-ils accessibles ? Les personnes concernées souhaitaient-elles participer à cet entraînement ? Quelles langues et quels points de vue sont moins présents ?

Un texte accessible sur le Web n’est pas, pour cette seule raison, un texte sans auteur ou sans conditions d’utilisation. Les grands modèles reposent sur des ressources et du travail qui viennent de nombreuses personnes.

À partir de 2023, des modèles comme GPT-4 prennent aussi en entrée plusieurs types de données, notamment du texte et des images. On parle de modèles **multimodaux**. Le rapport technique de GPT-4 indique cependant qu’il ne donne pas tous les détails de l’architecture et de l’entraînement.[^h6s5-gpt4]

Quelques secondes suffisent pour essayer l’outil dans une interface. Examiner sa fabrication demande beaucoup plus d’informations.


[^h6s5-c4]: [Dodge et ses collègues, Documenting Large Webtext Corpora (2021)](https://arxiv.org/abs/2104.08758).
[^h6s5-gpt4]: [OpenAI, GPT-4 Technical Report (2023)](https://arxiv.org/abs/2303.08774).

L’IA générative devient un outil avec lequel le public peut interagir directement. Mais un modèle capable de produire du texte n’est encore qu’une partie d’un agent qui consulte des fichiers, lance des outils et réalise une tâche en plusieurs étapes.

C’est cette évolution, ainsi que les possibilités de faire fonctionner des modèles soi-même, qui nous amène jusqu’aux usages actuels.
