# Travailler avec l’IA au-delà du code

État au 17 septembre 2026 : Hugo a retenu le fil rouge de l’organisation d’un événement. L’introduction, le premier chapitre et le dossier fictif sont préparés ; les six chapitres suivants restent à rédiger et leurs parcours à exécuter.

[Lire le début](../archives/redaction/hors-developpement/LECTURE.md) · [Ouvrir l’atelier](../../ateliers/hors-developpement/README.md) · [Vérifications](VERIFICATION.md)

## Le cas retenu

Une petite équipe organise **Les ateliers du quartier**, une journée fictive avec deux ateliers : Reliure et Cartographie. Elle reçoit des inscriptions et des questions, conserve un tableau de suivi et prépare son point d’équipe à partir de notes de réunion. Le premier lot contient cinq fichiers de courriel, dont une copie à l’identique, une demande déjà enregistrée et une inscription incomplète. Deux comptes rendus divergent sur la date de la journée.

Le livrable évolue au fil des chapitres : un point de suivi manuel, une proposition rédigée avec un assistant, puis une chaîne répétable qui prépare des fichiers et attend les décisions nécessaires. Aucun envoi réel ni accès à une messagerie n’est requis pour commencer.

La date contradictoire ne bloque pas toute lecture du dossier : on peut encore relever les demandes et préparer des questions. Elle bloque l’annonce d’une date certaine et les confirmations qui en dépendent. Cette distinction évite un pipeline qui arrête tout au premier doute ou, à l’inverse, propage une décision inventée.

## Une porte d’entrée pour les non-développeurs

Cette partie doit pouvoir se commencer directement avec un navigateur, un éditeur de texte et, facultativement, un tableur. Le premier chapitre ne demande aucun compte. La lecture des ateliers Python des parties précédentes ne doit pas devenir un prérequis caché.

Les termes nécessaires — modèle, contexte, outil, agent, permissions — seront rappelés brièvement au moment de leur usage. Les parties existantes apportent les explications approfondies. Les variantes par script resteront facultatives ; leur code ne doit pas être l’unique manière de suivre une manipulation.

Le parcours gratuit de lecture et de correction manuelle reste complet. Pour la variante avec un modèle, les conditions d’accès et les éventuelles dépenses devront être annoncées avant l’essai. Aucun service payant, modèle local ou matériel de Hugo n’a été essayé pour cette extension.

## Progression prévue

| Chapitre | Situation de départ | Ce que le lecteur fait et observe | Livrable et preuve à conserver |
| --- | --- | --- | --- |
| 1. Préparer le point d’équipe | Cinq courriels, un tableau et deux dates incompatibles | Retrouver les demandes, le doublon, les absences et les décisions ouvertes ; répartir les tâches entre règles, modèle et personnes | Point manuel comparé au corrigé fourni ; chapitre rédigé |
| 2. Faire travailler un assistant sur le dossier | L’équipe veut un compte rendu lisible et des brouillons de réponse | Fournir les bonnes sources, définir le résultat attendu, examiner les fichiers produits et remonter aux passages utilisés | Consigne, version de l’outil, sources réellement transmises, sorties brutes et corrections humaines |
| 3. Refaire le travail avec un pipeline | Un nouveau lot arrive ; recoller les mêmes informations devient pénible | Relier une entrée, des étapes de traitement, un appel de modèle et des sorties ; distinguer l’enchaînement fixé du choix d’outils par un agent | Pipeline exportable et premier journal réel ; erreurs de format et données manquantes visibles |
| 4. Donner accès aux bons outils | Le dossier autonome doit être relié à une source de travail | Délimiter les lectures et les écritures, examiner une intégration et une variante MCP ; limiter les fichiers exposés | Carte des accès, essai de refus et absence de secrets dans les exports |
| 5. Relire avant d’agir | Un brouillon est prêt, mais la date reste litigieuse | Comparer la proposition aux sources, approuver une version précise ou la refuser ; invalider l’accord si le contenu change | Proposition, décision et version concernée ; action finale simulée dans un dossier local |
| 6. Reprendre sans traiter deux fois | Un lancement s’interrompt puis le même lot revient | Retrouver l’état, distinguer message déjà vu et demande réellement nouvelle, limiter les reprises et examiner le coût total | Journaux avant/après, aucun doublon de sortie, durée de relecture séparée du temps machine |
| 7. Garder ce qui nous aide | Plusieurs façons de faire donnent un résultat comparable | Comparer travail manuel, règles classiques, espace de travail agentique et orchestrateur ; essayer une autre tâche courte | Décision argumentée, formats récupérables et procédure pour continuer sans l’outil |

