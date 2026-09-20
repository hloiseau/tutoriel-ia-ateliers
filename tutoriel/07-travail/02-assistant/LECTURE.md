# 2. Faire travailler un assistant sur le dossier

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Préparer le point d’équipe](../01-preparer/LECTURE.md) · [Suivant : Refaire le travail avec un pipeline](../03-pipeline/LECTURE.md)

**TL;DR** — Donnons à un assistant les documents reçus, les règles de l’équipe et une tâche précise. Nous garderons sa première réponse, puis nous vérifierons les faits dans les sources avant de demander une correction.

Vous avez déjà préparé le point de vendredi. Cela change beaucoup notre prochain essai : si l’assistant annonce trois ateliers ou inscrit Nora deux fois, nous pourrons lui demander d’où cela vient. Nous connaissons aussi les questions auxquelles les documents ne permettent pas de répondre.

Nous allons lui confier la rédaction d’un premier point, avec des références et des brouillons séparés. Si vous ne souhaitez pas utiliser de service d’IA, vous pouvez suivre la relecture avec le corrigé, puis essayer le pipeline du chapitre suivant sans compte. Les exemples fournis dans l’atelier sont fictifs ; une réponse obtenue avec votre assistant constituera votre propre essai.

## Choisir un espace de travail

Pour cet exercice, cherchez trois fonctions : joindre des fichiers texte, obtenir un document récupérable et revoir ce document après une correction. Une conversation avec pièces jointes peut déjà convenir. Un espace de travail capable de lire plusieurs fichiers et d’en créer d’autres permet de conserver plus facilement les résultats.

Le **modèle** est le système qui produit le texte. L’**assistant** est l’application avec laquelle vous échangez ; elle lui prépare un **contexte**, composé notamment de vos consignes, des messages et des passages des fichiers qu’elle lui transmet. Joindre un document rend son contenu accessible au système, sans prouver que chaque ligne sera utilisée dans la réponse. Nous demanderons donc des références vérifiables.

Quand l’application laisse le modèle choisir des opérations — ouvrir un fichier, rechercher un passage, créer un document, examiner le résultat — et enchaîne ces opérations, nous parlons d’un **agent**. Ici, sa marge de manœuvre restera modeste : lire un dossier d’exercice et produire des fichiers de travail. Cela suffit largement pour oublier un doublon. 😅

##### Avec ChatGPT Work

La documentation de ChatGPT Work décrit le choix du mode **Work**, l’ajout de fichiers sources et la création de documents à relire. Sur le Web, les fichiers produits peuvent être ouverts ou téléchargés depuis la conversation.[^p7-work-fichiers] Pour notre essai, démarrez une nouvelle tâche dans ce mode si votre compte le propose. Joignez les huit fichiers d’`entrees/`, puis `regles-equipe.md` et `modele-point.md`. Les huit entrées sont les cinq courriels, les deux notes de réunion et le CSV.

Vous n’avez aucun plugin à installer pour travailler avec ces pièces jointes. Si l’interface propose d’accéder à votre messagerie ou à un espace partagé, laissez cet accès de côté : tous les documents utiles sont déjà dans le dossier. L’option de travail local d’une application de bureau décrit l’endroit où elle utilise les fichiers et les outils ; elle ne suffit pas à établir que le modèle s’exécute sur votre ordinateur.

##### Avec Claude, notamment Cowork

La page d’Anthropic présente Cowork comme un moyen de confier une tâche portant sur les dossiers et outils choisis par l’utilisateur. Au 17 septembre 2026, elle annonce son intégration sous le nom Claude, en déploiement sur Pro et Max ; le nom visible dépend donc de l’accès proposé à votre compte.[^p7-claude-cowork]

Préparez un dossier de travail qui contient uniquement `entrees/`, les règles et le modèle de point. Dans le parcours de travail sur fichiers proposé par votre application, sélectionnez ce dossier. Gardez le corrigé ailleurs. Si votre version accepte seulement des pièces jointes, transmettez les mêmes dix fichiers dans une nouvelle conversation. Nous voulons retrouver les documents produits et les sources utilisées ; le nom du mode n’a aucune valeur dans notre grille de vérification.

Ces gestes suivent les documentations consultées le 17 septembre 2026 ; les parcours d’interface restent à essayer dans votre version. Avant l’essai, vérifiez les fonctions accessibles et le compteur d’usage de votre compte. ChatGPT Work documente un usage de crédits pour le travail effectué ; Anthropic rattache Cowork à ses offres payantes. Aucun abonnement n’est nécessaire pour poursuivre le parcours local du tutoriel. Si vous possédez déjà un outil qui remplit nos trois conditions, commencez avec lui.

