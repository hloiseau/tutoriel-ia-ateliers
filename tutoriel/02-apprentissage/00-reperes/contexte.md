Un modèle de langage traite le texte sous forme de **tokens** : des unités qui peuvent correspondre à un mot, à une partie de mot ou à un signe. Lorsqu’il génère une réponse, il calcule progressivement la suite à partir de ce qui lui a été fourni et de ce qu’il a déjà produit. Ce mécanisme peut servir à rédiger, traduire, expliquer une erreur ou extraire des informations.

Le **contexte** est l’ensemble des éléments disponibles pour cette réponse : consignes, messages, passages de documents, résultats d’outils… Il a une taille limitée. Un assistant peut sélectionner ou résumer ce qu’il y place. Un fichier joint à une conversation n’implique donc pas que tous ses passages aient participé à chaque réponse, avec le même niveau de détail.

Reprenons un exemple fictif. Une note dit « atelier le 10 octobre », une autre « affiche datée du 17 octobre ». Si nous ne fournissons que la première, l’assistant n’aura pas cette contradiction sous les yeux. Si nous fournissons les deux, il peut la relever ; il peut aussi passer à côté. Nous devrons vérifier ce qu’il a retenu avant d’annoncer une date.

Une consigne utile précise le travail, les sources, le résultat attendu et les décisions à laisser ouvertes. « Prépare un point à partir de ces deux comptes rendus ; indique les dates contradictoires avec leur source » donne une tâche plus exploitable que « sois très rigoureux ».

Le même principe sert en développement. Pour corriger une fonction, il faut connaître son comportement attendu, le code concerné et les cas que l’on veut conserver. Ajouter tout le dépôt sans expliquer le problème peut produire beaucoup de lecture et peu de progrès.
