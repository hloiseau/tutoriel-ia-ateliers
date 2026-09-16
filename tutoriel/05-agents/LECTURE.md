# Comprendre et encadrer les agents de code

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Nous allons suivre les appels d’outils, choisir ce qui entre dans le contexte et repérer les contrôles qui arrêtent une action. Nous préparerons aussi une reprise de session et un relevé de coût.

Dans la partie précédente, nous avons demandé à un agent d’ajouter des tests et de corriger une fonction. Nous avons relu son diff et exécuté les vérifications. Suivons maintenant le trajet complet : **que se passe-t-il entre notre demande et les fichiers modifiés ?**

Quand l’agent annonce qu’il va lancer les tests, qui les lance ? Quand il lit une consigne dans un fichier, doit-il la suivre ? Et s’il répète la même action sans avancer, combien de temps le laissons-nous continuer ?

Nous garderons l’assistant choisi pour la partie 4. À côté, un petit banc Python rejouera des demandes d’outils écrites à la main. Il nous donnera toujours les mêmes refus et les mêmes limites d’appels, ce qui est bien pratique pour examiner les contrôles sans attendre qu’un modèle veuille bien tomber dans notre piège. Ce banc n’appelle aucun modèle : ses traces montrent l’exécution du script, jamais le comportement d’un agent réel.

Gardez `mon-suivi` pour observer votre assistant. Le banc Python se télécharge dans un dossier séparé et fonctionne avec Python 3.12, sans nouveau service ni GPU. Les observations menées dans votre assistant dépendent, elles, de l’accès au modèle que vous utilisez déjà.

## 1. Suivre une demande jusqu’à l’outil

**TL;DR** — Une demande d’outil, son autorisation et son résultat sont trois étapes distinctes. Nous allons les retrouver dans un journal avant de les chercher dans notre assistant.

### Ouvrir le banc d’essai

Récupérez le dossier [ateliers/05-agents du dépôt](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/main/ateliers/05-agents), ou téléchargez [l’archive de cet atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-agents.zip). Décompressez-la dans un dossier de travail. Pour la suite, votre terminal doit être ouvert dans le dossier qui contient `banc.py`.

Le dossier `projet` contient la fonction initiale de suivi de prix et son ticket. Les fichiers de `cas` décrivent les appels que nous allons rejouer. Nous ne toucherons pas à votre correction de la partie 4.

Lancez :

```bash
python banc.py lecture --journal sorties/lecture.jsonl
```

Si nécessaire, remplacez `python` par `python3` ou par la commande qui vous servait déjà. Le programme affiche :

```text
1. lire_fichier : ok
2. lire_fichier : ok
Arrêt : fin_du_script (2 appels)
Journal : sorties/lecture.jsonl
```
Code: Deux demandes de lecture réellement exécutées par le banc

Le terminal résume le parcours ; le détail se trouve dans `sorties/lecture.jsonl`. Chaque ligne est un objet JSON qui conserve la demande, son résultat et le temps passé dans la fonction Python, sous la clé `secondes_outil`. Cette durée ne mesure aucune inférence de modèle.

Pour refaire l’essai, donnez un autre nom au journal. Le programme refuse d’écraser le premier, afin que vous puissiez comparer les traces.

### Qui a fait quoi ?

Ouvrez maintenant `cas/lecture.json`. Sa première demande est :

```json
{"outil": "lire_fichier", "arguments": {"chemin": "TICKET.md"}}
```

Dans notre banc, le fichier JSON choisit l’appel. Dans une session d’agent, la demande vient généralement d’une réponse du modèle. Le logiciel reçoit le nom de l’outil et ses arguments, applique ses contrôles, puis exécute la fonction ou renvoie un refus. Le résultat rejoint ensuite la conversation et le modèle peut choisir l’étape suivante[^p5-outils].

![Une demande passe par le contrôle du programme ; elle mène à l’outil ou à un refus, puis le résultat revient à la conversation](images/boucle.png)
Figure: La demande et son exécution sont deux moments différents

Dans le journal, retrouvez le contenu du ticket sous `resultat.contenu`. Voilà l’information qu’un assistant pourrait fournir au modèle au tour suivant. Une phrase comme « je vais lire le ticket » annonce seulement une intention ; le journal permet de vérifier l’appel et son résultat.

