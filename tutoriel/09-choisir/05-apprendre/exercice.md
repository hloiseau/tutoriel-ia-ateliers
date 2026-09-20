Choisissez l’exercice correspondant à votre parcours. Vous pourrez essayer l’autre ensuite si le sujet vous intéresse.

# Pour les tâches de travail

Reprenez les documents des Ateliers du quartier, puis fermez la conversation avec l’assistant. Voici une synthèse volontairement incorrecte, écrite pour cet exercice :

> La journée est confirmée le 17 octobre. Nora attend quatre places en Reliure et Léo deux places dans le même atelier. Nous pouvons envoyer les confirmations.

Cherchez dans les sources ce qui permet d’accepter ou de corriger chacune de ces phrases. Le compte rendu récent confirme-t-il la date ? Nora a-t-elle demandé quatre places ? Quel atelier Léo a-t-il choisi ? Qui a décidé des confirmations ? Vous pouvez vous aider de votre propre point, puis ouvrir le corrigé manuel du dossier pour comparer.

La correction garde la date à clarifier entre le 10 et le 17 octobre, deux places pour Nora, deux places sans atelier précisé pour Léo, et aucune confirmation envoyée. Le doublon de Nora n’ajoute aucune place. La note la plus récente ne documente pas une décision qui tranche le désaccord.

Après une autre tâche, essayez une variation : Léo répond « nous serons finalement trois, en Cartographie ». Que modifiez-vous ? Le nombre et le choix de l’atelier changent pour sa demande ; la date et l’autorisation d’envoyer les confirmations restent à vérifier. Être capable d’expliquer ce qui change vous permet de garder la main sur la suite.

# Pour le développement

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
