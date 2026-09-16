Évaluons chaque modèle sur les deux corpus :

```bash
python petit_modele.py evaluer --modele sorties/lora/modele.npz --corpus adaptation --sortie sorties/lora-test-adaptation.json
python petit_modele.py evaluer --modele sorties/lora/modele.npz --corpus base --sortie sorties/lora-test-base.json
```

Faites la même chose avec `sorties/complet/modele.npz`, puis avec `resultats-reference/base/modele.npz`, en choisissant de nouveaux noms de sortie. Sans option `--lot`, cette commande utilise le test.

La **perte** mesure ici à quel point le modèle attribue de mauvaises probabilités aux caractères attendus. Plus elle est basse, mieux il prédit les caractères de ce lot avec leurs vrais caractères précédents. Nous reviendrons sur ce dernier point.

| Modèle | Test sur les phrases initiales | Test sur les lignes `INFO` |
| --- | ---: | ---: |
| Base | 0,48 | 6,08 |
| Base avec LoRA | 8,77 | 0,95 |
| Adaptation complète | 1,76 | 0,84 |

![Les deux adaptations réduisent la perte sur les lignes INFO ; elles augmentent la perte sur les anciennes phrases, surtout avec l’adaptateur LoRA actif.](image:images/adaptation.png)
Figure: Résultats de notre essai, arrondis ; une barre plus courte indique une perte plus faible

Notre adaptateur améliore donc la prédiction du nouveau format, mais dégrade fortement celle des anciennes phrases. Les poids de base sont restés identiques, et pourtant la sortie du modèle a changé : la correction s’ajoute à chaque passage dans la couche.

Désactiver l’adaptateur permet de retrouver la base. Cela ne supprime pas la régression lorsqu’il est activé. Selon l’usage visé, nous pourrions essayer d’autres données, d’autres réglages ou un autre compromis ; il faudrait alors refaire une évaluation indépendante.

Ces résultats concernent notre minuscule réseau et nos gabarits. Ils ne classent pas LoRA et l’adaptation complète pour tous les modèles. Ils montrent surtout pourquoi nous avons gardé les anciens exemples dans l’évaluation.
