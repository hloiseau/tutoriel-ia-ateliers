# 1. Préparer le point d’équipe

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR** — Ouvrons les documents et préparons un premier point de suivi. Nous allons retrouver les demandes nouvelles, garder les informations manquantes et déterminer les décisions à demander à l’équipe.

On pourrait commencer par écrire « organise la journée » dans un assistant. Encore faudrait-il savoir ce que nous attendons de lui. Préparer un brouillon, inscrire quelqu’un et annoncer une date engagent des choses différentes. Notre première tâche sera plus précise : préparer le point de vendredi, sans envoyer de message ni modifier le tableau de référence.

## Ouvrir le dossier de la journée

Ouvrez le [dossier de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/usages-hors-dev-2026-09-17/ateliers/hors-developpement). Vous pouvez lire les fichiers directement sur GitHub ou récupérer l’[archive du dossier](https://raw.githubusercontent.com/hloiseau/tutoriel-ia-ateliers/usages-hors-dev-2026-09-17/telechargements/atelier-hors-developpement.zip), puis la décompresser dans un dossier de votre choix. Les chemins qui suivent partent de sa racine, là où se trouve `README.md`.

Commencez par `regles-equipe.md`. L’équipe y demande un point de suivi interne, accompagné de propositions de réponse. Elle garde la décision sur la date et les confirmations d’inscription. Les sorties de l’exercice seront de nouveaux fichiers ; les documents reçus resteront intacts.

Le dossier `entrees/` contient les pièces à lire :

| Fichiers | Ce qu’ils apportent |
| --- | --- |
| `courriels/01-nora.txt` à `courriels/05-question-nora.txt` | Cinq fichiers de messages reçus |
| `suivi-initial.csv` | Une demande déjà enregistrée par l’équipe |
| `reunions/01-preparation.md` | Le premier compte rendu |
| `reunions/02-communication.md` | Les notes de la réunion suivante |
Table: Les entrées du premier point d’équipe, dans `entrees/`

Le fichier CSV est un tableau en texte brut : les virgules séparent ses colonnes. Un tableur peut l’ouvrir ; si un dialogue d’import apparaît, choisissez UTF-8 et la virgule comme séparateur. Les noms de colonnes doivent apparaître dans des cellules distinctes. Vous pouvez aussi le lire comme un fichier texte : il ne contient qu’une ligne de données.

Cette ligne indique que la demande `M004`, pour une place en Reliure, est déjà enregistrée sous la référence `D001`. Le statut `demande_enregistree` signifie que l’équipe a reçu et relevé la demande. La place n’est pas encore confirmée.

Pour écrire votre point, partez de `modele-point.md` et enregistrez une copie nommée `point-equipe.md` dans votre propre dossier de travail. Vous pouvez aussi utiliser votre traitement de texte habituel. Gardez simplement un document distinct des entrées. Le dossier `corrige/` nous servira à comparer une fois cette première lecture terminée.

## Deux dates pour une seule journée

Ouvrez `entrees/reunions/01-preparation.md`, puis `02-communication.md`. Le premier compte rendu retient le **10 octobre 2026**. Le suivant mentionne le **17 octobre 2026** dans le projet d’affiche, sans expliquer ce changement.

Quelle date faut-il annoncer ? Avec ces deux documents, nous ne pouvons pas le décider. La seconde réunion est plus récente, mais sa note ne dit ni que le premier choix est annulé ni que la nouvelle date a été confirmée avec la salle. Elle contient peut-être une décision mal documentée. Ou une coquille.

Dans votre point, conservez les deux valeurs avec les fichiers et les sections où vous les avez trouvées. Ajoutez une question pour Camille, qui coordonne la journée : quelle date faut-il retenir et dans quel document la décision sera-t-elle consignée ? Nous pouvons continuer à lire les inscriptions pendant que cette question attend sa réponse.

Passons aux messages. Nora demande deux places en Reliure dans `01-nora.txt`. Ouvrez aussi `03-copie-nora.txt` : son contenu et son identifiant `Message-ID` sont identiques. Le dossier comporte deux copies du même message. Il faut garder une demande de deux places, en signalant la seconde copie, sans supprimer les pièces reçues.

Le message `05-question-nora.txt` vient de la même personne, mais il pose une autre question : à quelle heure commence l’atelier Cartographie ? Son identifiant est différent. Dédupliquer sur le nom ou l’adresse de Nora ferait perdre cette question. Pour notre dossier, l’identifiant du message permet de reconnaître la copie exacte. Avec de vrais courriels, il faudra aussi examiner les renvois, les fils de discussion et les messages dont l’identifiant est absent ; nous y reviendrons au moment des reprises.

Léo, dans `02-leo.txt`, demande une place pour lui et une pour un ami. Nous connaissons donc le nombre de places : deux. Il a oublié d’indiquer l’atelier. Conservez cette absence et préparez la question. Choisir Reliure parce que ce mot apparaît dans le message voisin ajouterait une information que Léo n’a pas donnée.

Enfin, comparez `04-samir.txt` à la ligne du tableau. Le même identifiant `M004` y figure déjà. Il faut conserver la demande enregistrée, sans ajouter une seconde ligne parce que le courriel se trouve à nouveau dans le dossier.

Nous arrivons à cinq fichiers de courriel, quatre messages distincts et trois messages encore absents du suivi initial. Parmi ces trois nouveautés, deux demandent une inscription et le troisième demande un horaire. Ces nombres nous serviront à repérer une copie oubliée ou une demande perdue dans les essais suivants.

## Écrire un point que l’équipe peut utiliser

Reprenez maintenant votre document `point-equipe.md`. L’équipe a besoin de retrouver ce qu’elle peut traiter et ce qu’elle doit encore décider. Une courte synthèse suffit, à condition de pouvoir vérifier ses informations.

Vous pouvez commencer ainsi :

> Deux nouvelles demandes d’inscription sont à examiner : Nora demande deux places en Reliure ; Léo demande deux places sans préciser l’atelier. Samir figure déjà dans le suivi. Nora demande aussi l’horaire de Cartographie.
>
> La date reste à clarifier : le premier compte rendu indique le 10 octobre, le second le 17. Aucun document du dossier ne donne l’horaire propre à Cartographie.

Il s’agit d’un exemple rédigé pour l’exercice. Ajoutez ensuite les références qui permettent à l’équipe de contrôler chaque ligne : un nom de fichier, un identifiant de message ou la section d’un compte rendu. Pour Nora, « `01-nora.txt`, M001 » est déjà plus utile que « d’après les courriels ».

Préparez aussi un brouillon à destination de Léo. Il peut être aussi simple que :

> Bonjour Léo,
>
> Votre demande porte sur deux places. Pour quel atelier souhaitez-vous vous inscrire : Reliure ou Cartographie ?
>
> Merci !

Ce texte pose la question manquante sans confirmer l’inscription ni annoncer de date. Gardez-le dans le document de travail. Nous n’avons besoin d’aucune connexion à une messagerie pour vérifier qu’il convient.

Ouvrez ensuite `corrige/point-equipe.md`. Comparez les faits et les décisions laissées ouvertes, pas le nombre de paragraphes ni les tournures de phrase. Votre version peut être plus courte et rester tout aussi utile. En revanche, si elle annonce quatre places pour Nora, confirme le 17 octobre ou donne une heure à Cartographie, remontez aux documents : quelque chose a été ajouté en chemin.

Il serait tentant de confier tout le dossier à un assistant, corrigé compris. Pour les essais, nous lui donnerons seulement les entrées et les règles de l’équipe. Nous garderons le corrigé pour examiner sa réponse. Sinon, nous mesurerions surtout sa capacité à recopier le résultat attendu.

## Répartir le travail

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

Gardez votre point d’équipe. Il contient les demandes nouvelles, les références permettant de les retrouver et les questions à résoudre. Nous avons pu avancer malgré la contradiction sur la date, tout en laissant l’annonce finale en attente.

Le prochain essai consistera à donner ce même travail à un assistant. Nous pourrons alors ouvrir ses fichiers et regarder ce qu’il a réellement conservé, oublié ou inventé.