[^p7-work-fichiers]: OpenAI, [Get started with ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work) et [Work with files](https://learn.chatgpt.com/docs/artifacts-viewer), documentations consultées le 17 septembre 2026.
[^p7-claude-cowork]: Anthropic, [Claude Cowork](https://claude.com/product/cowork), présentation, accès et changement de nom consultés le 17 septembre 2026.

## Donner les fichiers et la demande

Les fichiers sont prêts. Prenez maintenant la consigne de `consignes/point-equipe.md`, fournie dans l’[archive de l’atelier](https://raw.githubusercontent.com/hloiseau/tutoriel-ia-ateliers/d338b4cc84911d12bce1a53f0ccec3125db9578b/telechargements/atelier-hors-developpement.zip). Elle demande le même travail que celui du premier chapitre. Son début précise le résultat et le périmètre :

```text
Prépare le point interne de vendredi pour Les ateliers du quartier,
à partir des fichiers fournis. Applique regles-equipe.md.
Crée un point-equipe.md et un brouillons.md séparés des entrées.
Ne modifie pas les sources et ne contacte personne.
```

La suite demande de distinguer les messages nouveaux, les demandes déjà connues et les décisions ouvertes. Elle exige une référence pour chaque fait utile. Ces indications permettent d’examiner le livrable : « fais quelque chose de professionnel » aurait surtout renseigné le modèle sur notre goût pour les documents qui ont l’air sérieux.

Envoyez la consigne complète. Si l’assistant réclame une pièce manquante, fournissez-la avant de relancer la rédaction. S’il annonce qu’il ne peut pas ouvrir le CSV, vous pouvez en copier le contenu dans la conversation, en indiquant le nom du fichier. Conservez alors cette adaptation avec votre essai : vous n’avez plus exactement transmis les mêmes entrées.

Lorsqu’il présente son plan, vérifiez que celui-ci reste dans le dossier. Une recherche Web ne pourra pas trancher la date d’un événement fictif. Un calendrier relié à votre compte n’apportera rien non plus. Si l’assistant propose de les consulter, ramenez-le aux pièces fournies.

À la fin, récupérez les deux documents. Certains assistants fournissent des fichiers, d’autres affichent seulement leur contenu : dans ce second cas, copiez chaque texte dans un fichier distinct avec votre éditeur habituel. Le Markdown utilisé ici est du texte brut avec des titres et des listes ; il se lit sans logiciel spécialisé.

Gardez une copie de cette première réponse avant de poursuivre la conversation. Placez-la, par exemple, dans un dossier personnel `essai-01/`, avec la consigne réellement envoyée, les noms des pièces transmises et une note indiquant la date, l’application et le modèle affiché. Si l’application ne donne pas le nom exact du modèle ou le coût de cette tâche, notez simplement cette absence. Nous voulons pouvoir retrouver l’essai, sans remplir les blancs à sa place.

Pour une comparaison entre deux assistants, repartez ensuite d’une nouvelle conversation avec les mêmes sources et la même consigne. Une longue discussion de corrections donnerait au second essai des indices que le premier n’avait pas.

## Ouvrir et vérifier le résultat

Ouvrez le point produit à côté des sources. Commencez par les inscriptions : cherchez Nora, puis remontez à `01-nora.txt`. Le point doit relever deux places en Reliure et reconnaître `03-copie-nora.txt` comme une copie. Cherchez ensuite la question `M005`. Elle porte sur Cartographie et doit rester visible, bien qu’elle vienne elle aussi de Nora.

Pour Léo, vérifiez séparément les deux informations : deux places demandées, atelier absent. Un tableau rempli partout peut sembler plus propre qu’un tableau contenant « non précisé ». Ici, cette case vide est précisément ce qui permettra à l’équipe de poser la bonne question.

Regardez enfin la date et l’horaire. Le point conserve-t-il les deux dates avec leur origine ? Présente-t-il l’horaire de Cartographie comme inconnu ? Si vous trouvez « 17 octobre, 10 heures », cherchez le passage cité. Une référence vers un vrai fichier peut accompagner une affirmation que ce fichier ne contient pas.

La grille `corrige/grille-verification.md` rassemble les autres vérifications, dont le rattachement de Samir à la demande déjà enregistrée. Gardez aussi les brouillons sous les yeux. Une phrase comme « votre inscription est confirmée » changerait le sens du travail, même si le tableau des demandes est impeccable.

Voici un exemple de correction à demander si l’atelier de Léo a été inventé ; cette erreur est une situation pédagogique, pas une réponse d’assistant enregistrée :

```text
Dans point-equipe.md, tu attribues Reliure à M002.
Relis courriels/02-leo.txt : le message précise deux personnes,
mais aucun atelier. Corrige ce fait et les brouillons qui en dépendent.
Conserve la première version et nomme la nouvelle point-equipe-v2.md.
```

Une correction ciblée désigne le fait, la source et les conséquences à revoir. « Vérifie mieux » laisse l’assistant chercher ce qui nous a déplu. Après sa réponse, ouvrez la nouvelle version : le modèle peut corriger le tableau et oublier la même erreur dans le paragraphe de synthèse. Les deux lignes appartiennent à notre relecture.

À ce stade, vous pouvez décider que quelques retouches dans votre éditeur iront plus vite qu’un nouveau message. Gardez alors la réponse brute et la version corrigée séparément. Ce petit historique permet de voir ce que l’assistant a produit et ce que vous avez dû reprendre, y compris quand le résultat final est très bon.

Nous avons de quoi juger un essai : les pièces transmises, la consigne, la réponse brute et les corrections. Un point agréable à lire compte, mais l’équipe a surtout besoin de retrouver les bonnes demandes et les décisions encore ouvertes.

Refaire ces copier-coller chaque vendredi finirait par devenir pénible. Nous allons donner une forme régulière aux informations extraites, puis les faire passer dans une petite chaîne de traitement. Vous pourrez conserver l’assistant de votre choix, ou fournir vous-même l’extraction : les étapes suivantes recevront le même format.

---

[Précédent : Préparer le point d’équipe](../01-preparer/LECTURE.md) · [Suivant : Refaire le travail avec un pipeline](../03-pipeline/LECTURE.md)
