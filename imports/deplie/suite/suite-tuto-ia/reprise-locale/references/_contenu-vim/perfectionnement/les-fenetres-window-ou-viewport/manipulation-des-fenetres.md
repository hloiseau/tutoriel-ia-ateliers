Maintenant, nous savons découper notre fenêtre en autres fenêtres plus petite et se déplacer entre elles. Il nous manque encore une partie importante qui est la manipulation de ces dernières.

Lorsque nous avons plusieurs fenêtres ouvertes et que nous souhaitons seulement en garder une ouverte, nous pouvons utiliser la commande `:on` (ou `:only`). Cela va fermer toutes les fenêtres sauf celle dans laquelle nous sommes.

Bien sure, il est possible de redimensionner une fenêtre. Voici les commandes:

| Commande | Explication |
|:--------:|:------------|
| `Ctrl` + `w` puis `>` | Élargis la fenêtre d'une colonne |
| `Ctrl` + `w` puis `<` | Affine la fenêtre d'une colonne |
| `Ctrl` + `w` puis `-` | Rapetisse la fenêtre d'une ligne |
| `Ctrl` + `w` puis `+` | Agrandis la fenêtre d'une ligne |
| `Ctrl` + `w` puis `=` | Réarrange toutes les fenêtres de manière égale |

Bien sure, nous avons à notre disposition des commandes pour changer la taille des fenêtres plus facilement.

| Commande | Explication |
|:--------:|:------------|
| `Ctrl` + `w` puis `<n>` puis `>` | Élargis la fenêtre de `<n>` colonnes |
| `Ctrl` + `w` puis `<n>` puis `<` | Affine la fenêtre de `<n>` colonnes |
| `Ctrl` + `w` puis `<n>` puis `-` | Rapetisse la fenêtre de `<n>` lignes |
| `Ctrl` + `w` puis `<n>` puis `+` | Agrandis la fenêtre de `<n>` lignes |

[[information]]
| On pourrait aussi utiliser les commandes `:resize` et `:vertical resize`.  
| Ex: `:vertical resize +10` élargis la fenêtre de 10 colonnes.

L'on peut aussi très rapidement maximiser la taille d'une fenêtre avec les commandes `Ctrl` + `w` puis `|` pour la limite verticale et `Ctrl` + `w` puis `_` pour la limite horizontale