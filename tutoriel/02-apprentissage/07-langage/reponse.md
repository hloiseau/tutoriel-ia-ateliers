Notre bigramme produit du texte. Notre calcul d’attention combine des vecteurs. Nous n’avons pourtant pas un programme capable de répondre utilement à une demande.

Pour entraîner un modèle de langage autorégressif, on peut lui fournir une séquence et lui demander de prédire les tokens suivants. Le texte fournit alors lui-même une cible d’apprentissage : nul besoin d’écrire manuellement une étiquette pour chaque caractère. On parle notamment d’apprentissage **auto-supervisé**.

Un modèle préentraîné à poursuivre du texte peut ensuite être adapté avec des exemples de consignes et de réponses, ainsi qu’avec d’autres méthodes d’optimisation. Les travaux sur InstructGPT illustrent cette distinction entre le préentraînement et l’entraînement destiné à mieux suivre des instructions.[^p2-7-reponse-instructions]

La prédiction de la suite produit parfois une réponse utile, parfois une formule familière ou un dialogue qui part dans la mauvaise direction. La capacité à suivre une consigne se travaille et s’évalue comme un usage à part entière.

Et une réponse bien écrite peut être fausse. Nous avons déjà vu notre classifieur produire une mauvaise réponse avec un score élevé. Pour le langage, les erreurs prennent d’autres formes : une référence inexistante, une explication plausible mais incorrecte, une API inventée.

Nous n’avons pas mesuré les erreurs des grands modèles avec notre corpus de mille caractères. L’expérience rend seulement visibles deux mécanismes que l’on retrouve chez eux : produire une sortie à partir d’un contexte et sélectionner des possibilités selon des scores. Leur fiabilité doit ensuite être évaluée sur la tâche qui nous intéresse.


[^p2-7-reponse-instructions]: [Ouyang et ses collègues, Training language models to follow instructions with human feedback (2022)](https://arxiv.org/abs/2203.02155).
