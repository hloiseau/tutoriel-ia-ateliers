Nous l'avons vu précédemment, on peut réassigner un marque-page quand on le souhaite cependant nous cela remplace son contenu. On pourrait ouvrir notre fichier `.viminfo` et supprimer la ligne à la main.  
Il est déconseillé de faire cela car on pourrait corrompre le formatage du fichier.

À la place, pour supprimer un marque-page on utilise la commande `:delmarks` (ou `:delm`) suivi du nom du (ou des) marque-page(s) que l'on souhaite supprimer.  
On peut supprimer plusieurs marque-pages d'un coup. Par exemple si on veut supprimer les marque-pages de `P` à `Z` on utilisera la commande `:delm P-Z`.  
De manière similaire, si on veut supprimer tous les marque-pages en lien avec un fichier on peut faire la commande `:delm a-z`, cependant on peut faire plus court. La commande `:delm!` est équivalente.