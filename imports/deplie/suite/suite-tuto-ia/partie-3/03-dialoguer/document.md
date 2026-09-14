Essayons maintenant une question dont nous connaissons la réponse, sans dépendre des souvenirs du modèle :

```bash
python client.py --fichier questions/document.json --sortie resultats/document.json
python client.py --fichier questions/inconnue.json --sortie resultats/inconnue.json
```

Les deux fichiers parlent d’une bibliothèque fictive. Le document indique qu’elle ouvre le mardi à 10 heures et ferme à 17 heures. Le premier demande l’heure d’ouverture du mardi. Le second demande celle du dimanche, qui n’est pas fournie.

Pour le mardi, nous attendons **10 heures**. Pour le dimanche, nous attendons que le modèle dise qu’il ne sait pas. La consigne lui demande explicitement de se limiter au document.

S’il invente un horaire du dimanche, ne complétez pas le document pour rendre sa réponse vraie. Conservez l’erreur. Nous cherchons justement à voir s’il respecte une limite d’information.

Vous venez de construire deux petits cas d’évaluation : une réponse accessible et une information absente. Ce n’est pas encore une évaluation générale du modèle, mais c’est déjà beaucoup plus précis que « j’ai discuté dix minutes, ça avait l’air bien ».