Le banc s’arrête à la fin de la liste préparée. Un agent réel peut demander une autre action selon le résultat reçu, poser une question ou terminer. Son journal expose les actions et leurs résultats, sans nous livrer pour autant tout le raisonnement interne du modèle.

[^p5-outils]: Anthropic, [fonctionnement des appels d’outils](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview). Les noms des messages dépendent de l’API ; la demande et l’exécution restent distinctes.

### Retrouver ces étapes dans l’assistant

Revenez dans votre assistant de développement et ouvrez votre copie `mon-suivi`. Dans une nouvelle session, demandez :

```text
Lis TICKET.md et suivi.py.
Indique si la condition actuelle correspond au ticket.
Appuie ton explication sur la fonction présente dans ce dossier.
Ne modifie aucun fichier et ne lance pas les tests.
```

Dépliez les actions affichées par l’outil. Quels fichiers ont été lus ? À quel moment leur contenu est-il revenu ? Selon l’application, vous verrez les arguments complets, un extrait ou une simple indication de lecture. Notez uniquement ce que l’interface vous permet de vérifier.

Une réponse sans lecture visible peut aussi venir d’un fichier déjà joint au contexte par l’éditeur. Regardez les pièces jointes et les informations de session. Si l’interface ne permet pas de trancher, écrivez-le simplement dans votre relevé au lieu de reconstituer un parcours imaginaire.

Cette petite enquête laisse une question ouverte : qu’a réellement reçu le modèle en plus de notre demande ? C’est le sujet du prochain chapitre.

Le journal nous donne trois repères : la demande d’outil, le contrôle du programme et le résultat renvoyé. Pour comprendre la réponse finale, il faut maintenant regarder l’autre matière première de l’agent : son contexte.

## 2. Donner le contexte utile à l’étape en cours

**TL;DR** — Le contexte comprend nos messages, mais aussi les extraits et les résultats que l’assistant ajoute. Nous allons comparer deux demandes identiques dont l’une est encombrée par un historique sans rapport.

### Même question, deux contextes

Dans l’atelier, ouvrez `contexte/cible.txt`, puis `contexte/complet.txt`. Les deux contiennent la même fonction, le même cas de remise en stock et la même question. Le second ajoute une série d’anciens messages fictifs sur un tableau de bord.

Ouvrez deux conversations neuves avec le même modèle. Envoyez `cible.txt` dans la première et `complet.txt` dans la seconde, puis conservez les réponses. Demandez seulement une explication : aucune modification de fichier n’est utile ici.

Dans chacune, cherchez les trois valeurs : disponibilité actuelle vraie, baisse de prix fausse, ancienne indisponibilité vraie. Le `or` rend la parenthèse vraie. La réponse doit expliquer pourquoi la fonction initiale décide de notifier malgré le prix identique.

Vous obtiendrez peut-être deux bonnes réponses. Très bien : l’exercice n’a pas été truqué pour garantir une erreur. Comparez aussi les détours, les affirmations sans rapport et, si votre outil les expose, les tokens utilisés et le délai.

Avec deux réponses, nous pouvons examiner notre propre contexte et les mesures disponibles. Il en faudrait bien davantage, sur des tâches définies à l’avance, pour comparer sérieusement des modèles.

### Que faut-il garder ?

Pour expliquer une condition, la fonction et les valeurs d’entrée suffisent souvent. Pour modifier son comportement, il faut aussi la règle attendue, les appels concernés et les tests. Ce qui est utile dépend donc de l’action demandée.

![Le contexte de lecture contient un extrait et un cas ; le contexte de modification ajoute le ticket et les tests concernés](images/contexte.png)
Figure: Le contexte change avec la tâche

Préparez maintenant les informations pour cette demande : « ajoute un test du retour en stock avec hausse ». Retrouvez l’objet `Etat`, la fonction appelée, la façon dont les tests sont écrits et le résultat attendu. Vous devez pouvoir expliquer la présence de chaque extrait ; les anciens échanges sur la couleur d’un bouton resteront très bien là où ils sont.

