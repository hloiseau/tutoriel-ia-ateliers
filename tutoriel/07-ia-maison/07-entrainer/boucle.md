Lancez cette fois la commande sans `--base` :

```bash
python petit_modele.py entrainer --pas 1200 --sortie sorties/depuis-zero
```

Le programme initialise les paramètres, lit le corpus de base et effectue 1 200 mises à jour. À chaque pas, il sélectionne un petit lot de fenêtres, prédit les caractères suivants, calcule la perte et ajuste les paramètres.

La perte pénalise les probabilités trop faibles attribuées aux caractères attendus. La rétropropagation calcule comment chaque paramètre contribue à cette erreur. L’optimiseur Adam utilise ces gradients pour choisir les mises à jour. Ici, leurs calculs sont écrits avec NumPy ; les tests comparent également quelques gradients à des variations numériques de la perte.

Regardez `rapport.json`. Dans l’exécution fournie, la perte de validation passe d’environ 4,31 à 0,17. Le réseau a donc appris des régularités de nos phrases à partir des exemples, sans que nous inscrivions à la main chaque probabilité de caractère dans ses poids. La courbe est encourageante ; le texte généré va nous dire jusqu’où.

Pour rejouer l’essai avec moins de pas, choisissez un autre dossier de sortie. Comparez alors la validation et les échantillons. Gardez le test pour évaluer le réglage finalement retenu ; sinon, il devient progressivement un deuxième lot de validation.

La graine aléatoire et les versions des dépendances sont indiquées dans les fichiers. Gardez-les avec vos résultats : elles facilitent la comparaison entre essais, même si deux environnements ne produisent pas forcément chaque valeur à l’identique.
