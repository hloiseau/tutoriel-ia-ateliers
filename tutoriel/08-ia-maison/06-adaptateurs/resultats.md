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

Sur les lignes `INFO`, la perte passe de 6,08 à 0,95 avec LoRA. Sur les anciennes phrases, elle bondit de 0,48 à 8,77. Les poids de base sont restés identiques ; la correction active s’ajoute pourtant à chaque passage dans la couche et transforme la sortie du modèle.

Désactiver l’adaptateur permet de retrouver la base. Lorsqu’il est actif, la régression demeure. Selon l’usage visé, nous pourrions essayer d’autres données, d’autres réglages ou un autre compromis, puis reprendre l’évaluation avec des exemples restés à l’écart de ces choix.

Ces valeurs appartiennent à notre minuscule réseau et à ses gabarits ; elles ne servent pas à classer LoRA et l’adaptation complète sur tous les modèles. En revanche, elles donnent une excellente raison de garder les anciennes tâches dans l’évaluation.
