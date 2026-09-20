# 6. Reprendre sans traiter deux fois

**TL;DR** — Exportons notre état de travail, rouvrons-le et présentons à nouveau le même lot. Nous allons distinguer une reprise utile d’un deuxième traitement, puis regarder ce qu’il faudrait vérifier avant de programmer des lancements réguliers.

Le point est prêt et son fichier est enregistré. Vendredi prochain, quelqu’un ouvre à nouveau le dossier de courriels. Nora demande toujours deux places, Samir figure toujours dans le suivi et la copie de M001 n’a pas bougé. Comment notre outil saura-t-il ce qui a déjà été pris en compte ?

Il lui faut un état conservé entre deux séances. Nous allons le manipuler à la main dans l’application locale, puis examiner les conditions nécessaires à une future planification. Donner à une horloge une panne à répéter toutes les heures ne nous avancerait pas beaucoup. 😅


## Sauvegarder et reprendre le lot

Reprenons `pipeline/index.html`, ouvert dans le navigateur depuis le dossier de l’atelier. L’adresse commence normalement par `file://`. Gardez le point `point-quartier-01.md` exporté au chapitre précédent, puis cliquez sur **Exporter l’état**. Enregistrez le fichier `etat-quartier-01.json` à côté de ce point, dans votre dossier de travail.

Les deux fichiers ont des usages différents. Le point contient le texte à relire ou à partager plus tard selon les décisions de l’équipe. L’état permet à l’application de retrouver les messages pris en compte. Conserver seulement le point obligerait à reconstituer cette mémoire à partir de son contenu.

Ouvrez l’état avec un éditeur de texte. Son format JSON emploie les mêmes accolades et listes que l’extraction du chapitre 3. Cherchez les identifiants : M004 était connu dès le départ ; M001, M002 et M005 ont été retenus dans le point exporté. Leur présence indique une prise en compte dans ce travail interne. Elle ne confirme aucune inscription et ne donne aucune réponse à Nora.

Ouvrez maintenant l’application dans un nouvel onglet. Avec **Reprendre un état**, choisissez le fichier que vous venez d’enregistrer. Rechargez ensuite la même extraction JSON, ou cliquez sur **Charger l’exemple fictif** si vous suivez la démonstration, puis sur **Contrôler et préparer**. Ce lot ne doit plus apporter de message nouveau : l’application indique qu’il est déjà pris en compte et bloque l’export d’un rapport supplémentaire. Consultez le **Journal** pour retrouver le chargement et le contrôle. Si M001 revient comme une nouveauté, vérifiez que vous avez repris l’état sauvegardé *après* l’export du point.

Nous venons de distinguer deux doublons. La copie de M001 se trouvait dans un même lot : la comparaison des identifiants et des contenus permettait de la rapprocher. Ici, c’est un lot entier qui revient lors d’un autre lancement. Le programme a besoin de l’historique pour reconnaître ce retour. Le nom de Nora serait une mauvaise clé dans les deux cas, puisque M005 est une vraie question supplémentaire.

Le fichier d’état reste inspectable et modifiable. L’application vérifie sa structure et certaines cohérences, mais une personne peut toujours reprendre une ancienne sauvegarde ou travailler simultanément sur une autre copie. Cela convient à notre manipulation individuelle ; une équipe partageant un même traitement aurait besoin d’un stockage commun et de règles pour éviter les écritures concurrentes. Nous ne les obtenons pas en renommant ce fichier « base officielle ».

Gardez donc ensemble les entrées, l’extraction utilisée, le point et l’état qui suit son export. Vous pourrez retrouver ce qui a été fait sans dépendre d’un onglet resté ouvert depuis vendredi.


## Passer à des exécutions régulières

Imaginons maintenant deux interruptions. Ces scénarios sont fictifs ; ils servent à examiner notre procédure de reprise.

Dans le premier, l’onglet se ferme avant l’export du point. Reprenez le dernier état enregistré, rechargez l’extraction et préparez à nouveau le texte. La nouvelle proposition devra être relue et approuvée. Aucun message extérieur n’est parti pendant cette interruption, puisque l’application ne dispose d’aucun moyen d’en envoyer.

Dans le second, le point a été téléchargé, puis l’onglet se ferme avant **Exporter l’état**. Le fichier se trouve bien dans vos téléchargements, mais votre dernière sauvegarde d’état ignore encore ce traitement. Reprendre cette sauvegarde pourra produire à nouveau les mêmes propositions. Examinez le point conservé et son lot avant de poursuivre ; si vous refaites l’export local pour reconstituer l’état, gardez une seule version comme référence. Cela explique l’ordre de nos gestes : vérifier le fichier obtenu, puis sauvegarder l’état correspondant.

