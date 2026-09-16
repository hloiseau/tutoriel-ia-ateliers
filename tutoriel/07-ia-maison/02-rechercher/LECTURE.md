# 2. Construire une recherche dans nos documents

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Choisir ce que l’on veut modifier](../01-choisir/LECTURE.md) · [Suivant : Évaluer les sources avant les réponses](../03-evaluer/LECTURE.md)

**TL;DR** — Nous allons découper les textes, comparer leurs mots à ceux de la question et conserver les références des passages sélectionnés.

Un document entier peut contenir la bonne information et beaucoup d’autres choses. Essayons de ramener seulement le morceau dont nous avons besoin.

## Garder des morceaux que l’on peut retrouver

Ouvrez `recherche.py` et regardez `charger`. La fonction lit le catalogue des documents, exclut ceux qui sont archivés, puis sépare les textes en paragraphes. Nos pages sont petites et leurs paragraphes portent chacun une idée ; cette découpe suffit pour commencer.

Chaque passage conserve un identifiant comme `notification#2`, son texte, son fichier, son statut, sa révision et l’empreinte du document. Le `#2` désigne le deuxième paragraphe dans cette version. Si nous insérons un nouveau paragraphe, les numéros peuvent changer : c’est pour cela que le journal conserve aussi le texte et la version consultés.

Un morceau trop court pourrait perdre sa condition. Séparer « une remise en stock » de « à prix égal » ferait disparaître précisément ce qui nous intéresse. Un morceau trop long ramènerait des règles sans rapport avec la question. La découpe se juge donc en lisant les passages obtenus.

Le statut est traité **avant** le classement : l’ancienne règle de notification ne doit pas gagner simplement parce qu’elle répète les mots de la question. Nous conservons en revanche le document « à arbitrer », car dire qu’une décision manque est une information utile.

## Des mots à un score de recherche

Commençons par une recherche rudimentaire. Créez `ma_recherche.py` à côté de `recherche.py` et écrivez :

```python
from recherche import charger, mots

question = "remise en stock à prix égal"
attendus = set(mots(question))
for passage in charger():
    communs = attendus & set(mots(passage["texte"]))
    if communs:
        print(len(communs), passage["id"], sorted(communs))
```

Lancez `python ma_recherche.py`. La fonction `mots` du module fourni normalise la casse et les accents, puis écarte quelques mots fréquents comme « le » et « des ». Vous voyez les mots communs qui ont fait remonter chaque passage.

Compter les intersections traite pourtant tous les mots de la même manière. Un terme présent partout distingue peu les documents. Le classement livré dans `Index` utilise **TF-IDF** : la fréquence dans le passage est pondérée par la rareté du mot dans le corpus. Les vecteurs sont ensuite normalisés et comparés par leur produit scalaire, ce qui revient ici à une similarité cosinus.[^p7-tfidf]

Lancez cette version :

```bash
python recherche.py "Une remise en stock à prix égal envoie-t-elle une notification ?" --sortie sorties/recherche.json
```

Le deuxième paragraphe de `notification` doit apparaître en tête. Ouvrez le journal et lisez le texte : **le score aide à classer, il ne certifie pas la réponse**. Le seuil de `0.12` est un choix de cet exercice, pas une probabilité minimale de vérité.

[^p7-tfidf]: Manning, Raghavan et Schütze, [pondération TF-IDF](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html). Notre code utilise une variante lissée de l’IDF.

## Quand les mots ne sont pas les mêmes

Essayez :

```bash
python recherche.py "À quelle heure purge-t-on les fixtures ?" --sortie sorties/recherche-synonymes.json
```

Notre moteur ne trouve rien. Pourtant, `staging.md` explique quand les données de démonstration sont réinitialisées. La question emploie simplement un autre vocabulaire.

Ce manque n’est pas une preuve que l’information n’existe pas. Il décrit une limite de notre recherche. On peut ajouter des synonymes adaptés au domaine, reformuler la question, ou utiliser des embeddings appris pour rapprocher certaines formulations. Mais une proximité sémantique n’est toujours pas une garantie de pertinence : il faudra tester les passages retrouvés.

Pour le constater sans ajouter un modèle, remplacez la question par « Quand les données de staging sont-elles réinitialisées ? », avec un nouveau nom de sortie. Le passage attendu remonte alors.

Notre index est reconstruit en mémoire à chaque lancement. Un corpus plus grand demanderait peut-être de le conserver ; il faudrait alors prévoir sa mise à jour et la suppression des documents retirés. Pour l’instant, gardons cette version simple et mesurons ce qu’elle retrouve réellement.

La recherche réussit sur certaines formulations et échoue sur une autre dont nous connaissons pourtant la réponse. Gardons ce cas : il nous empêchera de confondre une démonstration réussie avec une recherche fiable en général.

---

[Précédent : Choisir ce que l’on veut modifier](../01-choisir/LECTURE.md) · [Suivant : Évaluer les sources avant les réponses](../03-evaluer/LECTURE.md)
