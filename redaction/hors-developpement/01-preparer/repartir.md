Sur un dossier aussi court, tout lire à la main reste raisonnable. Le travail devient plus répétitif quand les demandes arrivent chaque semaine, dans des formulations différentes. Avant de l’automatiser, regardons ce que nous faisons réellement.

Comparer deux identifiants, retrouver une ligne déjà enregistrée ou compter des demandes suit des règles précises. Un filtre de tableur ou une automatisation classique peut s’en charger. Nous n’avons pas besoin de demander à un modèle si `M004` est égal à `M004`.

Relever une demande dans un message libre est plus variable. « Nous serons deux », « une place pour moi et une pour un ami » et « pouvez-vous réserver pour deux personnes ? » expriment ici la même quantité. Un modèle peut proposer cette extraction et préparer une synthèse. Nous vérifierons les nombres, les ateliers et les références dans sa réponse, en particulier lorsque le message reste ambigu.

Pour la date, c’est l’équipe qui doit trancher. L’assistant peut rapprocher les deux notes et rédiger la question à Camille. Aucun détail supplémentaire dans la consigne ne lui donnera la réponse à une décision qui manque au dossier.

| Travail | Moyen à essayer | Résultat à vérifier |
| --- | --- | --- |
| Reconnaître la copie de `M001` | Comparaison des identifiants et du contenu | Une demande, deux fichiers conservés |
| Retrouver `M004` dans le suivi | Recherche dans le tableau | La ligne `D001` est gardée, sans doublon |
| Extraire les demandes des messages | Lecture humaine, puis proposition d’un modèle | Quantités, atelier demandé ou absent, source exacte |
| Rédiger le point et les questions | Rédaction humaine ou assistée | Les faits et les incertitudes restent visibles |
| Choisir la date et confirmer les places | Décision des personnes concernées | Décision consignée et message relu avant envoi |
Table: Une première répartition du travail dans notre exercice

En reliant ces opérations, nous obtiendrons un **pipeline** : un enchaînement d’étapes qui reçoit des données et produit un résultat. Certaines étapes appliqueront une règle, d’autres feront appel à un modèle, d’autres attendront une décision. Nous commencerons par des fichiers que l’on dépose soi-même ; le lancement automatique viendra lorsque nous saurons reprendre un traitement interrompu.

Pour l’instant, nous pouvons déjà formuler une demande bien plus précise que « organise la journée » : préparer un point sourcé et des brouillons à partir des fichiers fournis, sans modifier les entrées, sans choisir les informations manquantes et sans envoyer de message. C’est cette tâche que nous pourrons confier à un assistant.