Le marquage a lieu lorsque l’application déclenche le téléchargement. Elle ne peut pas savoir si vous l’annulez ensuite ou si vous conservez le fichier dans le bon dossier. Même avec cet ordre, il faut donc regarder le fichier obtenu. Nous maîtrisons ici une séance locale avec des fichiers, ce qui rend la récupération assez simple.

Une action distante ajoute une autre difficulté. Supposons qu’un futur outil demande à un service d’envoyer un courriel. Le service accepte, puis la connexion coupe avant que notre outil reçoive sa réponse. « Je n’ai pas reçu la confirmation » laisse deux possibilités : l’envoi a eu lieu, ou il n’a pas eu lieu. Relancer aveuglément peut envoyer le message deux fois ; marquer l’action comme terminée peut oublier un envoi qui a échoué.

Pour certaines API, une **clé d’idempotence** permet de désigner la même opération à chaque tentative. Le service qui prend en charge cette clé peut alors reconnaître la reprise. Il faut vérifier son contrat, notamment la durée de conservation des clés et la façon de retrouver le résultat.[^travail-idempotence] Un identifiant écrit uniquement dans notre journal ne suffit pas à obtenir ce comportement chez le destinataire. Si son service ne le propose pas, il faut prévoir une recherche du résultat distant et laisser les cas ambigus à une personne.

Avant un déclenchement régulier, faites donc fonctionner manuellement un lot, son rejeu, une entrée invalide et une reprise. Déterminez aussi qui regardera les échecs et comment arrêter les prochains lancements. L’application locale reste lancée à la demande : elle n’installe aucun traitement en arrière-plan.

Pour une future planification dans un autre outil, commencez avec une seule exécution à la fois et une fréquence adaptée à l’arrivée des données. Décidez quoi faire lorsqu’un lancement précédent attend encore une validation. Dans notre événement, accumuler dix propositions presque identiques pendant que Camille cherche la date aurait surtout pour effet d’occuper Camille.

[^travail-idempotence]: Stripe, [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), documentation consultée le 17 septembre 2026. Cet exemple décrit un contrat d’API prenant en charge une clé d’idempotence ; aucun appel à ce service n’est nécessaire dans l’atelier.


## Compter le coût du travail terminé

Ouvrez `evaluation/fiche-essai.md` et faites-en une copie pour votre séance. Elle permet de rapprocher le résultat et le travail nécessaire pour l’obtenir. Si vous avez utilisé **Charger l’exemple fictif**, indiquez-le : la durée mesurée concerne alors les contrôles et les manipulations, sans extraction par un modèle.

Pour un essai avec assistant, gardez la réponse brute avant de la corriger. Notez le temps passé à préparer les fichiers, attendre, relire les sources, corriger et reprendre une erreur. Le temps de relecture nous intéresse particulièrement. Un point produit rapidement mais dont chaque phrase demande une enquête peut coûter davantage de travail que notre première lecture manuelle.

Le **Journal** aide à retrouver les opérations de l’application. Votre fiche complète ce qu’il ne mesure pas : pourquoi vous avez refusé une proposition, quelles corrections vous avez faites et ce qui manque encore. Évitez d’y recopier des documents personnels entiers ; des références vers les fichiers utiles suffisent souvent. Notre dossier est fictif, mais une méthode de suivi doit aussi rester praticable avec de vraies données.

Pour l’argent, séparez l’accès à un service, les éventuels appels facturés à l’usage et l’hébergement d’un orchestrateur. Un abonnement de conversation et une API peuvent relever de facturations distinctes. Vérifiez ce que votre contrat inclut avant un essai. Quand le fournisseur fournit un relevé, conservez la quantité et le montant constatés avec leur unité ; lorsqu’il manque, écrivez « non disponible » plutôt que de déduire un prix à partir d’une durée.

Une exécution locale avec l’exemple fictif ne produit aucun appel de modèle. Elle ne permet donc pas d’estimer une consommation de tokens ou le prix d’une future automatisation. De même, un abonnement déjà payé reste une dépense, même si la facture ne détaille pas le coût de cette séance.

Comparez enfin le résultat au point manuel du premier chapitre. Avons-nous gardé les deux dates ? Léo attend-il toujours qu’on lui demande son atelier ? Le temps gagné, s’il y en a, concerne-t-il une tâche que vous ferez assez souvent pour entretenir le dispositif ? La fiche laisse ces réponses ouvertes : vos observations décideront de la suite.


Nous pouvons fermer le navigateur, reprendre un état et reconnaître un lot déjà retenu dans le point. Nous savons aussi où la reprise demande une vérification : entre la production d’un résultat et la sauvegarde qui en garde la trace, puis, pour un futur service distant, lorsque son accusé de réception manque.

Avec les fichiers de la séance et sa fiche d’essai, nous avons de quoi comparer les façons de travailler. Gardons-nous tout le pipeline, seulement une aide à la rédaction, ou notre premier tableau ? C’est le choix qui nous reste à faire.

