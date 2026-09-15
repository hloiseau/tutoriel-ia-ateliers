Le script suivant prend la validation et décale chaque image d’un pixel vers la droite. Il remplit la colonne de gauche avec des zéros ; la colonne qui sort à droite est perdue.

```bash
python 06_decaler.py
```

```text
Validation d'origine : 95.0%
Décalée d'un pixel à droite : 41.4%
```

Ouvrez `sorties/decalage.png` :

![Quatre chiffres correctement reconnus en haut deviennent mal classés après un décalage à droite, en bas.](image:images/decalage.png)
Figure: En haut, les images d’origine ; en bas, les mêmes images déplacées. Données d’E. Alpaydin et C. Kaynak, UCI, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Les poids sont restés identiques. Ce sont les entrées qui ont changé. Pour nous, beaucoup de ces chiffres restent reconnaissables. Pour le modèle, les zones claires ne tombent plus aux mêmes positions.

Le décalage n’est pas parfaitement neutre : sur une grille aussi petite, perdre une colonne peut retirer une partie du trait. Même avec cette limite, l’écart entre 95,0 % et 41,4 % montre combien ce modèle dépend de la présentation des images.

Une piste consiste à lui montrer des variations pendant l’entraînement : légers déplacements, par exemple. C’est une forme d’**augmentation de données**. On fabriquerait ces variantes à partir des seules images d’entraînement, puis on vérifierait leur effet sur la validation. Transformer aussi le test en exercices d’entraînement ferait disparaître la question que nous cherchons à mesurer.
