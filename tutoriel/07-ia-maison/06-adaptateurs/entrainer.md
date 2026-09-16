Repartons des mêmes poids de base que pour l’adaptation complète :

```bash
python petit_modele.py entrainer --base resultats-reference/base/modele.npz --mode lora --corpus adaptation --pas 800 --rang 4 --sortie sorties/lora
```

Ouvrez `sorties/lora/rapport.json`. Le rapport indique les paramètres entraînables et les empreintes des poids de base avant et après. Elles doivent être identiques : notre entraînement a modifié `A` et `B`, pas les matrices d’origine.

Deux fichiers sont produits. `modele.npz` rassemble le modèle et son adaptateur pour faciliter les essais. `adaptateur.npz` contient seulement la correction et l’empreinte de la base attendue.

Rechargeons ce deuxième fichier avec la base :

```bash
python petit_modele.py generer --modele resultats-reference/base/modele.npz --adaptateur sorties/lora/adaptateur.npz --debut "INFO "
```

Le programme vérifie que les poids de base correspondent. Relancez ensuite la génération sans `--adaptateur` : vous retrouvez le modèle de départ sans devoir « désapprendre » ce que nous venons d’ajouter.

Le mécanisme est pratique. Reste à savoir ce que la correction a réellement amélioré — et abîmé. Ouvrons les résultats avant de lui donner un nom impressionnant.
