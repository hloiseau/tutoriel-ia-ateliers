Lancez :

```bash
python banc.py boucle --limite 3 --journal sorties/boucle.jsonl
```

Le fichier `cas/boucle.json` contient huit demandes de lecture identiques. Le journal n’enregistre que trois appels, puis un arrêt pour `budget_appels`. Le quatrième appel n’est pas exécuté.

Ouvrez la fonction `rejouer` : c’est le programme qui compte les appels et arrête la boucle. Il ne demande pas au modèle de décider s’il a suffisamment dépensé. Le test associé vérifie aussi que les demandes refusées consomment ce budget.

Dans un véritable agent, une limite peut porter sur les tours, les tokens, la durée ou une dépense. Il faut savoir ce qui est compté. Notre limite d’appels ne borne pas le temps d’un outil bloqué ni la durée d’une requête au modèle ; il faudrait des délais d’expiration pour cela.

Relire un fichier n’est pas toujours inutile : il peut avoir changé. En revanche, lire trois fois le même contenu sans nouvelle question doit nous inciter à regarder ce qui manque, plutôt qu’à attendre le quatrième passage. 😅
