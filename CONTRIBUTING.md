# Corriger et maintenir le tutoriel

Pour suivre les exercices, partez de [l’accueil](README.md) ou des [téléchargements](telechargements/README.md).

## Corriger un passage

1. Retrouvez le chapitre dans le [sommaire](SOMMAIRE.md).
2. Modifiez le petit fichier Markdown déclaré dans le `manifest.json` de sa partie. Les pages `LECTURE.md` et les README de partie sont générés.
3. Régénérez les lectures et les deux archives d’import :

```bash
python outils/assembler_tutoriel.py --exports telechargements/zds/parties
python outils/assembler_global.py
python -m unittest discover -s outils -p 'test_assembler*.py' -v
python outils/verifier_liens.py
```

La première commande produit aussi les imports par partie. La seconde produit le ZIP du contenu complet et le ZIP des images ; les deux sont nécessaires dans le formulaire ZdS. Voir le [guide d’import](telechargements/zds/README.md).

Conservez le préfixe `image:` dans les sources : les assembleurs le transforment en chemin relatif pour GitHub et en `archive:` pour ZdS, hors des blocs de code.

## Modifier un atelier

Le [répertoire des ateliers](ateliers/README.md) donne le guide et les prérequis de chaque exercice. Les dossiers `ateliers/07-ia-maison` et `ateliers/08-choisir` gardent leurs noms historiques pour préserver les commandes et les anciens liens ; ils correspondent maintenant aux parties 8 et 9. Le nouveau parcours de la partie 7 se trouve dans `ateliers/hors-developpement`.

Après une modification, reconstruisez l’archive concernée :

```bash
python outils/assembler_annexes.py --atelier hors-developpement
```

Sans `--atelier`, les huit archives sont reconstruites. Les poids, environnements virtuels et sorties personnelles sont exclus. Rejouez les contrôles décrits dans le README de l’atelier concerné ; `python outils/verifier.py` couvre les contrôles rapides des parties 3 à 5.

Les entrées comportant des erreurs, doublons ou cas invalides peuvent faire partie de l’exercice. Ne les corrigez pas sans vérifier le chapitre et les tests associés. Distinguez toujours les références enregistrées, les exemples fictifs et les nouvelles observations.

## Suivi éditorial et provenance

Le [suivi du projet](docs/README.md) regroupe les validations et expériences restantes. Les anciens imports, brouillons et sauvegardes sont conservés sous [docs/archives](docs/archives/README.md). Les sources courantes à corriger sont sous `tutoriel/` et `ateliers/`.

Les textes et illustrations originales restent sous CC BY-SA 4.0 ; le code sous GPLv3. Conservez les crédits des éléments tiers.
