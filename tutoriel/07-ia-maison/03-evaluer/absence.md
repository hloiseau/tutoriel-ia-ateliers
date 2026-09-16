Il y a deux cas à distinguer dans nos documents. Pour l’horaire de staging, la réponse existe mais peut être mal retrouvée. Pour la temporisation de PRIX-2, le document est trouvé et dit précisément que la durée reste à décider.

Dans le premier cas, notre application peut seulement dire « aucun passage retrouvé » : le document est bien là, hors de portée de cette formulation. Dans le second, le passage remonte et la réponse attendue est une décision ouverte. Ajouter un nombre pour remplir la phrase contredirait la source.

Un seuil de recherche ne tranche pas cette différence. Un score élevé peut rapprocher une question d’un paragraphe qui décrit le problème sans donner la solution. C’est ce qui rend utile le champ `reponse_attendue` du jeu de questions : un humain peut comparer le sens de la réponse aux sources.

Gardez également les questions auxquelles le système devrait s’abstenir. Un jeu rempli uniquement de réponses présentes dans le corpus passerait sous silence son comportement lorsque les documents sont insuffisants.
