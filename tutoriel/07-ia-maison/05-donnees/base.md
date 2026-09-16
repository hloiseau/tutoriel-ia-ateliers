Le dossier `resultats-reference/base` contient les poids d’un modèle entraîné sur le premier corpus. Nous referons cet entraînement depuis zéro au chapitre 7. Pour l’instant, essayons ce qu’il produit :

```bash
python petit_modele.py generer --modele resultats-reference/base/modele.npz
```

Le résultat commence comme une phrase du corpus, puis finit par dérailler. C’est normal au sens où nous observons les limites de cette expérience ; ce n’est pas une réponse que nous devrions accepter dans une application.

Nous allons lui faire apprendre les lignes `INFO`. Une première possibilité consiste à continuer l’entraînement en autorisant la modification de tous ses paramètres : c’est ici notre **adaptation complète**.

```bash
python petit_modele.py entrainer --base resultats-reference/base/modele.npz --mode complet --corpus adaptation --pas 800 --sortie sorties/complet
```

Le dossier de sortie doit être nouveau. Il recevra les poids, le rapport et un échantillon généré. Les poids de départ restent dans leur dossier d’origine ; nous pouvons donc toujours revenir à eux.

Cette commande ne garantit pas que le modèle deviendra bon. Elle nous donne un premier résultat auquel comparer une adaptation plus petite, avec beaucoup moins de paramètres entraînables.
