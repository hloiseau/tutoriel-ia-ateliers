Vous aviez rejeté une solution ; plus tard dans la session, l’agent la propose de nouveau. Ou il oublie une contrainte et revient sur un fichier déjà vérifié. On parle souvent de *drift* ou de *drifting* pour cette dérive au fil de la session. Le mot décrit ce que nous observons, sans en désigner automatiquement la cause.

La cause peut se trouver dans un contexte incomplet, une consigne contradictoire, un résumé qui a perdu une décision ou les limites du modèle. Agrandir la fenêtre de contexte ne suffit pas toujours : des travaux ont notamment observé des variations selon la position de l’information dans les longs contextes étudiés[^p5-contexte].

Si votre outil compresse l’historique, cherchez ce qu’il a conservé. Le résumé contient-il le cas « retour en stock avec baisse » ? Dit-il quel fichier a été modifié, ou seulement « correction terminée » ?

Un autre agent peut chercher les passages utiles et renvoyer un résumé plus court. Gardez le moyen de retrouver ses sources et relisez ses conclusions. Cette délégation ajoute aussi des appels au modèle, donc du délai et, selon votre accès, des tokens facturés ou du quota consommé.

Lorsque l’historique devient difficile à suivre, revenez au ticket, aux décisions prises et aux fichiers présents. Nous transformerons ces points d’appui en fiche de reprise un peu plus loin.

[^p5-contexte]: Nelson F. Liu et al., [*Lost in the Middle: How Language Models Use Long Contexts*](https://arxiv.org/abs/2307.03172), 2023. Ces expériences portent sur des modèles et des tâches donnés ; elles ne fixent pas un seuil universel de longueur à éviter.
