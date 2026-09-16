Nous allons sélectionner des passages, les joindre à une question et demander au modèle de répondre avec ces sources. On parle souvent de **RAG**, pour *Retrieval-Augmented Generation*, ou génération augmentée par recherche documentaire.[^p7-rag]

![Le corpus alimente un index ; la question sert à choisir les passages, puis le modèle reçoit la question et les sources sélectionnées.](image:images/recherche.png)
Figure: Retrouver des sources avant de générer une réponse

Dans notre application, cet appel ne déclenche aucun entraînement. Le contexte transmis change, les poids restent identiques. Si nous redémarrons sans joindre les documents, ils ne sont pas devenus une connaissance acquise par le modèle.

MCP pourrait exposer notre recherche comme outil, de la même manière que `chercher_documentation` dans la partie 6. Le protocole ne choisirait pas pour autant la méthode de classement des passages : cette méthode appartient au programme derrière l’outil.

Commençons avec peu de documents et une recherche que nous pouvons lire. Une base vectorielle n’est pas un passage obligé pour retrouver dix paragraphes.

[^p7-rag]: Lewis et al., [*Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*](https://arxiv.org/abs/2005.11401). Notre application utilise une recherche lexicale simple ; elle ne reproduit pas le système entraîné dans cet article.
