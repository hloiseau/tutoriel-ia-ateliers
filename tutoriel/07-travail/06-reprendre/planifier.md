Imaginons maintenant deux interruptions. Ces scénarios sont fictifs ; ils servent à examiner notre procédure de reprise.

Dans le premier, l’onglet se ferme avant l’export du point. Reprenez le dernier état enregistré, rechargez l’extraction et préparez à nouveau le texte. La nouvelle proposition devra être relue et approuvée. Aucun message extérieur n’est parti pendant cette interruption, puisque l’application ne dispose d’aucun moyen d’en envoyer.

Dans le second, le point a été téléchargé, puis l’onglet se ferme avant **Exporter l’état**. Le fichier se trouve bien dans vos téléchargements, mais votre dernière sauvegarde d’état ignore encore ce traitement. Reprendre cette sauvegarde pourra produire à nouveau les mêmes propositions. Examinez le point conservé et son lot avant de poursuivre ; si vous refaites l’export local pour reconstituer l’état, gardez une seule version comme référence. Cela explique l’ordre de nos gestes : vérifier le fichier obtenu, puis sauvegarder l’état correspondant.

Le marquage a lieu lorsque l’application déclenche le téléchargement. Elle ne peut pas savoir si vous l’annulez ensuite ou si vous conservez le fichier dans le bon dossier. Même avec cet ordre, il faut donc regarder le fichier obtenu. Nous maîtrisons ici une séance locale avec des fichiers, ce qui rend la récupération assez simple.

Une action distante ajoute une autre difficulté. Supposons qu’un futur outil demande à un service d’envoyer un courriel. Le service accepte, puis la connexion coupe avant que notre outil reçoive sa réponse. « Je n’ai pas reçu la confirmation » laisse deux possibilités : l’envoi a eu lieu, ou il n’a pas eu lieu. Relancer aveuglément peut envoyer le message deux fois ; marquer l’action comme terminée peut oublier un envoi qui a échoué.

Pour certaines API, une **clé d’idempotence** permet de désigner la même opération à chaque tentative. Le service qui prend en charge cette clé peut alors reconnaître la reprise. Il faut vérifier son contrat, notamment la durée de conservation des clés et la façon de retrouver le résultat.[^travail-idempotence] Un identifiant écrit uniquement dans notre journal ne suffit pas à obtenir ce comportement chez le destinataire. Si son service ne le propose pas, il faut prévoir une recherche du résultat distant et laisser les cas ambigus à une personne.

Avant un déclenchement régulier, faites donc fonctionner manuellement un lot, son rejeu, une entrée invalide et une reprise. Déterminez aussi qui regardera les échecs et comment arrêter les prochains lancements. L’application locale reste lancée à la demande : elle n’installe aucun traitement en arrière-plan.

Pour une future planification dans un autre outil, commencez avec une seule exécution à la fois et une fréquence adaptée à l’arrivée des données. Décidez quoi faire lorsqu’un lancement précédent attend encore une validation. Dans notre événement, accumuler dix propositions presque identiques pendant que Camille cherche la date aurait surtout pour effet d’occuper Camille.

[^travail-idempotence]: Stripe, [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), documentation consultée le 17 septembre 2026. Cet exemple décrit un contrat d’API prenant en charge une clé d’idempotence ; aucun appel à ce service n’est nécessaire dans l’atelier.
