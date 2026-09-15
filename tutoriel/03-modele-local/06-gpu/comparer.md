Arrêtez le serveur CPU. Dans sa commande, retirez `--device none` et remplacez `-ngl 0` par `-ngl all`. Conservez le fichier GGUF, la taille de contexte, le nombre de requêtes simultanées et les autres paramètres.

Regardez les messages de démarrage : le moteur doit indiquer le placement des couches sur le GPU. Une commande qui accepte une option n’est pas une preuve que tout le calcul a été placé où vous l’imaginez.

Relancez la série :

```bash
python mesurer.py --nom gpu-contexte2048
```

Notez la commande exacte et la mémoire vidéo observée. Comparez les durées aux essais CPU et relisez les réponses. Nous utilisons un modèle minuscule à l’échelle de certaines cartes : cette comparaison ne permettra pas de prévoir le gain pour tous les modèles ou toutes les tailles de requêtes.

Une RTX 3090 Ti avec 24 Go de mémoire vidéo permet d’envisager des expériences plus grandes que celle-ci, mais il faut toujours tenir compte du modèle, de sa précision, du contexte et de la mémoire déjà occupée. Il n’y a pas de correspondance universelle « tant de Go = tel modèle sans aucune contrainte ».

Avant de télécharger plus gros, choisissez ce que vous voulez améliorer dans votre grille d’évaluation. Sinon, il est assez facile de passer la soirée à remplir un disque sans avoir avancé sur son besoin.
