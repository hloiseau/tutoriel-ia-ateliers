Ouvrez `donnees/langage/base-train.txt`, puis `adaptation-train.txt`. Le premier contient des phrases de notre service fictif. Le second exprime des situations sous forme de lignes de journal :

```text
INFO produit=... prix=... stock=oui decision=...
```
Code: Forme du deuxième corpus ; les points de suspension représentent ici les valeurs

Ces textes ont été fabriqués à partir de quelques gabarits. Les journaux sont des exemples d’écriture, pas les traces d’un service qui aurait réellement exécuté ces décisions. Notre objectif sera d’apprendre une forme de texte ; ce jeu ne permet pas de conclure que le modèle sait appliquer toutes les règles métier.

Les caractères sont volontairement simples et sans accents. Le vocabulaire fixé dans le code contient 75 caractères, dont un caractère de remplissage. Nous ne sommes plus en train d’adapter SmolLM2 : `petit_modele.py` décrit un autre réseau, créé pour cet atelier.

Ces exemples nous appartiennent et leur licence est fournie. Avec des données réelles, cette étape demanderait déjà du travail : a-t-on le droit de les utiliser, contiennent-elles des données personnelles, des secrets, des réponses erronées ? Plus de lignes n’améliorent pas forcément un mauvais corpus.
