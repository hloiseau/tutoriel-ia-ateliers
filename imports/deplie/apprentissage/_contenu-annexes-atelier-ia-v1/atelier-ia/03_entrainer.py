import argparse
import json
import time
import numpy as np
from threadpoolctl import threadpool_limits
from commun import donnees, graphique, SORTIES
from modele import initialiser, perte_gradient, bilan

parser = argparse.ArgumentParser()
parser.add_argument("--cachee", type=int, default=0)
parser.add_argument("--epochs", type=int, default=80)
parser.add_argument("--pas", type=float, default=0.2)
parser.add_argument("--nom", default="lineaire")
args = parser.parse_args()
if args.epochs < 1 or args.cachee < 0 or not np.isfinite(args.pas) or args.pas <= 0:
    parser.error("Il faut epochs >= 1, cachee >= 0 et un pas fini strictement positif.")
if not args.nom.isidentifier():
    parser.error("Le nom doit contenir des lettres, chiffres ou soulignements, sans chemin.")
X, y, train, validation, _ = donnees()
p = initialiser(args.cachee)
rng = np.random.default_rng(7)
historique = []
debut = time.perf_counter()
# Les multiplications matricielles utilisent un seul fil CPU.
with threadpool_limits(limits=1):
    for epoch in range(args.epochs + 1):
        if epoch:
            ordre = rng.permutation(train)
            for depart in range(0, len(ordre), 64):
                lot = ordre[depart:depart + 64]
                _, gradients = perte_gradient(X[lot], y[lot], p)
                for nom in p:
                    p[nom] -= args.pas * gradients[nom]
        lt, at = bilan(X[train], y[train], p)
        lv, av = bilan(X[validation], y[validation], p)
        if not all(np.isfinite(v) for v in (lt, lv)):
            raise SystemExit("Calcul non fini : recommencez avec un pas plus petit.")
        historique.append({"epoch": epoch, "perte_train": lt, "perte_validation": lv,
                           "exactitude_train": at, "exactitude_validation": av})
        if epoch % 20 == 0 or epoch == args.epochs:
            print(f"{epoch:3d} | perte {lt:.4f} / {lv:.4f} | exactitude {at:.1%} / {av:.1%}")
duree = time.perf_counter() - debut
np.savez_compressed(SORTIES / f"{args.nom}.npz", **p)
rapport = {"reglages": vars(args), "secondes_calcul": duree, "historique": historique}
(SORTIES / f"{args.nom}.json").write_text(json.dumps(rapport, indent=2))
plt = graphique()
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for prefix, label, color in [("train", "Entraînement", "#007e80"),
                             ("validation", "Validation", "#c36b30")]:
    axes[0].plot([h["epoch"] for h in historique], [h[f"perte_{prefix}"] for h in historique], label=label, color=color)
    axes[1].plot([h["epoch"] for h in historique], [100*h[f"exactitude_{prefix}"] for h in historique], label=label, color=color)
axes[0].set_ylabel("Perte moyenne")
axes[1].set_ylabel("Réponses correctes (%)")
for a in axes:
    a.set_xlabel("Passages sur l’entraînement (epochs)")
    a.legend()
fig.tight_layout()
fig.savefig(SORTIES / f"{args.nom}-courbes.png", dpi=150)
plt.close(fig)
print(f"Calcul : {duree:.3f} s ; modèle : sorties/{args.nom}.npz")
