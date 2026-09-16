# 2. Construire une recherche dans nos documents

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Choisir ce que l’on veut modifier](../01-choisir/LECTURE.md) · [Suivant : Évaluer les sources avant les réponses](../03-evaluer/LECTURE.md)

**TL;DR** — Nous allons découper les textes, comparer leurs mots à ceux de la question et conserver les références des passages sélectionnés.

Notre règle de notification occupe deux phrases au milieu d’un document. Envoyer toute la page au modèle ajouterait surtout du bruit ; essayons de ramener le passage qui répond à la question.

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

Ce premier résultat donne le même poids à tous les mots communs. Or, un terme présent dans presque tous les documents nous aide peu à choisir. Le classement livré dans `Index` utilise **TF-IDF** : la fréquence dans le passage est pondérée par la rareté du mot dans le corpus. Les vecteurs sont ensuite normalisés et comparés par leur produit scalaire, ce qui revient ici à une similarité cosinus.[^p7-tfidf]

Lancez cette version :

```bash
python recherche.py "Une remise en stock à prix égal envoie-t-elle une notification ?" --sortie sorties/recherche.json
```

Le deuxième paragraphe de `notification` doit apparaître en tête. Ouvrez le journal et lisez son texte. Le score nous a aidés à le classer ; il ne dit rien sur la vérité d’une future réponse. De même, le seuil de `0.12` sert uniquement à cet exercice : ce nombre n’est pas une probabilité minimale de vérité.

[^p7-tfidf]: Manning, Raghavan et Schütze, [pondération TF-IDF](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html). Notre code utilise une variante lissée de l’IDF.

## Quand les mots ne sont pas les mêmes

Essayez :

```bash
python recherche.py "À quelle heure purge-t-on les fixtures ?" --sortie sorties/recherche-synonymes.json
```

Notre moteur ne trouve rien. Pourtant, `staging.md` explique quand les données de démonstration sont réinitialisées. La question emploie simplement un autre vocabulaire.

Le document existe ; notre recherche vient simplement de le manquer. Nous pouvons ajouter des synonymes adaptés au domaine, reformuler la question ou utiliser des embeddings appris pour rapprocher certaines formulations. Cette dernière méthode devra elle aussi être évaluée sur les passages retrouvés : deux textes proches par le sens peuvent rester hors sujet pour notre question précise.

Pour le constater sans ajouter un modèle, remplacez la question par « Quand les données de staging sont-elles réinitialisées ? », avec un nouveau nom de sortie. Le passage attendu remonte alors.

Notre index est reconstruit en mémoire à chaque lancement. Avec un corpus plus grand, nous pourrions le conserver entre deux exécutions ; il faudrait alors prévoir sa mise à jour et la suppression des documents retirés. Pour l’instant, cette version simple nous laisse voir exactement ce qui remonte et ce qui lui échappe.

La règle de staging remonte avec une formulation et disparaît avec « purge des fixtures ». Gardons les deux questions : si nous changeons le classement, elles nous diront tout de suite ce que nous avons gagné — et peut-être perdu.

---

[Précédent : Choisir ce que l’on veut modifier](../01-choisir/LECTURE.md) · [Suivant : Évaluer les sources avant les réponses](../03-evaluer/LECTURE.md)
