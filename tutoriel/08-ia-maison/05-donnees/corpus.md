Ouvrez `donnees/langage/base-train.txt`, puis `adaptation-train.txt`. Le premier contient des phrases de notre service fictif. Le second exprime des situations sous forme de lignes de journal :

```text
INFO produit=... prix=... stock=oui decision=...
```
Code: Forme du deuxième corpus ; les points de suspension représentent ici les valeurs

Ces textes ont été fabriqués à partir de quelques gabarits. Les journaux montrent une forme d’écriture ; aucun service n’a réellement exécuté les décisions qu’ils racontent. Nous pourrons mesurer si le modèle apprend cette forme, pas lui attribuer la maîtrise de toutes les règles métier.

Les caractères sont volontairement simples et sans accents. Le vocabulaire fixé dans le code contient 75 caractères, dont un caractère de remplissage. Nous ne sommes plus en train d’adapter SmolLM2 : `petit_modele.py` décrit un autre réseau, créé pour cet atelier.

Ces exemples nous appartiennent et leur licence est fournie. Avec des données réelles, le travail commencerait déjà ici : a-t-on le droit de les utiliser ? Contiennent-elles des données personnelles, des secrets ou des réponses erronées ? Ajouter des milliers de lignes ne réparera pas un corpus incohérent.
