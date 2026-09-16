# 5. Préparer ce que notre modèle va apprendre

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Assembler notre assistant documentaire](../04-application/LECTURE.md) · [Suivant : Ajouter un petit adaptateur](../06-adaptateurs/LECTURE.md)

**TL;DR** — Nous quittons SmolLM2 pour un réseau de caractères assez petit pour être entraîné sur CPU. Avant de toucher à ses poids, nous séparons les données d’entraînement, de validation et de test.

Les réponses précédentes venaient du modèle local de la partie 3. Pour observer un entraînement sans carte graphique, nous passons maintenant à un autre réseau, beaucoup plus petit : son code tient dans un fichier et nous pourrons recommencer les essais autant que nécessaire.

## Un terrain de jeu que nous maîtrisons

Ouvrez `donnees/langage/base-train.txt`, puis `adaptation-train.txt`. Le premier contient des phrases de notre service fictif. Le second exprime des situations sous forme de lignes de journal :

```text
INFO produit=... prix=... stock=oui decision=...
```
Code: Forme du deuxième corpus ; les points de suspension représentent ici les valeurs

Ces textes ont été fabriqués à partir de quelques gabarits. Les journaux montrent une forme d’écriture ; aucun service n’a réellement exécuté les décisions qu’ils racontent. Nous pourrons mesurer si le modèle apprend cette forme, pas lui attribuer la maîtrise de toutes les règles métier.

Les caractères sont volontairement simples et sans accents. Le vocabulaire fixé dans le code contient 75 caractères, dont un caractère de remplissage. Nous ne sommes plus en train d’adapter SmolLM2 : `petit_modele.py` décrit un autre réseau, créé pour cet atelier.

Ces exemples nous appartiennent et leur licence est fournie. Avec des données réelles, le travail commencerait déjà ici : a-t-on le droit de les utiliser ? Contiennent-elles des données personnelles, des secrets ou des réponses erronées ? Ajouter des milliers de lignes ne réparera pas un corpus incohérent.

## Séparer les exemples avant de les découper

Lancez l’audit :

```bash
python auditer_donnees.py
```

Pour chacun des deux formats, nous avons 180 lignes d’entraînement, 30 de validation et 30 de test. Les identifiants sont répartis avant de fabriquer les fenêtres de caractères : les groupes 10 à 69 servent à l’entraînement, 70 à 79 à la validation et 80 à 89 au test.

Pourquoi cet ordre ? Si nous découpions d’abord une phrase en fenêtres presque identiques, puis les répartissions au hasard, le test pourrait présenter au modèle des morceaux qu’il a déjà vus à un caractère près. Ce serait un examen un peu arrangeant.

L’audit vérifie l’absence de lignes et d’identifiants communs entre les lots. Regardez néanmoins les trois fichiers : ils reprennent les mêmes gabarits. Notre test mesure donc un apprentissage très limité, sur des formes proches.

L’entraînement lit le lot `train`. Pendant le développement, la validation permet d’observer l’évolution et de choisir les réglages. Nous n’ouvrons le test qu’une fois l’essai fixé. Si ses erreurs vous conduisent ensuite à modifier les réglages, il rejoint de fait vos données de développement : prévoyez de nouveaux exemples pour l’évaluation finale.

## Partir d’un premier modèle déjà entraîné

Le dossier `resultats-reference/base` contient les poids d’un modèle entraîné sur le premier corpus. Nous referons cet entraînement depuis zéro au chapitre 7. Pour l’instant, essayons ce qu’il produit :

```bash
python petit_modele.py generer --modele resultats-reference/base/modele.npz
```

Le résultat commence comme une phrase du corpus, puis déraille. Gardez-le sous les yeux : ce modèle de départ sait reproduire quelques régularités, pas écrire une réponse que nous pourrions confier à une application.

Nous allons lui faire apprendre les lignes `INFO`. Une première possibilité consiste à continuer l’entraînement en autorisant la modification de tous ses paramètres : c’est ici notre **adaptation complète**.

```bash
python petit_modele.py entrainer --base resultats-reference/base/modele.npz --mode complet --corpus adaptation --pas 800 --sortie sorties/complet
```

Le dossier de sortie doit être nouveau. Il recevra les poids, le rapport et un échantillon généré. Les poids de départ restent dans leur dossier d’origine ; nous pouvons donc toujours revenir à eux.

Cette commande nous donnera un premier résultat. Nous le comparerons à une adaptation beaucoup plus petite, qui entraîne seulement 556 paramètres.

Nous avons séparé les lots et produit une première adaptation qui peut modifier les 15 055 paramètres. Essayons maintenant d’obtenir une correction avec 556 paramètres entraînables, ajoutés à une base figée.

---

[Précédent : Assembler notre assistant documentaire](../04-application/LECTURE.md) · [Suivant : Ajouter un petit adaptateur](../06-adaptateurs/LECTURE.md)
