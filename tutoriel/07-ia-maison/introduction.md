**TL;DR** — Nous allons retrouver des documents pour répondre à des questions, construire une petite application locale, puis adapter et entraîner un modèle de caractères. Les essais nous permettront aussi de voir ce qui ne fonctionne pas.

Dans la partie précédente, nous avons donné des outils et une procédure à notre agent. Ses poids, eux, n’ont pas changé. Peut-on aller plus loin et fabriquer quelque chose qui corresponde davantage à nos besoins ? Oui, mais « faire son IA » peut désigner des travaux très différents.

Pour commencer, nous allons aider un modèle à retrouver les informations de notre service de prix. Ensuite, nous regarderons ce qui se passe quand on modifie réellement les paramètres d’un réseau. Nous utiliserons alors un modèle minuscule, dont le code et les poids sont fournis : on pourra le réentraîner sur CPU sans attendre une nuit entière.

La recherche et l’entraînement de ce petit modèle ne demandent ni service payant ni carte graphique. La génération documentaire réutilise le serveur local de la partie 3. Une expérience avec un LLM plus grand sur GPU sera préparée séparément ; une RTX 3090 Ti n’est pas un prérequis pour suivre cette partie.

Nous garderons des résultats observables : les passages trouvés, les réponses réellement produites, les poids modifiés et les erreurs conservées. C’est nettement plus utile qu’un nom de modèle qui finit par « expert ». 🙂
