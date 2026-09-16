Téléchargez [l’archive de la partie 7](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-ia-maison.zip), ou ouvrez `ateliers/07-ia-maison` dans le dépôt. Placez le terminal à côté de `recherche.py`.

Créez un environnement avec Python 3.12 :

```bash
python -m venv .venv
```

Activez-le comme dans les ateliers précédents : `source .venv/bin/activate` sous Bash ou Zsh, `.venv\Scripts\Activate.ps1` sous PowerShell, ou `.venv\Scripts\activate.bat` dans l’invite Windows. Si l’activation PowerShell est refusée, employez directement `.venv\Scripts\python.exe` à la place de `python`.

Installez ensuite les deux dépendances du petit réseau :

```bash
python -m pip install -r requirements.txt
```

La recherche documentaire n’en a pas besoin ; NumPy servira aux calculs du modèle. Le dossier `donnees/documents` contient nos pages fictives, et `donnees/documents.json` indique leur identifiant, leur révision et leur statut.

Ouvrez `temporisation.md`. Il n’y a aucune durée validée pour PRIX-2. Gardez ce détail en tête : nous allons poser la question au modèle plus tard.
