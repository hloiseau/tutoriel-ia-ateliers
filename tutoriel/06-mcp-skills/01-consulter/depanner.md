Essayez maintenant un identifiant absent :

```bash
python client.py ticket PRIX-999 --journal sorties/inconnu.json
```

Cette fois, cherchez `isError` dans la réponse : sa valeur est `true`. Le serveur a reçu une demande compréhensible, mais ne possède pas ce ticket. Son message ne signifie pas que PRIX-999 n’existe nulle part ; seulement qu’il est absent de notre jeu de données.

C’est différent d’un client qui n’arrive même pas à démarrer :

| Ce que vous voyez | Où regarder d’abord |
| --- | --- |
| `No module named 'mcp'` | L’interpréteur utilisé et l’installation avec ce même Python |
| `can't open file ...client.py` | Le dossier dans lequel le terminal est ouvert |
| Le journal existe déjà | Un nouveau nom après `--journal` |
| `isError: true` dans un journal enregistré | Le message retourné par l’outil |
| Le serveur s’arrête avant de répondre | La sortie d’erreur du terminal et les dépendances |

Le client imprime les erreurs attendues de l’outil dans son journal et termine normalement. Un code de sortie nul signifie ici qu’il a pu enregistrer la réponse, pas que le ticket demandé a été trouvé.

Une erreur correctement remontée est déjà un résultat utile : l’agent pourra dire qu’il n’a pas obtenu le ticket. Une réponse inventée serait beaucoup plus ennuyeuse à repérer.
