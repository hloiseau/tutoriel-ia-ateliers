Les erreurs les plus courantes à cette étape concernent l’environnement, pas les réseaux de neurones.

| Ce que vous voyez | Ce qu’il faut vérifier |
| --- | --- |
| `No module named numpy` ou `sklearn` | Réactivez `.venv`, puis relancez `python -m pip install -r requirements.txt`. |
| `can't open file ...01_observer.py` | Le terminal doit être dans le dossier qui contient les scripts. |
| `No module named venv` ou absence d’`ensurepip` | Installez le composant venv correspondant à votre Python avec les paquets de votre distribution. |
| Aucune fenêtre ne s’ouvre | C’est le fichier `sorties/chiffres.png` qu’il faut ouvrir. |
| Un script a été enregistré en `.py.txt` | Affichez les extensions dans l’explorateur et conservez uniquement `.py`. |

Pour vérifier quel Python travaille réellement :

```bash
python -c "import sys; print(sys.executable)"
```

Le chemin doit contenir le dossier `.venv` de l’atelier. Cela évite de chercher pendant vingt minutes pourquoi une bibliothèque est « installée » et « introuvable » en même temps. 🙂
