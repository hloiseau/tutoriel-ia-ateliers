**TL;DR** — Exportons notre état de travail, rouvrons-le et présentons à nouveau le même lot. Nous allons distinguer une reprise utile d’un deuxième traitement, puis regarder ce qu’il faudrait vérifier avant de programmer des lancements réguliers.

Le point est prêt et son fichier est enregistré. Vendredi prochain, quelqu’un ouvre à nouveau le dossier de courriels. Nora demande toujours deux places, Samir figure toujours dans le suivi et la copie de M001 n’a pas bougé. Comment notre outil saura-t-il ce qui a déjà été pris en compte ?

Il lui faut un état conservé entre deux séances. Nous allons le manipuler à la main dans l’application locale, puis examiner les conditions nécessaires à une future planification. Donner à une horloge une panne à répéter toutes les heures ne nous avancerait pas beaucoup. 😅
