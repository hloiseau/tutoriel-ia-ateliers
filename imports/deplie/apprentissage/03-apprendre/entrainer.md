Lancez :

```bash
python 03_entrainer.py
```

Le programme mélange les indices d’entraînement, traite les images par lots de 64, puis recommence. Un passage sur toutes les images d’entraînement s’appelle une **epoch**. Nous en effectuons 80.

Voici les lignes obtenues. De chaque côté de la barre oblique, vous retrouvez l’entraînement puis la validation :

```text
0 | perte 2.2987 / 2.2985 | exactitude 10.3% / 10.3%
 20 | perte 0.3363 / 0.3716 | exactitude 94.6% / 95.0%
 40 | perte 0.2290 / 0.2651 | exactitude 95.7% / 95.0%
 60 | perte 0.1853 / 0.2213 | exactitude 96.4% / 95.0%
 80 | perte 0.1600 / 0.1973 | exactitude 97.2% / 95.0%
Calcul : 0.107 s ; modèle : sorties/lineaire.npz
```

La ligne zéro montre l’état avant les mises à jour. À la ligne 80, la perte d’entraînement a beaucoup diminué et 97,2 % des images d’entraînement sont bien classées. La validation est à 95,0 %.

Ouvrez `sorties/lineaire-courbes.png` :

![Courbes mesurées de perte et d’exactitude pour l’entraînement et la validation du modèle linéaire.](image:images/lineaire-courbes.png)
Figure: Les courbes sont calculées sur les mêmes groupes après chaque passage d’entraînement.

Regardez le graphique de droite : le résultat de validation reste souvent à 95 %, alors que sa perte continue à diminuer. Certaines probabilités s’améliorent sans changer le chiffre choisi. C’est pourquoi les deux mesures racontent des choses différentes.

Le programme a écrit `sorties/lineaire.npz`. Ce fichier contient les poids et les biais. `sorties/lineaire.json` contient les réglages, la durée du calcul et les valeurs des courbes.

Essayez maintenant un entraînement plus court, en conservant le premier modèle :

```bash
python 03_entrainer.py --epochs 20 --nom court
```

Vous obtenez `court.npz` et ses propres courbes. Comparez-les à celles de `lineaire`. Le nom différent empêche d’écraser notre premier résultat.

Chaque lancement repart de l’initialisation. Cette commande ne prolonge pas l’entraînement du modèle précédent.