On peut alléger une recherche en demandant d’abord les noms des fichiers concernés, puis en ouvrant ceux qui nous intéressent. De même, une sortie de commande peut commencer par le nom du test en échec et sa trace, au lieu de recopier des milliers de lignes réussies. Gardez cependant le journal complet accessible si le résumé masque la cause de l’erreur.

Un contexte plus court aide seulement s’il reste complet pour la tâche. Une signature séparée de ses conventions, ou un message d’erreur privé de la commande qui l’a produit, peut faire disparaître précisément l’information dont le modèle avait besoin.

### Quand la session commence à dériver

Vous aviez rejeté une solution ; plus tard dans la session, l’agent la propose de nouveau. Ou il oublie une contrainte et revient sur un fichier déjà vérifié. On parle souvent de *drift* ou de *drifting* pour cette dérive au fil de la session. Le mot décrit ce que nous observons, sans en désigner automatiquement la cause.

La cause peut se trouver dans un contexte incomplet, une consigne contradictoire, un résumé qui a perdu une décision ou les limites du modèle. Agrandir la fenêtre de contexte ne suffit pas toujours : des travaux ont notamment observé des variations selon la position de l’information dans les longs contextes étudiés[^p5-contexte].

Si votre outil compresse l’historique, cherchez ce qu’il a conservé. Le résumé contient-il le cas « retour en stock avec baisse » ? Dit-il quel fichier a été modifié, ou seulement « correction terminée » ?

Un autre agent peut chercher les passages utiles et renvoyer un résumé plus court. Gardez le moyen de retrouver ses sources et relisez ses conclusions. Cette délégation ajoute aussi des appels au modèle, donc du délai et, selon votre accès, des tokens facturés ou du quota consommé.

Lorsque l’historique devient difficile à suivre, revenez au ticket, aux décisions prises et aux fichiers présents. Nous transformerons ces points d’appui en fiche de reprise un peu plus loin.

