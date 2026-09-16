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

Le client enregistre les erreurs attendues de l’outil dans son journal et termine normalement. Son code de sortie nul nous apprend que l’échange a pu être conservé. Pour savoir si le ticket a été trouvé, il faut encore lire `isError` et le message de l’outil.

Cette erreur correctement remontée est déjà utile : l’agent pourra dire qu’il n’a pas obtenu le ticket. C’est tout de même plus facile à traiter qu’une réponse inventée avec beaucoup d’assurance. 😅
