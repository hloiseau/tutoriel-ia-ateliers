Voici les cas que nous voulons distinguer :

| Ancien état | Nouvel état | Notification attendue |
| --- | --- | --- |
| 20 €, disponible | 15 €, disponible | Oui |
| 15 €, disponible | 20 €, disponible | Non |
| 20 €, disponible | 15 €, indisponible | Non |
| 20 €, indisponible | 20 €, disponible | Non |
| 20 €, indisponible | 15 €, disponible | Oui |
| 20 €, indisponible | 25 €, disponible | Non |
| 20 €, disponible | 20 €, disponible | Non |
Table: Les situations que la règle doit départager

Les trois premières correspondent déjà à nos tests de départ. Les suivantes rendent visible ce que ces tests ne contrôlaient pas.

Vous pouvez demander à l’agent de proposer cette table avant de coder les tests. Relisez alors les **résultats attendus**, pas seulement le nombre de lignes. Une longue suite de tests qui attend la mauvaise réponse reste une longue suite de tests qui attend la mauvaise réponse.

Pour une règle aussi petite, faire la table soi-même prend peu de temps. Dans un projet plus grand, l’aide peut surtout servir à retrouver les cas oubliés ou à traduire une règle déjà décidée en scénarios exécutables.
