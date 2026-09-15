Supposons qu’une application dispose d’un outil nommé `lire_fiche`. Il accepte un nom de fiche et renvoie un texte. Un appel peut s’écrire sous cette forme :

```json
{"outil": "lire_fiche", "arguments": {"nom": "validation"}}
```
Code: appel.json

Notre bigramme ne sait pas choisir cet outil. Pour essayer le code qui reçoit et exécute un appel, nous lui fournissons donc directement le fichier `appel.json`.

```bash
python 10_outil.py appel.json
```

```text
{
  "outil": "lire_fiche",
  "resultat": "La validation sert à comparer les réglages sans utiliser le jeu de test."
}
```

Ouvrez `10_outil.py`. Le programme vérifie le nom de l’outil, les arguments et le nom de la fiche. Il va ensuite chercher le texte dans un dictionnaire Python.

Aucune commande système ne se cache derrière cette lecture. La valeur reçue ne passe ni à `eval`, ni à un shell. Un appel d’outil est une donnée que l’application examine avant d’exécuter une fonction.

Copiez `appel.json` dans `appel-refuse.json`, puis remplacez `lire_fiche` par `effacer_fichiers`. Lancez :

```bash
python 10_outil.py appel-refuse.json
```

Le résultat doit être :

```text
Appel refusé : Outil non autorisé.
```

Le refus vient d’une condition exécutée par Python. Il ne dépend pas de la bonne volonté d’un modèle qui aurait lu « merci de ne rien effacer ».
