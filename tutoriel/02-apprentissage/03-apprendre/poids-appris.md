L’image du trois qui était mal reconnue avant l’entraînement reçoit maintenant une probabilité de 99,4 % pour la classe trois.

![La même image de trois, avec les probabilités avant et après entraînement.](image:images/avant-apres.png)
Figure: Comparaison sur une image appartenant à l’entraînement.

Pour écrire les graphiques de comparaison et les cartes des poids, lancez :

```bash
python 11_figures.py
```

Ouvrez `sorties/poids.png`. Les 64 poids de chaque chiffre y sont rangés en une grille de 8 × 8 :

![Dix cartes de poids appris, une pour chaque score de chiffre. Les valeurs positives sont bleues et les négatives rouges.](image:images/poids.png)
Figure: Poids du modèle linéaire. Un pixel clair placé sur une zone bleue augmente le score correspondant ; sur une zone rouge, il le diminue.

Ce ne sont pas dix photographies mémorisées. Ce sont les coefficients utilisés dans nos multiplications. Certaines positions favorisent un chiffre, d’autres le défavorisent.

Le modèle sépare maintenant les classes à partir de ces positions. Rien dans ce calcul ne lui enseigne que « deux boucles superposées font un huit » ou qu’un chiffre garde son identité lorsqu’on le déplace. Nous allons justement essayer de le déplacer.
