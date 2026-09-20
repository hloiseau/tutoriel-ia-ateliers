Nous allons sélectionner des passages, les joindre à une question et demander au modèle de répondre avec ces sources. On parle souvent de **RAG**, pour *Retrieval-Augmented Generation*, ou génération augmentée par recherche documentaire.[^p7-rag]

![Le corpus alimente un index ; la question sert à choisir les passages, puis le modèle reçoit la question et les sources sélectionnées.](image:images/recherche.png)
Figure: Retrouver des sources avant de générer une réponse

Dans notre application, cet appel ne déclenche aucun entraînement. Nous changeons le contexte transmis à chaque question, tandis que les poids restent identiques. Redémarrez sans joindre les documents : le modèle ne saura pas soudain retrouver la règle de notification.

Un serveur MCP pourrait exposer cette recherche comme outil, à la manière de `chercher_documentation` dans la partie 6. Le programme placé derrière l’outil garderait la responsabilité de découper et classer les passages.

Avec dix paragraphes, nous pouvons commencer par une recherche que nous savons lire de bout en bout. Nous verrons son premier échec avant d’envisager une base vectorielle.

[^p7-rag]: Lewis et al., [*Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*](https://arxiv.org/abs/2005.11401). Notre application utilise une recherche lexicale simple ; elle ne reproduit pas le système entraîné dans cet article.
