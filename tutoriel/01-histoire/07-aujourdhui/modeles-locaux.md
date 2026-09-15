En 2023, Meta présente LLaMA, puis Llama 2. Ces publications participent au développement d’un écosystème où les paramètres de modèles sont distribués, avec des conditions qui diffèrent selon les versions.[^h7s3-llama][^h7s3-llama2]

Les **poids** sont les nombres ajustés pendant l’entraînement. Les récupérer permet d’exécuter le modèle avec un logiciel compatible, si l’on dispose des ressources nécessaires. Cela donne plus de prise sur son fonctionnement que le seul accès à une interface distante.

Il faut cependant distinguer plusieurs choses :

| Ce qui est disponible | Ce que cela permet d’examiner ou de faire |
| --- | --- |
| Une interface ou une API | Envoyer des demandes au service proposé |
| Les poids du modèle | Exécuter le modèle dans un environnement compatible |
| Le code d’entraînement | Examiner la procédure et éventuellement la réutiliser |
| Les données et leur documentation | Étudier les exemples utilisés et leurs conditions de collecte |
Table: Ces éléments peuvent être publiés séparément. Leur disponibilité ne donne pas automatiquement les mêmes droits d’utilisation.

Le mot « ouvert » mérite donc qu’on regarde ce qui est effectivement fourni. Des poids téléchargeables ne signifient pas nécessairement que toutes les données sont accessibles ou que tous les usages sont autorisés.

Des méthodes comme **LoRA**, présentée en 2021, permettent aussi d’adapter un modèle en entraînant un ensemble limité de paramètres supplémentaires. On peut ainsi réduire les ressources nécessaires à certaines adaptations, par rapport à la modification de tous les poids.[^h7s3-lora]

Faire tourner un modèle existant, l’adapter et en entraîner un depuis zéro sont trois travaux différents. Avoir installé un programme de conversation ne veut pas dire que nous avons entraîné le modèle qui lui répond.

Le local peut nous donner davantage de maîtrise sur les données envoyées et sur la disponibilité de l’outil. Il ne règle pas, à lui seul, les questions sur l’origine des données d’entraînement ou les conditions de fabrication du matériel.


[^h7s3-llama]: [Touvron et ses collègues, LLaMA (2023)](https://arxiv.org/abs/2302.13971).
[^h7s3-llama2]: [Touvron et ses collègues, Llama 2 (2023)](https://arxiv.org/abs/2307.09288).
[^h7s3-lora]: [Hu et ses collègues, LoRA (2021)](https://arxiv.org/abs/2106.09685).
