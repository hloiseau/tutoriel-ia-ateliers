Dans `03_entrainer.py`, la sauvegarde se fait avec :

```python
np.savez_compressed(SORTIES / f"{args.nom}.npz", **p)
```

Le format NPZ rassemble les tableaux NumPy dans une archive compressée. Les clés `W` et `b` deviennent les noms des tableaux du modèle linéaire.[^p2-5-sauvegarde-save]

Dans `05_lire_dessin.py`, nous les rechargeons :

```python
with np.load(chemin, allow_pickle=False) as archive:
    p = {k: archive[k] for k in archive.files}
```

Nous utilisons uniquement des tableaux de nombres, sans charger d’objets Python sérialisés. Le fichier `lineaire.npz` obtenu ici pèse environ 5,3 Kio. Nos 650 paramètres tiennent facilement dedans.

Fermez le terminal, ouvrez-en un autre, réactivez l’environnement et relancez la commande de lecture du dessin. Vous n’avez pas besoin de relancer l’entraînement.

Cette étape s’appelle l’**inférence** : nous utilisons les paramètres existants pour calculer une réponse. Montrer un nouveau dessin au programme ne modifie pas ces paramètres.

Si vous souhaitez ensuite lui faire apprendre vos dessins, il faudra aussi leur associer les bonnes étiquettes, les intégrer à un protocole d’entraînement et évaluer le résultat sur d’autres exemples. Accumuler seulement les dessins sur lesquels on vient de corriger une erreur ne fournit pas, à lui seul, un nouveau test indépendant.


[^p2-5-sauvegarde-save]: [NumPy, savez_compressed](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html).
