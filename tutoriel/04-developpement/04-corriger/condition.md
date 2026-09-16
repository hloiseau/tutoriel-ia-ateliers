Comparez maintenant sa proposition à la fonction initiale :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
    )
```

Lisez-la à voix haute : le produit doit être disponible maintenant ; ensuite, une baisse de prix **ou** une ancienne indisponibilité suffit.

Le second terme du `or` explique notre problème. Pour un retour en stock, `not ancien.disponible` vaut vrai. Le prix peut être identique ou même plus élevé : l’expression entre parenthèses sera tout de même vraie.

Le ticket exige les deux conditions : une disponibilité actuelle **et** une baisse stricte. Notre correction de référence est :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes
    )
```
Code: La fonction après correction

Une expression sur une ligne peut être tout aussi correcte. Ce que nous cherchons dans la proposition, c’est la disponibilité actuelle et la baisse stricte, sans condition supplémentaire.

Résistez à la tentation d’ajouter `ancien.disponible` dans la nouvelle condition. Une vraie baisse au moment du retour en stock serait alors ignorée, contrairement à la règle décidée.

![Seul le cas disponible maintenant avec baisse de prix autorise une notification](image:images/decision.png)
Figure: La règle complète tient dans ces quatre combinaisons
