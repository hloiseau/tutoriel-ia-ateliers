Copiez `questions/premiere.json` vers `questions/historique-absent.json`. Dans cette copie, gardez seulement un message `user` avec la question : « Quelle était ma question précédente ? », puis lancez :

```bash
python client.py --fichier questions/historique-absent.json --sortie resultats/historique-absent.json
```

Ouvrez `resultats/historique-absent.json` et regardez la partie `requete` : elle contient la nouvelle question, sans la précédente. Le modèle peut tout de même improviser une réponse, mais notre trace montre qu’il n’a reçu aucun historique. Le serveur traite uniquement les messages présents dans le fichier envoyé par le client.

![Deux requêtes indépendantes ; la seconde n’inclut un historique que si le client le transmet](image:images/historique.png)
Figure: L’historique est constitué par le programme qui prépare la demande

Pour poursuivre réellement l’échange, il faut envoyer les messages précédents et la nouvelle question. Les interfaces de discussion s’en chargent généralement pour nous, avec leurs propres choix de conservation, de résumé ou de suppression.

Le **cache de calcul** joue un autre rôle. Le moteur peut réutiliser des calculs pour accélérer le traitement d’un texte déjà rencontré, mais le cache n’ajoute pas à la requête les anciens messages. L’historique dépend toujours du programme qui prépare la liste envoyée.

Chaque ajout prend de la place dans le contexte et peut ramener des instructions anciennes, des détails devenus inutiles ou des contradictions. Un bon historique contient les éléments nécessaires à la suite de l’échange, pas forcément toutes les archives disponibles.
