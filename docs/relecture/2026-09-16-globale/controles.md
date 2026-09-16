# Contrôles exécutés

Session : `2026-09-16-globale`.

## Sources et diffs

- `git diff --check` : succès après intégration.
- Les huit agents ont vérifié que leurs fichiers de cours modifiés appartiennent au manifest de leur partie.
- Les blocs de code de la partie 6 et les blocs de code et commandes de la partie 7 sont identiques au commit de départ.
- Les illustrations ont été inspectées par les agents de partie ; `recherche.png` a été inspectée de nouveau après sa régénération.

## Génération

```bash
python outils/assembler_tutoriel.py --exports telechargements/zds
python outils/assembler_global.py
```

Résultat : huit parties et un groupe d’annexes, 56 chapitres, deux chapitres d’annexes, 196 sections, 46 images, 155 notes, 332 fichiers Markdown et 394 entrées dans le ZIP global.

## Tests de l’assembleur global

```bash
python -m unittest discover -s outils -p 'test_assembler_global.py' -v
```

Résultat : 4 tests réussis. Ils couvrent notamment les collisions d’images et de notes, les images manquantes, les notes non résolues et les sorties de dossier.

## Intégrité du ZIP global

```bash
sha256sum telechargements/zds/tutoriel-ia-complet.zip
unzip -t telechargements/zds/tutoriel-ia-complet.zip
```

Résultat : archive valide, SHA-256 `7bdbbb8d88d9b2aa76021f2e17579732970de938b45ba67206e5a3d4e1bed744`.

La liste de l’archive ne contient ni rapport de relecture, ni `LECTURE.md`, ni atelier.

## Contrôles rapides des ateliers inchangés

```bash
python outils/verifier.py
```

Résultat attendu et obtenu :

- 6 tests du client de la partie 3 réussis ;
- 3 tests initiaux de la partie 4 réussis ;
- 13 tests de l’état rouge, avec les 2 échecs attendus ;
- 13 tests de l’état corrigé réussis ;
- 12 tests du banc de la partie 5 réussis.

## Limites

- Le tutoriel Vim n’a pas pu être relu en ligne depuis cet environnement ; le guide détaillé du dépôt a servi de référence.
- Aucun essai local nouveau, GPU, navigateur réel, assistant réel ou service payant n’a été exécuté.
- L’import interactif dans ZdS reste à effectuer.
