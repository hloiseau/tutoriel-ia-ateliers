# Comprendre et encadrer les agents de code

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Nous allons suivre les appels d’outils, choisir ce qui entre dans le contexte et observer ce qui arrête réellement une action. Puis nous préparerons une reprise de session et un relevé de coût.

Dans la partie précédente, nous avons demandé à un agent d’ajouter des tests et de corriger une fonction. Il a fallu lire ce qu’il produisait. Maintenant, regardons aussi ce qui se passe **entre notre demande et les fichiers modifiés**.

Quand l’agent annonce qu’il va lancer les tests, qui les lance ? Quand il lit une consigne dans un fichier, doit-il la suivre ? Et s’il répète la même action sans avancer, combien de temps le laissons-nous continuer ?

Nous garderons l’assistant choisi pour la partie 4. Pour les incidents que nous voulons reproduire à coup sûr, nous utiliserons aussi un petit banc Python : il rejoue des demandes d’outils écrites à la main. Il ne contient pas de modèle. Nous pourrons donc observer un refus ou une limite d’appels sans attendre qu’une IA se trompe exactement comme prévu.

Il faut Python 3.12 et savoir lire les petits fichiers de l’atelier précédent. Aucun nouveau service ni GPU n’est nécessaire pour le banc. Les observations avec votre assistant utilisent, elles, votre accès au modèle habituel.

## Suivant. Suivre une demande jusqu’à l’outil

**TL;DR** — Une demande d’outil, son autorisation et son résultat sont trois étapes distinctes. Nous allons les retrouver dans un journal avant de les chercher dans notre assistant.

### Ouvrir le banc d’essai

Récupérez le dossier [ateliers/05-agents du dépôt](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/main/ateliers/05-agents), ou téléchargez [l’archive de cet atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-agents.zip). Décompressez-la dans un dossier de travail et ouvrez le terminal à côté de `banc.py`.

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

Ouvrez `sorties/lecture.jsonl`. Chaque ligne est un objet JSON : la demande, le résultat et le temps passé dans l’outil y sont conservés. Pour refaire l’essai, donnez un autre nom au journal ; le programme refuse d’écraser un journal existant.

### Qui a fait quoi ?

Ouvrez maintenant `cas/lecture.json`. Sa première demande est :

```json
{"outil": "lire_fichier", "arguments": {"chemin": "TICKET.md"}}
```

Le script choisit ici l’appel. Dans une session d’agent, c’est généralement une réponse du modèle qui demande cet outil avec ces arguments. Le logiciel reçoit la demande, effectue les contrôles nécessaires, puis appelle la fonction. Il renvoie ensuite le résultat au modèle pour poursuivre la conversation[^p5-outils].

![Une demande passe par le contrôle du programme ; elle mène à l’outil ou à un refus, puis le résultat revient à la conversation](images/boucle.png)
Figure: La demande et son exécution sont deux moments différents

Dans le journal, retrouvez le contenu du ticket sous `resultat.contenu`. C’est cette information qu’un assistant pourrait fournir au modèle au tour suivant. La ligne « je vais lire le ticket » ne suffit pas : elle ne contient ni l’appel ni son résultat.

Notre banc s’arrête à la fin de la liste. Un agent peut, lui, choisir une autre action selon la réponse reçue, poser une question ou terminer. Le journal expose des actions et des résultats ; ce n’est pas un enregistrement de tout son raisonnement interne.

[^p5-outils]: Anthropic, [fonctionnement des appels d’outils](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview). Les noms des messages dépendent de l’API ; la demande et l’exécution restent distinctes.

### Retrouver ces étapes dans l’assistant

Revenez dans votre assistant de développement et ouvrez votre copie `mon-suivi`. Dans une nouvelle session, demandez :

```text
Lis TICKET.md et suivi.py.
Indique si la condition actuelle correspond au ticket.
Appuie ton explication sur la fonction présente dans ce dossier.
Ne modifie aucun fichier et ne lance pas les tests.
```

