# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

import numpy as np
from threadpoolctl import threadpool_limits
from commun import donnees, graphique, SORTIES
from modele import initialiser, perte_gradient, bilan

X, y, train, validation, _ = donnees()
petit = train[:80]
y_hasard = np.random.default_rng(17).integers(0, 10, len(petit))
p = initialiser(cachee=64)
historique = []
with threadpool_limits(limits=1):
    for epoch in range(801):
        if epoch:
            _, g = perte_gradient(X[petit], y_hasard, p)
            for nom in p:
                p[nom] -= 0.3 * g[nom]
        if epoch % 20 == 0:
            _, a = bilan(X[petit], y_hasard, p)
            _, v = bilan(X[validation], y[validation], p)
            historique.append((epoch, a, v))
            if epoch % 200 == 0:
                print(f"{epoch:3d} | étiquettes arbitraires apprises : {a:.1%} | vrais chiffres de validation : {v:.1%}")
plt = graphique()
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([h[0] for h in historique], [100*h[1] for h in historique], label="80 images, étiquettes arbitraires", color="#007e80")
ax.plot([h[0] for h in historique], [100*h[2] for h in historique], label="Validation, véritables étiquettes", color="#c36b30")
ax.set(xlabel="Mises à jour", ylabel="Réponses correctes (%)", ylim=(0, 105))
ax.legend()
fig.tight_layout()
fig.savefig(SORTIES / "memorisation.png", dpi=150)
plt.close(fig)
