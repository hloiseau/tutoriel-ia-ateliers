L’atelier utilise Python 3.12 et sa bibliothèque standard. Si vous avez suivi la partie précédente, conservez votre installation : nous n’ajouterons ni NumPy ni dépendance vers une API payante.

[Téléchargez les fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/b95165289276a45bc299d0826e3c540727e8e203/telechargements/annexes-modele-local-v1.zip), décompressez l’archive, puis ouvrez un terminal dans le dossier `atelier-local`.

Dans les commandes, `python` désigne votre Python 3.12. Selon votre installation, écrivez `python3` sous Linux ou macOS, ou `py -3.12` sous Windows. Vérifiez-le avant de poursuivre :

```bash
python --version
python inventaire.py
```
Code: Identifier l’environnement utilisé

Le second programme enregistre les informations dans `resultats/machine.json`. Il relève notamment le système, l’architecture et le nombre de processeurs logiques. S’il trouve `nvidia-smi`, il lui demande aussi le nom de la carte NVIDIA et sa mémoire. Le parcours sur CPU continue normalement lorsque cette commande est absente.

Gardez au moins quelques gigaoctets libres sur le disque pour le moteur, le modèle et les résultats. Pour la RAM, vérifiez la mémoire **disponible**, pas seulement la quantité installée : les autres applications en occupent déjà une partie. Le fichier du modèle approche 386 Mo, mais le programme aura besoin de mémoire supplémentaire.

Notre premier réglage utilisera deux fils CPU et un contexte limité à 2 048 tokens. Si la machine manque de mémoire ou devient peu réactive, arrêtez le serveur avant de modifier ses paramètres. Faire tourner un petit modèle lentement est suffisant pour comprendre la manipulation ; planter tout le bureau n’apporte pas grand-chose. 😅
