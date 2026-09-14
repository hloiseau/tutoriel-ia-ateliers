# Choisir et installer son assistant de développement

## Raccord à la fin de la partie 3

Nous avons fait tourner un modèle sur notre machine et envoyé nos premières requêtes à son serveur. Il nous manque encore quelque chose pour travailler sur un projet : une interface qui nous permette de lui montrer du code, de discuter d’une modification et, éventuellement, de lui laisser utiliser des outils.

C’est ce que nous allons installer dans la partie suivante. Nous regarderons d’abord les solutions disponibles, leur coût et ce qu’elles font de nos données. Puis nous suivrons deux chemins : utiliser un service hébergé ou relier notre serveur local à un assistant dans l’éditeur.

Ensuite, place au code ! Nous aurons un petit programme à comprendre, un ticket à clarifier et un comportement à corriger. Le modèle pourra nous aider, mais il faudra encore vérifier ce qu’il propose. 🙂

## Introduction de la partie 4

Un modèle répond dans notre terminal. Très bien. Mais comment passer de cette conversation à une modification dans un vrai projet ?

Il existe des extensions pour les éditeurs, des éditeurs qui intègrent directement l’IA, des assistants en ligne de commande et des agents qui travaillent sur une machine distante. Certains utilisent un abonnement, d’autres une API facturée à l’usage. Certains peuvent parler à notre serveur local. On peut vite passer davantage de temps à choisir son outil qu’à s’en servir. 😅

Nous allons prendre le temps de nous y retrouver, puis installer de quoi travailler. Vous pourrez utiliser un service hébergé sans acheter de carte graphique, ou poursuivre avec un modèle sur votre machine. Un abonnement payant ne sera pas nécessaire pour commencer.

Nous ouvrirons ensuite un petit projet Python de suivi de prix. Ses tests passent, mais il envoie une notification dans un cas où nous n’en voulons plus. Nous suivrons la modification jusqu’au bout : comprendre le programme, préciser la demande, reproduire le problème, corriger le code et vérifier le résultat.

Si vous débutez, prenez aussi le temps de faire votre propre lecture du code. Une explication très convaincante peut être fausse ; pour s’en apercevoir, il faut pouvoir suivre ce que fait le programme.

**TL;DR**

- Nous choisissons un assistant en regardant ses fonctions, son coût et l’endroit où il traite nos données.
- Deux installations sont proposées : VS Code avec GitHub Copilot, ou VS Code avec Continue et notre serveur local.
- Nous commençons par discuter du code, avant de laisser un outil le modifier.
- Le même atelier sert ensuite à apprendre à relire, tester et valider une correction, avec ou sans agent.

## 1. Avec quoi va-t-on développer ?

**TL;DR** — Le modèle produit une réponse, le moteur le fait tourner et l’assistant organise le travail autour. Pour développer, on peut demander une suggestion, discuter d’un extrait ou laisser un agent intervenir dans le projet. Ce ne sont pas les mêmes besoins.

Avant de choisir un nom dans une liste, regardons ce que nous voulons lui faire faire. « Développer avec une IA » peut vouloir dire accepter une ligne proposée dans l’éditeur comme confier plusieurs fichiers à un agent. Entre les deux, il y a de quoi trouver une utilisation qui vous convienne.

### Le modèle, le moteur et l’assistant

Reprenons notre installation de la partie précédente.

Le fichier GGUF contient les paramètres du **modèle**. **llama.cpp** fournit le moteur qui les utilise pour calculer une réponse. Notre petit client Python envoie la question au serveur et affiche le résultat.

Pour travailler dans un éditeur, nous pouvons remplacer ce client par un **assistant de développement**. C’est lui qui prépare la requête avec notre question et les extraits de code, affiche la réponse et, selon ses fonctions, propose une modification ou exécute une commande.

| Élément | Dans notre installation locale | Ce qu’il fait |
| --- | --- | --- |
| Modèle | Un fichier GGUF | Fournit les paramètres utilisés pour produire la réponse |
| Moteur et serveur | `llama-server` | Charge le modèle, effectue les calculs et reçoit les requêtes |
| Assistant | Continue dans l’éditeur | Prépare la conversation et permet de travailler avec le code |
Table: Les trois éléments que nous allons relier

Changer d’assistant ne signifie donc pas forcément changer de modèle. Et changer de modèle ne demande pas forcément de quitter son éditeur.

