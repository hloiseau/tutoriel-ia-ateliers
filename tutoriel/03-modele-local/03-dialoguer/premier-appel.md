Ouvrez `questions/premiere.json`. Vous y trouverez deux messages :

```json
[
  {"role": "system", "content": "Answer briefly in English."},
  {"role": "user", "content": "Explain what a variable is in programming, in two sentences."}
]
```
Code: Les messages envoyés au modèle

Le premier donne une consigne générale ; le second contient notre question. Nous commençons en anglais parce que c’est la langue principale du modèle retenu.

Lancez :

```bash
python client.py
```

Le client affiche le texte reçu et écrit `resultats/reponse.json`. Ouvrez ce fichier : il contient la demande, la réponse brute et le temps écoulé autour de l’appel. Si le modèle vous surprend demain, vous aurez mieux qu’une phrase recopiée de mémoire pour comprendre pourquoi. 🙂

Lisez la réponse. Respecte-t-elle les deux phrases demandées ? Son explication d’une variable est-elle correcte ? Vérifiez les deux : un texte bien présenté peut toujours raconter n’importe quoi.

Si le client finit par signaler un délai dépassé, regardez le terminal du serveur avant de recommencer. Une expiration côté client n’implique pas forcément que le calcul côté serveur s’est arrêté.
