Essayons maintenant une question dont nous connaissons la réponse, sans dépendre des souvenirs du modèle :

```bash
python client.py --fichier questions/document.json --sortie resultats/document.json
python client.py --fichier questions/inconnue.json --sortie resultats/inconnue.json
```

Les deux fichiers parlent d’une bibliothèque fictive. Le document indique qu’elle ouvre le mardi à 10 heures et ferme à 17 heures. Le premier demande l’heure d’ouverture du mardi. Le second demande celle du dimanche, qui n’est pas fournie.

Pour le mardi, nous attendons **10 heures**. Pour le dimanche, nous attendons que le modèle dise qu’il ne sait pas. La consigne lui demande explicitement de se limiter au document.

S’il invente un horaire du dimanche, conservez l’erreur. Compléter le document après coup rendrait le cas beaucoup moins intéressant : nous voulons savoir comment il réagit lorsqu’une information manque.

Ces deux cas ciblent désormais un comportement chacun : retrouver une réponse présente et s’abstenir lorsque l’information manque. Ils ne résument pas les capacités du modèle ; ils donnent en revanche deux observations que nous pourrons rejouer au prochain changement.