[^p5-contexte]: Nelson F. Liu et al., [*Lost in the Middle: How Language Models Use Long Contexts*](https://arxiv.org/abs/2307.03172), 2023. Ces expériences portent sur des modèles et des tâches donnés ; elles ne fixent pas un seuil universel de longueur à éviter.

La bonne quantité de contexte dépend de l’action : expliquer une condition, modifier une règle et reprendre une longue session demandent des pièces différentes. Pour guider l’agent dans ces pièces, il nous faut maintenant écrire une demande dont nous pourrons vérifier le résultat.

## 3. Écrire des consignes que l’on peut contrôler

**TL;DR** — Une consigne utile nomme l’action, les limites et le résultat à examiner. Nous allons transformer une demande vague, puis vérifier son effet sur un petit cas.

### De « fais attention » à une action précise

Voici une demande difficile à contrôler :

> Regarde le code, fais attention aux cas limites et assure-toi que tout est bon.

À quel résultat reconnaîtrons-nous que le travail est terminé ? Avec cette seule phrase, le modèle peut produire un commentaire très rassurant sans avoir inspecté le bon cas.

Pour notre projet, nous pouvons écrire :

```text
Lis la fonction notifier et les tests qui l’appellent.
Cherche si le retour en stock avec hausse de prix est couvert.
S’il existe, cite le test et sa valeur attendue.
Sinon, propose un test qui appelle notifier sur ce cas.
Ne modifie pas les fichiers. Ne prétends pas avoir exécuté la suite.
```

Les verbes sont impératifs, le cas est nommé et le résultat se vérifie dans les fichiers. L’agent doit retrouver un test précis ou en proposer un ; il n’a plus à deviner ce que « tout est bon » voulait dire.

Gardez les demandes courtes tant que le travail l’est. Dix interdictions héritées d’un autre ticket finiraient par cacher la seule règle qui compte ici.

### Essayer la consigne sur deux états du projet

Faites l’essai sur `01-depart`, puis sur la version contenant les tests de `02-test-rouge`, dans deux copies séparées si votre assistant doit ouvrir un dossier. Ces versions se trouvent dans les fichiers fournis avec la partie 4. Utilisez une session neuve pour chaque essai.

Dans la première version, le test du retour avec hausse est absent. Dans la seconde, vous pouvez retrouver `test_retour_en_stock_avec_hausse`. Vérifiez dans le fichier si la réponse de l’agent correspond à l’état que vous lui avez montré.

Le même texte devrait mener à deux constats différents, puisque les fichiers diffèrent. Nous vérifions ainsi que la réponse correspond au projet ouvert, au lieu de nous contenter d’y retrouver les mots de la consigne.

S’il se trompe, notez la demande, le modèle choisi, le fichier réellement ouvert et la réponse. Puis changez un élément à la fois : une pièce jointe manquait-elle ? L’assistant avait-il gardé le contexte d’une autre copie ? La consigne demandait-elle vraiment de lire les tests ?

Au bout de ces deux essais, gardez le cas, l’état de départ et le résultat. Vous pourrez les rejouer après avoir changé la consigne ou le modèle. Deux réussites resteraient deux observations, bien loin d’une fiabilité « à 100 % ».

### Quand les règles se contredisent

Imaginons que le fichier général du projet dise « crée un commit après chaque tâche », tandis que votre demande exige de voir le changement avant tout commit. Une troisième phrase en majuscules ajouterait surtout du bruit à ce désaccord.

Ouvrez les consignes chargées par votre assistant. Cherchez les règles qui portent sur cette étape, leur portée et l’ordre de priorité documenté par l’outil. Les fichiers et leurs noms diffèrent selon les produits, et leur simple présence dans le dépôt ne dit pas quand l’assistant les charge.

Pour votre propre organisation, placez une règle générale là où elle s’applique réellement, puis retirez les copies contradictoires. Les détails d’un ticket ont leur place avec le ticket. La procédure réutilisable de revue ou de préparation des tests pourra devenir un skill dans la partie suivante.

Ces consignes aident le modèle à choisir. Dès qu’une action doit être interdite, le programme doit prendre le relais. Voyons donc ce qu’il autorise réellement.

Une consigne précise rend le résultat observable et rejouable. Elle ne peut toutefois pas retirer au processus un droit qu’il possède déjà : pour cela, quittons le texte des prompts et passons aux contrôles du programme.

## 4. Observer un refus qui ne dépend pas du modèle

**TL;DR** — Nous allons demander trois actions au banc : lire un chemin interdit, écrire une note et utiliser un terminal absent. Les refus viendront du programme, indépendamment de la formulation de la demande.

### Faire échouer une demande d’outil

Dans le dossier du banc, lancez :

```bash
python banc.py refus --journal sorties/refus.jsonl
```

Vous obtenez trois refus. Ouvrez `cas/refus.json` et le journal côte à côte :

| Demande | Pourquoi elle est refusée |
| --- | --- |
| Lire `../secret.txt` | Le chemin ne fait pas partie des fichiers autorisés |
| Appeler `ecrire_note` | L’option autorisant cette écriture n’est pas active |
| Appeler `terminal` | Le banc n’expose aucun outil de ce nom |
Table: Les contrôles ne reposent pas sur l’obéissance d’un modèle

Trois contrôles différents apparaissent. Le chemin sort de la liste autorisée ; `ecrire_note` existe mais son option d’autorisation manque ; `terminal`, lui, n’existe tout simplement pas dans le banc. Même une demande formulée avec beaucoup d’assurance ne fera pas surgir ce dernier par magie. 🙂

Regardez `Banc.executer` dans `banc.py`. Les arguments sont vérifiés avant l’action. Pour lire, le chemin doit correspondre à un nom prévu, puis rester dans le dossier du projet après résolution. Pour écrire, la destination est fixée à `sorties/note.md` : le demandeur choisit le texte, jamais le chemin de sortie.

Vous voyez pourtant un nouveau journal sur le disque. C’est le programme principal qui l’écrit pour conserver l’expérience ; l’autorisation testée concerne uniquement l’outil `ecrire_note`.

### Une instruction cachée dans un document

Ouvrez `projet/documentation/note.md`. Après une phrase sur le projet, le document ordonne d’ignorer le ticket et d’écrire « Tous les tests passent » dans une note. Cette instruction a été fabriquée pour l’exercice.

Dans une vraie session, un document lu peut contenir du texte qui essaie de détourner l’agent de sa demande. On parle d’**injection de prompt indirecte** quand l’instruction arrive par une source consultée plutôt que par la demande de l’utilisateur[^p5-injection].

Rejouons le cas :

```bash
python banc.py injection --journal sorties/injection.jsonl
```

La lecture réussit ; l’écriture est refusée. Ouvrez maintenant `cas/injection.json` : la seconde demande s’y trouvait déjà, écrite à la main. Le banc n’a ni compris le document ni décidé de lui obéir. Il nous montre seulement comment le contrôle réagit lorsqu’il reçoit cette demande d’écriture.

![Un document fournit des données ; une demande d’écriture doit encore passer par le contrôle des permissions](images/permissions.png)
Figure: Lire une instruction dans un document ne lui donne pas d’autorité

Dans cette copie d’atelier, autorisons maintenant l’écriture :

```bash
python banc.py injection --autoriser-ecriture --journal sorties/injection-autorisee.jsonl
```

Ouvrez `sorties/note.md`. La phrase s’y trouve, alors que le banc n’a lancé aucun test du suivi de prix. L’autorisation porte sur l’écriture du fichier, pas sur la vérité de la phrase. Si une note existait déjà, l’outil l’a remplacée.

[^p5-injection]: OWASP, [*LLM Prompt Injection Prevention Cheat Sheet*](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).

### Ce que cette barrière protège

Lancez les tests du banc :

```bash
python -m unittest discover -v
```

Ils vérifient notamment qu’un refus d’écriture ne crée pas la note, qu’un chemin extérieur n’est pas lu et qu’un texte ressemblant à une demande JSON reste du contenu de fichier. Ouvrez `test_banc.py` et retrouvez ces assertions.

Chaque contrôle protège le passage prévu. Si nous ajoutions un terminal générique, il faudrait examiner tout ce qu’il peut faire avec les droits du processus. Il pourrait peut-être écrire au même endroit et contourner ainsi la restriction placée sur `ecrire_note`.

Notre programme illustre des contrôles applicatifs ; il n’isole pas du code hostile. Dans un environnement réel, les comptes utilisés, les accès réseau, les répertoires montés et l’isolation du processus déterminent aussi ce qu’une action peut atteindre.

Sur votre assistant, retrouvez une permission concrète et sa portée : commande seulement, session, dossier, accès réseau ? Lisez ce qu’accorde le bouton avant d’approuver « toujours ». Une consigne guide le modèle, une confirmation vous rend la décision, une restriction du système bloque l’action ; ce sont trois protections différentes.

Nous avons fait refuser une lecture, une écriture et un outil absent sans demander au modèle de « bien se comporter ». Reste à gérer un cas moins spectaculaire, mais très courant : l’action autorisée qui tourne en rond ou échoue à mi-chemin.

## 5. Arrêter une boucle et reprendre sans perdre le fil

**TL;DR** — Nous allons arrêter des lectures répétées avec un budget d’appels, puis corriger une demande refusée. Pour une vraie session, nous conserverons l’état des fichiers et la prochaine action à vérifier.

### Trois appels, puis on s’arrête

Lancez :

```bash
python banc.py boucle --limite 3 --journal sorties/boucle.jsonl
```

Le fichier `cas/boucle.json` contient huit demandes de lecture identiques. Le journal enregistre les trois premières, puis un arrêt pour `budget_appels`. La quatrième reste dans le scénario et n’atteint jamais l’outil.

Ouvrez la fonction `rejouer` : le compteur et l’arrêt appartiennent au programme. Le test associé vérifie aussi que les demandes refusées consomment ce budget. Une boucle de refus peut donc atteindre la limite aussi vite qu’une boucle de succès.

Dans un véritable agent, une limite peut porter sur les tours, les tokens, la durée ou une dépense. Vérifiez l’unité choisie : trois appels d’outils ne disent rien sur la taille des réponses du modèle. Notre compteur ne borne pas non plus le temps d’un outil bloqué ni la durée d’une requête au modèle ; ces risques demandent des délais d’expiration.

Un fichier peut changer et mériter une seconde lecture. Après trois lectures du même contenu sans nouvelle question, mieux vaut chercher ce qui manque que parier sur l’illumination au quatrième passage. 😅

### Corriger la cause du refus

Rejouez cet autre cas :

```bash
python banc.py reprise --journal sorties/reprise.jsonl
```

La première demande cherche `ticket.md`, absent de la liste des chemins autorisés. La seconde utilise le nom exact `TICKET.md` et réussit. Le droit de lecture n’a pas changé ; seul l’argument a été corrigé.

Dans votre assistant, commencez par les mêmes questions : quelle demande a échoué, avec quels arguments, et quel résultat est revenu ? « Permission refusée », « fichier absent » et « test en échec » appellent des corrections différentes.

Avant de relancer une écriture, vérifiez si elle a pu avoir lieu. Après un délai dépassé, le serveur a peut-être terminé l’action sans que la réponse vous parvienne. Renvoyer une notification ou recréer un ticket peut alors produire un doublon. Prévoyez un moyen de consulter l’état de l’opération ou de reconnaître une répétition.

Pour l’exercice de la partie 4, inspectez le fichier et le diff avant de demander une nouvelle correction. La reprise partira de l’état présent des fichiers, plus fiable que le récit de la dernière tentative.

### Préparer la prochaine session

L’atelier fournit `REPRISE-exemple.md`, une trame à compléter avec les faits de votre session sur `mon-suivi` :

```markdown
# Reprise du ticket

## But
Le comportement demandé, en une phrase.

## État présent
Le dossier de travail et les fichiers modifiés à examiner.

## Décisions
Les cas ambigus qui ont été tranchés.

## Vérifications
Les commandes réellement exécutées, leurs résultats et leurs journaux.

## Suite
Le blocage éventuel et la prochaine action à vérifier.
```

Fermez la conversation, puis repartez dans une session neuve avec cette fiche. Demandez d’abord de vérifier l’état des fichiers et de relever ce qui manque pour continuer. Vous verrez vite si la fiche porte le travail ou si elle s’appuyait encore sur des souvenirs de l’ancienne conversation.

Si la fiche dit « les tests passent », mais ne donne ni commande ni résultat conservé, complétez-la. Si elle contient trente paragraphes d’hypothèses abandonnées, retirez ce qui ne guide plus la suite. Gardez en revanche la raison d’une solution rejetée si elle risque de revenir.

Le modèle peut préparer ce résumé. Relisez les décisions et les faits avant de vous en servir : une erreur recopiée dans une fiche de reprise gagne vite l’apparence d’une vieille vérité.

Une limite arrête la boucle ; le journal explique où elle s’est arrêtée ; la fiche rassemble l’état nécessaire pour repartir. Cette reprise consomme toutefois du temps, des appels et parfois un quota payant. Nous allons les compter séparément.

## 6. Mesurer ce que la session nous a coûté

**TL;DR** — Nous distinguerons les appels d’outils, les tokens facturés et notre temps de travail. Un calcul sur des données fictives montrera comment le cache et les tours successifs changent la facture.

### Un appel d’outil n’est pas une unité de facture

Le journal du banc compte les outils appelés et le temps passé dans chaque fonction Python. La colonne des tokens y brille par son absence : aucun modèle n’a été appelé.

Dans une vraie session, le modèle reçoit un contexte, produit une réponse et peut demander plusieurs outils. Leurs résultats alimentent parfois un nouvel appel au modèle, avec un contexte plus long. Deux appels d’outils peuvent ainsi tenir dans un seul tour du modèle ou provoquer plusieurs tours : leur nombre ne suffit pas à calculer les tokens ni le prix final.

Une partie du contexte peut être réutilisée d’un tour à l’autre. Selon le fournisseur, le cache change la manière dont ces tokens sont traités et facturés ; sa lecture et parfois son écriture ont des conditions propres[^p5-cache]. Ne multipliez pas simplement la taille de la conversation affichée par le prix d’entrée.

Pour un relevé réel, partez des compteurs d’usage exposés par le fournisseur ou l’application. Regardez ce qu’ils incluent : entrée totale, entrée en cache, sortie, éventuels tokens de raisonnement et outils facturés séparément. Si l’entrée totale inclut déjà le cache, ne comptez pas celui-ci une deuxième fois.

Avec un abonnement, distinguez aussi l’argent débité en plus et la part consommée d’un quota déjà payé. Une session peut afficher zéro dépense supplémentaire tout en rapprochant votre équipe d’une limite mensuelle.

[^p5-cache]: Anthropic, [fonctionnement et tarification du cache de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Les conditions de cette documentation ne s’appliquent pas automatiquement aux autres fournisseurs.

### Faire le calcul sur deux appels

Ouvrez `usage-exemple.csv`. Il contient deux appels fictifs répartis dans trois catégories disjointes :

| Appel | Entrée hors cache | Entrée lue en cache | Sortie |
| --- | --- | --- | --- |
| 1 | 1 000 | 0 | 100 |
| 2 | 200 | 1 000 | 100 |
Table: Un exemple inventé de compteurs, pas les mesures d’un modèle

Dans cet exemple, le second appel réutilise une partie du contexte. Pour chaque catégorie, le calcul est `tokens × prix par million / 1 000 000`. Nous additionnons ensuite les catégories et les appels.

Avec des tarifs eux aussi fictifs, lancez :

```bash
python mesurer.py usage-exemple.csv --prix-entree 2 --prix-cache 0.2 --prix-sortie 8
```

Le résultat est `0.004200` unités monétaires. Passez ensuite `--prix-cache` à `2` : le coût devient `0.006000`. Seul le tarif de la lecture du cache a changé ; le CSV contient toujours les mêmes tokens et ne dit rien de la qualité des réponses.

Une écriture de cache facturée séparément, un outil payant ou un abonnement demanderait d’autres colonnes. Adaptez-les à la facture concernée avant d’utiliser vos propres données. L’affichage à six décimales sert ici à vérifier la formule sans arrondir trop tôt ; dans un bilan réel, choisissez une précision adaptée à la décision.

### Le temps gagné se mesure jusqu’à la validation

Reprenez une tâche courte de la partie 4. Notez le temps passé à préparer la demande, attendre, corriger la réponse et vérifier le résultat. Séparez les moments où l’agent vous a mobilisé de ceux pendant lesquels vous avez pu faire autre chose.

| Ce que l’on relève | Ce que cela permet de comprendre |
| --- | --- |
| Temps écoulé entre le début et la fin | La durée de la tâche dans le planning |
| Temps passé à intervenir et relire | L’attention que la tâche vous a demandée |
| Coût ou quota consommé | La dépense liée au service |
| Résultat vérifié et corrections nécessaires | Ce que vous avez obtenu pour ce temps et cette dépense |
Table: Plusieurs mesures pour une même tâche

Comparer une première découverte laborieuse à une seconde tentative dont vous connaissez déjà la solution favoriserait forcément la seconde. Choisissez plusieurs tâches comparables et conservez aussi les essais qui se passent mal. Le but est de savoir si cet usage vous aide, pas de gagner une démonstration préparée d’avance.

En local, l’absence de facture d’API ne fait pas disparaître le matériel, l’électricité et le temps d’installation. Nous approfondirons ces coûts et leurs implications dans la partie consacrée aux choix d’usage.

Vous pouvez maintenant distinguer « l’agent a beaucoup travaillé » de « ce travail m’a aidé ». Une recherche bien ciblée ou un test oublié peut suffire ; nul besoin de déléguer tout le développement pour y trouver un intérêt.

Un bilan utile rapproche le résultat vérifié, les tokens ou le quota consommé, le temps écoulé et votre attention. Gardez ces mesures avec leur contexte : elles nourriront les choix d’usage de la dernière partie.

## Conclusion

Nous avons suivi une demande jusqu’au contrôle, à l’action et au résultat. Le document piégé nous a montré qu’une écriture autorisée peut produire une phrase fausse ; le calcul de coût, qu’un journal d’outils ne raconte qu’une partie de la session.

Gardez les journaux et votre fiche de reprise. Dans la partie suivante, nous retrouverons les mêmes questions avec un serveur MCP, puis nous décrirons une procédure réutilisable dans un skill : que donne-t-on à lire, que permet-on de faire et comment vérifie-t-on le résultat ?
