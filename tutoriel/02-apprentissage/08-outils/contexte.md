Reprenons les opérations que nous avons réellement effectuées :

| Action | Ce qui change |
| --- | --- |
| Modifier les pixels de `dessin.json` | L’entrée de l’inférence |
| Réentraîner le classifieur | Les poids et les biais |
| Ajouter une phrase à `corpus.txt`, puis recompter | La table du modèle de bigrammes |
| Changer `--debut` | Le texte de départ, donc le contexte |
| Changer la température | La répartition utilisée pour choisir le caractère suivant |
| Lire une fiche avec un outil | Les informations que l’application peut fournir ensuite au modèle |

Le tableau montre pourquoi deux changements qui se ressemblent dans une interface peuvent agir à des endroits très différents. Ajouter une documentation enrichit les informations disponibles pour la réponse en cours ; adapter le modèle modifie ses poids. Une consigne plus prudente, elle, laisse intactes les données qui ont servi à l’entraînement.

Un agent peut aussi perdre l’accès à une information si son application la retire, la résume mal ou ne la charge pas au bon moment. Notre bigramme avait une limite extrêmement visible : un caractère de contexte. Les modèles actuels en utilisent beaucoup plus, mais la quantité d’informations accessible et la manière de les exploiter restent des contraintes.

Pour travailler sur du code, on peut vérifier des faits avec les fichiers du projet, une documentation ou une commande. Encore faut-il donner à l’agent les bons éléments, puis regarder si sa conclusion en découle réellement.
