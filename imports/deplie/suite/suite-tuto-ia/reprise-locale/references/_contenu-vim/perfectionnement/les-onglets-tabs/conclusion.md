Nous avons vu que Vim nous met à disposition un système d'onglet tout comme notre navigateur.

[[information]]
| On peut ouvrir plusieurs fichiers dans plusieurs onglets avec l'option `-p`.  
| Ex: `vim -p file1.txt file2.txt`

Voici un récapitulatif des commandes que nous avons vu:

| Commande | Explication |
|:--------:|:------------|
| `:tabnew` | Ouvre un nouvel onglet |
| `gt` | Passer à l'onglet suivant |
| `gT` | Passer à l'onglet précédent |
| `<nb>gt` | Passer à l'onglet `<nb>` |
| `:tabclose` | Fermer un onglet |
| `:tabmove <nb>` | Déplace l'onglet en position `<nb>`, si `<nb>` est absent l'onglet sera mis en dernier |
| `Ctrl` + `w` puis `T` | Convertis une fenêtre en onglet |

[[attention | On sait maintenant:]]
| - Ouvrir et fermer des onglets
| - Se déplacer entre les onglets