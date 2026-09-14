import numpy as np
from commun import donnees
from modele import initialiser, probabilites

X, y, train, _, _ = donnees()
p = initialiser()
index = train[0]
probas = probabilites(X[index:index + 1], p)[0]
print(f"Étiquette attendue : {y[index]}")
print("Probabilités :", np.round(probas, 3))
print("Classe choisie :", probas.argmax())
print("Paramètres :", sum(v.size for v in p.values()))
print(f"Exactitude avant entraînement : {np.mean(probabilites(X[train], p).argmax(1) == y[train]):.1%}")