Il faut aussi distinguer **l’endroit où l’assistant agit** et **l’endroit où le modèle tourne**. Un agent lancé dans votre terminal peut lire des fichiers et exécuter les tests sur votre ordinateur, tout en envoyant le contexte à un service distant pour obtenir ses réponses.

À l’inverse, une extension peut envoyer ses requêtes à `127.0.0.1`, comme notre client Python. Dans ce cas, c’est notre serveur qui calcule les réponses. Le mot « local » mérite donc une petite question supplémentaire : *qu’est-ce qui tourne localement, exactement ?*

### De la suggestion à l’agent

Vous êtes en train d’écrire une fonction. L’éditeur suggère la fin de la ligne : c’est de la **complétion**. Vous décidez si vous la gardez.

Un peu plus loin, vous tombez sur une condition difficile à lire. Vous sélectionnez ces lignes et demandez une explication : c’est une **discussion avec du contexte**. Vous n’avez pas besoin que l’outil puisse modifier le dépôt pour vous aider.

Vous pouvez aussi demander une **modification ciblée** : ajouter un cas de test, simplifier une fonction ou proposer un autre nom. L’assistant prépare alors du code ou un diff, que vous relisez.

Enfin, un **agent** peut enchaîner plusieurs actions : chercher le fichier concerné, le lire, le modifier, lancer les tests, lire l’erreur et recommencer. Il lui faut un modèle, mais aussi un programme qui exécute les actions et lui renvoie leurs résultats.

| Votre besoin | Fonction à chercher |
| --- | --- |
| Écrire moins de code répétitif au clavier | Complétion dans l’éditeur |
| Comprendre une fonction ou une erreur | Discussion avec sélection de code |
| Obtenir une proposition facile à relire | Modification ciblée et affichage du diff |
| Faire avancer une tâche dans plusieurs fichiers | Agent avec accès au projet et au terminal |
| Confier une tâche pendant que vous faites autre chose | Exécution en arrière-plan, locale ou distante |
Table: Partir du travail à faire pour choisir une fonction

Ces fonctions peuvent cohabiter dans un même produit. Cela ne vous oblige pas à toutes les activer.

Si votre difficulté actuelle est d’imaginer des cas de test, commencez par là. Vous pouvez écrire le code vous-même et demander à l’assistant quels comportements vous avez oubliés. Vous pouvez aussi préférer déboguer seul et ne lui demander qu’une explication de documentation. Il n’y a pas de formule complète à adopter pour avoir le droit de s’en servir. 🙂

### Faire le tour des outils

Voici un panorama de douze solutions, pour couvrir les principales façons de travailler : extension, éditeur, terminal et agent distant. Ce n’est pas la liste de tous les produits existants, ni un classement de leurs modèles.

Les offres et les fonctions décrites correspondent aux pages officielles consultées le **14 septembre 2026**. Si vous lisez ce chapitre plus tard, les liens en notes permettront de retrouver leur état actuel.

| Solution | Où l’utiliser | Ce qu’il faut regarder pour notre usage |
| --- | --- | --- |
| GitHub Copilot | Dans plusieurs éditeurs, en CLI et sur GitHub | Complétion, discussion, agent et revue ; fonctions et quotas selon l’offre[^p4-out-copilot] |
| Cursor | Éditeur dédié | Complétion et travail avec un agent dans le projet ; offre gratuite limitée[^p4-out-cursor] |
| Claude Code | Terminal et intégrations dans les éditeurs | Travail avec un agent ; accès par abonnement compatible ou API[^p4-out-claude] |
| Codex | Terminal, extension d’éditeur et interfaces hébergées | Tâches de développement, commandes et revue ; exécution locale ou distante selon l’interface[^p4-out-codex] |
| Devin | Desktop, CLI et Cloud | Complétion et agents ; vérifier quelle interface et quel quota couvre le forfait[^p4-out-devin] |
| JetBrains AI Assistant et Junie | Environnement JetBrains | Aide dans l’IDE et travail avec un agent ; quota cloud partagé selon l’offre[^p4-out-jetbrains] |
| Google Antigravity | Éditeur et CLI | Complétion et agents ; accès gratuit limité et offres Google AI[^p4-out-google] |
| Zed | Éditeur | Prédictions d’édition, modèles hébergés ou API personnelle, agents externes[^p4-out-zed] |
| Continue | Extension d’éditeur | Discussion, édition et complétion configurables ; serveur local possible[^p4-out-continue] |
| Cline | Extension VS Code et CLI | Agent avec plusieurs fournisseurs possibles, dont des solutions auto-hébergées[^p4-out-cline] |
| Aider | Terminal | Modifications du code et intégration Git ; API distante ou serveur compatible local[^p4-out-aider] |
| OpenCode | Terminal, application et extension d’éditeur | Agent avec plusieurs fournisseurs ; configuration de modèles locaux possible[^p4-out-opencode] |
Table: Quelques portes d’entrée pour développer avec une IA

