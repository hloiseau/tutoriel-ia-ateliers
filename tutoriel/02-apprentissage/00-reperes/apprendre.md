Imaginez que nous voulions reconnaître des chiffres manuscrits. Nous pouvons montrer à un programme des images accompagnées de la réponse attendue, comparer ses prédictions aux étiquettes et modifier ses paramètres pour réduire les erreurs. Les paramètres sont des nombres qui participent au calcul ; leur ensemble fait partie de ce que nous appelons un **modèle**.

Ce travail d’ajustement est l’**entraînement**. Il faut ensuite essayer le modèle sur des exemples qui n’ont pas servi à l’ajuster. S’il ne reconnaît que les images déjà rencontrées, il nous servira assez peu pour lire notre prochain dessin. Les ateliers de cette partie montreront ces calculs sur de petites images.

Lorsque nous utilisons ensuite le modèle pour obtenir une réponse, nous réalisons une **inférence**. Les paramètres appris participent au calcul de cette réponse. Une conversation ordinaire ne les réentraîne pas à chaque message : ajouter un document au contexte et modifier le modèle sont deux opérations différentes. Le service peut, par ailleurs, conserver des conversations ou proposer une mémoire ; cela dépend de ses fonctions et de ses conditions d’usage.

![Des exemples et une comparaison ajustent les paramètres pendant l’entraînement. À l’usage, une demande et du contexte passent par le modèle pour produire une réponse.](image:images/entrainement-usage.png)
Figure: Entraîner le modèle et utiliser ses paramètres pour répondre

Les modèles de langage apprennent à partir de textes, et certains modèles utilisent également des images, du son ou d’autres données. Leur entraînement peut comprendre plusieurs étapes, dont des ajustements à partir d’exemples de réponses et de préférences humaines. Nous verrons ensuite comment fabriquer une version minuscule d’un modèle de langage. Elle nous permettra de manipuler le principe sans télécharger un centre de données dans le salon.

Pour les tâches de travail, retenez surtout cette conséquence : fournir les notes de votre réunion donne au modèle des informations à utiliser pour cette demande. Cela ne prouve ni qu’il les retrouvera la semaine suivante, ni qu’elles sont devenues une connaissance fiable enregistrée dans ses paramètres.
