Vous aviez rejeté une solution, et l’agent la propose de nouveau. Il oublie une contrainte ou revient sur un fichier déjà vérifié. On parle souvent de *drift* ou de *drifting* pour décrire cette dérive au fil de la session ; le mot ne donne pas, à lui seul, sa cause.

Une mauvaise réponse peut venir d’un contexte incomplet, d’une consigne contradictoire, d’un résumé qui a perdu une décision ou des limites du modèle. Une grande fenêtre de contexte ne garantit pas que toutes les informations seront exploitées aussi bien. Des travaux ont notamment observé des variations selon la position de l’information dans les longs contextes étudiés[^p5-contexte].

Si votre outil compresse l’historique, cherchez ce qu’il a conservé. Le résumé contient-il le cas « retour en stock avec baisse » ? Dit-il quel fichier a été modifié, ou seulement « correction terminée » ?

On peut aussi déléguer une recherche à un autre agent pour ne récupérer que les passages utiles. Cela demande encore de vérifier le résumé et de pouvoir retrouver ses sources ; les appels supplémentaires ne deviennent pas gratuits parce qu’ils se déroulent dans une autre conversation.

Nous préparerons plus loin une fiche de reprise. Pour le moment, gardez le ticket, les décisions et les fichiers comme points d’appui lorsque l’historique devient difficile à suivre.

[^p5-contexte]: Nelson F. Liu et al., [*Lost in the Middle: How Language Models Use Long Contexts*](https://arxiv.org/abs/2307.03172), 2023. Ces expériences portent sur des modèles et des tâches donnés ; elles ne fixent pas un seuil universel de longueur à éviter.
