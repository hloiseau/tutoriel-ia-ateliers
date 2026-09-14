import numpy as np
from commun import graphique, SORTIES

# Quatre positions ; vecteurs choisis à la main pour observer le calcul.
Q = np.array([[1., 0.], [0., 1.], [1., 1.], [1., -1.]])
K = Q.copy()
V = np.array([[1., 0.], [0., 1.], [2., 1.], [1., 2.]])
scores = Q @ K.T / np.sqrt(K.shape[1])
# À la position i, seules les positions <= i sont accessibles.
futur = np.triu(np.ones(scores.shape, dtype=bool), k=1)
scores[futur] = -np.inf
exponentielles = np.exp(scores - scores.max(axis=1, keepdims=True))
attention = exponentielles / exponentielles.sum(axis=1, keepdims=True)
resultat = attention @ V
print("Poids d'attention :")
print(np.round(attention, 3))
print("Valeurs combinées :")
print(np.round(resultat, 3))
plt = graphique()
fig, ax = plt.subplots(figsize=(6, 5))
ax.imshow(attention, cmap="Blues", vmin=0, vmax=1)
for i in range(4):
    for j in range(4):
        ax.text(j, i, f"{attention[i,j]:.2f}", ha="center", va="center", color="white" if attention[i,j] > .5 else "#233844")
ax.set(xticks=range(4), yticks=range(4), xlabel="Position consultée", ylabel="Position qui calcule")
fig.tight_layout()
fig.savefig(SORTIES / "attention.png", dpi=150)
plt.close(fig)
