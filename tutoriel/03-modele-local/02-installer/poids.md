Toujours dans `atelier-local`, lancez :

```bash
python telecharger.py
```

Le programme lit `modele.json`, télécharge le fichier retenu dans `modeles/` et vérifie sa taille ainsi que son empreinte SHA-256. Le téléchargement est lié à une révision précise du dépôt ; un futur changement de sa branche principale ne changera pas silencieusement notre fichier.

Pendant le transfert, le fichier porte une extension `.part`. Il ne prend son nom définitif qu’après vérification. Si la connexion coupe, relancez la commande : ce petit script recommence le transfert, il ne sait pas le reprendre au milieu.

Ouvrez `modele.json`. Son nom de dépôt, sa révision, sa taille et son empreinte répondent à une question très pratique : « Avons-nous réellement testé le même fichier ? » Des noms proches peuvent cacher deux versions différentes.

L’empreinte détecte un fichier différent de celui attendu. La confiance envers son auteur et la provenance des données d’entraînement demandent d’autres informations, à commencer par la fiche et les documents publiés avec le modèle.
