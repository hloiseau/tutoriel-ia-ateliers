Dans le dossier du banc, lancez :

```bash
python banc.py refus --journal sorties/refus.jsonl
```

Vous obtenez trois refus. Ouvrez `cas/refus.json` et le journal côte à côte :

| Demande | Pourquoi elle est refusée |
| --- | --- |
| Lire `../secret.txt` | Le chemin ne fait pas partie des fichiers autorisés |
| Appeler `ecrire_note` | L’option autorisant cette écriture n’est pas active |
| Appeler `terminal` | Le banc n’expose aucun outil de ce nom |
Table: Les contrôles ne reposent pas sur l’obéissance d’un modèle

Trois contrôles différents apparaissent. Le chemin sort de la liste autorisée ; `ecrire_note` existe mais son option d’autorisation manque ; `terminal`, lui, n’existe tout simplement pas dans le banc. Même une demande formulée avec beaucoup d’assurance ne fera pas surgir ce dernier par magie. 🙂

Regardez `Banc.executer` dans `banc.py`. Les arguments sont vérifiés avant l’action. Pour lire, le chemin doit correspondre à un nom prévu, puis rester dans le dossier du projet après résolution. Pour écrire, la destination est fixée à `sorties/note.md` : le demandeur choisit le texte, jamais le chemin de sortie.

Vous voyez pourtant un nouveau journal sur le disque. C’est le programme principal qui l’écrit pour conserver l’expérience ; l’autorisation testée concerne uniquement l’outil `ecrire_note`.
