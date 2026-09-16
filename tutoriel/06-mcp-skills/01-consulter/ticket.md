Lancez :

```bash
python client.py ticket PRIX-1 --journal sorties/prix-1.json
```

Le client démarre `serveur.py`, appelle l’outil de lecture, puis arrête le serveur. Vous n’avez pas de deuxième terminal à ouvrir.

La réponse est assez longue : le SDK fournit notamment une représentation textuelle et un contenu structuré. Ouvrez `sorties/prix-1.json` et cherchez `structuredContent`. Vous y retrouverez cet extrait :

```json
{
  "id": "PRIX-1",
  "titre": "Ne plus notifier une simple remise en stock",
  "statut": "a preparer",
  "regle": "Notifier seulement si le produit est disponible dans le nouvel état et si son prix baisse strictement.",
  "questions_ouvertes": [],
  "documents": ["regle-notification"],
  "revision": "exemple-1"
}
```
Code: Contenu du ticket fictif retourné par le serveur

Comparez-le avec `donnees/tickets.json` : les champs correspondent. Le client a lu la règle par l’intermédiaire du serveur, sans demander à un modèle de la deviner ou de la reformuler.

Le journal conserve aussi `protocole`, la version employée lors de l’échange. Notre exécution avec le SDK fourni utilise `2026-07-28`. Nous y enregistrons le résultat obtenu par le client ; pour examiner chaque message du transport, il faudrait une trace plus détaillée.

Pour refaire la commande, choisissez un autre nom de journal. Le client refuse d’écraser le premier : nous pourrons comparer nos essais sans perdre la réponse précédente.
