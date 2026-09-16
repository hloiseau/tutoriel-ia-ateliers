Commençons sans lancer le serveur :

```bash
python assistant_local.py "Quel délai de temporisation est validé ?" --sortie sorties/contexte-delai.json
```

Ouvrez le fichier produit. `passages` contient les résultats de recherche avec leur provenance. `messages` contient ce qui serait envoyé au modèle : une consigne, puis les passages et la question.

La consigne demande de répondre avec les sources, de citer leurs identifiants et de signaler une décision encore ouverte. Elle précise aussi que les documents sont des données à lire, pas des ordres à exécuter. Vous retrouvez le problème rencontré avec la documentation piégée de la partie 6.

À ce stade, aucun appel réseau n’a eu lieu. Vous pouvez lire tranquillement le contexte avant de lancer le serveur. Si la recherche ne ramène aucun passage, le programme s’arrête là au lieu de demander au modèle de combler le vide.

Ce comportement correspond à notre besoin : nous interrogeons les règles du service. Une application chargée de répondre à des questions générales pourrait faire un autre choix, à condition de l’annoncer clairement au lecteur de la réponse.
