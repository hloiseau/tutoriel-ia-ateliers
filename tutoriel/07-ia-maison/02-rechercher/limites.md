Essayez :

```bash
python recherche.py "À quelle heure purge-t-on les fixtures ?" --sortie sorties/recherche-synonymes.json
```

Notre moteur ne trouve rien. Pourtant, `staging.md` explique quand les données de démonstration sont réinitialisées. La question emploie simplement un autre vocabulaire.

Le document existe ; notre recherche vient simplement de le manquer. Nous pouvons ajouter des synonymes adaptés au domaine, reformuler la question ou utiliser des embeddings appris pour rapprocher certaines formulations. Cette dernière méthode devra elle aussi être évaluée sur les passages retrouvés : deux textes proches par le sens peuvent rester hors sujet pour notre question précise.

Pour le constater sans ajouter un modèle, remplacez la question par « Quand les données de staging sont-elles réinitialisées ? », avec un nouveau nom de sortie. Le passage attendu remonte alors.

Notre index est reconstruit en mémoire à chaque lancement. Avec un corpus plus grand, nous pourrions le conserver entre deux exécutions ; il faudrait alors prévoir sa mise à jour et la suppression des documents retirés. Pour l’instant, cette version simple nous laisse voir exactement ce qui remonte et ce qui lui échappe.
