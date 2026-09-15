Une autre piste consiste à limiter le domaine traité et à fournir au programme des connaissances très spécialisées. C’est le principe des **systèmes experts**.

MYCIN, développé à Stanford dans les années 1970, est un exemple connu de système destiné à conseiller sur certaines infections bactériennes et leurs traitements. John McCarthy s’en sert pour discuter les limites d’un programme spécialisé : son utilisation suppose que la personne qui l’interroge comprenne le contexte et les limites du système.[^h4s2-mycin]

Nous n’allons pas reproduire de règles médicales ici. Prenons plutôt un atelier fictif qui aide à identifier un problème de lampe. Le programme dispose d’une base de connaissances et pose des questions pour sélectionner les règles utiles.

![Un exemple de diagnostic de lampe distingue un problème d’alimentation d’une ampoule à examiner, à partir de réponses à des questions.](image:images/systeme-expert.png)
Figure: Quelques règles de diagnostic pour une lampe : chaque réponse ouvre une nouvelle piste.

Le **moteur d’inférence** est la partie du programme qui applique les règles aux faits disponibles. La **base de connaissances** contient les informations et les règles du domaine. C’est donc bien quelque chose qu’il faut constituer et entretenir.

Si nous ajoutons un modèle de lampe avec un fonctionnement différent, quelqu’un doit vérifier quelles règles restent valables. Si deux règles se contredisent, il faut comprendre pourquoi. L’expertise n’a pas disparu : une partie de son travail a été déplacée vers la construction du système.


[^h4s2-mycin]: [John McCarthy, Some Expert Systems Need Common Sense](https://www-formal.stanford.edu/jmc/someneed/someneed.html).
