Dans la partie 6, notre serveur MCP lisait des documents sur notre ordinateur. Cela ne décidait pas où tournait le modèle qui recevait ensuite les résultats. Nous retrouvons la même question avec une interface installée localement : ses fichiers sont chez nous, mais ses requêtes peuvent partir ailleurs.

Ouvrez `fiches/flux.md` et remplissez une ligne par trajet : de l’éditeur au modèle, de l’agent au serveur MCP, du serveur aux tickets, puis vers les éventuels journaux. Pour chaque trajet, notez ce qui passe, où cela arrive et ce qui vous permet de l’affirmer.

| Élément de notre atelier | Information que nous pouvons établir |
| --- | --- |
| Client documentaire de la partie 7 | Son code envoie la requête à `127.0.0.1:8080` |
| Réponse reçue | Le journal conserve le contexte transmis et la sortie |
| Assistant installé pour la partie 4 | Le trajet dépend du produit, de sa configuration et du fournisseur sélectionné |
| Politique d’un service externe | Elle doit être vérifiée pour ce service et l’offre utilisée |

« Non utilisé pour l’entraînement » ne signifie pas forcément « jamais conservé ». La rétention des journaux, l’accès de tiers et la localisation du traitement sont des questions distinctes. Il faut lire les engagements applicables plutôt que déduire toutes les réponses d’une seule option.

Pour notre exercice, restez sur les documents fictifs fournis. Une fois la carte des trajets dessinée, vous pourrez décider quelles données de votre propre projet seraient acceptables dans cette configuration.
