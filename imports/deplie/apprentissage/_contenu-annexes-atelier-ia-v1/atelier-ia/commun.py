from pathlib import Path
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

RACINE = Path(__file__).resolve().parent
SORTIES = RACINE / "sorties"
SORTIES.mkdir(exist_ok=True)


def donnees():
    chiffres = load_digits()
    # L'échelle 0..16 appartient au format des données, elle n'est pas apprise.
    X = chiffres.data.astype(np.float64) / 16.0
    y = chiffres.target
    indices = np.arange(len(y))
    developpement, test = train_test_split(
        indices, test_size=0.20, random_state=42, stratify=y
    )
    train, validation = train_test_split(
        developpement, test_size=0.25, random_state=42,
        stratify=y[developpement]
    )
    return X, y, train, validation, test


def graphique():
    import matplotlib
    matplotlib.use("Agg")  # Écrit des images ; aucune fenêtre à configurer.
    import matplotlib.pyplot as plt
    plt.rcParams.update({"figure.facecolor": "#f5f3ed", "axes.facecolor": "#f5f3ed"})
    return plt
