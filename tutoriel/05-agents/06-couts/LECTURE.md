# 6. Mesurer ce que la session nous a coûté

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Arrêter une boucle et reprendre sans perdre le fil](../05-reprise/LECTURE.md)

**TL;DR** — Nous distinguerons les appels d’outils, les tokens facturés et notre temps de travail. Un calcul sur des données fictives montrera comment le cache et les tours successifs changent la facture.

## Un appel d’outil n’est pas une unité de facture

Le journal du banc compte les outils appelés et le temps passé dans chaque fonction Python. La colonne des tokens y brille par son absence : aucun modèle n’a été appelé.

Dans une vraie session, le modèle reçoit un contexte, produit une réponse et peut demander plusieurs outils. Leurs résultats alimentent parfois un nouvel appel au modèle, avec un contexte plus long. Deux appels d’outils peuvent ainsi tenir dans un seul tour du modèle ou provoquer plusieurs tours : leur nombre ne suffit pas à calculer les tokens ni le prix final.

Une partie du contexte peut être réutilisée d’un tour à l’autre. Selon le fournisseur, le cache change la manière dont ces tokens sont traités et facturés ; sa lecture et parfois son écriture ont des conditions propres[^p5-cache]. Ne multipliez pas simplement la taille de la conversation affichée par le prix d’entrée.

Pour un relevé réel, partez des compteurs d’usage exposés par le fournisseur ou l’application. Regardez ce qu’ils incluent : entrée totale, entrée en cache, sortie, éventuels tokens de raisonnement et outils facturés séparément. Si l’entrée totale inclut déjà le cache, ne comptez pas celui-ci une deuxième fois.

Avec un abonnement, distinguez aussi l’argent débité en plus et la part consommée d’un quota déjà payé. Une session peut afficher zéro dépense supplémentaire tout en rapprochant votre équipe d’une limite mensuelle.

[^p5-cache]: Anthropic, [fonctionnement et tarification du cache de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Les conditions de cette documentation ne s’appliquent pas automatiquement aux autres fournisseurs.

## Faire le calcul sur deux appels

Ouvrez `usage-exemple.csv`. Il contient deux appels fictifs répartis dans trois catégories disjointes :

| Appel | Entrée hors cache | Entrée lue en cache | Sortie |
| --- | --- | --- | --- |
| 1 | 1 000 | 0 | 100 |
| 2 | 200 | 1 000 | 100 |
Table: Un exemple inventé de compteurs, pas les mesures d’un modèle

Dans cet exemple, le second appel réutilise une partie du contexte. Pour chaque catégorie, le calcul est `tokens × prix par million / 1 000 000`. Nous additionnons ensuite les catégories et les appels.

Avec des tarifs eux aussi fictifs, lancez :

```bash
python mesurer.py usage-exemple.csv --prix-entree 2 --prix-cache 0.2 --prix-sortie 8
```

Le résultat est `0.004200` unités monétaires. Passez ensuite `--prix-cache` à `2` : le coût devient `0.006000`. Seul le tarif de la lecture du cache a changé ; le CSV contient toujours les mêmes tokens et ne dit rien de la qualité des réponses.

Une écriture de cache facturée séparément, un outil payant ou un abonnement demanderait d’autres colonnes. Adaptez-les à la facture concernée avant d’utiliser vos propres données. L’affichage à six décimales sert ici à vérifier la formule sans arrondir trop tôt ; dans un bilan réel, choisissez une précision adaptée à la décision.

## Le temps gagné se mesure jusqu’à la validation

Reprenez une tâche courte de la partie 4. Notez le temps passé à préparer la demande, attendre, corriger la réponse et vérifier le résultat. Séparez les moments où l’agent vous a mobilisé de ceux pendant lesquels vous avez pu faire autre chose.

| Ce que l’on relève | Ce que cela permet de comprendre |
| --- | --- |
| Temps écoulé entre le début et la fin | La durée de la tâche dans le planning |
| Temps passé à intervenir et relire | L’attention que la tâche vous a demandée |
| Coût ou quota consommé | La dépense liée au service |
| Résultat vérifié et corrections nécessaires | Ce que vous avez obtenu pour ce temps et cette dépense |
Table: Plusieurs mesures pour une même tâche

Comparer une première découverte laborieuse à une seconde tentative dont vous connaissez déjà la solution favoriserait forcément la seconde. Choisissez plusieurs tâches comparables et conservez aussi les essais qui se passent mal. Le but est de savoir si cet usage vous aide, pas de gagner une démonstration préparée d’avance.

En local, l’absence de facture d’API ne fait pas disparaître le matériel, l’électricité et le temps d’installation. Nous approfondirons ces coûts et leurs implications dans la partie consacrée aux choix d’usage.

Vous pouvez maintenant distinguer « l’agent a beaucoup travaillé » de « ce travail m’a aidé ». Une recherche bien ciblée ou un test oublié peut suffire ; nul besoin de déléguer tout le développement pour y trouver un intérêt.

Un bilan utile rapproche le résultat vérifié, les tokens ou le quota consommé, le temps écoulé et votre attention. Gardez ces mesures avec leur contexte : elles nourriront les choix d’usage de la dernière partie.

---

[Précédent : Arrêter une boucle et reprendre sans perdre le fil](../05-reprise/LECTURE.md)
