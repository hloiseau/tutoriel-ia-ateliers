# 1. Avec quoi va-t-on développer ?

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR** — Le modèle produit une réponse, le moteur le fait tourner et l’assistant organise le travail autour. Pour développer, on peut demander une suggestion, discuter d’un extrait ou laisser un agent intervenir dans le projet. Ce ne sont pas les mêmes besoins.

Avant de choisir un nom dans une liste, regardons ce que nous voulons lui faire faire. « Développer avec une IA » peut vouloir dire accepter une ligne proposée dans l’éditeur comme confier plusieurs fichiers à un agent. Entre les deux, il y a de quoi trouver une utilisation qui vous convienne.

## Le modèle, le moteur et l’assistant

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

## De la suggestion à l’agent

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

## Faire le tour des outils

Commençons par les outils que vous pouvez rencontrer dans un éditeur, un terminal ou un service distant. Nous compléterons ce panorama avec les harness extensibles, dont Pi, dans la section suivante. Ce n’est pas la liste de tous les produits existants, ni un classement de leurs modèles.

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

## Pi et les autres harness

Vous croiserez souvent le mot **harness** dans les discussions sur les agents. Il désigne le programme qui organise leur fonctionnement : préparer le contexte, appeler le modèle, exécuter ses demandes d’outils et poursuivre la conversation avec les résultats.

Dans notre premier client Python, nous envoyions une question et recevions du texte. Un harness peut ajouter la boucle suivante : le modèle demande à lire un fichier, le programme le lit et lui renvoie le contenu, puis le modèle choisit la prochaine action. La gestion des sessions, des permissions et des modifications appartient aussi à cet entourage logiciel.

Deux agents utilisant le même modèle peuvent donc se comporter différemment. Ils ne préparent pas forcément le même contexte et ne lui donnent pas les mêmes outils.

##### Les agents que l’on rencontre déjà dans les offres

Claude Code, Codex, OpenCode, Aider, Cline ou encore l’agent de Copilot ne sont pas simplement des fenêtres de discussion. Ils organisent un travail sur le projet. Les comparer demande de regarder leur fonctionnement, au-delà du modèle annoncé.

| Famille | Exemples déjà rencontrés | Ce qui compte pour choisir |
| --- | --- | --- |
| Agent lié à une offre de fournisseur | Claude Code, Codex, Copilot | Modèles accessibles, mode de facturation, permissions et interfaces disponibles |
| Agent permettant de choisir son fournisseur | OpenCode, Aider, Cline | Compatibilité de l’API, modèle local possible, outils et manière d’appliquer les changements |
| Éditeur intégrant un agent | Cursor, Antigravity, environnement JetBrains | Intégration au code, complétion, lecture du diff et place laissée aux outils habituels |
Table: Les offres présentées plus haut ne se situent pas toutes au même niveau

Ces catégories se recoupent. Un même agent peut être accessible en terminal et intégré à plusieurs éditeurs. Les modalités d’accès restent celles documentées pour chaque offre.

##### Pi, et les autres possibilités à connaître

**Pi** mérite qu’on s’y arrête. Il propose un agent en terminal que l’on peut étendre et intégrer à ses propres outils. Sa conception laisse une grande place aux extensions et aux modèles de consignes, plutôt que de fournir par défaut toutes les étapes d’une méthode de développement. Il dispose aussi d’interfaces permettant de le piloter depuis un programme[^p4-h-pi].

Cela rejoint une question qui nous suivra dans le tutoriel : est-ce l’outil qui décide de notre manière de travailler, ou pouvons-nous le modifier pour qu’il nous aide là où nous en avons besoin ?

