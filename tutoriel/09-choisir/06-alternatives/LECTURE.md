# 6. Alternatives, logiciels libres et possibilités de s’en passer

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Apprendre et exercer notre métier](../05-apprendre/LECTURE.md) · [Suivant : Construire ses propres critères de choix](../07-decider/LECTURE.md)

**TL;DR** — Comparons des solutions à une tâche précise, jusqu’au résultat utilisable. Le bilan comprend la préparation, la relecture, la correction et la possibilité de travailler sans IA.

Pour repérer un prix négatif, Python sait déjà comparer deux nombres. Il n’a pas besoin qu’on lui explique gentiment de faire attention.

## Repartir de la difficulté réelle

Ouvrez les trois demandes de `cas/equipe.md`. Pour chacune, essayez d’abord de formuler ce qui est pénible ou fragile aujourd’hui.

| Difficulté | Une première possibilité |
| --- | --- |
| Vérifier les mêmes contraintes sur chaque ligne | Script, contraintes de données ou tests automatisés |
| Retrouver une règle dans quelques pages | Recherche classique ou documentation mieux rangée |
| Oublier des scénarios lors d’une recette | Gabarit, revue par un collègue ou proposition de scénarios par une IA |
| Comprendre un bug inhabituel | Débogueur, documentation, réduction du cas, discussion ou aide ciblée de l’IA |

Le choix peut combiner ces outils. Un modèle peut proposer des scénarios, puis un humain les vérifier et un programme exécuter les assertions. Nous n’avons pas besoin de lui confier également le droit de décider que le résultat est bon.

Pour gagner en autonomie, nous pouvons privilégier des formats exportables, des logiciels libres et des modèles dont les conditions permettent l’usage envisagé. Nous disposerons ainsi de davantage de moyens d’agir sur l’outil. Les données et le travail humain restent à examiner, quelle que soit la licence.

Vous pouvez aussi garder l’IA hors de votre développement. Si les tests manuels sont la partie qui vous épuise, commencez éventuellement par une aide sur leur préparation. Si cette aide ne vous convient pas, un gabarit amélioré peut rester le meilleur résultat de l’expérience.

## Compter jusqu’au résultat utilisable

Choisissez une petite tâche dont vous saurez vérifier le résultat, par exemple préparer les scénarios d’un ticket bien déterminé ou le point d’équipe à partir d’un lot de messages. Avant de commencer, définissez ce que vous attendez : les cas importants, les résultats attendus et les décisions qui doivent rester ouvertes.

Dans `fiches/comparaison.md`, préparez deux essais : l’un sans IA, avec documentation et outils habituels ; l’autre avec l’aide que vous souhaitez examiner. Évitez de faire deux fois exactement le même problème en appelant cela une comparaison équitable : le deuxième essai profite du premier. Deux tâches proches, un ordre alterné sur plusieurs essais et des critères identiques réduisent certains biais, sans transformer notre carnet personnel en étude scientifique.

Notez le temps actif consacré à préparer, produire, relire, corriger et vérifier, sans compter deux fois le même intervalle. Ajoutez séparément l’attente qui vous a réellement bloqué. Si le modèle travaille pendant que vous faites autre chose, ce temps n’est pas une attente bloquante ; vous pouvez le noter dans le commentaire.

Vous pouvez remplir cette comparaison dans un document ou un tableau, sans programme. Le script ci-dessous est une variante facultative pour calculer le bilan fourni :

```bash
python bilan.py exemples/temps-fictifs.json
```

Les nombres du fichier sont **inventés pour montrer le calcul**. Dans ce scénario fictif, l’essai assisté produit plus vite et demande davantage de relecture et de correction : son occupation totale atteint 28 minutes, contre 23 pour l’autre. Aucune comparaison avec un outil réel n’a été réalisée ici.

![Dans cet exemple fictif, la production prend 12 minutes sans IA et 3 avec IA ; les autres étapes portent le total à 23 et 28 minutes.](../images/temps.png)
Figure: Durées inventées pour illustrer le calcul, sans comparaison d’outils réels

Si vous utilisez le script, copiez ensuite `exemples/temps-a-remplir.json`, remplacez ses valeurs manquantes par vos observations et lancez-le sur votre copie. Pour le parcours travail, vous pouvez conserver la fiche d’essai remplie à la main. Une durée inconnue reste inconnue dans les deux cas. Conservez aussi le statut du résultat : un travail abandonné ou encore incorrect ne devient pas « meilleur » parce qu’il s’est arrêté plus tôt.

Vous pouvez ouvrir `corriges/comparaison.md` pour examiner les pièges du bilan fictif et la façon de décrire un essai resté incomplet.

## Quand les études ne racontent pas toutes la même chose

Une expérience METR menée en 2025 sur 16 développeurs expérimentés travaillant dans leurs dépôts a mesuré un ralentissement avec les outils alors disponibles. Les participants avaient pourtant l’impression d’être accélérés. Ce résultat appartient à des développeurs, des tâches, des dépôts et des outils précis.[^p8-metr25]

En février 2026, METR explique que son expérience suivante rencontre des biais de sélection et des difficultés de mesure, notamment avec des usages parallèles. L’organisme considère ces nouvelles données insuffisantes pour donner une estimation fiable de l’effet courant. On ne peut donc pas transporter le résultat de 2025 jusqu’à aujourd’hui comme une constante, ni annoncer son contraire avec la même assurance.[^p8-metr26]

Conservons donc nos traces. « J’ai eu l’impression d’aller plus vite » et « le résultat vérifié m’a demandé moins de travail » sont deux observations possibles, qui peuvent diverger.

Le confort compte aussi. Une aide peut rendre une tâche moins pénible sans réduire son temps total, et ce résultat peut très bien nous convenir si nous le décrivons ainsi. Quant au nombre de lignes produites, il renseigne surtout sur le nombre de lignes que quelqu’un devra ensuite comprendre.

Enfin, notre essai doit inclure les personnes qui récupèrent le travail. Si nous économisons vingt minutes en passant une heure de correction à un collègue, nous avons surtout changé l’endroit où le coût apparaît.

[^p8-metr25]: Becker et al., [*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*](https://arxiv.org/abs/2507.09089), 2025.
[^p8-metr26]: METR, [*We are Changing our Developer Productivity Experiment Design*](https://metr.org/blog/2026-02-24-uplift-update/), 24 février 2026.

Le bilan fait apparaître la préparation, les corrections, l’attente et l’état du résultat derrière la vitesse d’apparition du code. Il nous reste à transformer ces observations en décision applicable par l’équipe.

---

[Précédent : Apprendre et exercer notre métier](../05-apprendre/LECTURE.md) · [Suivant : Construire ses propres critères de choix](../07-decider/LECTURE.md)
