Commençons sans lancer le serveur :

```bash
python assistant_local.py "Quel délai de temporisation est validé ?" --sortie sorties/contexte-delai.json
```

Ouvrez le fichier produit. `passages` contient les résultats de recherche avec leur provenance. `messages` contient ce qui serait envoyé au modèle : une consigne, puis les passages et la question.

La consigne demande de répondre avec les sources, de citer leurs identifiants et de signaler une décision encore ouverte. Elle précise aussi que les documents sont des données à lire, pas des ordres à exécuter. Vous retrouvez le problème rencontré avec la documentation piégée de la partie 6.

La préparation n’a fait aucun appel réseau. Vous pouvez donc examiner le contexte avant de lancer quoi que ce soit. Si aucun passage n’est retrouvé, le programme le signale et ne demande pas au modèle de combler le vide.

Cela reste une décision de notre application. D’autres usages peuvent avoir besoin d’une réponse générale malgré l’absence de source locale ; ici, nous cherchons une réponse sur les règles de notre service.
