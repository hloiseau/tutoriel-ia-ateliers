Dans la partie 6, notre serveur MCP lisait des documents sur notre ordinateur, puis transmettait ses résultats au modèle choisi par l’assistant. Avec une interface installée localement, les fichiers du programme restent chez nous tandis que les requêtes peuvent partir ailleurs. Le mot « local » décrit ici un morceau du trajet.

Ouvrez `fiches/flux.md` et remplissez une ligne par trajet : de l’éditeur au modèle, de l’agent au serveur MCP, du serveur aux tickets, puis vers les éventuels journaux. Pour chaque trajet, notez ce qui passe, où cela arrive et ce qui vous permet de l’affirmer.

Pour le parcours de tâches de travail, partez des fichiers joints à l’assistant, puis du document ou du JSON qu’il produit. La page locale reçoit ensuite ce JSON par copier-coller ; elle le traite dans le navigateur et déclenche des téléchargements, sans appeler de service. Cela ne renseigne pas sur le traitement antérieur des pièces par l’assistant choisi. Inscrivez ces deux étapes séparément dans votre carte.

| Élément de notre atelier | Information que nous pouvons établir |
| --- | --- |
| Client documentaire de la partie 8 | Son code envoie la requête à `127.0.0.1:8080` |
| Réponse reçue | Le journal conserve le contexte transmis et la sortie |
| Assistant installé pour la partie 4 | Le trajet dépend du produit, de sa configuration et du fournisseur sélectionné |
| Politique d’un service externe | Elle doit être vérifiée pour ce service et l’offre utilisée |

Une option « non utilisé pour l’entraînement » répond à une question précise. Pour connaître la durée de conservation des journaux, l’accès de tiers et la localisation du traitement, il reste à lire les engagements applicables au service et à l’offre choisis.

Pour notre exercice, restez sur les documents fictifs fournis. Une fois la carte des trajets dessinée, vous pourrez décider quelles données de votre propre projet seraient acceptables dans cette configuration.
