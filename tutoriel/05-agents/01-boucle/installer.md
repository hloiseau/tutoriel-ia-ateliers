Récupérez le dossier [ateliers/05-agents du dépôt](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/main/ateliers/05-agents), ou téléchargez [l’archive de cet atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-agents.zip). Décompressez-la dans un dossier de travail. Pour la suite, votre terminal doit être ouvert dans le dossier qui contient `banc.py`.

Le dossier `projet` contient la fonction initiale de suivi de prix et son ticket. Les fichiers de `cas` décrivent les appels que nous allons rejouer. Nous ne toucherons pas à votre correction de la partie 4.

Lancez :

```bash
python banc.py lecture --journal sorties/lecture.jsonl
```

Si nécessaire, remplacez `python` par `python3` ou par la commande qui vous servait déjà. Le programme affiche :

```text
1. lire_fichier : ok
2. lire_fichier : ok
Arrêt : fin_du_script (2 appels)
Journal : sorties/lecture.jsonl
```
Code: Deux demandes de lecture réellement exécutées par le banc

Le terminal résume le parcours ; le détail se trouve dans `sorties/lecture.jsonl`. Chaque ligne est un objet JSON qui conserve la demande, son résultat et le temps passé dans la fonction Python, sous la clé `secondes_outil`. Cette durée ne mesure aucune inférence de modèle.

Pour refaire l’essai, donnez un autre nom au journal. Le programme refuse d’écraser le premier, afin que vous puissiez comparer les traces.
