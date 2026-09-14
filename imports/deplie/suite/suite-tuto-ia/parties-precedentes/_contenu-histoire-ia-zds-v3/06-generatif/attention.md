En 2017, une équipe de chercheurs publie *Attention Is All You Need*. L’article présente une architecture appelée **transformer**, étudiée notamment pour la traduction automatique.[^h6s1-attention]

L’un de ses mécanismes essentiels est l’**attention** : il permet de combiner des informations venant de différentes positions d’une séquence. Prenons cette phrase :

> Le chat poursuit la souris parce qu’elle a volé son fromage.

Pour interpréter « elle », le contexte est utile. Un mécanisme d’attention permet au calcul effectué à une position de tenir compte d’autres éléments de la phrase. Cela ne signifie pas qu’on lui a écrit une règle « elle désigne toujours la souris » : les paramètres qui organisent ces calculs sont appris.

![Le mot « elle » est relié à plusieurs éléments de la phrase ; les liens illustrent l’accès au contexte et ne représentent pas des poids mesurés.](image:images/attention.png)
Figure: Illustration du rôle du contexte. Les liens ne proviennent pas de l’analyse d’un modèle réel.

Les transformers permettent notamment de paralléliser une partie des calculs d’entraînement qui étaient séquentiels dans les réseaux récurrents. Leur architecture va être reprise et adaptée à de nombreuses tâches.


[^h6s1-attention]: [Vaswani et ses collègues, Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762).
