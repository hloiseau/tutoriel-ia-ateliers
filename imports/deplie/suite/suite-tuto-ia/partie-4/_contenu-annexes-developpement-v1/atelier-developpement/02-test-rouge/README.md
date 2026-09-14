# Atelier de suivi de prix

Python 3.12, bibliothèque standard uniquement. Aucun compte ni service distant.

```bash
python -m unittest discover -v
python suivi.py scenarios/retour-stock.json
```

Le programme affiche une décision en JSON. Il n’envoie aucune notification.

Le prix est en centimes, pour une seule devise implicite. Les changements de devise et les historiques de plusieurs observations ne font pas partie du modèle.
