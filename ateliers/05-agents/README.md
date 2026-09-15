# Observer les outils d’un agent

Python 3.12, bibliothèque standard uniquement. Ouvrez le terminal dans ce dossier.

Ce banc **ne contient pas de modèle**. Les fichiers `cas/*.json` sont des demandes d’outils écrites à la main pour reproduire un comportement. Les journaux sont les résultats réels de leur exécution, pas des réponses attribuées à une IA.

```bash
python banc.py lecture --journal sorties/lecture.jsonl
python banc.py refus --journal sorties/refus.jsonl
python banc.py injection --journal sorties/injection.jsonl
python banc.py boucle --limite 3 --journal sorties/boucle.jsonl
python banc.py reprise --journal sorties/reprise.jsonl
python -m unittest discover -v
```

Choisissez un autre nom si un journal existe déjà. Un refus est un résultat attendu dans ces démonstrations, pas un plantage du programme.

Pour observer une écriture autorisée, dans la copie d’atelier :

```bash
python banc.py injection --autoriser-ecriture --journal sorties/injection-autorisee.jsonl
```

Cette commande écrit ou remplace `sorties/note.md` avec le texte demandé par le script. Elle démontre une permission du programme ; aucun modèle n’a interprété le document piégé. Le dossier `projet` reste inchangé.

`banc.py` n’offre aucun terminal ni accès réseau. Ses contrôles applicatifs illustrent des règles ; ce n’est pas un bac à sable destiné à exécuter un agent hostile ou du code arbitraire. L’option d’écriture concerne l’outil `ecrire_note`. Le journal, écrit par le programme pour chaque essai, est distinct de cette permission.

## Comparer le contexte avec votre assistant

Les deux fichiers de `contexte/` donnent la même demande et le même code, avec ou sans un historique fictif sans rapport. Utilisez deux conversations neuves et le même modèle. Conservez les réponses et leurs erreurs ; aucun résultat comparatif n’est présumé.

## Calcul simplifié de coût

Le CSV et les tarifs de cette commande sont **fictifs**, choisis pour comprendre le calcul. Les trois colonnes de tokens sont disjointes. Le script ne mesure pas les tokens de vos messages.

```bash
python mesurer.py usage-exemple.csv --prix-entree 2 --prix-cache 0.2 --prix-sortie 8
```

Résultat : `0.004200` unités monétaires. Le calcul ne couvre ni les écritures de cache facturées séparément, ni les outils payants, ni les abonnements. Pour un cas réel, prenez les compteurs d’usage et la tarification du fournisseur concerné.

## Sources et licence

[Partie 5 du tutoriel](../../tutoriel/05-agents/README.md). Code : GPL-3.0-only ; textes : CC BY-SA 4.0. Les fichiers du projet proviennent de l’atelier de la partie 4, par Hugo Loiseau. Les données sont fictives.
