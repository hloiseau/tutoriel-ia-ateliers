Un résumé de l’agent raconte ce qu’il pense avoir fait. Le diff montre les fichiers modifiés. Ouvrez celui de votre éditeur, puis cherchez le changement dans `suivi.py`.

La correction fournie retire ce morceau :

```diff
-        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
+        nouveau.prix_centimes < ancien.prix_centimes
```
Code: Le changement de comportement dans la fonction

Si Git est installé, vous pouvez aussi comparer les deux dossiers depuis leur dossier parent :

```bash
git diff --no-index 01-depart/suivi.py mon-suivi/suivi.py
```

Cette commande fonctionne sans créer de dépôt Git. Avec `--no-index`, un code de sortie égal à 1 signifie que les fichiers diffèrent ; ce n’est pas forcément un échec de la comparaison.[^p4-diff]

Regardez ensuite les autres fichiers modifiés. Les nouveaux tests sont attendus. Une modification des données d’entrée pour éviter le bug, une suppression de validation ou une réécriture de tout le programme demandent une explication.

Si vous débutez, choisissez une ligne retirée et une ligne conservée, puis expliquez leur rôle sans recopier le résumé de l’agent. Si vous n’y arrivez pas encore, revenez à la fonction. Le résultat est assez petit pour que cette lecture reste abordable.

[^p4-diff]: Git, [comparaison de fichiers avec `git diff --no-index`](https://git-scm.com/docs/git-diff).
