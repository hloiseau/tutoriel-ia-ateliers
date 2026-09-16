Exécutez :

```bash
python 02_predire.py
```

```text
Étiquette attendue : 3
Probabilités : [0.099 0.099 0.104 0.099 0.092 0.103 0.102 0.097 0.102 0.102]
Classe choisie : 2
Paramètres : 650
Exactitude avant entraînement : 10.3%
```

Le chiffre attendu est un trois. Le modèle choisit un deux. Ses probabilités sont toutes proches d’un dixième : les poids viennent d’être tirés au hasard, il n’a encore reçu aucune correction.

Les 10,3 % de bonnes réponses nous donnent un point de départ. Avec dix classes assez équilibrées, une règle naïve ou un choix au hasard peut déjà obtenir un résultat de cet ordre. L’entraînement devra faire nettement mieux.

Ouvrez `02_predire.py`. Remplacez :

```python
index = train[0]
```

par :

```python
index = train[1]
```

Relancez le programme. Les scores changent parce que l’image a changé. Les paramètres, eux, sont exactement les mêmes : exécuter une prédiction ne les modifie pas.

Vous pouvez conserver cette modification ou remettre `train[0]` pour retrouver l’exemple du trois. Le script d’entraînement choisit ses propres lots et ne dépend pas de ce changement.
