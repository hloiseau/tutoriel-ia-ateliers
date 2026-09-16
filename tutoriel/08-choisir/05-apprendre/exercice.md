Ouvrez `cas/lecture_code.py`, sans le lancer tout de suite. La fonction décide si un produit doit déclencher une notification. Les prix sont des entiers en centimes ; les entrées sont supposées déjà validées.

```python
def doit_notifier(ancien_prix, nouveau_prix, disponible):
    if not disponible:
        return False
    return nouveau_prix <= ancien_prix
```
Code: Une fonction volontairement incorrecte

La règle demandée est celle de notre service : notifier uniquement si le nouveau prix baisse strictement et que le produit est disponible. Prévoyez le résultat pour un prix qui baisse, un prix inchangé, un prix qui monte et un produit indisponible. Écrivez aussi le résultat attendu par la règle.

Vous pouvez ensuite lancer :

```bash
python cas/lecture_code.py
```

Le programme affiche les cas, le résultat obtenu et le résultat attendu, puis sort avec le code 1 : le cas du prix égal révèle le bug prévu dans l’exercice. Corrigez la fonction et relancez. Le corrigé est dans `corriges/lecture_code.py`, accompagné d’une explication dans `corriges/lecture_code.md`.

Le lendemain, ou simplement après une autre tâche, essayez une petite variante sans rouvrir la réponse : ne notifier que si la baisse atteint au moins 100 centimes, toujours avec un produit disponible. Que se passe-t-il pour une baisse de 99, de 100 et de 101 centimes ? La correction de cette variante est fournie elle aussi.

Personne ne ramassera la copie. 🙂 Observez plutôt ce que vous savez encore expliquer et modifier après avoir fermé l’outil.
