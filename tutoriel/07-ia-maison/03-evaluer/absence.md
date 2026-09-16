Il y a deux cas à distinguer dans nos documents. Pour l’horaire de staging, la réponse existe mais peut être mal retrouvée. Pour la temporisation de PRIX-2, le document est trouvé et dit précisément que la durée reste à décider.

Notre application pourra dire « aucun passage retrouvé » dans le premier cas. Elle ne devrait pas transformer cela en « cette information n’existe pas ». Dans le second cas, la réponse attendue est une décision ouverte, pas un nombre choisi pour remplir la phrase.

Un seuil de recherche ne tranche pas cette différence. Un score élevé peut rapprocher une question d’un paragraphe qui décrit le problème sans donner la solution. C’est ce qui rend utile le champ `reponse_attendue` du jeu de questions : un humain peut comparer le sens de la réponse aux sources.

Gardez également les questions auxquelles le système devrait s’abstenir. Tester seulement les réponses présentes dans le corpus ne nous apprendrait pas comment il se comporte lorsque les documents sont insuffisants.
