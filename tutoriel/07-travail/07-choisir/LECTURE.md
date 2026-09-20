# 7. Garder ce qui nous aide

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Reprendre sans traiter deux fois](../06-reprendre/LECTURE.md)

**TL;DR** — Comparons ce que chaque outil nous apporte sur le même dossier, puis essayons de transférer la méthode à une courte veille documentaire. Nous conserverons ce qui facilite le travail, avec les fichiers nécessaires pour continuer autrement.

Le point d’équipe pourrait être prêt depuis le premier chapitre. Depuis, nous avons décomposé sa préparation, utilisé ou préparé un essai d’assistant, relié des étapes et conservé leur état. Ce détour nous donne plusieurs solutions possibles. Encore faut-il choisir celle qui mérite une place dans notre travail quotidien.

Prenez votre point manuel, vos autres résultats si vous avez fait les essais, et la fiche du chapitre précédent. Nous allons les regarder côte à côte, en gardant les erreurs et le temps de correction dans la comparaison.

## Comparer les façons de faire

Commencez par les faits. Un point qui annonce le 17 octobre sans décision supplémentaire contient une erreur, même si ses titres sont impeccables. Un autre qui oublie la question M005 de Nora laisse une tâche de côté. La grille de `corrige/grille-verification.md` nous aide à comparer les résultats avec les mêmes attentes.

Pour les méthodes que vous n’avez pas essayées, gardez la mention « non essayé ». La démonstration locale nous montre des contrôles et des exports ; elle ne mesure pas la qualité d’un modèle. Une documentation commerciale ne remplit pas non plus la ligne « temps de relecture » de notre fiche.

| Manière de travailler | Ce qu’elle peut prendre en charge ici | Ce que nous devons observer |
| --- | --- | --- |
| Lecture et rédaction manuelles | Lire les sources, relever les demandes, écrire le point | Oublis, fidélité aux documents, durée et facilité de reprise |
| Règles classiques, tableur ou application locale | Comparer des identifiants, contrôler les champs et conserver un état | Règles adaptées, cas refusés, comportement au rejeu |
| Assistant ou agent dans un espace de travail | Proposer une extraction, rédiger, parfois manipuler des fichiers et des outils autorisés | Sources réellement utilisées, modifications, corrections et permissions |
| Orchestrateur | Relier les étapes, conserver leurs sorties, déclencher ou reprendre le traitement selon sa configuration | Visibilité des erreurs, validation, maintenance et coût de l’ensemble |
Table: Des moyens qui peuvent être combinés dans le même travail

Un orchestrateur peut appeler un modèle ; une personne peut travailler avec un tableur et un assistant. Nous comparons donc des répartitions du travail. Demander « quel outil est le meilleur ? » sans préciser ce qu’on lui confie laisserait de côté la moitié de notre expérience.

Pour notre petit lot, un tableau et une lecture attentive peuvent suffire. Si les messages deviennent nombreux et variés, l’extraction assistée mérite un essai. Si les mêmes opérations reviennent souvent, leur enchaînement peut devenir intéressant. Chacune de ces décisions dépend encore du temps de contrôle, des incidents et de la facilité à transmettre le travail à quelqu’un d’autre.

Écrivez votre choix dans la fiche : ce que vous gardez, ce que vous laissez manuel et ce qui vous ferait changer d’avis. « Je garde les contrôles de doublons et je rédige moi-même » est une conclusion tout à fait exploitable. « L’outil semble puissant » nous aidera beaucoup moins vendredi prochain.

## Essayer sur une autre tâche

Essayons une tâche voisine : préparer une courte veille pour l’équipe qui organise la journée. Ouvrez `evaluation/veille.md`. Vous y trouverez trois notices entièrement fictives sur le prêt d’un vidéoprojecteur. Elles permettent de tester la méthode sans chercher sur le Web ni transmettre de données personnelles.

Notre destinataire veut savoir si une réservation est possible et à quelle heure retirer le matériel. Une notice décrit la procédure, une autre signale une indisponibilité et la troisième rapporte une possibilité non confirmée. Préparez quatre ou cinq phrases, en gardant pour chaque affirmation sa source et sa date. Faites d’abord votre lecture ; vous pourrez ensuite donner les notices et la consigne à l’assistant de votre choix pour comparer sa proposition.

Le point de vigilance ressemble à celui de notre date d’événement : le document le plus récent ne contient pas forcément une décision. Ici, le compte rendu récent rapporte une suggestion de prêt par un partenaire. Il n’établit ni la disponibilité de son appareil ni son accord. La synthèse doit conserver cette question ouverte.

La transposition demande pourtant de nouveaux critères. Dans les courriels, un identifiant nous aidait à reconnaître une copie. Pour une veille, deux pages différentes peuvent reprendre la même annonce. Il faut regarder leur origine avant de les présenter comme deux confirmations indépendantes. Et une procédure publiée avant la panne du vidéoprojecteur peut rester utile pour comprendre la réservation, tout en étant insuffisante pour affirmer que le matériel est disponible aujourd’hui.

