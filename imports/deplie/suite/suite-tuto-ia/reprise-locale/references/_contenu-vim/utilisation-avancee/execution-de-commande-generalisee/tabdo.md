Tout comme `:bufdo` et `:wondo`, la commande `:tabdo` exécute une commande dans tous les onglets ouverts.

[[attention]]
| Le type de commande que nous allons exécuter dans les onglets est différent. Un onglet est très différent d'un buffer ou d'une fenêtre.

Effectivement, que contient un onglet ? Il contient une ou plusieurs fenêtres.  
Les commandes qui suivent `:tabdo` vont être des commandes de manipulation ou de déplacement de fenêtre ou entre fenêtres.

Par exemple, si l'on a plusieurs onglets, qui, chacun ont deux fenêtres ouvertes et séparées verticalement comme suit:

->![](/media/galleries/11359/200d2bbe-efcf-4a09-bef3-f53c608ec0a2.png)<-

Nous pouvons faire la commande `:tabdo wincmd l` pour déplacer le curseur dans la fenêtre de droite **dans tous les onglets**.

[[secret]]
| Je n'explique pas la commande `:wincmd` mais vous pouvez trouver les informations correspondantes avec la commande `:h wincmd`

[[information]]
| Si un onglet n'est pas découpé de la même manière, ou qu'un onglet ne possède qu'une fenêtre, Vim ne donnera pas d'erreur, il restera silencieux.