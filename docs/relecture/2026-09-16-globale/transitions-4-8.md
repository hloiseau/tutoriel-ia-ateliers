# Passe adverse — transitions des parties 4 à 8

Session : `2026-09-16-globale`
Périmètre : lecture seule des raccords 4→5, 5→6, 6→7 et 7→8, puis de la fermeture de la partie 8.

## Bilan général

Les statuts expérimentaux restent cohérents :

- la partie 5 annonce clairement que son banc rejoue des demandes écrites à la main et n’appelle aucun modèle ;
- la partie 6 distingue son client et son serveur MCP sur CPU, sans modèle, des essais menés dans l’assistant habituel ;
- la partie 7 attribue ses résultats au parcours CPU et laisse l’adaptation du LLM sur RTX 3090 Ti à exécuter ;
- aucun raccord ne promet qu’une courte réponse sur CPU suffit à obtenir un agent de code utilisable.

Les principaux défauts concernent le passage entre les dossiers des parties 4 et 5, quelques promesses trop larges et le résumé final, qui aplatit parfois la différence entre banc, protocole et agent réel.

## Raccord 4→5

### 1. Deux dossiers de travail sont momentanément confondus

La conclusion de la partie 4 demande de conserver `mon-suivi`. L’introduction de la partie 5 ajoute : « Il vous faut Python 3.12 et les petits fichiers de l’atelier précédent. » Pourtant, le premier chapitre de la partie 5 fait télécharger un dossier séparé, contenant `banc.py` et une copie initiale du projet, puis précise : « Nous ne toucherons pas à votre correction de la partie 4. » `mon-suivi` ne sert que pour les observations dans l’assistant.

Le lecteur peut donc croire qu’il doit lancer le banc dans `mon-suivi`, où `banc.py` n’existe pas.

Proposition précise dans `tutoriel/05-agents/introduction.md` : remplacer la dernière phrase par une distinction explicite, par exemple :

> Gardez `mon-suivi` pour observer votre assistant. Le banc Python se télécharge dans un dossier séparé et fonctionne avec Python 3.12, sans nouveau service ni GPU.

Le chapitre d’installation peut alors conserver son explication de la copie initiale du projet.

### 2. « Combien coûte la session » promet une mesure que la partie ne produit pas seule

La conclusion de la partie 4 annonce « combien coûte la session ». La partie 5 explique correctement comment lire des compteurs réels, mais son calcul fourni repose sur des tokens et des tarifs fictifs. Le relevé de temps réel dépend d’une manipulation du lecteur dans son assistant.

Proposition précise dans `tutoriel/04-developpement/conclusion.md` : annoncer « ce qu’il faut compter pour estimer le coût d’une session » ou « ce que les journaux permettent réellement de compter ». Cette formulation correspond au contenu sans transformer l’exemple fictif en mesure.

### 3. Définitions

`agent` et `contexte` ne sont pas redéfinis inutilement. Le mode agent a déjà été rencontré en partie 4, et le premier chapitre de la partie 5 décompose immédiatement demande, contrôle et résultat. La progression est bonne.

## Raccord 5→6

### 1. Le banc ne « devient » pas le serveur MCP

La conclusion de la partie 5 dit : « lorsque les outils quitteront notre petit banc » puis « nous allons les brancher avec MCP ». La partie 6 construit en réalité un nouvel atelier autour de tickets et de documents fictifs. Le serveur MCP est bien réel au sens du protocole, mais il ne s’agit pas d’une conversion du banc de la partie 5.

Proposition précise dans `tutoriel/05-agents/conclusion.md` : remplacer ce mouvement par :

> Gardez les journaux et votre fiche de reprise. Dans la partie suivante, nous retrouverons les mêmes questions avec un serveur MCP, puis nous décrirons une procédure réutilisable dans un skill.

Cette phrase conserve le lien conceptuel sans promettre une continuité de code inexistante.

### 2. Première mention de MCP

