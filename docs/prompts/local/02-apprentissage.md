# Mission locale — partie 2, apprendre avec de petits modèles

Applique le [prompt coordinateur](../LOCAL-COORDINATEUR.md). Le code de départ est dans `ateliers/02-apprentissage/atelier-ia/` ; les chapitres sont dans `tutoriel/02-apprentissage/`. Lis le README et les résultats de référence avant de définir les sorties du nouvel essai.

## Ce qu’il faut vérifier

Le parcours CPU a déjà été exécuté dans l’environnement de rédaction. Nous voulons vérifier qu’un lecteur sur la machine de Hugo peut refaire les étapes, comprendre les fichiers produits et essayer le dessin dans un vrai navigateur. Une interaction sous DOM simulé ne valide pas ce dernier point.

Crée un environnement Python isolé avec les dépendances de l’atelier. Utilise une copie de travail pour ne pas écraser les sorties existantes. Suis le README et les chapitres, en conservant le dossier courant et l’état des fichiers entre les commandes. La progression inclut notamment :

```bash
python 01_observer.py
python 02_predire.py
python 03_entrainer.py
python 04_evaluer.py
python 06_decaler.py
python 05_lire_dessin.py dessin-exemple.json
python 03_entrainer.py --cachee 32 --nom reseau
python 04_evaluer.py --nom reseau
python 07_memoriser.py
python 08_langage.py
python 09_attention.py
python 10_outil.py appel.json
```

Vérifie dans le README courant les prérequis et options avant l’exécution ; cette liste n’autorise pas à sauter une création de fichier expliquée dans le chapitre. Ne lance pas les scripts depuis la racine du dépôt par erreur.

Relève les effectifs des lots, les graines, les pertes et les scores obtenus. Vérifie la séparation entraînement/évaluation et les expériences de décalage ou de mémorisation. Les résultats différents de la référence doivent être conservés et expliqués quand c’est possible. Ne change pas le découpage pour retrouver un chiffre attendu.

## Page de dessin

Ouvre réellement `dessiner.html` dans un navigateur disponible. Vérifie la lisibilité, la grille, le dessin au pointeur, l’effacement et l’export JSON. Recharge le dessin exporté avec le classifieur. Essaie au moins un dessin exploitable et un cas qui montre une limite, sans rechercher artificiellement une démonstration parfaite.

Conserve le JSON exporté, la prédiction et une capture sans informations personnelles. Décris les gestes effectués. Si tu ne peux pas piloter le navigateur, prépare les étapes minimales pour Hugo et marque cette vérification comme bloquée ; les expériences Python continuent.

## Compréhension et livrable

Pour chaque difficulté, vérifie si le texte donne assez d’éléments : où est le fichier produit, quel modèle est chargé, que veut dire le score, pourquoi le dessin personnel peut être mal reconnu ? Corrige les trous concrets, sans ajouter un cours théorique parallèle.

Rends un rapport avec les commandes, les résultats propres à cette machine, les fichiers de dessin, les différences par rapport aux références et les corrections nécessaires. Ne présente pas les petits scripts de langage ou d’outil comme un LLM ou un agent complet. Aucun GPU n’est requis pour valider cette partie.
