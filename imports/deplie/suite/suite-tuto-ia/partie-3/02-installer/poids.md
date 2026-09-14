Toujours dans `atelier-local`, lancez :

```bash
python telecharger.py
```

Le programme lit `modele.json`, télécharge le fichier retenu dans `modeles/` et vérifie sa taille ainsi que son empreinte SHA-256. Le téléchargement est lié à une révision précise du dépôt ; un futur changement de sa branche principale ne changera pas silencieusement notre fichier.

Pendant le transfert, le fichier porte une extension `.part`. Il ne prend son nom définitif qu’après vérification. Si la connexion coupe, relancez la commande : ce petit script recommence le transfert, il ne sait pas le reprendre au milieu.

Vous pouvez ouvrir `modele.json`. Les informations servent à répondre à une question très pratique : « Avons-nous réellement testé le même fichier ? » Deux fichiers nommés de façon proche ne sont pas forcément identiques.

L’empreinte permet de détecter un fichier différent de celui attendu. Elle ne prouve pas que son auteur est digne de confiance ni que les données d’entraînement ont toutes été obtenues dans de bonnes conditions. Ce sont deux vérifications différentes.
