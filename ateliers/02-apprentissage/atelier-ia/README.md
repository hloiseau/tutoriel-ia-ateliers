# Atelier : comprendre un modèle en le construisant

Ouvrez un terminal dans ce dossier `atelier-ia`. Utilisez Python 3.12 en 64 bits.

## Installation

Linux/macOS :

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Windows, Invite de commandes (`cmd`) :

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

Sous PowerShell, vous pouvez appeler `.venv\Scripts\python.exe` directement à la place de `python`. La connexion Internet sert à installer les dépendances. Les programmes n’utilisent aucune API distante.

## Parcours

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

Pour dessiner, ouvrez `dessiner.html` dans un navigateur, exportez `dessin.json` et déplacez-le dans ce dossier. Lancez ensuite `python 05_lire_dessin.py dessin.json`.

`../resultats-reference/` contient les modèles, graphiques et rapports de référence. Les scripts créent `sorties/` pour vos propres résultats. Pour employer un modèle fourni sans l’entraîner, copiez son fichier `.npz` dans `sorties/` après le lancement de `01_observer.py`. Les programmes d’entraînement repartent de l’initialisation et remplacent le résultat du même nom. Utilisez `--nom essai` pour conserver une variante distincte.

Les fichiers de référence sont issus d’exécutions réelles sous Linux avec Python 3.12.14 ; voir les limites de validation dans `docs/verification.md` à la racine du dépôt. Les temps ne sont pas garantis sur une autre machine.

## Données

Les images sont fournies par `sklearn.datasets.load_digits`. Source : E. Alpaydin et C. Kaynak (1998), Optical Recognition of Handwritten Digits, UCI, https://doi.org/10.24432/C50P49, licence CC BY 4.0. Les figures de chiffres sont des visualisations de ces données, parfois décalées d’un pixel.

`corpus.txt` et `dessin-exemple.json` ont été créés pour ce projet.
