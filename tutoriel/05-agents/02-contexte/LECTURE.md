# 2. Donner le contexte utile à l’étape en cours

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Suivre une demande jusqu’à l’outil](../01-boucle/LECTURE.md) · [Suivant : Écrire des consignes que l’on peut contrôler](../03-consignes/LECTURE.md)

**TL;DR** — Le contexte comprend nos messages, mais aussi les extraits et les résultats que l’assistant ajoute. Nous allons comparer deux demandes identiques dont l’une est encombrée par un historique sans rapport.

## Même question, deux contextes

Dans l’atelier, ouvrez `contexte/cible.txt`, puis `contexte/complet.txt`. Les deux contiennent la même fonction, le même cas de remise en stock et la même question. Le second ajoute une série d’anciens messages fictifs sur un tableau de bord.

Dans deux conversations neuves, avec le même modèle, envoyez un fichier puis l’autre. Restez en discussion : nous cherchons une explication, pas une modification. Conservez les deux réponses.

Dans chacune, cherchez les trois valeurs : disponibilité actuelle vraie, baisse de prix fausse, ancienne indisponibilité vraie. Le `or` rend la parenthèse vraie. La réponse doit expliquer pourquoi la fonction initiale décide de notifier malgré le prix identique.

Les deux réponses peuvent être correctes. Ce ne serait pas un échec de l’exercice : cet exemple ne promet pas qu’ajouter du texte fait systématiquement échouer le modèle. Regardez aussi les détours, les affirmations sans rapport et, si votre outil les expose, les tokens utilisés et le délai.

Deux essais ne donnent pas un classement des modèles. Ils permettent de voir ce que vous envoyez et ce que vous pouvez mesurer avant d’en tirer une conclusion.

## Que faut-il garder ?

Pour expliquer une condition, la fonction et les valeurs d’entrée suffisent souvent. Pour modifier son comportement, il faut aussi la règle attendue, les appels concernés et les tests. Ce qui est utile dépend donc de l’action demandée.

![Le contexte de lecture contient un extrait et un cas ; le contexte de modification ajoute le ticket et les tests concernés](../images/contexte.png)
Figure: Le contexte change avec la tâche

Essayez de préparer vous-même les informations pour cette demande : « ajoute un test du retour en stock avec hausse ». Il faut notamment retrouver l’objet `Etat`, la fonction appelée, la façon dont les tests sont écrits et le résultat attendu. Les anciens échanges sur la couleur d’un bouton ne servent pas ici.

On peut alléger une recherche en demandant d’abord les noms des fichiers concernés, puis en ouvrant ceux qui nous intéressent. De même, une sortie de commande peut commencer par le nom du test en échec et sa trace, au lieu de recopier des milliers de lignes réussies. Gardez cependant le journal complet accessible si le résumé masque la cause de l’erreur.

**Réduire le contexte ne consiste pas à couper au hasard.** Une signature sans ses conventions, ou un message d’erreur sans la commande qui l’a produit, peut faire perdre précisément l’information dont le modèle avait besoin.

## Quand la session commence à dériver

Vous aviez rejeté une solution, et l’agent la propose de nouveau. Il oublie une contrainte ou revient sur un fichier déjà vérifié. On parle souvent de *drift* ou de *drifting* pour décrire cette dérive au fil de la session ; le mot ne donne pas, à lui seul, sa cause.

Une mauvaise réponse peut venir d’un contexte incomplet, d’une consigne contradictoire, d’un résumé qui a perdu une décision ou des limites du modèle. Une grande fenêtre de contexte ne garantit pas que toutes les informations seront exploitées aussi bien. Des travaux ont notamment observé des variations selon la position de l’information dans les longs contextes étudiés[^p5-contexte].

Si votre outil compresse l’historique, cherchez ce qu’il a conservé. Le résumé contient-il le cas « retour en stock avec baisse » ? Dit-il quel fichier a été modifié, ou seulement « correction terminée » ?

On peut aussi déléguer une recherche à un autre agent pour ne récupérer que les passages utiles. Cela demande encore de vérifier le résumé et de pouvoir retrouver ses sources ; les appels supplémentaires ne deviennent pas gratuits parce qu’ils se déroulent dans une autre conversation.

Nous préparerons plus loin une fiche de reprise. Pour le moment, gardez le ticket, les décisions et les fichiers comme points d’appui lorsque l’historique devient difficile à suivre.

[^p5-contexte]: Nelson F. Liu et al., [*Lost in the Middle: How Language Models Use Long Contexts*](https://arxiv.org/abs/2307.03172), 2023. Ces expériences portent sur des modèles et des tâches donnés ; elles ne fixent pas un seuil universel de longueur à éviter.



---

[Précédent : Suivre une demande jusqu’à l’outil](../01-boucle/LECTURE.md) · [Suivant : Écrire des consignes que l’on peut contrôler](../03-consignes/LECTURE.md)