« Un vrai serveur MCP » apparaît dans le TL;DR avant que son rôle soit donné. MCP et les skills ont déjà été présentés brièvement en partie 2, puis annoncés à la fin de la partie 5 ; il n’y a donc pas de notion entièrement nouvelle supposée sans préparation. Le paragraphe suivant donne une distinction suffisante : le serveur fournit l’accès, le skill décrit la procédure.

Une micro-précision serait néanmoins utile lors de l’harmonisation : écrire « un serveur utilisant le protocole MCP » à la première occurrence évite de donner à « vrai » le sens de « avec un modèle ». Le premier chapitre rappelle heureusement qu’aucun modèle n’intervient.

### 3. Preuves

Aucune contradiction trouvée entre le banc et le modèle réel. Les rappels « sans modèle » sont nombreux, mais ils protègent une distinction qui change le sens des résultats. Ils peuvent rester.

## Raccord 6→7

### 1. Le meilleur raccord disparaît avant le changement de partie

La section `06-mcp-skills/07-ranger/suite.md` prépare très bien la partie 7 avec l’échec de la recherche littérale entre « alerte » et « notification ». Elle annonce ensuite la recherche documentaire puis la modification des poids. Le chapitre et la partie se terminent toutefois par deux conclusions plus générales ; lorsque le lecteur arrive à la partie 7, ce fil concret s’est éloigné.

Proposition précise dans `tutoriel/06-mcp-skills/conclusion.md` : ajouter une seule phrase finale qui reprend l’incident sans refaire toute la morale, par exemple :

> Notre recherche littérale manque encore `alerte` lorsque la source parle de `notification`. La partie suivante partira de cet échec pour améliorer la recherche avant de toucher aux poids d’un modèle.

L’introduction de la partie 7 peut rester telle quelle : elle rappelle que les poids sont restés intacts et ouvre naturellement les différentes significations de « faire son IA ».

### 2. Définitions et preuves

Le **RAG** est défini au moment où il devient utile. `contexte`, `poids`, `MCP` et `skill` sont réemployés sans nouvelle définition scolaire ; le lecteur les a déjà manipulés. Les affirmations CPU/GPU concordent avec les journaux : génération documentaire et petit réseau sur CPU, adaptation de LLM sur GPU encore à faire.

### 3. Emplacement possible d’un futur parcours hors développement

La jointure après la partie 6 reste le meilleur point d’insertion pour un futur parcours documentaire et de pipelines : outils, permissions, MCP et skills sont acquis, tandis que l’adaptation des modèles n’a pas commencé. Aucun contenu ne doit être greffé pendant cette passe. Si ce chantier est accepté plus tard, il faudra seulement remplacer le raccord direct « recherche littérale → partie suivante » par un raccord vers la nouvelle partie, puis renuméroter les références à la dernière partie.

## Raccord 7→8

### 1. Le raccord concret existe dans le chapitre, mais pas dans la conclusion de partie

`07-ia-maison/08-comparer/conclusion.md` pose exactement la bonne question : voulons-nous consentir l’effort, avec quelles données, dépendances et conséquences ? La conclusion globale de la partie 7 se termine ensuite sur le statut de l’expérience GPU. Cette précision est nécessaire, mais elle devient la toute dernière idée avant le changement de partie.

Proposition précise dans `tutoriel/07-ia-maison/conclusion.md` : conserver la phrase sur le GPU, puis ajouter une phrase courte vers la décision, par exemple :

> Il reste maintenant à décider si les bénéfices observés justifient les données, les dépendances et le travail que chaque piste demande.

### 2. « Notre petit modèle » est devenu ambigu

L’introduction de la partie 8 commence par « Notre petit modèle fonctionne. Enfin… il calcule ». La partie 7 vient pourtant d’utiliser deux objets très différents : SmolLM2 pour trois réponses documentaires et un réseau de caractères entraîné et adapté sur CPU. « Notre petit modèle » peut désigner l’un ou l’autre.

Proposition précise dans `tutoriel/08-choisir/introduction.md` : partir des résultats plutôt que d’un modèle indéterminé, par exemple :