| Outil | Interface et approche | Choix du modèle et usage local |
| --- | --- | --- |
| **Pi** | Agent en terminal, extensible ; API et interfaces d’intégration | Plusieurs fournisseurs et configuration de serveurs locaux[^p4-h-pi-models] |
| **Kilo Code** | Agent dans VS Code, JetBrains et en CLI | Choix de modèles et de fournisseurs ; distinguer l’agent des services de calcul Kilo[^p4-h-kilo] |
| **goose** | Application de bureau, CLI et API ; usages au-delà du code | Plusieurs fournisseurs, dont Ollama pour l’inférence locale[^p4-h-goose] |
| **Amp** | Agent et environnements de travail appelés *orbs* ; exécution hébergée ou sur ses propres runners | API personnelle ou abonnements compatibles selon l’offre ; son propre runner ne signifie pas que le modèle tourne dessus[^p4-h-amp] |
| **Mistral Vibe** | Agent en CLI, avec une offre intégrée de développement | Fournisseurs configurables ; vérifier le format d’API et le modèle utilisés[^p4-h-vibe][^p4-h-vibe-config] |
| **Kiro** | IDE et CLI, avec une place importante donnée aux spécifications et aux règles du projet | Modèles et crédits proposés par le service ; modèle à poids ouverts ne signifie pas inférence locale[^p4-h-kiro] |
| **OpenHands** | Agent et environnement de travail ; Agent Canvas peut aussi accueillir d’autres agents | Exécution locale ou distante ; documentation pour les modèles locaux[^p4-h-openhands][^p4-h-openhands-local] |
Table: Compléter le panorama des harness et des environnements d’agents

Pour Pi, la documentation permet par exemple de déclarer l’adresse d’un serveur compatible dans un fichier de configuration. Nous retrouvons ainsi la séparation entre modèle et assistant, sans devoir adopter un fournisseur unique[^p4-h-pi-models].

Cette liberté n’implique pas que toutes les protections soient installées d’avance. Le dépôt de Pi précise que le programme s’exécute avec les droits du processus qui le lance, sans système intégré de restriction des accès aux fichiers, aux processus ou au réseau. Une isolation supplémentaire relève donc de l’environnement dans lequel on l’exécute[^p4-h-pi-droits]. C’est une différence concrète à connaître lorsqu’on compare deux harness.

##### Les noms que vous trouverez dans d’anciens comparatifs

**Roo Code** a sa place dans l’histoire de ces outils, mais son dépôt officiel est archivé depuis le **15 mai 2026**. Nous ne le présenterons donc pas comme une installation maintenue au même titre que les projets actifs de cette liste[^p4-h-roo].

**Gemini CLI** mérite aussi d’être nommé explicitement. Le changement annoncé par Google concerne notamment les parcours gratuits et les abonnements individuels transférés vers Antigravity ; il ne faut pas en déduire que tous les usages professionnels ou toutes les modalités d’accès ont disparu[^p4-h-gemini].

Les noms, les offres et parfois les dépôts changent. Le comparatif est une photographie de septembre 2026, pas une liste à apprendre par cœur. Les étoiles GitHub peuvent aider à repérer un projet connu ; elles ne disent pas si sa manière de travailler convient à votre équipe.

[^p4-h-pi]: Pi, [présentation du harness et de ses extensions](https://pi.dev/).
[^p4-h-pi-models]: Pi, [modèles et fournisseurs personnalisés](https://pi.dev/docs/latest/models).
[^p4-h-kilo]: Kilo, [interfaces et fournisseurs](https://github.com/Kilo-Org/kilocode).
[^p4-h-goose]: goose, [présentation et fournisseurs](https://github.com/aaif-goose/goose).
[^p4-h-amp]: Amp, [documentation](https://ampcode.com/docs) et [offres, runners et modèles](https://ampcode.com/pricing).
[^p4-h-vibe]: Mistral, [Vibe CLI](https://github.com/mistralai/mistral-vibe).
[^p4-h-vibe-config]: Mistral, [configuration des fournisseurs et des permissions](https://docs.mistral.ai/vibe/code/cli/configuration-reference).
[^p4-h-kiro]: Kiro, [CLI](https://kiro.dev/docs/cli/) et [offres](https://kiro.dev/pricing/).
[^p4-h-openhands]: OpenHands, [Agent Canvas et ses modes d’exécution](https://github.com/OpenHands/OpenHands).
[^p4-h-openhands-local]: OpenHands, [utiliser un modèle local](https://docs.openhands.dev/openhands/usage/llms/local-llms).
[^p4-h-pi-droits]: Pi, [permissions et conteneurisation](https://github.com/earendil-works/pi#permissions--containerization).
[^p4-h-roo]: [Dépôt officiel Roo Code, archivé](https://github.com/RooCodeInc/Roo-Code).
[^p4-h-gemini]: Google, [transition de Gemini CLI vers Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/).


