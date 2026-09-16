# 4. Promesses, systèmes experts et hivers de l’IA

[Sommaire de la partie](../README.md) · [Sources](.)

Une démonstration réussie donne envie de passer à un problème plus grand. Pour les chercheurs comme pour les personnes qui financent leurs travaux, la tentation est compréhensible : si la machine réussit ici, pourquoi ne réussirait-elle pas ailleurs ?

Le passage est parfois beaucoup plus difficile qu’il n’en a l’air. Les années 1970 vont le rappeler assez brutalement à une partie de la recherche en IA.

## Quand le petit monde devient trop grand

Dans nos exemples, les objets et les règles étaient peu nombreux. Mina était un chat, les catégories étaient connues et les termes ne changeaient pas de sens au milieu du raisonnement.

Imaginons maintenant qu’un programme doive organiser les déplacements dans un entrepôt. Il connaît quelques allées et quelques caisses. Il trouve facilement un parcours. Puis nous ajoutons des centaines de caisses, des passages bloqués, plusieurs engins et des horaires à respecter.

Le programme doit examiner beaucoup plus de situations. Il faut aussi lui fournir des informations nouvelles : une caisse peut être fragile, un passage momentanément fermé, un engin indisponible. Les règles qui suffisaient à la démonstration ne décrivent plus toute la tâche.

Le programme rencontre donc deux difficultés : le nombre de possibilités à calculer et la quantité de connaissances à représenter. Ajouter de la puissance ne fournit pas automatiquement les règles manquantes.

En 1973, un rapport de James Lighthill, commandé pour examiner l’IA au Royaume-Uni, critique une partie de ses résultats et de ses perspectives. Le témoignage historique de l’université d’Édimbourg décrit la perte de confiance qui suit, ainsi que les réorganisations et les années difficiles pour la recherche.[^h4s1-edinburgh]

On parle d’**hiver de l’IA** pour ces périodes de recul de l’intérêt et des financements. Le froid n’atteint pas tous les laboratoires de la même manière : à Édimbourg, des travaux et des enseignements se poursuivent avant un nouvel essor des applications dans les années 1980.


[^h4s1-edinburgh]: [Jim Howe, Artificial Intelligence at Edinburgh University: a Perspective (2007)](https://www.inf.ed.ac.uk/about/AIhistory.html).

## Concentrer les connaissances sur un métier

Une autre piste consiste à limiter le domaine traité et à fournir au programme des connaissances très spécialisées. C’est le principe des **systèmes experts**.

MYCIN, développé à Stanford dans les années 1970, est un exemple connu de système destiné à conseiller sur certaines infections bactériennes et leurs traitements. John McCarthy s’en sert pour discuter les limites d’un programme spécialisé : son utilisation suppose que la personne qui l’interroge comprenne le contexte et les limites du système.[^h4s2-mycin]

Nous n’allons pas reproduire de règles médicales ici. Prenons plutôt un atelier fictif qui aide à identifier un problème de lampe. Le programme dispose d’une base de connaissances et pose des questions pour sélectionner les règles utiles.

![Un exemple de diagnostic de lampe distingue un problème d’alimentation d’une ampoule à examiner, à partir de réponses à des questions.](../images/systeme-expert.png)
Figure: Quelques règles de diagnostic pour une lampe : chaque réponse ouvre une nouvelle piste.

Le **moteur d’inférence** applique les règles aux faits disponibles. La **base de connaissances** contient les informations et les règles du domaine ; des personnes doivent la constituer, puis l’entretenir.

Ajoutons un modèle de lampe au fonctionnement différent : quelqu’un doit vérifier quelles règles restent valables et comprendre les éventuelles contradictions. Une partie du travail des spécialistes s’est déplacée vers la construction du système.


[^h4s2-mycin]: [John McCarthy, Some Expert Systems Need Common Sense](https://www-formal.stanford.edu/jmc/someneed/someneed.html).

## Des systèmes utilisés dans les entreprises

Au début des années 1980, le système R1, qui sera connu sous le nom XCON, aide à configurer des ordinateurs chez Digital Equipment Corporation. John McDermott décrit un programme qui examine les composants commandés, repère certains éléments manquants et prépare leur organisation.[^h4s3-r1]

Le cas est intéressant parce qu’il ne s’agit plus seulement de gagner une partie ou de réussir une démonstration. Le résultat doit servir aux personnes qui assemblent les machines.

Le rapport raconte aussi le travail nécessaire : apprendre les règles du domaine, consulter la documentation et échanger avec les spécialistes pour traiter des commandes plus complexes. Un système expert demande donc bien plus que de recopier quelques conditions dans un fichier.

Cela ressemble à ce qui se passe lorsque vous reprenez une application métier. Une règle qui tient en une phrase dans la documentation peut cacher des exceptions connues de la seule personne qui utilise le logiciel depuis quinze ans. Il vaut mieux lui parler avant de considérer le sujet comme terminé. 😅

Dans un exemple fictif de configuration, une carte peut être compatible avec un ordinateur mais exiger un câble absent de la commande. Une autre carte peut prendre la place nécessaire à ce câble. Il faut représenter les relations entre les composants, pas seulement conserver une liste de références.


[^h4s3-r1]: [John McDermott, R1: An Expert in the Computer Systems Domain (1980)](https://cdn.aaai.org/AAAI/1980/AAAI80-076.pdf).

## Pourquoi plusieurs « hivers » ?

Les récits de l’IA distinguent habituellement une première période de désillusion dans les années 1970, puis une autre à la fin des années 1980 et au début des années 1990. Les dates varient selon les pays et les domaines : personne n’a éteint deux fois un interrupteur mondial.

Les systèmes spécialisés ont montré leur utilité, mais leur coût de développement, leur maintenance et les limites de leur domaine peuvent rendre leur déploiement décevant. Une entreprise n’achète pas seulement une démonstration : elle doit pouvoir utiliser et faire évoluer le système.[^h4s4-histoire]

L’apprentissage statistique, les réseaux, la recherche de solutions et les systèmes de connaissances ne disparaissent pas tous en même temps. Certaines techniques deviennent même des composants ordinaires de logiciels, sans être présentées en permanence comme de l’IA.

Organiser quelques caisses ne suffit pas à gérer tout un entrepôt. La démonstration peut malgré tout avoir appris quelque chose d’utile aux chercheurs.


[^h4s4-histoire]: [IBM, The History of Artificial Intelligence (mis à jour en 2026)](https://www.ibm.com/think/topics/history-of-artificial-intelligence).

Les promesses difficiles à tenir coexistent donc avec des applications spécialisées qui rendent de vrais services. La suite va aussi dépendre des progrès du matériel, des données et des méthodes d’apprentissage.
