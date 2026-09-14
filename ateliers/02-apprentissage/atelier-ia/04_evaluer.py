# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

import argparse
import json
import numpy as np
from threadpoolctl import threadpool_limits
from sklearn.metrics import confusion_matrix
from commun import donnees, graphique, SORTIES
from modele import probabilites

parser = argparse.ArgumentParser()
parser.add_argument("--nom", default="lineaire")
args = parser.parse_args()
if not args.nom.isidentifier():
    parser.error("Nom de modèle invalide.")
chemin = SORTIES / f"{args.nom}.npz"
if not chemin.exists():
    raise SystemExit("Modèle absent : lancez d'abord 03_entrainer.py avec ce nom.")
with np.load(chemin, allow_pickle=False) as archive:
    p = {k: archive[k] for k in archive.files}
X, y, _, _, test = donnees()
with threadpool_limits(limits=1):
    proba = probabilites(X[test], p)
pred = proba.argmax(1)
correct = int(np.sum(pred == y[test]))
print(f"Test : {correct}/{len(test)} réponses correctes ({correct / len(test):.1%})")
cm = confusion_matrix(y[test], pred, labels=np.arange(10))
plt = graphique()
fig, a = plt.subplots(figsize=(7, 6))
a.imshow(cm, cmap="Blues")
for i in range(10):
    for j in range(10):
        a.text(j, i, str(cm[i, j]), ha="center", va="center", color="white" if cm[i, j] > cm.max()/2 else "#233844")
a.set(xticks=range(10), yticks=range(10), xlabel="Chiffre prédit", ylabel="Étiquette attendue")
fig.tight_layout()
fig.savefig(SORTIES / f"{args.nom}-confusions.png", dpi=150)
plt.close(fig)
erreurs = np.flatnonzero(pred != y[test])
fig, axes = plt.subplots(2, 4, figsize=(10, 5))
for a in axes.flat:
    a.axis("off")
for a, i in zip(axes.flat, erreurs[:8]):
    a.imshow(X[test[i]].reshape(8, 8), cmap="gray", vmin=0, vmax=1)
    a.set_title(f"Attendu {y[test[i]]} → prédit {pred[i]}\nScore {proba[i, pred[i]]:.0%}")
fig.tight_layout()
fig.savefig(SORTIES / f"{args.nom}-erreurs.png", dpi=150)
plt.close(fig)
(SORTIES / f"{args.nom}-test.json").write_text(json.dumps({"correct": correct, "total": len(test), "confusions": cm.tolist()}, indent=2))
