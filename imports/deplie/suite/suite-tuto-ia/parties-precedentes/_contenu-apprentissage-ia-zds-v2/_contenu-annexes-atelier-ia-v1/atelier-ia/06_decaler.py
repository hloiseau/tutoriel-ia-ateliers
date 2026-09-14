import numpy as np
from commun import donnees, graphique, SORTIES
from modele import probabilites

chemin = SORTIES / "lineaire.npz"
if not chemin.exists():
    raise SystemExit("Lancez d'abord 03_entrainer.py.")
with np.load(chemin, allow_pickle=False) as archive:
    p = {k: archive[k] for k in archive.files}
X, y, _, validation, _ = donnees()
images = X[validation].reshape(-1, 8, 8)
decalees = np.zeros_like(images)
decalees[:, :, 1:] = images[:, :, :-1]
a = probabilites(X[validation], p).argmax(1)
b = probabilites(decalees.reshape(-1, 64), p).argmax(1)
print(f"Validation d'origine : {np.mean(a == y[validation]):.1%}")
print(f"Décalée d'un pixel à droite : {np.mean(b == y[validation]):.1%}")
indices = np.flatnonzero((a == y[validation]) & (b != y[validation]))[:4]
plt = graphique()
fig, axes = plt.subplots(2, 4, figsize=(10, 5))
for ax in axes.flat:
    ax.axis("off")
for colonne, i in enumerate(indices):
    for ligne, image, pred in [(0, images[i], a[i]), (1, decalees[i], b[i])]:
        axes[ligne, colonne].imshow(image, cmap="gray", vmin=0, vmax=1)
        axes[ligne, colonne].set_title(f"Attendu {y[validation[i]]} → prédit {pred}")
fig.tight_layout()
fig.savefig(SORTIES / "decalage.png", dpi=150)
plt.close(fig)
