# 5. Préparer ce que notre modèle va apprendre

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Assembler notre assistant documentaire](../04-application/LECTURE.md) · [Suivant : Ajouter un petit adaptateur](../06-adaptateurs/LECTURE.md)

**TL;DR** — Nous changeons de modèle pour pouvoir expérimenter sur CPU. Avant de toucher aux poids, nous séparons les données d’entraînement, de validation et de test.

Entraîner un grand modèle n’est pas nécessaire pour voir comment un réseau apprend. Nous allons utiliser un modèle de caractères suffisamment petit pour lire son code et recommencer nos essais.

## Un terrain de jeu que nous maîtrisons

Ouvrez `donnees/langage/base-train.txt`, puis `adaptation-train.txt`. Le premier contient des phrases de notre service fictif. Le second exprime des situations sous forme de lignes de journal :

```text
INFO produit=... prix=... stock=oui decision=...
```
Code: Forme du deuxième corpus ; les points de suspension représentent ici les valeurs

Ces textes ont été fabriqués à partir de quelques gabarits. Les journaux sont des exemples d’écriture, pas les traces d’un service qui aurait réellement exécuté ces décisions. Notre objectif sera d’apprendre une forme de texte ; ce jeu ne permet pas de conclure que le modèle sait appliquer toutes les règles métier.

Les caractères sont volontairement simples et sans accents. Le vocabulaire fixé dans le code contient 75 caractères, dont un caractère de remplissage. Nous ne sommes plus en train d’adapter SmolLM2 : `petit_modele.py` décrit un autre réseau, créé pour cet atelier.

Ces exemples nous appartiennent et leur licence est fournie. Avec des données réelles, cette étape demanderait déjà du travail : a-t-on le droit de les utiliser, contiennent-elles des données personnelles, des secrets, des réponses erronées ? Plus de lignes n’améliorent pas forcément un mauvais corpus.

## Séparer les exemples avant de les découper

Lancez l’audit :

```bash
python auditer_donnees.py
```

Pour chacun des deux formats, nous avons 180 lignes d’entraînement, 30 de validation et 30 de test. Les identifiants sont répartis avant de fabriquer les fenêtres de caractères : les groupes 10 à 69 servent à l’entraînement, 70 à 79 à la validation et 80 à 89 au test.

Pourquoi cet ordre ? Si nous découpions d’abord une phrase en fenêtres presque identiques, puis les répartissions au hasard, le test pourrait présenter au modèle des morceaux qu’il a déjà vus à un caractère près. Ce serait un examen un peu arrangeant.

L’audit vérifie l’absence de lignes et d’identifiants communs entre les lots. Il ne rend pas pour autant notre test difficile : les mêmes gabarits restent présents dans les trois lots. Nous mesurons donc un apprentissage très limité, sur des formes proches.

L’entraînement lit le lot `train`. La validation sert à observer l’évolution et à choisir les réglages lors du développement. Le test est lu séparément, une fois l’essai fixé. Si vous adaptez vos réglages après avoir étudié ses erreurs, prévoyez ensuite de nouveaux exemples pour l’évaluation finale.

## Partir d’un premier modèle déjà entraîné

Le dossier `resultats-reference/base` contient les poids d’un modèle entraîné sur le premier corpus. Nous referons cet entraînement depuis zéro au chapitre 7. Pour l’instant, essayons ce qu’il produit :

```bash
python petit_modele.py generer --modele resultats-reference/base/modele.npz
```

Le résultat commence comme une phrase du corpus, puis finit par dérailler. C’est normal au sens où nous observons les limites de cette expérience ; ce n’est pas une réponse que nous devrions accepter dans une application.

Nous allons lui faire apprendre les lignes `INFO`. Une première possibilité consiste à continuer l’entraînement en autorisant la modification de tous ses paramètres : c’est ici notre **adaptation complète**.

```bash
python petit_modele.py entrainer --base resultats-reference/base/modele.npz --mode complet --corpus adaptation --pas 800 --sortie sorties/complet
```

Le dossier de sortie doit être nouveau. Il recevra les poids, le rapport et un échantillon généré. Les poids de départ restent dans leur dossier d’origine ; nous pouvons donc toujours revenir à eux.

Cette commande ne garantit pas que le modèle deviendra bon. Elle nous donne un premier résultat auquel comparer une adaptation plus petite, avec beaucoup moins de paramètres entraînables.

Nous avons un corpus, une séparation des lots et une première adaptation complète. Voyons maintenant comment changer le comportement du modèle en laissant ses paramètres de départ figés.

---

[Précédent : Assembler notre assistant documentaire](../04-application/LECTURE.md) · [Suivant : Ajouter un petit adaptateur](../06-adaptateurs/LECTURE.md)
