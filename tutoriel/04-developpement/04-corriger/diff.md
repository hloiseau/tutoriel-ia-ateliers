Ouvrez la comparaison des fichiers dans votre éditeur. Dans VS Code, ouvrez la version originale `01-depart/suivi.py` et copiez tout son contenu. Revenez dans `mon-suivi/suivi.py`, ouvrez la palette de commandes et lancez **File: Compare Active File with Clipboard**[^p4-diff-vscode]. Les libellés peuvent être traduits dans votre installation.

Notre correction de référence montre :

```diff
-        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
+        nouveau.prix_centimes < ancien.prix_centimes
```
Code: La règle retirée par notre correction

Si Git est installé, vous pouvez faire la même comparaison depuis un terminal, sans créer de dépôt :

```bash
git diff --no-index "/chemin/vers/atelier-developpement/01-depart/suivi.py" "/chemin/vers/mon-suivi/suivi.py"
```

Remplacez les deux chemins par ceux de vos fichiers. Cette commande ne suppose pas que les dossiers sont voisins. Avec `--no-index`, le code de sortie 1 signifie que les fichiers diffèrent[^p4-diff].

Cette première comparaison ne porte que sur `suivi.py`. Reprenez ensuite la liste des fichiers touchés affichée par l’assistant. Comparez chaque fichier qui existait déjà à son original dans `01-depart`, puis lisez entièrement le nouveau `test_ticket.py`.

Le test ajouté est attendu. Changer les données de `retour-stock.json`, supprimer un test ou modifier une validation sortirait en revanche du correctif demandé. Si vous trouvez l’un de ces changements, demandez sa raison puis retirez-le s’il ne sert aucun cas du ticket.

[^p4-diff-vscode]: Microsoft, [comparaison des fichiers dans VS Code](https://code.visualstudio.com/docs/editing/codebasics#_compare-files).
[^p4-diff]: Git, [comparaison avec git diff --no-index](https://git-scm.com/docs/git-diff).