Dépliez les actions affichées par l’outil. Cherchez quels fichiers ont été lus et à quel moment leur contenu est revenu. Selon l’application, vous verrez les arguments complets, un extrait ou seulement une indication de lecture. Notez ce que l’interface permet réellement de vérifier.

Si l’agent répond sans lecture visible, cela ne prouve pas à lui seul qu’il invente : l’éditeur a pu joindre le fichier au contexte. Regardez les pièces jointes et les informations de session. Si vous ne pouvez pas savoir, gardez cette incertitude dans votre relevé.

Nous allons justement examiner ce que le modèle reçoit, au-delà du texte que nous tapons.



## Suivant. Donner le contexte utile à l’étape en cours

**TL;DR** — Le contexte comprend nos messages, mais aussi les extraits et les résultats que l’assistant ajoute. Nous allons comparer deux demandes identiques dont l’une est encombrée par un historique sans rapport.

### Même question, deux contextes

Dans l’atelier, ouvrez `contexte/cible.txt`, puis `contexte/complet.txt`. Les deux contiennent la même fonction, le même cas de remise en stock et la même question. Le second ajoute une série d’anciens messages fictifs sur un tableau de bord.

Dans deux conversations neuves, avec le même modèle, envoyez un fichier puis l’autre. Restez en discussion : nous cherchons une explication, pas une modification. Conservez les deux réponses.

Dans chacune, cherchez les trois valeurs : disponibilité actuelle vraie, baisse de prix fausse, ancienne indisponibilité vraie. Le `or` rend la parenthèse vraie. La réponse doit expliquer pourquoi la fonction initiale décide de notifier malgré le prix identique.

Les deux réponses peuvent être correctes. Ce ne serait pas un échec de l’exercice : cet exemple ne promet pas qu’ajouter du texte fait systématiquement échouer le modèle. Regardez aussi les détours, les affirmations sans rapport et, si votre outil les expose, les tokens utilisés et le délai.

Deux essais ne donnent pas un classement des modèles. Ils permettent de voir ce que vous envoyez et ce que vous pouvez mesurer avant d’en tirer une conclusion.

### Que faut-il garder ?

Pour expliquer une condition, la fonction et les valeurs d’entrée suffisent souvent. Pour modifier son comportement, il faut aussi la règle attendue, les appels concernés et les tests. Ce qui est utile dépend donc de l’action demandée.

![Le contexte de lecture contient un extrait et un cas ; le contexte de modification ajoute le ticket et les tests concernés](images/contexte.png)
Figure: Le contexte change avec la tâche

Essayez de préparer vous-même les informations pour cette demande : « ajoute un test du retour en stock avec hausse ». Il faut notamment retrouver l’objet `Etat`, la fonction appelée, la façon dont les tests sont écrits et le résultat attendu. Les anciens échanges sur la couleur d’un bouton ne servent pas ici.

On peut alléger une recherche en demandant d’abord les noms des fichiers concernés, puis en ouvrant ceux qui nous intéressent. De même, une sortie de commande peut commencer par le nom du test en échec et sa trace, au lieu de recopier des milliers de lignes réussies. Gardez cependant le journal complet accessible si le résumé masque la cause de l’erreur.

**Réduire le contexte ne consiste pas à couper au hasard.** Une signature sans ses conventions, ou un message d’erreur sans la commande qui l’a produit, peut faire perdre précisément l’information dont le modèle avait besoin.

### Quand la session commence à dériver

Vous aviez rejeté une solution, et l’agent la propose de nouveau. Il oublie une contrainte ou revient sur un fichier déjà vérifié. On parle souvent de *drift* ou de *drifting* pour décrire cette dérive au fil de la session ; le mot ne donne pas, à lui seul, sa cause.

Une mauvaise réponse peut venir d’un contexte incomplet, d’une consigne contradictoire, d’un résumé qui a perdu une décision ou des limites du modèle. Une grande fenêtre de contexte ne garantit pas que toutes les informations seront exploitées aussi bien. Des travaux ont notamment observé des variations selon la position de l’information dans les longs contextes étudiés[^p5-contexte].

