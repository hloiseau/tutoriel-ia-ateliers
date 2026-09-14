La durée commence juste avant l’envoi de la requête et s’arrête après la réception de sa réponse complète. Elle inclut donc le traitement de l’entrée, la génération et les échanges avec le serveur local. Elle n’inclut pas le téléchargement ni le démarrage du moteur.

Quand le serveur fournit le nombre de tokens produits, le script le divise par cette durée. La colonne s’appelle volontairement `tokens_sortie_par_seconde_globale`. **Ce n’est pas le débit du seul décodage** que certains outils affichent dans leurs journaux.

Prenons un calcul indépendant de notre machine : si un appel produit 60 tokens en 3 secondes, ce rapport vaut 20 tokens par seconde. Cela ne nous apprend pas combien de temps s’est écoulé avant le premier token. Deux installations peuvent avoir le même rapport global et donner une impression différente dans une interface qui affiche progressivement le texte.

Regardez aussi la longueur et la raison d’arrêt. Une réponse plus courte peut arriver plus vite sans que le moteur calcule plus vite. Une réponse vide serait même redoutablement efficace au chronomètre… et assez peu utile. 😅

Le programme affiche la médiane des trois durées. Trois essais suffisent à repérer une différence grossière, pas à annoncer une supériorité universelle. Gardez les valeurs individuelles au lieu de conserver uniquement celle qui vous arrange.
