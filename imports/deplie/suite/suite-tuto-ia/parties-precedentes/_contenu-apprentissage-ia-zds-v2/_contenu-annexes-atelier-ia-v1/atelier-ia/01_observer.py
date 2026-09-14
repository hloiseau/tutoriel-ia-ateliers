import json
from commun import donnees, graphique, SORTIES

X, y, train, validation, test = donnees()
print(f"Images : {len(X)} ; pixels par image : {X.shape[1]}")
print(f"Entraînement : {len(train)} ; validation : {len(validation)} ; test : {len(test)}")
print(f"Valeurs normalisées : {X.min():.1f} à {X.max():.1f}")
plt = graphique()
fig, axes = plt.subplots(2, 5, figsize=(10, 4.5))
for chiffre, axe in enumerate(axes.flat):
    index = next(i for i in train if y[i] == chiffre)
    axe.imshow(X[index].reshape(8, 8), cmap="gray", vmin=0, vmax=1)
    axe.set_title(f"Étiquette : {chiffre}")
    axe.axis("off")
fig.tight_layout()
fig.savefig(SORTIES / "chiffres.png", dpi=150)
plt.close(fig)
index = int(train[0])
(SORTIES / "exemple.json").write_text(json.dumps({"pixels": X[index].reshape(8, 8).tolist()}))
print(f"exemple.json : chiffre {y[index]}, provenant de l'entraînement")
print("Image écrite : sorties/chiffres.png")
