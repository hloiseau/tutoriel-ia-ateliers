Modifiez maintenant une question pour demander : « Quelle était ma question précédente ? » Lancez-la dans un nouveau fichier de messages.

Notre client n’ajoute aucun historique automatiquement. Le serveur reçoit uniquement les messages présents dans ce fichier. Il ne suffit donc pas que nous ayons parlé au même processus quelques secondes plus tôt pour que la nouvelle demande contienne l’ancienne conversation.

![Deux requêtes indépendantes ; la seconde n’inclut un historique que si le client le transmet](image:images/historique.png)
Figure: L’historique est constitué par le programme qui prépare la demande

Pour poursuivre réellement l’échange, il faut envoyer les messages précédents et la nouvelle question. Les interfaces de discussion s’en chargent généralement pour nous, avec leurs propres choix de conservation, de résumé ou de suppression.

Il faut aussi distinguer cet historique d’un **cache de calcul**. Un moteur peut réutiliser des calculs pour accélérer le traitement d’un texte déjà rencontré. Cela ne lui donne pas une autorisation d’inventer des messages absents de la requête, ni une mémoire personnelle permanente.

Plus nous ajoutons de texte, plus il faut de place pour le traiter. Et ce texte peut contenir des instructions anciennes, des détails devenus inutiles ou des contradictions. Donner toutes ses archives au modèle n’est donc pas toujours une bonne façon de l’aider.