Si votre outil compresse l’historique, cherchez ce qu’il a conservé. Le résumé contient-il le cas « retour en stock avec baisse » ? Dit-il quel fichier a été modifié, ou seulement « correction terminée » ?

On peut aussi déléguer une recherche à un autre agent pour ne récupérer que les passages utiles. Cela demande encore de vérifier le résumé et de pouvoir retrouver ses sources ; les appels supplémentaires ne deviennent pas gratuits parce qu’ils se déroulent dans une autre conversation.

Nous préparerons plus loin une fiche de reprise. Pour le moment, gardez le ticket, les décisions et les fichiers comme points d’appui lorsque l’historique devient difficile à suivre.

[^p5-contexte]: Nelson F. Liu et al., [*Lost in the Middle: How Language Models Use Long Contexts*](https://arxiv.org/abs/2307.03172), 2023. Ces expériences portent sur des modèles et des tâches donnés ; elles ne fixent pas un seuil universel de longueur à éviter.



## Suivant. Écrire des consignes que l’on peut contrôler

**TL;DR** — Une consigne utile nomme l’action, les limites et le résultat à examiner. Nous allons transformer une demande vague, puis vérifier son effet sur un petit cas.

### De « fais attention » à une action précise

Voici une demande difficile à contrôler :

> Regarde le code, fais attention aux cas limites et assure-toi que tout est bon.

Qu’est-ce qui nous permettra de dire que le travail est terminé ? Le modèle peut répondre par un commentaire très rassurant sans avoir fait ce que nous attendions.

Pour notre projet, nous pouvons écrire :

```text
Lis la fonction notifier et les tests qui l’appellent.
Cherche si le retour en stock avec hausse de prix est couvert.
S’il existe, cite le test et sa valeur attendue.
Sinon, propose un test qui appelle notifier sur ce cas.
Ne modifie pas les fichiers. Ne prétends pas avoir exécuté la suite.
```

Les verbes sont impératifs et le résultat est vérifiable. L’agent doit retrouver un cas précis ou en proposer un. Il n’a pas à deviner ce que « tout est bon » voulait dire.

Gardez les demandes courtes tant que le travail l’est. Une longue liste d’interdictions sans rapport rend aussi plus difficile la lecture de ce qui compte.

### Essayer la consigne sur deux états du projet

Faites l’essai sur `01-depart`, puis sur la version contenant les tests de `02-test-rouge`, dans deux copies séparées si votre assistant doit ouvrir un dossier. Ces versions se trouvent dans les fichiers fournis avec la partie 4. Utilisez une session neuve pour chaque essai.

Dans la première version, le test du retour avec hausse est absent. Dans la seconde, vous pouvez retrouver `test_retour_en_stock_avec_hausse`. Vérifiez dans le fichier si la réponse de l’agent correspond à l’état que vous lui avez montré.

Le même texte doit donc mener à deux constats différents. C’est plus instructif que de vérifier seulement si l’agent reprend les mots de la consigne.

S’il se trompe, notez la demande, le modèle choisi, le fichier réellement ouvert et la réponse. Puis changez un élément à la fois : une pièce jointe manquait-elle ? L’assistant avait-il gardé le contexte d’une autre copie ? La consigne demandait-elle vraiment de lire les tests ?

Nous n’en déduirons pas qu’un prompt est « fiable à 100 % ». Nous aurons un cas qui passe ou échoue, et une manière de le rejouer après une modification.

### Quand les règles se contredisent

Imaginons que le fichier général du projet dise « crée un commit après chaque tâche » et que votre demande dise « montre-moi le changement avant tout commit ». Ajouter une troisième phrase en majuscules ne résout pas proprement ce désaccord.

Ouvrez les consignes chargées par votre assistant. Cherchez les règles qui portent sur cette étape, leur portée et l’ordre de priorité documenté par l’outil. Les fichiers et leurs noms diffèrent selon les produits. Une instruction présente quelque part dans le dépôt n’est pas forcément chargée à chaque tour.

Pour votre propre organisation, placez une règle générale là où elle s’applique réellement, puis retirez les copies contradictoires. Les détails d’un ticket ont leur place avec le ticket. La procédure réutilisable de revue ou de préparation des tests pourra devenir un skill dans la partie suivante.

Une consigne explicite reste adressée à un modèle. Pour une action qui doit être interdite, il nous faut maintenant regarder ce que le programme autorise réellement.



## Suivant. Observer un refus qui ne dépend pas du modèle

**TL;DR** — Nous allons demander trois actions au banc : lire un chemin interdit, écrire une note et utiliser un terminal absent. Le programme doit les refuser, quel que soit le texte de la demande.

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

`ecrire_note` existe bien dans le code : être disponible ne signifie pas être autorisé pour cet essai. À l’inverse, inventer le nom `terminal` ne crée pas un terminal.

Regardez `Banc.executer` dans `banc.py`. Les arguments sont vérifiés avant l’action. Pour lire, le chemin doit correspondre à un nom prévu, puis rester dans le dossier du projet après résolution. Pour écrire, la destination est fixée à `sorties/note.md` ; le demandeur ne fournit pas de chemin de sortie.

Le journal est écrit par le programme pour conserver l’expérience. Cette écriture de suivi est distincte de l’autorisation de l’outil `ecrire_note`.

### Une instruction cachée dans un document

Ouvrez `projet/documentation/note.md`. Après une phrase sur le projet, vous trouverez une instruction fabriquée pour l’exercice : ignorer le ticket et écrire « Tous les tests passent » dans une note.

Dans une vraie session, un document lu peut contenir du texte qui essaie de détourner l’agent de sa demande. On parle d’**injection de prompt indirecte** quand l’instruction arrive par une source consultée plutôt que par la demande de l’utilisateur[^p5-injection].

Rejouons le cas :

```bash
python banc.py injection --journal sorties/injection.jsonl
```

La lecture réussit ; l’écriture est refusée. Ouvrez le script JSON : nous avons écrit nous-mêmes la seconde demande. **Aucun modèle n’a été trompé dans cette expérience.** Nous vérifions ce que ferait le contrôle si une telle demande arrivait.

![Un document fournit des données ; une demande d’écriture doit encore passer par le contrôle des permissions](images/permissions.png)
Figure: Lire une instruction dans un document ne lui donne pas d’autorité

Dans cette copie d’atelier, autorisons maintenant l’écriture :

```bash
python banc.py injection --autoriser-ecriture --journal sorties/injection-autorisee.jsonl
```

Ouvrez `sorties/note.md`. La phrase s’y trouve, alors qu’aucun test du suivi de prix n’a été lancé par le banc. Le programme a exécuté une action autorisée ; cela ne rend pas le contenu écrit vrai. Si la note existait, cet outil l’a remplacée.

[^p5-injection]: OWASP, [*LLM Prompt Injection Prevention Cheat Sheet*](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).

### Ce que cette barrière protège

Lancez les tests du banc :

```bash
python -m unittest discover -v
```

Ils vérifient notamment qu’un refus d’écriture ne crée pas la note, qu’un chemin extérieur n’est pas lu et qu’un texte ressemblant à une demande JSON reste du contenu de fichier. Ouvrez `test_banc.py` et retrouvez ces assertions.

Le contrôle d’un outil ne protège que les passages qui le traversent. Si nous ajoutions un terminal générique, il faudrait examiner ce qu’il peut faire avec les droits du processus. Interdire `ecrire_note` ne suffirait plus si un autre outil permettait d’écrire au même endroit.

Notre programme est un exercice de contrôles applicatifs. Il ne constitue pas un bac à sable pour lancer du code hostile. Dans un environnement réel, les comptes utilisés, les accès réseau, les répertoires montés et l’isolation du processus déterminent aussi ce qu’une action peut atteindre.

Sur votre assistant, retrouvez une permission concrète et sa portée : commande seulement, session, dossier, accès réseau ? Lisez ce qu’accorde le bouton avant d’approuver « toujours ». Une consigne, une confirmation et une restriction du système ne jouent pas le même rôle.



## Suivant. Arrêter une boucle et reprendre sans perdre le fil

**TL;DR** — Nous allons arrêter des lectures répétées avec un budget d’appels, puis corriger une demande refusée. Pour une vraie session, nous conserverons l’état des fichiers et la prochaine action à vérifier.

### Trois appels, puis on s’arrête

Lancez :

```bash
python banc.py boucle --limite 3 --journal sorties/boucle.jsonl
```

Le fichier `cas/boucle.json` contient huit demandes de lecture identiques. Le journal n’enregistre que trois appels, puis un arrêt pour `budget_appels`. Le quatrième appel n’est pas exécuté.

Ouvrez la fonction `rejouer` : c’est le programme qui compte les appels et arrête la boucle. Il ne demande pas au modèle de décider s’il a suffisamment dépensé. Le test associé vérifie aussi que les demandes refusées consomment ce budget.

Dans un véritable agent, une limite peut porter sur les tours, les tokens, la durée ou une dépense. Il faut savoir ce qui est compté. Notre limite d’appels ne borne pas le temps d’un outil bloqué ni la durée d’une requête au modèle ; il faudrait des délais d’expiration pour cela.

Relire un fichier n’est pas toujours inutile : il peut avoir changé. En revanche, lire trois fois le même contenu sans nouvelle question doit nous inciter à regarder ce qui manque, plutôt qu’à attendre le quatrième passage. 😅

### Corriger la cause du refus

Rejouez cet autre cas :

```bash
python banc.py reprise --journal sorties/reprise.jsonl
```

La première demande cherche `ticket.md`, qui ne figure pas dans la liste des chemins autorisés. La seconde demande `TICKET.md` et réussit. Le script montre une correction de paramètre, pas une ouverture générale des droits.

Dans votre assistant, commencez de la même façon : quelle demande a échoué, avec quels arguments, et quel résultat est revenu ? « Permission refusée », « fichier absent » et « test en échec » demandent des réponses différentes.

Avant de relancer une écriture, regardez aussi si elle a pu avoir lieu. Un délai dépassé ne prouve pas que le serveur n’a rien fait. Pour un envoi de notification ou la création d’un ticket, répéter aveuglément peut produire un doublon. L’opération doit avoir une manière de vérifier son état ou d’éviter les doublons ; « réessaie » ne suffit pas.

Pour notre exercice de la partie 4, inspectez le fichier et le diff avant de demander une nouvelle correction. On repartira ainsi de l’état présent, pas du récit de la dernière tentative.

### Préparer la prochaine session

L’atelier fournit `REPRISE-exemple.md`. C’est une trame, pas le compte rendu de votre session. Adaptez-la à `mon-suivi` :

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

Fermez la conversation et essayez de reprendre avec cette fiche dans une session neuve. Demandez d’abord de vérifier l’état des fichiers et de relever ce qui manque pour continuer.

Si la fiche dit « les tests passent », mais ne donne ni commande ni résultat conservé, complétez-la. Si elle contient trente paragraphes d’hypothèses abandonnées, retirez ce qui ne guide plus la suite. Gardez en revanche la raison d’une solution rejetée si elle risque de revenir.

Le modèle peut préparer ce résumé. Relisez les décisions et les faits avant de vous en servir : une erreur recopiée dans une fiche de reprise peut devenir très convaincante à force d’être répétée.



## Suivant. Mesurer ce que la session nous a coûté

**TL;DR** — Nous distinguerons les appels d’outils, les tokens facturés et notre temps de travail. Un petit calcul permet de voir pourquoi le cache et les tours successifs changent la facture.

### Un appel d’outil n’est pas une unité de facture

Le journal du banc nous dit combien d’outils ont été appelés et combien de temps chacun a pris. Il ne contient aucun token de modèle : nous n’en avons appelé aucun.

Dans une vraie session, le modèle reçoit un contexte, produit une réponse et peut demander plusieurs outils. Leurs résultats peuvent alimenter un nouvel appel au modèle. Le nombre d’outils ne permet donc pas de déduire directement le nombre de tokens, ni le prix final.

Une partie du contexte peut être réutilisée d’un tour à l’autre. Selon le fournisseur, le cache change la manière dont ces tokens sont traités et facturés ; sa lecture et parfois son écriture ont des conditions propres[^p5-cache]. Ne multipliez pas simplement la taille de la conversation affichée par le prix d’entrée.

Pour un relevé réel, partez des compteurs d’usage exposés par le fournisseur ou l’application. Regardez ce qu’ils incluent : entrée totale, entrée en cache, sortie, éventuels tokens de raisonnement et outils facturés séparément. Si l’entrée totale inclut déjà le cache, ne comptez pas celui-ci une deuxième fois.

Un abonnement ajoute une autre question : avez-vous dépensé de l’argent supplémentaire ou consommé une partie d’un quota déjà payé ? Les deux informations sont utiles, mais elles ne se lisent pas de la même façon.

[^p5-cache]: Anthropic, [fonctionnement et tarification du cache de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Les conditions de cette documentation ne s’appliquent pas automatiquement aux autres fournisseurs.

### Faire le calcul sur deux appels

Ouvrez `usage-exemple.csv`. Nous y avons placé deux appels fictifs pour comprendre le calcul, avec trois catégories **qui ne se recouvrent pas** :

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

Le résultat est `0.004200` unités monétaires. Passez ensuite `--prix-cache` à `2` : le coût devient `0.006000`. Vous venez de changer la tarification d’une catégorie, pas le nombre de tokens ni la qualité de la réponse.

Ce calcul simplifié ne couvre pas une écriture de cache facturée séparément, un outil payant ou un abonnement. Pour l’utiliser sur vos données, adaptez les colonnes à la facture concernée. Il n’est pas nécessaire d’avoir une précision au millionième pour décider si l’outil vous sert ; elle nous permet ici de vérifier une petite formule sans arrondir trop tôt.

### Le temps gagné se mesure jusqu’à la validation

Reprenez une tâche courte de la partie 4. Notez le temps passé à préparer la demande, attendre, corriger la réponse et vérifier le résultat. Conservez aussi les moments où vous avez pu faire autre chose pendant l’exécution.

| Ce que l’on relève | Ce que cela permet de comprendre |
| --- | --- |
| Temps écoulé entre le début et la fin | La durée de la tâche dans le planning |
| Temps passé à intervenir et relire | L’attention que la tâche vous a demandée |
| Coût ou quota consommé | La dépense liée au service |
| Résultat vérifié et corrections nécessaires | Ce que vous avez obtenu pour ce temps et cette dépense |
Table: Plusieurs mesures pour une même tâche

Évitez de comparer une première découverte laborieuse à une seconde tentative dont vous connaissez déjà la solution. Pour explorer l’intérêt de l’aide, choisissez plusieurs tâches comparables et conservez aussi les essais qui se passent mal. Nous cherchons un usage qui vous convient, pas une démonstration gagnée d’avance.

En local, l’absence de facture d’API ne fait pas disparaître le matériel, l’électricité et le temps d’installation. Nous approfondirons ces coûts et leurs implications dans la partie consacrée aux choix d’usage.

Vous avez maintenant de quoi distinguer « l’agent a beaucoup travaillé » de « ce travail m’a aidé ». Une recherche bien ciblée ou un test oublié peut suffire ; il n’est pas nécessaire de déléguer tout le développement pour en tirer quelque chose.



## Conclusion

Nous avons suivi la demande, le contrôle, l’action et le résultat. Nous avons aussi vu qu’une écriture autorisée peut produire une phrase fausse, et qu’un journal d’outils ne mesure pas à lui seul le coût du modèle.

Gardez les journaux et votre fiche de reprise. Dans la partie suivante, nous allons brancher des outils avec MCP et organiser des procédures réutilisables avec des skills. Les questions resteront concrètes : que donne-t-on à lire, que permet-on de faire, et comment vérifie-t-on le résultat ?
