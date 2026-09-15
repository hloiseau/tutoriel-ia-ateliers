[Télécharger les fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/b95165289276a45bc299d0826e3c540727e8e203/telechargements/annexes-atelier-ia-v1.zip).

Décompressez l’archive. Elle contient deux dossiers :

- `atelier-ia` : le code, les données du petit corpus et la grille de dessin ;
- `resultats-reference` : les modèles entraînés, les graphiques et les journaux de nos essais.

Ouvrez le dossier `atelier-ia` dans votre éditeur. Les commandes partiront de ce dossier. Le programme y créera `sorties` pour vos propres résultats ; ceux de référence restent à part.

Vous pouvez commencer en regardant ces fichiers :

| Fichier | Rôle |
| --- | --- |
| `01_observer.py` | Charger les images et les afficher |
| `commun.py` | Préparer les données et les trois groupes |
| `modele.py` | Calculer les réponses et les gradients |
| `03_entrainer.py` | Répéter les mises à jour et sauvegarder |
| `dessiner.html` | Dessiner un chiffre à fournir au modèle |

Les autres scripts seront utilisés au fil des manipulations.

Nous utiliserons **Python 3.12 en version 64 bits**. Les exécutions présentées ici ont été faites avec Python 3.12.14 sous Linux. Les commandes d’installation pour Windows et macOS suivent la documentation de Python ; elles n’ont pas été exécutées sur ces deux systèmes.[^p2-1-installer-windows][^p2-1-installer-mac]

Ouvrez un terminal dans `atelier-ia`. Sous Windows, utilisez ici l’**Invite de commandes** (`cmd`). Vérifiez que Python est disponible :

```bat
py -3.12 --version
```
Code: Windows, Invite de commandes

```bash
python3.12 --version
```
Code: Linux et macOS

Si la commande est introuvable, installez Python 3.12 depuis les distributions proposées par Python ou par votre système. Si votre commande `python3` affiche déjà Python 3.12, vous pouvez l’utiliser à la place de `python3.12`.

Créons un **environnement virtuel**. Il gardera les bibliothèques de cet atelier dans son propre dossier, `.venv`.[^p2-1-installer-venv]

Sous Windows, dans l’Invite de commandes :

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

Sous Linux ou macOS :

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

L’installation utilise Internet. Ensuite, les expériences se déroulent localement : les données sont incluses dans scikit-learn, et aucun appel à une API d’IA n’est nécessaire.

Dans les commandes suivantes, `python` désigne celui de cet environnement activé. À chaque nouveau terminal, revenez dans `atelier-ia` et relancez la commande d’activation. Sous PowerShell, vous pouvez aussi appeler directement `.venv\Scripts\python.exe` à la place de `python`, sans activer l’environnement.

Le fichier `requirements.txt` fixe les versions utilisées :

```text
numpy==2.3.5
scikit-learn==1.8.0
matplotlib==3.10.8
threadpoolctl==3.6.0
```
Code: requirements.txt

NumPy effectuera les calculs sur les tableaux. scikit-learn fournira les images et leur découpage en groupes. Matplotlib écrira les graphiques dans des fichiers PNG. `threadpoolctl` limitera les multiplications matricielles de l’entraînement à un seul fil CPU.

Nous n’utiliserons pas de modèle de reconnaissance déjà entraîné : les paramètres partiront de valeurs initiales et seront ajustés par notre propre code.


[^p2-1-installer-windows]: [Python 3.12, installation sous Windows](https://docs.python.org/3.12/using/windows.html).

[^p2-1-installer-mac]: [Python 3.12, installation sur macOS](https://docs.python.org/3.12/using/mac.html).

[^p2-1-installer-venv]: [Python, environnements virtuels avec venv](https://docs.python.org/3.12/library/venv.html).
