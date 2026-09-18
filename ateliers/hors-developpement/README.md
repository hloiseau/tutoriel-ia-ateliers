# Les ateliers du quartier — dossier fictif

Ce dossier accompagne les sept chapitres du parcours « Travailler avec l’IA au-delà du code », partie 7 du tutoriel. Les personnes, messages et décisions sont entièrement fictifs. Le parcours local se suit sans programmer et sans compte d’IA.

## Commencer

Lisez `regles-equipe.md`, puis les fichiers de `entrees/`. Faites une copie de `modele-point.md` dans votre dossier de travail et préparez votre point. Le dossier `corrige/` contient ensuite une référence commentée et une grille de vérification.

Les messages sont de simples fichiers UTF-8, sans pièce jointe ni lien à ouvrir. Deux fichiers de courriel sont intentionnellement identiques. Ne les effacez pas : leur présence fait partie de l’exercice.

`entrees/suivi-initial.csv` utilise UTF-8 et la virgule comme séparateur. La première ligne contient les noms de colonnes. Le fichier ne contient ni macro ni formule ; un tableur ou un éditeur de texte suffit. Il décrit l’état avant le traitement du lot, et doit rester inchangé. Une version `.xlsx` du même tableau est fournie dans `supports/` pour une ouverture directe dans un tableur ; n’utilisez qu’une des deux versions comme source.

## Où travailler ?

Les chemins des chapitres partent de la racine de ce dossier. Enregistrez votre point et vos brouillons dans un dossier de travail distinct des entrées. Commencez par votre lecture ; l’application viendra ensuite.

Pour l’essai avec un assistant, fournissez `regles-equipe.md`, `modele-point.md` et les huit fichiers de `entrees/`. Gardez `corrige/` à part pour l’évaluation ; ne transmettez pas tout le dépôt du tutoriel. Conservez les réponses réellement obtenues séparément des exemples fournis.

## Poursuivre les sept chapitres

| Étape | Fichiers à utiliser |
| --- | --- |
| Préparer le point à la main | Entrées, règles, modèle, puis corrigé et grille de vérification |
| Essayer un assistant | `consignes/point-equipe.md`, puis `consignes/extraction.md` |
| Contrôler l’extraction | Ouvrir [pipeline/index.html](pipeline/index.html) dans le navigateur ; [mode d’emploi](pipeline/README.md) |
| Examiner les accès et garder la méthode | `procedures/preparer-point.md`, document portable à fournir explicitement, sans installation automatique |
| Approuver une version | Boutons de relecture, d’approbation et d’export de l’application locale |
| Reprendre le lot | Exporter l’état, le recharger et vérifier l’absence de nouvelles demandes |
| Comparer et transposer | `evaluation/fiche-essai.md` et `evaluation/veille.md` |

L’application locale est conçue pour le seul lot `quartier-01`. Elle ne fait aucune requête réseau et n’appelle aucun modèle. Elle reçoit le JSON par copier-coller, ou charge une extraction explicitement fictive. Les contrôles vérifient la forme et les références ; la fidélité des faits reste à examiner. Le générateur ajoute aussi des rappels connus du dossier : sa sortie ne mesure pas, à elle seule, la qualité d’une extraction par un assistant.

L’export d’un point marque ses messages comme pris en compte dans ce rapport. Il ne confirme aucune inscription. L’application ne connaît aucun compte de messagerie, n’effectue aucun envoi et ne modifie aucun tableau partagé. Conservez le point et l’état après avoir vérifié leur téléchargement.

La variante [n8n](n8n/README.md) est facultative. Elle contient un workflow manuel inactif avec une extraction fictive et des contrôles ; l’approbation, le suivi durable et l’appel d’un modèle ne font pas partie de cet export. Son code est testé hors n8n ; son import et son exécution dans n8n restent à vérifier. L’essai réel de l’interface locale dans un navigateur reste également à réaliser.

## Vérifier les matériaux de l’atelier

Depuis la racine du dépôt, les contrôles de cohérence se lancent avec Python, facultativement :

```bash
python -m unittest discover -s ateliers/hors-developpement -p 'test_dossier.py' -v
```

Depuis l’archive décompressée, placez-vous dans ce dossier puis lancez :

```bash
python -m unittest discover -s . -p 'test_dossier.py' -v
```

Ces tests contrôlent les fichiers fictifs, leurs identifiants, les références et les incidents prévus. Ils ne font appel à aucun modèle et n’évaluent pas automatiquement votre rédaction. Le corrigé est écrit à partir des données ; il ne représente pas une sortie observée d’assistant.

Les personnes qui maintiennent l’atelier peuvent aussi tester le moteur et les nœuds avec Node.js, depuis la racine du dépôt :

```bash
node --test ateliers/hors-developpement/pipeline/test-moteur.cjs ateliers/hors-developpement/n8n/test_workflow.js
```

Dans l’archive décompressée, les chemins deviennent `pipeline/test-moteur.cjs` et `n8n/test_workflow.js`. Aucun de ces tests ne lance le navigateur, n8n ou un assistant distant.

Textes et données : CC BY-SA 4.0. Script de vérification : GPL-3.0-only.
