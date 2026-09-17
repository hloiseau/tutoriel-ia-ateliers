# Première étape hors développement — vérifications

Contrôles exécutés le 17 septembre 2026 dans l’environnement de rédaction, sous Linux. Aucun essai sur le PC de Hugo.

## Périmètre livré

- Un [plan de sept chapitres](PLAN.md), dont seul le premier est rédigé.
- Une introduction, un chapitre de quatre sections et une conclusion provisoire, en huit petits Markdown référencés par un manifest.
- Un [atelier fictif](../../ateliers/hors-developpement/README.md) comprenant cinq fichiers de courriel, un CSV d’état initial et sa version XLSX, deux comptes rendus, les règles, un modèle de point et un corrigé manuel.
- Des lectures générées, un [ZIP du début de cours](../../telechargements/zds-brouillons/hors-developpement.zip) et une [archive d’atelier](../../telechargements/atelier-hors-developpement.zip).

La branche de travail part de la réécriture publiée `1f5c8cbb90480701f3057db28855adf6a4f04b99`. Avant le travail, `main` pointait toujours sur `102e5ccf29bff571da46bcdae0a51a5b1d089f95`. Les sources des huit parties et les résultats de référence n’ont pas été modifiés.

## Contrôles exécutés

| Contrôle | Résultat |
| --- | --- |
| `python -m unittest discover -s ateliers/hors-developpement -p 'test_dossier.py' -v` | Neuf tests réussis : comptage, copie exacte, même expéditeur avec message distinct, suivi initial, champ absent, dates et horaires ouverts, fiction, références du corrigé, concordance XLSX/CSV |
| Extraction de l’archive d’atelier, puis `python -m unittest discover -s . -p 'test_dossier.py' -v` depuis le dossier extrait | Les neuf mêmes tests réussissent |
| `python -m unittest discover -s outils -p 'test_assembler*.py' -v` | Huit tests réussis, dont quatre nouveaux pour l’assemblage ciblé et quatre pour l’assembleur global |
| `python outils/assembler_tutoriel.py --partie redaction/hors-developpement --exports telechargements/zds-brouillons` | Un chapitre, quatre sections, huit sources Markdown ; lecture et ZIP produits séparément |
| `python outils/assembler_annexes.py --atelier hors-developpement` | Archive d’atelier produite avec les notices de licence |
| `unzip -t telechargements/zds-brouillons/hors-developpement.zip` | Dix entrées, aucune erreur d’intégrité |
| Rendu du tableau XLSX et examen visuel | Une feuille, en-têtes et ligne lisibles, mention des données fictives ; aucune interface Excel ou LibreOffice essayée |
| Inspection des cellules et du contenu du XLSX | Même ligne que le CSV, nombre de places stocké comme nombre, aucune formule, macro ou lien externe au classeur |
| Relecture du chapitre assemblé | Chemins, données, décomptes et renvois au corrigé cohérents ; les exemples ne sont pas présentés comme des sorties réelles |
| Liens locaux des Markdown modifiés | 139 liens contrôlés, aucune cible manquante |
| `git diff --cached --check` | Aucune erreur d’espacement dans les fichiers à publier |
| `python outils/assembler_global.py` | Huit parties, 56 chapitres et deux annexes ; ZIP strictement identique à celui du 16 septembre |

L’option `--partie` permet de régénérer un dossier précis sans réécrire les statistiques du parcours complet. Sans cette option, l’assembleur continue de parcourir uniquement `tutoriel/` ; les brouillons sous `redaction/` restent exclus.

Empreintes SHA-256 des archives vérifiées :

```text
77f753aed6fcd62c6b0a0ce4fdff9bec85c6698c86c0b58ba00c3210f6f7bd91  atelier-hors-developpement.zip
896d842a8550e4b27202574ace6acc34e5baac9523847b7088dbfa93a4450526  zds-brouillons/hors-developpement.zip
7bdbbb8d88d9b2aa76021f2e17579732970de938b45ba67206e5a3d4e1bed744  zds/tutoriel-ia-complet.zip
```

Les deux premières archives utilisent les dates des fichiers comme les exports séparés existants ; une reconstruction peut donc changer leur empreinte après un changement de date des sources. Le ZIP global conserve ses dates fixes et son empreinte reproductible.

## Ce qui reste à faire

Les chapitres 2 à 7 restent à rédiger. Aucun assistant, pipeline, service payant, MCP de messagerie, envoi, approbation par une interface ou lancement planifié n’a été exécuté pour ce parcours. Le corrigé est une référence écrite, distincte d’une trace d’exécution.

Il faudra choisir et essayer un espace de travail IA et une implémentation de pipeline, conserver leurs entrées et sorties brutes, puis vérifier les permissions, reprises, validations et coûts observables. La comparaison des produits devra être revue dans leurs documentations officielles au moment de ces essais. Aucun comportement courant de produit n’est affirmé dans le premier chapitre.

L’ouverture du CSV dans différents tableurs, celle du XLSX dans leurs interfaces, les manipulations sur Windows et macOS et l’import interactif de l’archive ZdS restent à vérifier. Aucun import ZdS n’a été tenté.

Le tutoriel Vim n’a pas été relu sur le site pendant cette étape ; la progression s’appuie sur l’analyse déjà disponible dans le guide de voix. L’auteur doit encore relire ce nouveau texte. Son accord sur le fil rouge ne vaut pas approbation de chaque chapitre ni du renumérotage.

## Suite de la rédaction

Le chapitre 2 peut maintenant partir des mêmes fichiers pour demander à un assistant un point sourcé et des brouillons. Les règles et les entrées lui seront transmises ; le corrigé et la grille resteront réservés à la vérification. Un essai manquant sera signalé comme tel, sans reconstruire une réponse plausible pour remplir le chapitre.
