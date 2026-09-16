**TL;DR** — Nous allons retrouver des documents pour répondre à des questions, construire une petite application locale, puis adapter et entraîner un modèle de caractères. À chaque étape, nous garderons aussi les ratés : ce sont eux qui montrent où intervenir.

Dans la partie précédente, nous avons donné des outils et une procédure à notre agent. Ses poids sont restés intacts. Si nous voulons maintenant fabriquer quelque chose qui corresponde davantage à nos besoins, encore faut-il préciser ce que nous voulons changer : « faire son IA » recouvre des travaux très différents.

Nous commencerons par aider un modèle à retrouver les informations de notre service de prix. Puis nous modifierons réellement les paramètres d’un réseau minuscule, dont le code et les poids sont fournis. Il tient sur CPU et s’entraîne assez vite pour que nous puissions recommencer, comparer et lire les sorties sans y passer la nuit.

La recherche et l’entraînement de ce petit modèle ne demandent ni service payant ni carte graphique. Pour la génération documentaire, nous réutiliserons le serveur local de la partie 3. L’adaptation d’un LLM plus grand sur RTX 3090 Ti reste une expérience à mener séparément ; aucun résultat GPU n’est supposé dans cette partie.

Nous garderons des résultats observables : les passages trouvés, les réponses réellement produites, les poids modifiés et les erreurs conservées. C’est nettement plus utile qu’un nom de modèle qui finit par « expert ». 🙂
