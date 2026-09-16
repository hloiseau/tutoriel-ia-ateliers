Rejouez cet autre cas :

```bash
python banc.py reprise --journal sorties/reprise.jsonl
```

La première demande cherche `ticket.md`, absent de la liste des chemins autorisés. La seconde utilise le nom exact `TICKET.md` et réussit. Le droit de lecture n’a pas changé ; seul l’argument a été corrigé.

Dans votre assistant, commencez par les mêmes questions : quelle demande a échoué, avec quels arguments, et quel résultat est revenu ? « Permission refusée », « fichier absent » et « test en échec » appellent des corrections différentes.

Avant de relancer une écriture, vérifiez si elle a pu avoir lieu. Après un délai dépassé, le serveur a peut-être terminé l’action sans que la réponse vous parvienne. Renvoyer une notification ou recréer un ticket peut alors produire un doublon. Prévoyez un moyen de consulter l’état de l’opération ou de reconnaître une répétition.

Pour l’exercice de la partie 4, inspectez le fichier et le diff avant de demander une nouvelle correction. La reprise partira de l’état présent des fichiers, plus fiable que le récit de la dernière tentative.
