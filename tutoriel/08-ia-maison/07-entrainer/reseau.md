Prenons un début de phrase : `le produit 2`. Le modèle reçoit les douze caractères et doit attribuer une probabilité à chaque caractère possible pour la suite.

![Douze identifiants de caractères deviennent douze vecteurs de douze nombres, puis une représentation de 64 nombres et enfin 75 probabilités.](image:images/modele.png)
Figure: Le réseau utilisé dans cet atelier

Chaque caractère devient un identifiant, puis un vecteur de douze nombres grâce à la table `E`. Nous réunissons ces vecteurs en 144 nombres. Une couche de 64 unités les transforme avec `tanh`, puis la couche de sortie produit 75 scores. `softmax` les convertit en probabilités.

Les tableaux `E`, `W`, `b`, `U` et `c` contiennent au total 15 055 paramètres. Les petits `b` et `c` sont des biais, ajoutés aux transformations. Ce réseau utilise une fenêtre fixe de douze caractères. Sans mécanisme d’attention, il ne peut pas revenir consulter le début d’une phrase sorti de cette fenêtre, comme le ferait un Transformer.

Dans `charger_lot`, chaque ligne donne plusieurs couples entrée/cible. Au début d’une ligne, un caractère spécial remplit les places encore vides. Une fenêtre ne passe jamais de la fin d’une ligne au début de la suivante.

Ouvrez `calculer` pour retrouver ces transformations dans le code. Les noms courts correspondent aux matrices du schéma ; les dimensions permettent de suivre les produits sans devoir deviner ce que contient chaque tableau.
