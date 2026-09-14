import argparse
import json
from pathlib import Path
import numpy as np
from commun import SORTIES, graphique
from modele import probabilites

parser = argparse.ArgumentParser()
parser.add_argument("dessin", type=Path)
parser.add_argument("--nom", default="lineaire")
args = parser.parse_args()
if not args.nom.isidentifier():
    parser.error("Nom de modèle invalide.")
try:
    document = json.loads(args.dessin.read_text(encoding="utf-8"))
    pixels = np.asarray(document["pixels"], dtype=np.float64)
    if pixels.shape != (8, 8) or not np.isfinite(pixels).all() or pixels.min() < 0 or pixels.max() > 1:
        raise ValueError("Il faut une grille de 8 × 8 nombres finis entre 0 et 1.")
except (OSError, ValueError, KeyError, TypeError) as erreur:
    raise SystemExit(f"Dessin invalide : {erreur}")
chemin = SORTIES / f"{args.nom}.npz"
if not chemin.exists():
    raise SystemExit("Modèle absent : lancez d'abord 03_entrainer.py.")
with np.load(chemin, allow_pickle=False) as archive:
    p = {k: archive[k] for k in archive.files}
proba = probabilites(pixels.reshape(1, 64), p)[0]
for chiffre in np.argsort(proba)[::-1][:3]:
    print(f"Chiffre {chiffre} : {proba[chiffre]:.1%}")
plt = graphique()
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].imshow(pixels, cmap="gray", vmin=0, vmax=1)
axes[0].set_title("Votre grille")
axes[0].axis("off")
axes[1].bar(range(10), proba, color="#007e80")
axes[1].set(xticks=range(10), ylim=(0, 1), xlabel="Chiffre", ylabel="Probabilité du modèle")
fig.tight_layout()
fig.savefig(SORTIES / "dessin-resultat.png", dpi=150)
plt.close(fig)