Deux changements peuvent vous éviter de suivre une ancienne procédure d’installation. Google a annoncé le passage des utilisateurs individuels de Gemini CLI et Gemini Code Assist vers Antigravity CLI à compter du 18 juin 2026[^p4-out-migration]. De son côté, l’adresse de tarification de Windsurf redirige, lors de cette consultation, vers celle de Devin[^p4-out-windsurf]. Si vous reconnaissez un ancien nom, vérifiez donc aussi le parcours d’accès actuel.

Pour notre installation, nous allons garder deux possibilités : Copilot dans VS Code pour essayer un service hébergé, et Continue dans le même éditeur pour réutiliser notre serveur. Ce choix nous donne des manipulations concrètes à suivre ; les étapes de lecture du code et de validation resteront utilisables avec les autres outils.

[^p4-out-copilot]: GitHub, [offres et fonctions de Copilot](https://github.com/features/copilot/plans).
[^p4-out-cursor]: Cursor, [offres et fonctions](https://cursor.com/pricing).
[^p4-out-claude]: Anthropic, [offres Claude](https://claude.com/pricing) ; Microsoft, [intégration des agents dans VS Code](https://code.visualstudio.com/docs/agents/run/agent-harnesses).
[^p4-out-codex]: OpenAI, [offres Codex](https://learn.chatgpt.com/docs/pricing).
[^p4-out-devin]: Devin, [offres et interfaces](https://devin.ai/pricing).
[^p4-out-jetbrains]: JetBrains, [abonnements et usage de JetBrains AI](https://www.jetbrains.com/help/ai-assistant/licensing-and-subscriptions.html).
[^p4-out-google]: Google, [offres Antigravity](https://antigravity.google/pricing/).
[^p4-out-zed]: Zed, [offres](https://zed.dev/pricing).
[^p4-out-continue]: Continue, [projet](https://github.com/continuedev/continue) et [configuration d’un serveur compatible](https://docs.continue.dev/customize/model-providers/top-level/openai).
[^p4-out-cline]: Cline, [offres](https://cline.bot/pricing).
[^p4-out-aider]: Aider, [présentation](https://aider.chat/) et [serveurs compatibles](https://aider.chat/docs/llms/openai-compat.html).
[^p4-out-opencode]: OpenCode, [présentation](https://opencode.ai/) et [fournisseurs](https://opencode.ai/docs/providers/).
[^p4-out-migration]: Google, [annonce de la transition vers Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), 19 mai 2026.
[^p4-out-windsurf]: [Page de tarification de Windsurf](https://windsurf.com/pricing), redirection constatée le 14 septembre 2026.

## 2. Choisir une solution adaptée à ses besoins

**TL;DR** — Un abonnement, un logiciel gratuit et une API à l’usage ne se comparent pas avec le seul prix affiché. Regardez ce qui est inclus, ce qui déclenche une dépense supplémentaire et où part votre code. Pour commencer, une offre gratuite ou un petit modèle local suffit à essayer notre démarche.

Nous avons les noms. Maintenant, lequel installer ? Votre budget compte, mais votre façon de travailler aussi. Un outil qui vous oblige à changer d’éditeur, envoie du code que vous ne pouvez pas transmettre ou vous fait attendre trop longtemps peut être mal adapté, même s’il produit de bonnes réponses.

### Combien cela coûte-t-il ?

Les montants ci-dessous sont les tarifs individuels affichés en **dollars américains, par mois avec facturation mensuelle**, relevés le **14 septembre 2026**. Les offres annuelles, promotions et contrats d’entreprise ne sont pas comparés ici. Le prix finalement facturé dépend aussi du pays, des taxes et du canal d’achat.

| Solution | Accès gratuit ou coût du logiciel | Offres payantes et limite à comprendre |
| --- | --- | --- |
| GitHub Copilot | Free : 2 000 complétions mensuelles et accès limité à la discussion et aux agents | Pro : 10 $ ; Pro+ : 39 $ ; Max : 100 $. Les usages IA reposent sur des crédits, distincts du nombre de complétions[^p4-prix-copilot] |
| Cursor | Hobby, avec usage limité | Pro : 20 $ ; Pro+ : 60 $ ; Ultra : 200 $. Usage supplémentaire possible au-delà de l’enveloppe incluse[^p4-prix-cursor] |
| Claude Code | Le forfait Claude Free ne l’inclut pas | Inclus dans Pro à 20 $ ; Max à partir de 100 $. Des limites d’usage s’appliquent[^p4-prix-claude] |
| Codex | L’accès gratuit dépend de l’offre en vigueur ; ne pas compter dessus pour une capacité fixe | Plus : 20 $ ; Pro à partir de 100 $ ; API facturée séparément. Le palier Pro à 200 $ existe, mais les nouvelles souscriptions sont temporairement suspendues à la date du relevé[^p4-prix-codex][^p4-prix-pro] |
| Devin | Free, avec quota limité | Pro : 20 $ ; Max : 200 $. Quotas et usage supplémentaire à vérifier selon l’interface[^p4-prix-devin] |
| JetBrains AI | Free : 3 crédits par période de 30 jours | Pour les particuliers : Pro à 10 $, Ultimate à 30 $. Respectivement 10 et 35 crédits par période de 30 jours ; licence de l’IDE à considérer séparément[^p4-prix-jb] |
| Google Antigravity | Offre individuelle gratuite, limitée | Google AI Pro : 19,99 $ sur la page américaine ; donne accès à des limites plus élevées. D’autres paliers existent[^p4-prix-google][^p4-prix-google-pro] |
| Zed | Personal gratuit, utilisable avec ses propres API ou des agents externes | Pro : 10 $, dont 5 $ d’usage de modèles ; facturation supplémentaire au-delà[^p4-prix-zed] |
| Continue | Extension libre utilisable avec son modèle local | Avec un fournisseur distant, l’inférence reste à financer selon le fournisseur[^p4-prix-continue] |
| Cline | Logiciel gratuit pour un usage individuel | Inférence à l’usage via le service proposé ou son propre fournisseur ; auto-hébergement possible[^p4-prix-cline] |
| Aider | Logiciel libre | API à financer séparément ou calcul local[^p4-prix-aider] |
| OpenCode | Logiciel libre | Modèles accessibles selon le fournisseur choisi : offre hébergée, API personnelle ou modèle local[^p4-prix-opencode] |
Table: Prix d’accès et origine des dépenses

« Gratuit » peut donc désigner deux choses : un service qui vous accorde un petit quota, ou un logiciel que vous installez sans payer, mais auquel il faut fournir un modèle. Dans le second cas, brancher une API payante ne rend pas ses réponses gratuites.

De même, une complétion et une tâche d’agent ne représentent pas la même quantité de travail. Un agent peut lire plusieurs fichiers, produire du code, recevoir une sortie de tests et recommencer. Selon la tarification, cela consomme des tokens, des crédits ou une partie d’un quota. Les crédits de deux fournisseurs ne sont pas une unité commune.

Avant d’acheter un abonnement, essayez quelques tâches que vous faites réellement. Regardez le temps consacré à obtenir **et vérifier** le résultat. Si vous avez gagné cinq minutes de saisie et ajouté vingt minutes de réparation, l’offre la moins chère ne résout pas votre problème. 😅

[^p4-prix-copilot]: [Tarifs GitHub Copilot](https://github.com/features/copilot/plans).
[^p4-prix-cursor]: [Tarifs Cursor](https://cursor.com/pricing).
[^p4-prix-claude]: [Tarifs Claude](https://claude.com/pricing).
[^p4-prix-codex]: [Tarifs Codex](https://learn.chatgpt.com/docs/pricing) ; [séparation entre abonnement ChatGPT Plus et API](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus).
[^p4-prix-pro]: OpenAI, [paliers Pro et suspension temporaire des nouvelles souscriptions Pro à 200 $](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers).
[^p4-prix-devin]: [Tarifs Devin](https://devin.ai/pricing).
[^p4-prix-jb]: JetBrains, [tarifs individuels, quotas et offres d’organisation](https://www.jetbrains.com/help/ai-assistant/licensing-and-subscriptions.html).
[^p4-prix-google]: [Offres Antigravity](https://antigravity.google/pricing/).
[^p4-prix-google-pro]: Google, [tarifs Google AI aux États-Unis](https://one.google.com/intl/en_us/about/google-ai-plans/).
[^p4-prix-zed]: [Tarifs Zed](https://zed.dev/pricing).
[^p4-prix-continue]: [Projet Continue](https://github.com/continuedev/continue) et [fonctionnement sans Internet](https://docs.continue.dev/guides/running-continue-without-internet).
[^p4-prix-cline]: [Tarifs Cline](https://cline.bot/pricing).
[^p4-prix-aider]: [Aider](https://aider.chat/).
[^p4-prix-opencode]: [OpenCode](https://opencode.ai/) et [ses fournisseurs](https://opencode.ai/docs/providers/).

### Où faire tourner le modèle ?

Pour un service hébergé, votre ordinateur doit surtout faire tourner l’éditeur et le projet. Le fournisseur effectue les calculs du modèle. Vous avez besoin d’un accès au service et d’une connexion réseau, mais pas d’une grosse carte graphique.

En local, vous fournissez aussi la mémoire et le calcul. Cela permet de garder l’inférence sur votre machine et de travailler sans accès au fournisseur une fois les éléments nécessaires téléchargés. En échange, il faut choisir un modèle qui tient en mémoire et dont le temps de réponse vous convient.

| Situation | Point de départ possible |
| --- | --- |
| Petit ordinateur, priorité à une installation simple | Offre hébergée gratuite, si l’envoi du code est acceptable |
| Envoi du code exclu, aucune carte graphique dédiée | Petit modèle de code sur CPU et demandes courtes |
| Machine disposant de davantage de mémoire et d’un GPU compatible | Même principe local, puis essais de modèles plus volumineux |
| Assistant déjà fourni par votre équipe | Commencer avec cet outil, dans les conditions d’usage de l’équipe |
Table: Plusieurs chemins pour le même atelier

Notre SmolLM2 de la partie 3 nous a servi à comprendre l’inférence. Il ne faut pas attendre de lui qu’il explore un dépôt et corrige un ticket tout seul. Nous allons d’abord l’utiliser pour vérifier la connexion, puis proposer un petit modèle spécialisé dans le code.

Une grosse carte graphique donnera davantage de possibilités, mais elle ne sera pas le ticket d’entrée du tutoriel. Avec un modèle modeste, on peut discuter d’une fonction, demander un exemple et appliquer soi-même une proposition. Les manipulations sur le programme resteront les mêmes.

Reste la question des données. Une API personnelle peut vous laisser choisir votre fournisseur, sans rendre l’inférence locale. Et une option « ne pas utiliser mes données pour l’entraînement » ne signifie pas que le code ne quitte jamais l’ordinateur : elle porte sur un usage des données après leur transmission.

Pour notre atelier, nous utiliserons des fichiers publics et un ticket fictif. Pour votre travail, il faudra savoir ce que votre équipe autorise à transmettre. Nous reviendrons plus largement sur ces choix ; ils comptent déjà au moment d’installer l’outil.

## 3. Installer notre premier assistant

**TL;DR** — Préparez une copie du projet, puis choisissez un seul des deux parcours. Avec Copilot, le modèle est hébergé. Avec Continue, nous allons réutiliser notre serveur local, puis essayer un petit modèle de code. Dans les deux cas, la première demande portera sur la lecture d’un extrait.

Nous allons maintenant faire apparaître l’assistant à côté de notre code. Il n’a encore rien à corriger : commençons par vérifier que nous savons ce que nous lui envoyons et d’où vient sa réponse.

### Ouvrir notre copie du projet

Téléchargez [les fichiers de l’atelier de développement](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/b95165289276a45bc299d0826e3c540727e8e203/telechargements/annexes-developpement-v1.zip), puis décompressez l’archive. Vous pouvez aussi les récupérer dans [le dépôt](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/b95165289276a45bc299d0826e3c540727e8e203/ateliers/04-developpement).

Dans `atelier-developpement`, copiez le dossier `01-depart` dans un nouveau dossier nommé `mon-suivi`, **en dehors du dépôt téléchargé**. Gardez les autres dossiers à côté pour plus tard : ils contiennent les étapes de correction.

Installez [Visual Studio Code](https://code.visualstudio.com/download), si vous ne l’avez pas déjà, puis utilisez **Fichier → Ouvrir le dossier** pour ouvrir `mon-suivi`. L’explorateur doit afficher `suivi.py`, les tests et le dossier `scenarios`. Il ne doit pas afficher `02-test-rouge` et `03-corrige` : autant éviter de poser une devinette à l’agent en lui laissant la réponse sous le nez. 🙂

Pour le moment, ouvrez simplement `suivi.py`. Nous lancerons les tests dans le chapitre consacré au projet.

Si vous utilisez déjà Cursor, Codex, Claude Code ou un autre assistant, vous pouvez garder votre outil et ouvrir cette même copie. La demande de lecture en fin de chapitre sera identique.

### Utiliser un service hébergé

Dans ce parcours, nous utilisons **GitHub Copilot dans VS Code**, avec un compte GitHub et l’offre gratuite si votre compte y est éligible. Le modèle tournera chez le fournisseur ; le code ajouté à la conversation lui sera transmis.

Dans la barre d’état de VS Code, ouvrez le menu de l’icône Copilot, choisissez **Use AI Features**, puis suivez la connexion à GitHub. Un compte sans abonnement peut être inscrit à Copilot Free. Le tableau de bord Copilot, accessible depuis la barre d’état, permet de suivre l’usage[^p4-install-copilot].

Ouvrez la vue de discussion. Pour cette première demande, choisissez une session **Copilot** et le rôle **Ask**, qui permet de poser des questions sans modifier le code. Choisissez un modèle disponible dans votre offre, ou **Auto** si cette option est proposée[^p4-install-roles].

Nous ne lançons pas encore de tâche en arrière-plan. Nous voulons une réponse que nous puissions comparer à quelques lignes sous nos yeux.

Si l’interface vous demande de souscrire pour continuer, vérifiez le compte connecté, son éligibilité et le quota restant. Le parcours local reste disponible ; vous n’avez pas besoin de payer pour accéder aux fichiers et faire l’atelier.

Une fois la discussion ouverte, passez à la section « Notre première demande de lecture ». L’installation locale ci-dessous constitue l’autre parcours.

[^p4-install-copilot]: Microsoft, [configuration de Copilot dans VS Code](https://code.visualstudio.com/docs/setup/copilot).
[^p4-install-roles]: Microsoft, [choix de l’agent, du rôle et du modèle](https://code.visualstudio.com/docs/agents/run/agent-harnesses).

### Relier l’éditeur à notre modèle local

Nous allons conserver le serveur de la partie 3 et remplacer notre client Python par **Continue**.

#### Retrouver le serveur

Relancez `llama-server` avec la commande qui fonctionnait sur votre machine dans la partie précédente. Pour cette première connexion, conservez le port `8080`, l’adresse `127.0.0.1`, l’alias `atelier-local` et le contexte de `2048` tokens.

Ouvrez <http://127.0.0.1:8080/health> dans le navigateur. Lorsque le modèle est chargé, ce point d’accès doit indiquer que le serveur est prêt. Vous pouvez également ouvrir <http://127.0.0.1:8080/v1/models> pour retrouver le nom exposé par le serveur[^p4-install-server].

Si rien ne répond, regardez d’abord le terminal du serveur. Installer une extension ne réparera pas un modèle qui n’a pas fini de charger.

#### Ajouter Continue

Dans les extensions de VS Code, recherchez **Continue**, ou ouvrez directement [sa page officielle](https://marketplace.visualstudio.com/items?itemName=Continue.continue), puis installez l’extension[^p4-install-continue].

Ouvrez son panneau et choisissez la configuration locale. La roue dentée associée à **Local Config** permet d’ouvrir le fichier YAML. Il se trouve dans `~/.continue/config.yaml` sous Linux et macOS, ou `%USERPROFILE%\.continue\config.yaml` sous Windows[^p4-install-config].

Si vous utilisez déjà Continue, conservez une copie de votre configuration avant cet essai. Pour notre installation, utilisez ce contenu :

```yaml
name: Atelier local
version: 1.0.0
schema: v1

models:
  - name: SmolLM2 - connexion locale
    provider: openai
    model: atelier-local
    apiBase: http://127.0.0.1:8080/v1
    apiKey: local
    roles:
      - chat
    defaultCompletionOptions:
      contextLength: 2048
      maxTokens: 128
      temperature: 0
```
Code: Configuration de Continue pour le serveur de la partie 3

Ici, `provider: openai` indique le format d’API utilisé. **La destination est l’adresse de `apiBase`**, donc notre ordinateur. La valeur `local` est un remplissage pour le champ de clé ; notre serveur d’atelier n’a pas d’authentification configurée. Ce n’est pas une clé de compte OpenAI[^p4-install-compatible].

La longueur de contexte correspond à celle de notre serveur. Nous limitons aussi la réponse à 128 tokens pour ce premier essai. Le rôle `chat` nous suffit ; nous ne déclarons pas de capacité d’utilisation d’outils pour ce modèle[^p4-install-yaml].

Enregistrez, sélectionnez la configuration et le modèle locaux, puis choisissez le mode **Chat**. Envoyez une question très courte, par exemple :

> Reply with the word hello.

Ce n’est pas un test d’intelligence. Nous cherchons une réponse, même imparfaite, et une requête correspondante dans le terminal de `llama-server`. Si une erreur mentionne une clé de service distant, vérifiez le modèle sélectionné et `apiBase`.

Continue propose un réglage **Allow Anonymous Telemetry** dans les paramètres de l’extension : désactivez-le pour cet usage local[^p4-install-offline]. Les réglages réseau de VS Code et des autres extensions restent séparés. Pour vérifier que cette conversation n’a pas besoin d’Internet, vous pouvez couper la connexion après les téléchargements, ouvrir une nouvelle discussion et envoyer une autre question.

#### Passer à un modèle de code

La connexion fonctionne ? Nous pouvons changer ce que le serveur charge.

Pour un premier essai sur CPU, prenons **Qwen2.5-Coder-1.5B-Instruct**, dans sa version GGUF `Q4_K_M`. C’est un petit modèle destiné au code, qui reste adapté à des demandes courtes ; nous n’en attendrons pas les capacités d’un gros agent hébergé[^p4-install-qwen].

Dans [le dépôt officiel du modèle](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/tree/main), téléchargez **`qwen2.5-coder-1.5b-instruct-q4_k_m.gguf`**, puis placez-le dans le dossier `modeles` utilisé en partie 3. Ce fichier pèse environ **1,1 Go** ; prévoyez aussi de la mémoire pour le contexte et les programmes ouverts[^p4-install-qwen-fichier].

Arrêtez le serveur précédent avec **Ctrl+C**. Dans sa commande de lancement, remplacez le chemin après `-m` par celui de ce fichier, passez le contexte de `2048` à `4096` et l’alias à `atelier-code`. Gardez les réglages de chargement des bibliothèques qui fonctionnaient déjà sur votre système.

Avec l’arborescence Linux de la partie 3, la commande devient :

```bash
./moteur/llama-server -m modeles/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf --host 127.0.0.1 --port 8080 -c 4096 -t 2 -ngl 0 --device none --parallel 1 --alias atelier-code
```
Code: Lancement du modèle de code sur CPU

Sous Windows ou macOS, reprenez votre chemin d’exécutable de la partie 3 avec ces mêmes changements. Le but est de remplacer le modèle dans une installation qui fonctionne déjà.

Remplacez ensuite la configuration Continue par :

```yaml
name: Atelier code local
version: 1.0.0
schema: v1

models:
  - name: Qwen Coder - CPU
    provider: openai
    model: atelier-code
    apiBase: http://127.0.0.1:8080/v1
    apiKey: local
    roles:
      - chat
    defaultCompletionOptions:
      contextLength: 4096
      maxTokens: 512
      temperature: 0
```
Code: Configuration de discussion avec le modèle de code

Ouvrez une nouvelle conversation après le changement de modèle. Nous allons lui montrer une fonction, pas le dépôt entier.

Si la réponse est lente, commencez par raccourcir la demande et la sortie attendue. Si la machine manque de mémoire, revenez au contexte précédent ou au petit modèle pour finir le diagnostic de connexion. Pour l’atelier, vous pouvez toujours effectuer les modifications vous-même : il n’est pas nécessaire de laisser un modèle en difficulté multiplier les tentatives.

[^p4-install-server]: llama.cpp, [documentation du serveur et des points d’accès HTTP](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).
[^p4-install-continue]: Continue, [installation de l’extension](https://docs.continue.dev/ide-extensions/install).
[^p4-install-config]: Continue, [configuration locale](https://docs.continue.dev/customize/deep-dives/configuration).
[^p4-install-compatible]: Continue, [serveurs compatibles avec l’API OpenAI](https://docs.continue.dev/customize/model-providers/top-level/openai).
[^p4-install-yaml]: Continue, [référence du fichier YAML](https://docs.continue.dev/reference).
[^p4-install-offline]: Continue, [fonctionnement sans Internet](https://docs.continue.dev/guides/running-continue-without-internet).
[^p4-install-qwen]: Qwen, [Qwen2.5-Coder-1.5B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF).
[^p4-install-qwen-fichier]: Qwen, [fichiers GGUF proposés](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/tree/main).

### Notre première demande de lecture

Dans `suivi.py`, repérez la fonction `notifier`. Copiez-la dans la discussion, avec la définition de `Etat` juste au-dessus. Dans Continue, vous pouvez aussi sélectionner le code et utiliser **Ctrl+L**, ou **Cmd+L** sur macOS, pour l’ajouter à la conversation[^p4-install-chat].

Ajoutez cette demande :

> Explique ce que représente un état et dans quels cas cette fonction renvoie vrai. Appuie-toi uniquement sur cet extrait. Ne modifie aucun fichier et ne propose pas encore de correction.

Nous n’attendons pas une réponse mot pour mot. Le code doit permettre de retrouver deux informations : un état contient un prix en centimes et une disponibilité ; la fonction décide de notifier lorsque le produit est disponible et qu’au moins une des deux conditions de la parenthèse est vraie.

Lisez l’explication en gardant le code ouvert. Si le modèle parle d’un envoi de courriel ou d’une base de données, cherchez ce qui lui permet de l’affirmer dans l’extrait. Vous ne trouverez rien : cette fonction renvoie seulement un booléen.

Votre modèle local répond mal en français ? Vous pouvez essayer la même demande en anglais :

> Explain what an Etat represents and when notifier returns True. Use only this snippet. Do not change any files or suggest a fix yet.

L’objectif reste de comprendre la fonction. Si l’explication ne vous aide pas, revenez au code et décomposez la condition vous-même. Nous allons justement le faire dans le chapitre suivant.

#### Et pour les modifications ?

Les deux parcours ne donneront pas exactement la même expérience. Avec un agent, vous pourrez lui demander de préparer les changements puis examiner le diff. Avec notre configuration locale en mode Chat, vous pourrez demander une proposition et l’appliquer vous-même après lecture. Nous n’avons pas configuré ce petit modèle pour piloter le terminal.

Dans les chapitres suivants, une consigne destinée à un agent pourra donc aussi servir à obtenir du code dans la discussion. Vous exécuterez alors vous-même les commandes indiquées et lui montrerez seulement la sortie utile. Le programme et les critères de réussite seront identiques.

Gardez votre dossier `mon-suivi` : nous allons maintenant y lancer les tests et comprendre pourquoi un programme dont les tests passent peut tout de même avoir besoin d’une correction.

[^p4-install-chat]: Continue, [discussion et sélection de code](https://docs.continue.dev/ide-extensions/chat/quick-start).

## Raccord au chapitre suivant : lancer les tests du projet

Votre dossier `mon-suivi` est déjà ouvert dans l’éditeur depuis l’installation de l’assistant. Gardez cette copie : inutile de télécharger ou de recopier le projet une seconde fois.

Ouvrez un terminal dans ce dossier. Il doit contenir `suivi.py` et `scenarios`. Pour exécuter cet atelier, nous utilisons Python 3.12 ; aucune bibliothèque externe n’est nécessaire.

```bash
python -m unittest discover -v
python suivi.py scenarios/retour-stock.json
```
Code: Lancer les tests existants et le scénario de remise en stock

Si votre installation utilise la commande `python3` ou `py -3.12`, utilisez-la à la place de `python` dans les commandes de l’atelier.

Les trois tests de départ passent. Le scénario affiche pourtant une décision de notification pour une simple remise en stock. Le programme n’envoie rien sur le réseau : il affiche sa décision en JSON.

Nous allons suivre le chemin qui mène à cette décision avant de demander une correction.
