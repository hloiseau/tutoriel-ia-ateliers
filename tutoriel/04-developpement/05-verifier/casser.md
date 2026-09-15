Cette expérience est facultative. Copiez le dossier corrigé `mon-suivi` dans un dossier voisin nommé **`mon-suivi-mutations`**. Depuis le terminal placé dans `mon-suivi`, entrez dans cette nouvelle copie :

```bash
cd ../mon-suivi-mutations
```

Ouvrez **le fichier `suivi.py` de cette copie**, remplacez `<` par `<=`, enregistrez, puis relancez `python -m unittest discover -v` dans ce terminal.

Le prix identique autorise maintenant une notification. Les tests qui attendent l’absence de notification à prix inchangé doivent échouer. S’ils ne le font pas, vérifiez que vous avez exécuté la bonne copie et que ces cas sont présents.

Rétablissez ensuite `<`, puis retirez temporairement la condition `nouveau.disponible and`. Le test de baisse sur un produit indisponible doit cette fois protester.

Ces modifications volontaires sont de petites **mutations** : nous introduisons une erreur précise pour voir si les tests la remarquent. Cela ne prouve pas qu’ils détecteront tous les bugs. Cela permet de vérifier que les cas importants ne sont pas seulement décoratifs.

Rétablissez la condition dans `mon-suivi-mutations`, puis revenez à notre copie de travail restée intacte :

```bash
cd ../mon-suivi
python -m unittest discover -v
```

Le but est de tester nos tests, pas de préparer discrètement le prochain ticket. 🙂
