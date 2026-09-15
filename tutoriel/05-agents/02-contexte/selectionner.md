Pour expliquer une condition, la fonction et les valeurs d’entrée suffisent souvent. Pour modifier son comportement, il faut aussi la règle attendue, les appels concernés et les tests. Ce qui est utile dépend donc de l’action demandée.

![Le contexte de lecture contient un extrait et un cas ; le contexte de modification ajoute le ticket et les tests concernés](image:images/contexte.png)
Figure: Le contexte change avec la tâche

Essayez de préparer vous-même les informations pour cette demande : « ajoute un test du retour en stock avec hausse ». Il faut notamment retrouver l’objet `Etat`, la fonction appelée, la façon dont les tests sont écrits et le résultat attendu. Les anciens échanges sur la couleur d’un bouton ne servent pas ici.

On peut alléger une recherche en demandant d’abord les noms des fichiers concernés, puis en ouvrant ceux qui nous intéressent. De même, une sortie de commande peut commencer par le nom du test en échec et sa trace, au lieu de recopier des milliers de lignes réussies. Gardez cependant le journal complet accessible si le résumé masque la cause de l’erreur.

**Réduire le contexte ne consiste pas à couper au hasard.** Une signature sans ses conventions, ou un message d’erreur sans la commande qui l’a produit, peut faire perdre précisément l’information dont le modèle avait besoin.
