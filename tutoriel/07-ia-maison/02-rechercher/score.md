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
