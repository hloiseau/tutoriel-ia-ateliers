Essayez :

```bash
python recherche.py "À quelle heure purge-t-on les fixtures ?" --sortie sorties/recherche-synonymes.json
```

Notre moteur ne trouve rien. Pourtant, `staging.md` explique quand les données de démonstration sont réinitialisées. La question emploie simplement un autre vocabulaire.

Ce manque n’est pas une preuve que l’information n’existe pas. Il décrit une limite de notre recherche. On peut ajouter des synonymes adaptés au domaine, reformuler la question, ou utiliser des embeddings appris pour rapprocher certaines formulations. Mais une proximité sémantique n’est toujours pas une garantie de pertinence : il faudra tester les passages retrouvés.

Pour le constater sans ajouter un modèle, remplacez la question par « Quand les données de staging sont-elles réinitialisées ? », avec un nouveau nom de sortie. Le passage attendu remonte alors.

Notre index est reconstruit en mémoire à chaque lancement. Un corpus plus grand demanderait peut-être de le conserver ; il faudrait alors prévoir sa mise à jour et la suppression des documents retirés. Pour l’instant, gardons cette version simple et mesurons ce qu’elle retrouve réellement.
