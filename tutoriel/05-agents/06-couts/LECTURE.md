# 6. Mesurer ce que la session nous a coûté

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Arrêter une boucle et reprendre sans perdre le fil](../05-reprise/LECTURE.md)

**TL;DR** — Nous distinguerons les appels d’outils, les tokens facturés et notre temps de travail. Un petit calcul permet de voir pourquoi le cache et les tours successifs changent la facture.

## Un appel d’outil n’est pas une unité de facture

Le journal du banc nous dit combien d’outils ont été appelés et combien de temps chacun a pris. Il ne contient aucun token de modèle : nous n’en avons appelé aucun.

Dans une vraie session, le modèle reçoit un contexte, produit une réponse et peut demander plusieurs outils. Leurs résultats peuvent alimenter un nouvel appel au modèle. Le nombre d’outils ne permet donc pas de déduire directement le nombre de tokens, ni le prix final.

Une partie du contexte peut être réutilisée d’un tour à l’autre. Selon le fournisseur, le cache change la manière dont ces tokens sont traités et facturés ; sa lecture et parfois son écriture ont des conditions propres[^p5-cache]. Ne multipliez pas simplement la taille de la conversation affichée par le prix d’entrée.

Pour un relevé réel, partez des compteurs d’usage exposés par le fournisseur ou l’application. Regardez ce qu’ils incluent : entrée totale, entrée en cache, sortie, éventuels tokens de raisonnement et outils facturés séparément. Si l’entrée totale inclut déjà le cache, ne comptez pas celui-ci une deuxième fois.

Un abonnement ajoute une autre question : avez-vous dépensé de l’argent supplémentaire ou consommé une partie d’un quota déjà payé ? Les deux informations sont utiles, mais elles ne se lisent pas de la même façon.

[^p5-cache]: Anthropic, [fonctionnement et tarification du cache de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Les conditions de cette documentation ne s’appliquent pas automatiquement aux autres fournisseurs.

## Faire le calcul sur deux appels

Ouvrez `usage-exemple.csv`. Nous y avons placé deux appels fictifs pour comprendre le calcul, avec trois catégories **qui ne se recouvrent pas** :

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

Le résultat est `0.004200` unités monétaires. Passez ensuite `--prix-cache` à `2` : le coût devient `0.006000`. Vous venez de changer la tarification d’une catégorie, pas le nombre de tokens ni la qualité de la réponse.

Ce calcul simplifié ne couvre pas une écriture de cache facturée séparément, un outil payant ou un abonnement. Pour l’utiliser sur vos données, adaptez les colonnes à la facture concernée. Il n’est pas nécessaire d’avoir une précision au millionième pour décider si l’outil vous sert ; elle nous permet ici de vérifier une petite formule sans arrondir trop tôt.

## Le temps gagné se mesure jusqu’à la validation

Reprenez une tâche courte de la partie 4. Notez le temps passé à préparer la demande, attendre, corriger la réponse et vérifier le résultat. Conservez aussi les moments où vous avez pu faire autre chose pendant l’exécution.

| Ce que l’on relève | Ce que cela permet de comprendre |
| --- | --- |
| Temps écoulé entre le début et la fin | La durée de la tâche dans le planning |
| Temps passé à intervenir et relire | L’attention que la tâche vous a demandée |
| Coût ou quota consommé | La dépense liée au service |
| Résultat vérifié et corrections nécessaires | Ce que vous avez obtenu pour ce temps et cette dépense |
Table: Plusieurs mesures pour une même tâche

Évitez de comparer une première découverte laborieuse à une seconde tentative dont vous connaissez déjà la solution. Pour explorer l’intérêt de l’aide, choisissez plusieurs tâches comparables et conservez aussi les essais qui se passent mal. Nous cherchons un usage qui vous convient, pas une démonstration gagnée d’avance.

En local, l’absence de facture d’API ne fait pas disparaître le matériel, l’électricité et le temps d’installation. Nous approfondirons ces coûts et leurs implications dans la partie consacrée aux choix d’usage.

Vous avez maintenant de quoi distinguer « l’agent a beaucoup travaillé » de « ce travail m’a aidé ». Une recherche bien ciblée ou un test oublié peut suffire ; il n’est pas nécessaire de déléguer tout le développement pour en tirer quelque chose.



---

[Précédent : Arrêter une boucle et reprendre sans perdre le fil](../05-reprise/LECTURE.md)