> Nos programmes tournent, mais leurs résultats restent inégaux : une recherche manque une formulation, une réponse invente une durée et une adaptation dégrade l’ancien format. 🙂

La phrase suivante peut alors mener aux décisions d’usage sans réexpliquer le fonctionnement des modèles.

### 3. Le résumé rapproche trop le banc d’un agent réel

« Nous savons aussi qu’un agent peut appeler des outils, préparer une recette ou modifier du code » rassemble sous un même sujet des preuves différentes : agent utilisé dans l’atelier de développement, demandes rejouées par un banc sans modèle, serveur MCP exécuté sans modèle et skill dont les essais avec un assistant réel restent à mener.

Proposition précise : remplacer cette phrase par une formulation sur les mécanismes réellement distingués, par exemple :

> Nous avons aussi séparé la demande d’outil de son exécution, construit un serveur MCP et écrit une procédure réutilisable.

La décision d’usage peut ensuite porter sur ces éléments sans affirmer qu’une seule expérience d’agent les a tous validés.

## Fermeture de la partie 8

### 1. Inventaire final trop aplati

La conclusion résume « travaillé avec des agents, des MCP et des skills ». Cette formule efface de nouveau les statuts de preuve et emploie MCP comme un objet pluriel indéterminé.

Proposition précise dans `tutoriel/08-choisir/conclusion.md` : remplacer ce segment par un inventaire factuel :

> […] développé avec un assistant, observé la boucle d’outils avec un banc, construit un serveur MCP et écrit un skill, puis assemblé notre propre assistant documentaire.

Cette précision suffit ; la conclusion n’a pas besoin de répéter toutes les limites expérimentales.

### 2. Morale répétée

Trois idées reviennent dans l’introduction puis dans les trois derniers paragraphes : adapter l’outil au besoin, ne pas organiser le métier autour de lui et pouvoir s’en passer. Elles appartiennent bien à la thèse de Hugo, mais leur répétition immédiate affaiblit la chute.

Proposition de resserrement :

- conserver le paragraphe assumé « Selon moi […] il a raté sa place », qui porte la voix de l’auteur ;
- réduire le paragraphe suivant à la liberté de choix, sans répéter l’exemple des tests déjà présent dans l’introduction ;
- garder le dernier paragraphe presque intact, car il donne une action concrète et ferme le tutoriel sur une décision réversible.

Une version possible du paragraphe intermédiaire serait :

> Vous pouvez continuer sans IA, ou lui réserver une tâche précise dont vous savez vérifier le résultat. Aucun abonnement ne vous oblige à glisser l’outil partout. 🙂

### 3. Future ouverture hors développement

La conclusion actuelle parle surtout de génération de code et de « continuer à développer sans IA », ce qui reste cohérent avec le tutoriel présent. Si la partie hors développement est ajoutée, il faudra alors élargir ce bilan aux documents et aux pipelines. Le faire dès maintenant annoncerait un parcours absent ; aucune modification n’est recommandée dans cette passe.

## Priorités proposées au coordinateur

1. Corriger le double dossier au raccord 4→5 : c’est le seul problème susceptible de bloquer directement une manipulation.
2. Préciser le résumé de la partie 8 pour préserver la distinction entre banc, MCP et agent réel.
3. Rétablir les deux raccords concrets 6→7 et 7→8 dans les conclusions globales.
4. Resserer la morale finale sans affaiblir la position de l’auteur.
5. Garder la jointure après la partie 6 disponible pour le chantier hors développement, sans l’annoncer dans le cours actuel.

## Contrôle

- Lecture effectuée sur les introductions et conclusions globales des parties 4 à 8, ainsi que sur les premiers et derniers chapitres nécessaires pour vérifier les raccords.
- Recherche ciblée des occurrences d’`agent`, `contexte`, `MCP`, `skill`, `CPU`, `GPU`, `banc` et `modèle réel` dans les parties concernées.
- Aucun fichier du tutoriel modifié.
