Nous avons ajouté des contraintes sur l’identifiant des documents. Comparons deux erreurs :

```bash
python client.py document ../tickets --serveur mon_serveur.py --journal sorties/controle-format.json
python client.py document document-absent --serveur mon_serveur.py --journal sorties/controle-absent.json
```

Les deux appels échouent, mais pour des raisons différentes. Le premier ne respecte pas le format attendu ; la fonction ne doit pas traiter cette demande. Le second passe la validation, puis notre recherche dans le catalogue constate que le document n’existe pas.

Regardez ensuite `catalogue("documents.json")` dans votre code. Le nom du fichier est fixé par le programme. L’identifiant reçu sert à chercher une clé dans l’objet chargé, **pas à construire un chemin**. C’est cette conception qui limite les fichiers accessibles par cet outil ; le simple fait d’accepter une chaîne ne l’aurait pas fait.

Le contrôle de la recherche apporte un autre exemple : essayez `chercher "   "` à la place de `document document-absent`, avec un nouveau journal. La chaîne a bien trois caractères, mais notre fonction la nettoie et constate qu’elle ne contient aucun terme utile.

Ces contrôles ne disent pas qui a le droit de lire quel ticket. Notre jeu fictif n’a qu’un seul niveau d’accès. Dans un service partagé, il faudrait aussi vérifier les droits du demandeur : connaître un identifiant valide ne donne pas une autorisation.
