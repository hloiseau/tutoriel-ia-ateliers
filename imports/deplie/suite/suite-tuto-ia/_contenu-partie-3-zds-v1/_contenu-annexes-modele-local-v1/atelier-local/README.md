# Atelier — un modèle local

Python 3.12, bibliothèque standard uniquement. llama.cpp et les poids se téléchargent séparément. Les poids ne sont pas inclus.

1. Ouvrir un terminal dans ce dossier ; utiliser `python3` sur Linux/macOS ou `py -3.12` sous Windows à la place de `python` si nécessaire.
2. `python inventaire.py`
3. `python telecharger.py` — environ 386 Mo, une fois. Une interruption recommence le téléchargement.
4. Installer llama.cpp selon le chapitre, conserver les bibliothèques fournies à côté de l’exécutable.
Sous Linux, dans le terminal de lancement : `export LD_LIBRARY_PATH="$PWD/moteur${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"` ; adapter le chemin au dossier des `.so`.

5. Lancer dans ce dossier, en adaptant le chemin de l’exécutable :

```
llama-server -m modeles/smollm2-360m-instruct-q8_0.gguf --host 127.0.0.1 --port 8080 -c 2048 -t 2 -ngl 0 --device none --parallel 1 --alias atelier-local --cors-origins http://127.0.0.1:8080
```

6. Dans un deuxième terminal, ouvert ici : `python client.py`
7. `python mesurer.py --nom cpu-contexte2048`
8. Arrêter le serveur par Ctrl+C dans son terminal.

Les résultats réels vont dans `resultats/`. Il n’y a pas de réponse préremplie du modèle.

`python -m unittest -v test_client` vérifie le client avec des réponses factices. Ce test ne télécharge et ne fait fonctionner aucun modèle.

Le dépôt et la révision du modèle, sa taille et son empreinte sont dans `modele.json`. Lire sa fiche et sa licence avant un usage autre que l’atelier. Le modèle est principalement anglophone.
