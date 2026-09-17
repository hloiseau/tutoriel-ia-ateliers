# Les ateliers du quartier — dossier fictif

Ce dossier accompagne le premier chapitre du parcours « Travailler avec l’IA au-delà du code ». Il se lit sans installation et sans compte de service. Les personnes, messages et décisions sont entièrement fictifs.

## Commencer

Lisez `regles-equipe.md`, puis les fichiers de `entrees/`. Faites une copie de `modele-point.md` dans votre dossier de travail et préparez votre point. Le dossier `corrige/` contient ensuite une référence commentée et une grille de vérification.

Les messages sont de simples fichiers UTF-8, sans pièce jointe ni lien à ouvrir. Deux fichiers de courriel sont intentionnellement identiques. Ne les effacez pas : leur présence fait partie de l’exercice.

`entrees/suivi-initial.csv` utilise UTF-8 et la virgule comme séparateur. La première ligne contient les noms de colonnes. Le fichier ne contient ni macro ni formule ; un tableur ou un éditeur de texte suffit. Il décrit l’état avant le traitement du lot, et doit rester inchangé. Une version `.xlsx` du même tableau est fournie dans `supports/` pour une ouverture directe dans un tableur ; n’utilisez qu’une des deux versions comme source.

## Où travailler ?

Les chemins du chapitre partent de la racine de ce dossier. Enregistrez votre point et vos brouillons dans un dossier de travail distinct des entrées. Aucun programme de traitement, agent, serveur de messagerie ou envoi n’est inclus dans cette première étape.

Lors des futurs essais avec un assistant, fournissez uniquement `regles-equipe.md` et `entrees/`. Le modèle de point est une aide de présentation facultative. Gardez `corrige/` à part pour l’évaluation ; ne transmettez pas non plus tout le dépôt du tutoriel.

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

Textes et données : CC BY-SA 4.0. Script de vérification : GPL-3.0-only.
