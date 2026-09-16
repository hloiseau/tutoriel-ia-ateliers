Notre réseau transforme sa représentation interne `h` en scores pour les caractères suivants avec une matrice `U`. Pour l’adapter, nous remplaçons ce calcul par :

```python
scores = h @ (U + A @ B) + c
```

Le symbole `@` désigne un produit de matrices en Python. `U` et le biais `c` restent figés ; seules les matrices `A` et `B` apprennent. C’est le principe d’une adaptation de faible rang, ou **LoRA**.[^p7-lora]

![La sortie additionne le trajet de base figé et la correction passant par deux petites matrices entraînables.](image:images/lora.png)
Figure: Deux chemins se rejoignent avant le calcul des probabilités

Dans notre cas, `U` comporte 64 × 75 nombres. Avec un rang de 4, `A` contient 64 × 4 nombres et `B`, 4 × 75 : soit 556 paramètres entraînables, au lieu des 15 055 du modèle complet.

Le rang limite la forme de la correction possible. Ce n’est ni un nombre de connaissances ni un niveau d’intelligence. Notre exemple applique LoRA uniquement à la couche de sortie, avec un facteur d’échelle égal à 1 ; une adaptation de LLM peut viser d’autres couches et employer d’autres réglages.

[^p7-lora]: Hu et al., [*LoRA: Low-Rank Adaptation of Large Language Models*](https://arxiv.org/abs/2106.09685).
