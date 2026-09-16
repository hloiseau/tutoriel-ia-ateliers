Arrêtez le serveur CPU. Dans sa commande, retirez `--device none` et remplacez `-ngl 0` par `-ngl all`. Conservez le fichier GGUF, la taille de contexte, le nombre de requêtes simultanées et les autres paramètres.

Regardez les messages de démarrage : le moteur doit indiquer le placement des couches sur le GPU. C’est ce journal, puis l’activité de la carte, qui nous dira si l’option a produit l’effet attendu.

Relancez la série :

```bash
python mesurer.py --nom gpu-contexte2048
```

Notez la commande exacte et la mémoire vidéo observée. Comparez les durées aux essais CPU et relisez les réponses. Avec ce modèle de 360 millions de paramètres et ces courtes requêtes, les résultats décriront cette expérience précise. Un modèle plus grand ou un contexte plus long changeraient le travail demandé à la carte.

Une RTX 3090 Ti avec 24 Go de mémoire vidéo permet d’envisager des expériences plus grandes que celle-ci. Avant de choisir la suivante, comptez le modèle, sa précision, le contexte et la mémoire déjà occupée : la capacité de la carte ne suffit pas à désigner un modèle universellement adapté.

Avant de télécharger plus gros, choisissez ce que vous voulez améliorer dans votre grille d’évaluation. Sinon, il est assez facile de passer la soirée à remplir un disque sans avoir avancé sur son besoin.
