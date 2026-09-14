# Corriger le suivi de prix

Copiez `atelier-developpement/01-depart` dans un dossier de travail nommé `mon-suivi`. Ouvrez votre terminal dans cette copie. Python 3.12 suffit ; le projet utilise seulement la bibliothèque standard.

```bash
python -m unittest discover -v
python suivi.py scenarios/retour-stock.json
```

Le programme initial possède trois tests qui passent. Il décide pourtant de notifier une simple remise en stock. Il n’envoie aucune notification : il affiche seulement sa décision en JSON.

Lisez `TICKET.md` pour connaître le comportement attendu. `PROMPTS.md` propose des consignes si vous voulez travailler avec un agent. Vous pouvez également réaliser la correction vous-même.

## Les trois états

- `01-depart` : trois tests passent ; la règle du ticket n’est pas encore appliquée.
- `02-test-rouge` : treize tests, dont deux en échec. C’est l’étape qui reproduit le problème.
- `03-corrige` : treize tests passent ; les scénarios permettent de vérifier le programme complet.

`correction.diff` montre le changement de la fonction. Pour observer le travail d’un agent, commencez dans votre copie de `01-depart`, sans lui donner les dossiers de correction.

## Recette après correction

```bash
python suivi.py scenarios/retour-stock.json
python suivi.py scenarios/baisse.json
python suivi.py scenarios/rupture.json
```

Les décisions attendues sont respectivement `false`, `true`, `false`.