Si vous poursuivez avec de vraies sources publiques, partez d’un périmètre étroit : quelques documents identifiés et une question précise. Conservez leur adresse, le titre, la date du document lorsqu’elle existe et la date de consultation. Lisez les passages qui soutiennent la synthèse. Quand une information manque ou que deux sources se contredisent, gardez la question à résoudre et la personne ou le service susceptible de répondre.

Vous pouvez limiter cet essai aux documents déjà choisis. Demander à un agent de chercher seul ajoute un autre travail à examiner : quelles sources a-t-il trouvées, lesquelles a-t-il écartées, et pourquoi ? Les pièces jointes privées, courriels personnels et accès aux comptes ne sont d’aucune utilité pour notre petit exercice de veille publique.

Si une synthèse correcte nécessite finalement autant de recherches que la rédaction manuelle, notez-le. Elle a peut-être encore un intérêt pour reformuler le texte, ou aucun pour cette tâche. Le transfert de la méthode consiste justement à refaire ce choix, pas à déplacer partout le même pipeline.

## Transmettre et faire évoluer le travail

Avant de garder un outil dans votre équipe, demandez-vous comment une autre personne reprendra le travail. Elle devrait retrouver les entrées, les règles, les propositions et les décisions sans avoir à fouiller dans votre historique de conversation. Dans notre atelier, le dossier de sources, le point et la sauvegarde d’état forment déjà un début de transmission. Ajoutez la fiche d’essai et quelques phrases sur les vérifications qui ont posé problème.

Les formats récupérables comptent autant que les boutons qui font gagner du temps. Un texte Markdown s’ouvre dans un éditeur ; un CSV se relit dans un tableur ; le JSON garde une structure pour un programme. Exporter ces fichiers ne suffit toutefois pas à recréer tout un service : les permissions, les déclencheurs et les validations dépendent aussi de sa configuration. Conservez donc la procédure qui explique leur rôle, ainsi que la façon d’arrêter les prochains traitements.

Essayez une reprise sans assistant. Avec nos fichiers, vous pouvez relire les nouveaux messages, rapprocher leurs identifiants, compléter le point et demander les décisions manquantes. Ce travail est plus ou moins long selon le volume ; il reste identifiable. Si personne ne sait expliquer une sortie sans relancer l’agent, il manque encore quelque chose à la transmission.

Cette question touche aussi l’apprentissage. Une personne qui débute dans la coordination d’un événement doit apprendre à distinguer une demande et un engagement, trouver une information dans les documents et repérer ce qui demande une décision. Lui confier seulement le clic sur « approuver » suppose précisément les acquis qu’elle est en train de construire.

Le premier point manuel conserve ici son intérêt. On peut aussi préparer une extraction, comparer ensuite celle de l’assistant et discuter une différence précise. Léo a demandé deux places, mais n’a pas choisi d’atelier : retrouver cette absence dans son message apprend davantage que corriger silencieusement une ligne. Pour un junior en développement, le même raisonnement s’applique lorsqu’il relit une fonction dont il ne comprend pas encore les conditions.

Selon la tâche, vous pourrez réserver l’assistant à une reformulation, lui confier une première proposition à vérifier, automatiser quelques règles ou tout faire vous-même. Votre choix pourra évoluer avec votre expérience et celle de l’équipe. Il n’impose pas de réorganiser toutes vos habitudes autour du dernier outil essayé.

À ce stade, gardez un dossier assez simple pour pouvoir réellement le reprendre. Une date confirmée devra rejoindre les décisions, un brouillon obsolète être identifiable, et un traitement arrêté le rester. Ces petits gestes rendent le travail transmissible, quel que soit le nombre de modèles cachés derrière l’interface.

Le dossier de l’événement nous a conduits des documents reçus à un point relu, puis à un traitement que nous pouvons reprendre. Vous pouvez en garder toute la chaîne ou seulement quelques éléments : une consigne, une grille de vérification, des contrôles classiques, une sauvegarde lisible. Le même examen s’applique à une veille, un compte rendu ou d’autres travaux de bureau.

Le parcours consacré aux tâches de travail rejoint maintenant la partie 9, sur les choix d’usage et leurs conséquences. Nous y élargirons les questions déjà rencontrées : ce que nous déléguons, ce que nous devons apprendre, les dépendances que nous acceptons et le travail qui reste aux personnes.

Pour les lecteurs qui souhaitent ouvrir le capot, la partie 8 propose un approfondissement facultatif : construire une petite IA maison avec Python. Elle demande de programmer ; vous pouvez rejoindre directement les enjeux et les choix d’usage sans la suivre.

---

[Précédent : Reprendre sans traiter deux fois](../06-reprendre/LECTURE.md)
