Choisissez une petite tâche dont vous saurez vérifier le résultat, par exemple préparer les scénarios d’un ticket bien déterminé ou le point d’équipe à partir d’un lot de messages. Avant de commencer, définissez ce que vous attendez : les cas importants, les résultats attendus et les décisions qui doivent rester ouvertes.

Dans `fiches/comparaison.md`, préparez deux essais : l’un sans IA, avec documentation et outils habituels ; l’autre avec l’aide que vous souhaitez examiner. Évitez de faire deux fois exactement le même problème en appelant cela une comparaison équitable : le deuxième essai profite du premier. Deux tâches proches, un ordre alterné sur plusieurs essais et des critères identiques réduisent certains biais, sans transformer notre carnet personnel en étude scientifique.

Notez le temps actif consacré à préparer, produire, relire, corriger et vérifier, sans compter deux fois le même intervalle. Ajoutez séparément l’attente qui vous a réellement bloqué. Si le modèle travaille pendant que vous faites autre chose, ce temps n’est pas une attente bloquante ; vous pouvez le noter dans le commentaire.

Vous pouvez remplir cette comparaison dans un document ou un tableau, sans programme. Le script ci-dessous est une variante facultative pour calculer le bilan fourni :

```bash
python bilan.py exemples/temps-fictifs.json
```

Les nombres du fichier sont **inventés pour montrer le calcul**. Dans ce scénario fictif, l’essai assisté produit plus vite et demande davantage de relecture et de correction : son occupation totale atteint 28 minutes, contre 23 pour l’autre. Aucune comparaison avec un outil réel n’a été réalisée ici.

![Dans cet exemple fictif, la production prend 12 minutes sans IA et 3 avec IA ; les autres étapes portent le total à 23 et 28 minutes.](image:images/temps.png)
Figure: Durées inventées pour illustrer le calcul, sans comparaison d’outils réels

Si vous utilisez le script, copiez ensuite `exemples/temps-a-remplir.json`, remplacez ses valeurs manquantes par vos observations et lancez-le sur votre copie. Pour le parcours travail, vous pouvez conserver la fiche d’essai remplie à la main. Une durée inconnue reste inconnue dans les deux cas. Conservez aussi le statut du résultat : un travail abandonné ou encore incorrect ne devient pas « meilleur » parce qu’il s’est arrêté plus tôt.

Vous pouvez ouvrir `corriges/comparaison.md` pour examiner les pièges du bilan fictif et la façon de décrire un essai resté incomplet.
