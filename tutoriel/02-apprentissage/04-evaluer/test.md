Pour le modèle linéaire, nous conservons nos 80 epochs et notre pas de 0,2. Nous pouvons maintenant ouvrir le jeu de test :

```bash
python 04_evaluer.py
```

```text
Test : 345/360 réponses correctes (95.8%)
```

Cela fait quinze erreurs. Le résultat porte sur les 360 images de ce découpage, pas sur tous les chiffres que quelqu’un pourrait écrire.

Ouvrez `sorties/lineaire-confusions.png` :

![Matrice des réponses du modèle : les lignes sont les étiquettes et les colonnes les chiffres prédits.](image:images/lineaire-confusions.png)
Figure: Chaque case compte des images du jeu de test.

C’est une **matrice de confusion**. Sur la diagonale, le chiffre prédit correspond à l’étiquette. En dehors, nous voyons les confusions. La ligne du huit indique notamment ce que deviennent les images étiquetées huit : reconnues, ou prises pour un autre chiffre.

Un score global pourrait cacher un modèle qui reconnaît très bien certaines classes et presque jamais une autre. Cette grille permet d’aller regarder lesquelles.

Le test doit rester un bilan. Si nous le consultons après chaque changement pour choisir le meilleur réglage, il devient un autre jeu de validation. Garder son nom « test » dans le code ne lui rendra pas son indépendance. 🙂
