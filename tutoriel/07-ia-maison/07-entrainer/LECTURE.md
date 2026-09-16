# 7. Entraîner notre réseau depuis zéro

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Ajouter un petit adaptateur](../06-adaptateurs/LECTURE.md) · [Suivant : Choisir la suite sans changer de machine par défaut](../08-comparer/LECTURE.md)

**TL;DR** — Notre réseau prédit le prochain caractère à partir des douze précédents. Nous allons partir de nombres aléatoires, entraîner ses 15 055 paramètres, puis regarder où il échoue.

Tout le modèle tient dans `petit_modele.py`. Il n’a ni outils, ni mémoire documentaire, ni capacité particulière à développer un logiciel. Il nous permet en revanche de voir l’entraînement à une échelle accessible.

## Douze caractères pour deviner le suivant

Prenons un début de phrase : `le produit 2`. Le modèle reçoit les douze caractères et doit attribuer une probabilité à chaque caractère possible pour la suite.

![Douze identifiants de caractères deviennent douze vecteurs de douze nombres, puis une représentation de 64 nombres et enfin 75 probabilités.](../images/modele.png)
Figure: Le réseau utilisé dans cet atelier

Chaque caractère devient un identifiant, puis un vecteur de douze nombres grâce à la table `E`. Nous réunissons ces vecteurs en 144 nombres. Une couche de 64 unités les transforme avec `tanh`, puis la couche de sortie produit 75 scores. `softmax` les convertit en probabilités.

Les tableaux `E`, `W`, `b`, `U` et `c` contiennent au total 15 055 paramètres. Les petits `b` et `c` sont des biais, ajoutés aux transformations. C’est un réseau à fenêtre fixe, pas un Transformer : il n’a aucun mécanisme d’attention et ne peut pas examiner le début d’une phrase situé au-delà de ses douze caractères d’entrée.

Dans `charger_lot`, chaque ligne donne plusieurs couples entrée/cible. Au début d’une ligne, un caractère spécial remplit les places encore vides. Une fenêtre ne passe jamais de la fin d’une ligne au début de la suivante.

Ouvrez `calculer` pour retrouver ces transformations dans le code. Les noms courts correspondent aux matrices du schéma ; les dimensions permettent de suivre les produits sans devoir deviner ce que contient chaque tableau.

## Des nombres aléatoires aux premières régularités

Lancez cette fois la commande sans `--base` :

```bash
python petit_modele.py entrainer --pas 1200 --sortie sorties/depuis-zero
```

Le programme initialise les paramètres, lit le corpus de base et effectue 1 200 mises à jour. À chaque pas, il sélectionne un petit lot de fenêtres, prédit les caractères suivants, calcule la perte et ajuste les paramètres.

La perte pénalise les probabilités trop faibles attribuées aux caractères attendus. La rétropropagation calcule comment chaque paramètre contribue à cette erreur. L’optimiseur Adam utilise ces gradients pour choisir les mises à jour. Ici, leurs calculs sont écrits avec NumPy ; les tests comparent également quelques gradients à des variations numériques de la perte.

Regardez `rapport.json`. Dans l’exécution fournie, la perte de validation passe d’environ 4,31 à 0,17. Le réseau a appris des régularités de nos phrases. Nous n’avons pas inscrit à la main chaque probabilité de caractère dans ses poids.

Pour rejouer l’essai avec moins de pas, choisissez un autre dossier de sortie. Comparez alors la validation et les échantillons. Gardez le test pour évaluer le réglage finalement retenu ; sinon, il devient progressivement un deuxième lot de validation.

La graine aléatoire et les versions des dépendances sont indiquées dans les fichiers. Elles rendent les essais plus faciles à reproduire, sans promettre une identité numérique sur toutes les machines.

## Pourquoi une petite perte peut produire du charabia

Ouvrez `echantillon.txt`. L’échantillon fourni commence ainsi :

```text
le produit 27 revient en stock. son prix reste a 50 centimes. le service prepare une notification.
```
Code: Début réellement généré par notre modèle de base

La phrase ressemble à notre corpus, mais son sens pose déjà problème : elle prépare une notification après un simple retour en stock à prix inchangé. Puis la génération se détériore. Avec l’adaptateur, l’échantillon commence par `INFO produit=28 prix=44`, avant de partir lui aussi dans une suite incohérente.

Comment peut-on obtenir cela avec une perte en baisse ? Pendant l’évaluation, nous donnons au modèle les **vrais caractères précédents**. Pendant la génération, il reçoit progressivement ses **propres caractères produits**. Une erreur peut donc l’amener dans un contexte qu’il a peu rencontré, puis en provoquer d’autres.

Ajoutons la courte fenêtre, le petit réseau et les gabarits très répétitifs : nous sommes loin d’un assistant capable de comprendre notre service. La génération tire aussi les caractères selon les probabilités produites, avec une graine fixée pour nos échantillons.

Notre essai a réussi à entraîner un modèle et à changer ses prédictions. Il n’a pas produit un générateur fiable de règles ou de journaux. Conserver les deux observations nous évite de transformer une courbe encourageante en promesse que les sorties ne tiennent pas.

Nous avons entraîné de vrais paramètres, mais sur une tâche volontairement minuscule. Voyons maintenant ce que cette expérience permet de préparer sur une autre machine, et ce qu’elle ne permet pas de promettre.

---

[Précédent : Ajouter un petit adaptateur](../06-adaptateurs/LECTURE.md) · [Suivant : Choisir la suite sans changer de machine par défaut](../08-comparer/LECTURE.md)
