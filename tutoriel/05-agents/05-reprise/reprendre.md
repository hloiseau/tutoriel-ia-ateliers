Rejouez cet autre cas :

```bash
python banc.py reprise --journal sorties/reprise.jsonl
```

La première demande cherche `ticket.md`, qui ne figure pas dans la liste des chemins autorisés. La seconde demande `TICKET.md` et réussit. Le script montre une correction de paramètre, pas une ouverture générale des droits.

Dans votre assistant, commencez de la même façon : quelle demande a échoué, avec quels arguments, et quel résultat est revenu ? « Permission refusée », « fichier absent » et « test en échec » demandent des réponses différentes.

Avant de relancer une écriture, regardez aussi si elle a pu avoir lieu. Un délai dépassé ne prouve pas que le serveur n’a rien fait. Pour un envoi de notification ou la création d’un ticket, répéter aveuglément peut produire un doublon. L’opération doit avoir une manière de vérifier son état ou d’éviter les doublons ; « réessaie » ne suffit pas.

Pour notre exercice de la partie 4, inspectez le fichier et le diff avant de demander une nouvelle correction. On repartira ainsi de l’état présent, pas du récit de la dernière tentative.
