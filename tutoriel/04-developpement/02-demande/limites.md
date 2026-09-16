Ajoutons quelques limites simples à notre travail : nous conservons la fonction `notifier`, les fichiers JSON et les validations existantes. Nous n’ajoutons pas de base, d’envoi de courriel ou de système de préférences.

Pourquoi le préciser ? Parce qu’une demande d’« amélioration des notifications » pourrait facilement produire une architecture plus ambitieuse que notre besoin. Ici, le programme doit continuer à prendre deux états et à renvoyer une décision.

Ces limites guideront aussi notre revue. Si un nouveau fichier de configuration apparaît dans le diff, nous pourrons demander quel comportement du ticket le rend nécessaire.

Dans votre propre travail, gardez ce périmètre à la taille de la tâche. Une condition à corriger mérite que l’on tranche ses cas ambigus ; elle réclame rarement un document de conception de dix pages.