Les difficultés se répartissent dans cette progression. Le premier chapitre ne doit pas épuiser les permissions, l’approbation et les mécanismes de reprise avant qu’ils deviennent utiles.

## Outils : ordre de décision

Le chapitre 2 doit montrer un travail réel dans un espace de travail IA, avec les entrées et les fichiers produits. Les familles évoquées par Hugo — ChatGPT Work, Claude/Cowork et équivalents — restent des pistes à examiner dans leurs documentations courantes. Leurs noms, accès, capacités et limites devront être vérifiés lors de la rédaction. Le relevé du 16 septembre dans la proposition initiale ne prouve aucune exécution.

Le chapitre 3 doit fournir au moins une implémentation de pipeline concrète et exportable. Un orchestrateur visuel, dont n8n est un candidat, correspond au public visé. Le choix n’est pas encore arrêté : il dépendra de l’installation réellement accessible, du modèle utilisable et du fonctionnement vérifié des validations et reprises. Une solution en code pourra compléter ce parcours pour les lecteurs qui le souhaitent.

Conserver un même contrat d’entrée et de sortie permettra de changer d’outil sans changer d’exercice. Éviter de rédiger cinq parcours d’interface avant d’en avoir exécuté un. Les comparaisons détaillées et les captures d’écran porteront une date ; les notions communes resteront dans le corps du cours.

## Intégration dans le tutoriel

Emplacement proposé : après les agents, MCP et skills, avant l’IA maison et les choix d’usage. Aucune renumérotation n’est effectuée à ce stade. Les sources provisoires sont dans `redaction/hors-developpement/`, selon le même format de manifest et de petits Markdown que le tutoriel. Elles restent hors du ZIP global des huit parties.

Lors de l’intégration complète :

- ajuster l’introduction générale et ses prérequis pour indiquer un parcours sans développement ;
- envisager avec Hugo le titre « Comprendre l’IA et travailler avec elle », en conservant toute la pratique de développement ;
- annoncer en fin de partie 6 le passage des tickets aux documents et aux demandes de l’équipe ;
- reprendre le début de l’IA maison, dont « dans la partie précédente » renvoie actuellement au MCP ;
- garder la conclusion sur les choix d’usage à la fin du parcours ;
- mettre à jour sommaire, manifests, liens, statistiques et exports ensemble.

Les acquis des parties 5 et 6 doivent rester utilisables : leurs exemples de développement illustrent déjà les appels d’outils, les limites d’accès et les procédures. Cette nouvelle partie les applique à d’autres tâches, avec une entrée autonome pour les lecteurs qui ne développent pas.

## Jusqu’où le fil rouge porte-t-il ?

L’événement couvre bien la coordination, les sources dispersées et les demandes répétées. Il couvre moins bien l’analyse d’un grand tableau ou la veille documentaire. Le dernier chapitre pourra proposer une variante courte de veille, avec les mêmes questions de provenance, de sélection et de validation, sans créer un deuxième atelier complet.

La suite immédiate est le chapitre 2 : une consigne précise, les fichiers d’entrée seuls, puis un essai réel documenté. Le corrigé et les critères de vérification restent du côté de l’évaluation ; les donner au modèle fausserait la comparaison.
