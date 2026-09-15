Lisez la documentation associée au ticket :

```bash
python client.py document regle-notification --journal sorties/regle.json
```

Cette commande convient quand nous connaissons déjà l’identifiant. Si nous cherchons où l’on parle des notifications, utilisons plutôt :

```bash
python client.py chercher notification --journal sorties/recherche.json
```

La recherche renvoie des **identifiants, des titres et un statut**, pas le texte complet des documents. On peut ensuite ouvrir celui qui nous intéresse. La réponse est limitée à cinq résultats ; `tronque` indique si le serveur en a trouvé davantage.

Notre fonction fait une recherche littérale, sans distinction de casse, dans le titre et le texte. « notification » peut trouver « notifications », mais « alerte » ne trouvera pas automatiquement « notification ». Il n’y a ni embeddings ni recherche sémantique cachés dans ces quelques lignes.

Vous remarquerez deux résultats : la règle en vigueur et une note archivée. Le statut fait partie de la réponse parce qu’il change la façon dont on doit lire le document. Une vieille note peut expliquer l’histoire d’une décision ; elle ne remplace pas automatiquement la règle actuelle.

Dans un vrai serveur, la recherche pourrait appeler l’API documentaire de l’équipe. Nous conserverions la même séparation : **trouver les sources**, puis **lire celles qui servent à la tâche**. Nous remplacerions l’accès aux fichiers, pas nécessairement toute l’interface MCP.
