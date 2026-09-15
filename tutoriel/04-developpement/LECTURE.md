# Développer avec une IA, du problème au changement vérifié

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

Un modèle répond dans notre terminal. Très bien. Mais comment passer de cette conversation à une modification dans un vrai projet ?

Il existe des extensions pour les éditeurs, des éditeurs qui intègrent directement l’IA, des assistants en ligne de commande et des agents qui travaillent sur une machine distante. Certains utilisent un abonnement, d’autres une API facturée à l’usage. Certains peuvent parler à notre serveur local. On peut vite passer davantage de temps à choisir son outil qu’à s’en servir. 😅

Nous allons prendre le temps de nous y retrouver, puis installer de quoi travailler. Pour commencer sans carte graphique dédiée, nous utiliserons un assistant dont le modèle est hébergé, avec un accès gratuit si votre compte y est éligible. Nous garderons aussi une expérience facultative avec notre serveur local, pour voir ce que donne une discussion sur quelques lignes de code. Cet essai ne constitue pas un parcours d’agent de code sur CPU.

Nous ouvrirons ensuite un petit projet Python de suivi de prix. Ses tests passent, mais il envoie une notification dans un cas où nous n’en voulons plus. Nous suivrons la modification jusqu’au bout : comprendre le programme, préciser la demande, reproduire le problème, corriger le code et vérifier le résultat.

Si vous débutez, prenez aussi le temps de faire votre propre lecture du code. Une explication très convaincante peut être fausse ; pour s’en apercevoir, il faut pouvoir suivre ce que fait le programme.

**TL;DR**

- Nous choisissons un assistant en regardant ses fonctions, son coût et l’endroit où il traite nos données.
- Le parcours principal utilise VS Code avec GitHub Copilot ; vous pouvez conserver un assistant que vous utilisez déjà.
- L’essai local avec Continue est facultatif. Faire répondre un modèle ne suffit pas à montrer qu’il peut prendre en charge notre atelier.
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

### Pi et les autres harness

Vous croiserez souvent le mot **harness** dans les discussions sur les agents. Il désigne le programme qui organise leur fonctionnement : préparer le contexte, appeler le modèle, exécuter ses demandes d’outils et poursuivre la conversation avec les résultats.

Dans notre premier client Python, nous envoyions une question et recevions du texte. Un harness peut ajouter la boucle suivante : le modèle demande à lire un fichier, le programme le lit et lui renvoie le contenu, puis le modèle choisit la prochaine action. La gestion des sessions, des permissions et des modifications appartient aussi à cet entourage logiciel.

Deux agents utilisant le même modèle peuvent donc se comporter différemment. Ils ne préparent pas forcément le même contexte et ne lui donnent pas les mêmes outils.

###### Les agents que l’on rencontre déjà dans les offres

Claude Code, Codex, OpenCode, Aider, Cline ou encore l’agent de Copilot ne sont pas simplement des fenêtres de discussion. Ils organisent un travail sur le projet. Les comparer demande de regarder leur fonctionnement, au-delà du modèle annoncé.

| Famille | Exemples déjà rencontrés | Ce qui compte pour choisir |
| --- | --- | --- |
| Agent lié à une offre de fournisseur | Claude Code, Codex, Copilot | Modèles accessibles, mode de facturation, permissions et interfaces disponibles |
| Agent permettant de choisir son fournisseur | OpenCode, Aider, Cline | Compatibilité de l’API, modèle local possible, outils et manière d’appliquer les changements |
| Éditeur intégrant un agent | Cursor, Antigravity, environnement JetBrains | Intégration au code, complétion, lecture du diff et place laissée aux outils habituels |
Table: Les offres présentées plus haut ne se situent pas toutes au même niveau

Ces catégories se recoupent. Un même agent peut être accessible en terminal et intégré à plusieurs éditeurs. Les modalités d’accès restent celles documentées pour chaque offre.

###### Pi, et les autres possibilités à connaître

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

###### Les noms que vous trouverez dans d’anciens comparatifs

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



## 2. Choisir une solution adaptée à ses besoins

**TL;DR** — Un abonnement, un logiciel gratuit et une API à l’usage ne se comparent pas avec le seul prix affiché. Regardez ce qui est inclus, ce qui déclenche une dépense supplémentaire et où part votre code. Sans carte graphique dédiée, un modèle hébergé permet de commencer. L’essai avec un petit modèle local sert à explorer ses possibilités, sans présumer qu’il saura mener l’atelier.

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

###### Prix des autres harness et environnements

Pour les logiciels libres, le prix du programme est souvent le point le plus simple. Il faut ensuite compter l’inférence et, si vous utilisez une machine distante, son exécution.

| Solution | Logiciel ou accès de départ | Ce qui peut être facturé |
| --- | --- | --- |
| Pi | Logiciel libre, sans abonnement Pi requis | Fournisseur du modèle ou ressources de votre machine[^p4-prix-pi] |
| goose | Logiciel libre | Modèle choisi et éventuelle infrastructure[^p4-prix-goose] |
| Kilo Code | Offre individuelle du logiciel gratuite | Inférence séparée ; achat de crédits avec frais annoncés de 5 % ; Kilo Pass facultatif à partir de 19 $/mois ; calcul cloud séparé[^p4-prix-kilo] |
| Amp | Hobby gratuit, avec ses propres runners ou exécution à l’usage | Offre individuelle affichée à 20 $/mois ; modèles apportés par API ou abonnement compatible et ressources d’exécution à distinguer[^p4-prix-amp] |
| Mistral Vibe | Offre gratuite avec sessions de code limitées ; CLI disponible en source | Pro affiché à 14,99 $/mois hors taxes ; limites d’usage ; API selon son propre tarif[^p4-prix-vibe] |
| Kiro | Free : 50 crédits | Pro : 20 $ ; Pro+ : 40 $ ; Pro Max : 100 $ ; Power : 200 $ par mois. Crédits supplémentaires selon l’offre[^p4-prix-kiro] |
| OpenHands | Logiciel local libre et accès individuel hébergé gratuit | API personnelle ou modèles à l’usage ; conditions distinctes pour l’entreprise[^p4-prix-openhands] |
Table: Tarifs complémentaires, relevés le 14 septembre 2026 en USD

Un abonnement au modèle, un abonnement au logiciel et une machine qui exécute l’agent peuvent donc représenter trois dépenses distinctes. Avant de comparer les totaux, regardez qui fournit chacun de ces éléments.

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

[^p4-prix-pi]: [Pi, logiciel sous licence MIT](https://github.com/earendil-works/pi) et [configuration des modèles](https://pi.dev/docs/latest/models).
[^p4-prix-goose]: [goose, logiciel sous licence Apache 2.0](https://github.com/aaif-goose/goose).
[^p4-prix-kilo]: [Tarifs Kilo, inférence, frais et calcul](https://kilo.ai/pricing).
[^p4-prix-amp]: [Tarifs Amp](https://ampcode.com/pricing).
[^p4-prix-vibe]: [Tarifs Mistral](https://mistral.ai/pricing/).
[^p4-prix-kiro]: [Tarifs Kiro](https://kiro.dev/pricing/).
[^p4-prix-openhands]: [Tarifs OpenHands](https://www.openhands.dev/pricing).

### Où faire tourner le modèle ?

Pour un service hébergé, votre ordinateur doit surtout faire tourner l’éditeur et le projet. Le fournisseur effectue les calculs du modèle. Vous avez besoin d’un accès au service et d’une connexion réseau, mais pas d’une grosse carte graphique.

En local, vous fournissez aussi la mémoire et le calcul. Cela permet de garder l’inférence sur votre machine et de travailler sans accès au fournisseur une fois les éléments nécessaires téléchargés. En échange, il faut choisir un modèle qui tient en mémoire et dont le temps de réponse vous convient.

| Situation | Point de départ possible |
| --- | --- |
| Petit ordinateur, priorité à une installation simple | Offre hébergée gratuite, si l’envoi du code est acceptable |
| Envoi du code exclu, aucune carte graphique dédiée | Essai local limité ; aucun parcours d’agent validé ici pour cette configuration |
| Machine disposant de davantage de mémoire et d’un GPU compatible | Tester un modèle local sur les tâches visées, puis mesurer le délai et vérifier le résultat |
| Assistant déjà fourni par votre équipe | Commencer avec cet outil, dans les conditions d’usage de l’équipe |
Table: Choisir selon ses contraintes

Notre SmolLM2 de la partie 3 nous a servi à comprendre l’inférence. Il ne faut pas attendre de lui qu’il explore un dépôt et corrige un ticket tout seul. Nous allons d’abord l’utiliser pour vérifier la connexion, puis proposer un petit modèle spécialisé dans le code.

Il faut distinguer deux choses : **le logiciel de l’agent peut tourner sur votre ordinateur pendant que son modèle tourne chez un fournisseur**. Dans ce cas, vous n’avez pas besoin d’une grosse carte graphique. Faire aussi tourner le modèle chez vous pose une autre question.

llama.cpp permet l’inférence sur CPU[^p4-cpu-moteur]. Mais charger un modèle et obtenir une réponse ne prouve pas qu’il sera utile pour développer. Un agent doit exploiter le code qu’il lit, choisir ses actions, comprendre les résultats des commandes et poursuivre la tâche. Le temps de traitement du contexte s’ajoute à celui des réponses, à chaque étape. Il faut vérifier tout cela sur une tâche réelle.

Notre essai avec Qwen2.5-Coder à 1,5 milliard de paramètres n’a pas été exécuté dans cette configuration. Nous ne savons donc pas encore s’il apporte une aide utile sur cet atelier, ni combien de temps il demande. Continue cite d’ailleurs un modèle Qwen Coder de cette taille pour la complétion, et d’autres modèles pour le travail d’agent[^p4-cpu-roles]. Ce sont des usages différents.

Si vous ne pouvez ni envoyer votre code à un service ni utiliser un modèle local adapté, vous pouvez faire les exercices Python vous-même. Vous apprendrez à reproduire le problème et à vérifier la correction ; l’utilisation d’un agent restera à expérimenter avec une configuration qui le permet.

Reste la question des données. Une API personnelle peut vous laisser choisir votre fournisseur, sans rendre l’inférence locale. Et une option « ne pas utiliser mes données pour l’entraînement » ne signifie pas que le code ne quitte jamais l’ordinateur : elle porte sur un usage des données après leur transmission.

Pour notre atelier, nous utiliserons des fichiers publics et un ticket fictif. Pour votre travail, il faudra savoir ce que votre équipe autorise à transmettre. Nous reviendrons plus largement sur ces choix ; ils comptent déjà au moment d’installer l’outil.

[^p4-cpu-moteur]: llama.cpp, [moteur d’inférence et plateformes prises en charge](https://github.com/ggml-org/llama.cpp).
[^p4-cpu-roles]: Continue, [configuration et modèles recommandés pour le mode Agent](https://docs.continue.dev/ide-extensions/agent/model-setup).



## 3. Installer notre premier assistant

**TL;DR** — Préparez une copie du projet, puis ouvrez votre assistant. Le parcours principal utilise Copilot avec un modèle hébergé. L’essai local avec Continue est facultatif et reste à vérifier : il explore la discussion sur un extrait, sans configurer un agent pour réaliser l’atelier.

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

Si l’interface vous demande de souscrire pour continuer, vérifiez le compte connecté, son éligibilité et le quota restant. Vous pouvez utiliser un autre assistant auquel vous avez accès, attendre le renouvellement du quota ou poursuivre les exercices Python vous-même. Les fichiers et les corrigés restent accessibles sans abonnement. L’essai CPU ci-dessous ne garantit pas de remplacer le service hébergé.

Une fois la discussion ouverte, passez à la section « Notre première demande de lecture ». L’installation locale ci-dessous est une expérience facultative.

[^p4-install-copilot]: Microsoft, [configuration de Copilot dans VS Code](https://code.visualstudio.com/docs/setup/copilot).
[^p4-install-roles]: Microsoft, [choix de l’agent, du rôle et du modèle](https://code.visualstudio.com/docs/agents/run/agent-harnesses).

### Relier l’éditeur à notre modèle local

Vous voulez essayer de discuter avec notre modèle depuis l’éditeur ? Nous allons conserver le serveur de la partie 3 et remplacer notre client Python par **Continue**. Cette expérience est facultative. Le raccord à Continue et l’essai du modèle de code ci-dessous restent à exécuter ; nous n’avons pas encore de résultat ni de temps de réponse à vous montrer.

###### Retrouver le serveur

Relancez `llama-server` avec la commande qui fonctionnait sur votre machine dans la partie précédente. Pour cette première connexion, conservez le port `8080`, l’adresse `127.0.0.1`, l’alias `atelier-local` et le contexte de `2048` tokens.

Ouvrez <http://127.0.0.1:8080/health> dans le navigateur. Lorsque le modèle est chargé, ce point d’accès doit indiquer que le serveur est prêt. Vous pouvez également ouvrir <http://127.0.0.1:8080/v1/models> pour retrouver le nom exposé par le serveur[^p4-install-server].

Si rien ne répond, regardez d’abord le terminal du serveur. Installer une extension ne réparera pas un modèle qui n’a pas fini de charger.

###### Ajouter Continue

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

La longueur de contexte correspond à celle de notre serveur. Nous limitons aussi la réponse à 128 tokens pour ce premier essai. Nous déclarons le rôle `chat`, puis nous sélectionnerons le mode **Chat** dans l’interface. Ce rôle de configuration ne constitue pas à lui seul une interdiction d’utiliser des outils[^p4-install-yaml].

Enregistrez, sélectionnez la configuration et le modèle locaux, puis choisissez le mode **Chat**. Envoyez une question très courte, par exemple :

> Reply with the word hello.

Ce n’est pas un test d’intelligence. Nous cherchons une réponse, même imparfaite, et une requête correspondante dans le terminal de `llama-server`. Si une erreur mentionne une clé de service distant, vérifiez le modèle sélectionné et `apiBase`.

Continue propose un réglage **Allow Anonymous Telemetry** dans les paramètres de l’extension : désactivez-le pour cet usage local[^p4-install-offline]. Les réglages réseau de VS Code et des autres extensions restent séparés. Pour vérifier que cette conversation n’a pas besoin d’Internet, vous pouvez couper la connexion après les téléchargements, ouvrir une nouvelle discussion et envoyer une autre question.

###### Passer à un modèle de code

La connexion fonctionne ? Nous pouvons changer ce que le serveur charge.

Pour un premier essai sur CPU, prenons **Qwen2.5-Coder-1.5B-Instruct**, dans sa version GGUF `Q4_K_M`. C’est un petit modèle destiné au code. Nous allons lui soumettre un extrait court pour examiner sa réponse ; sa fiche ne permet pas de conclure qu’il sera utile sur notre exercice[^p4-install-qwen].

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

###### Et pour les modifications ?

Avec un assistant disposant d’un mode agent, vous pourrez ensuite lui demander de préparer les changements, puis examiner le diff et les résultats des tests.

L’expérience locale s’arrête ici : une réponse sur une fonction ne valide pas la capacité du modèle à modifier le projet. Si vous voulez poursuivre en mode Chat, vous pourrez examiner ses propositions et les appliquer vous-même, mais nous n’avons pas vérifié que ce petit modèle saura suivre les demandes des chapitres suivants.

Les exercices Python peuvent aussi se faire sans IA. Les corrigés vous permettront de vérifier votre travail ; cela ne remplacera pas l’expérience de piloter un agent.

Gardez votre dossier `mon-suivi` : nous allons maintenant y lancer les tests et comprendre pourquoi un programme dont les tests passent peut tout de même avoir besoin d’une correction.

[^p4-install-chat]: Continue, [discussion et sélection de code](https://docs.continue.dev/ide-extensions/chat/quick-start).



## 4. Ouvrir un projet que l’on peut comprendre

**TL;DR :** nous allons lire le programme et vérifier son état de départ. Un agent peut nous aider à nous repérer, mais les fichiers restent notre point de contrôle.

### Lancer les tests du projet

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

Si vous lisez « Ran 0 tests », vous n’avez pas encore vérifié le projet. Regardez le dossier courant et la présence de `test_suivi.py`. Un lancement sans test trouvé peut se terminer sans erreur, ce qui rend la dernière ligne trompeuse si on la lit seule.[^p4-unittest]

[^p4-unittest]: Python, [découverte et exécution des tests avec `unittest`](https://docs.python.org/3.12/library/unittest.html).

### Suivre une entrée jusqu’à la décision

Ouvrez `scenarios/retour-stock.json`. Il décrit deux observations du même produit : un prix de 2 000 centimes avant et après, avec un passage d’indisponible à disponible.

Lancez :

```bash
python suivi.py scenarios/retour-stock.json
```

Le programme initial affiche :

```json
{"notifier": true}
```
Code: Décision du programme avant notre modification

Il n’envoie aucun courriel et ne contacte aucun service : il calcule une décision et l’affiche. Nous pouvons donc rejouer le scénario autant de fois que nécessaire.

Ouvrez maintenant `suivi.py` et suivez les appels. `main` charge le fichier JSON. `lire_etat` vérifie les champs de chaque observation et crée un `Etat`. La fonction `notifier` reçoit l’ancien et le nouvel état, puis renvoie un booléen. Enfin, `main` affiche ce résultat en JSON.

![Le fichier JSON est lu, transformé en deux états puis envoyé à la fonction de décision](images/projet.png)
Figure: Le parcours d’un scénario dans notre programme

Vous n’avez pas besoin de mémoriser tout le fichier. En revanche, vous devez pouvoir montrer la fonction qui décide et expliquer quelles données elle reçoit. Essayez de la retrouver une deuxième fois sans relire ce paragraphe.

### Demander de l’aide pour lire

Si vous utilisez un agent, ouvrez uniquement le dossier `mon-suivi` dans son espace de travail. Commencez par une demande de lecture :

```text
Lis README.md, suivi.py, test_suivi.py et TICKET.md.
Explique le chemin entre le fichier JSON et la décision.
Cite les fonctions concernées.
N’édite aucun fichier pendant cette lecture.
Signale les questions auxquelles les fichiers ne répondent pas.
```
Code: Une consigne pour se repérer dans le projet

Cette consigne peut être utilisée dans différents outils. La manière de choisir le dossier et d’autoriser une lecture dépend de votre application. Vérifiez ce périmètre dans son interface avant de lui demander d’agir.

Comparez ensuite son explication au code. S’il parle d’une file de messages, d’un appel réseau ou d’une base de données, cherchez où cela apparaît. Dans notre projet, aucun de ces éléments n’existe. Une explication plausible n’est pas une preuve de lecture.

Vous pouvez aussi lui demander d’expliquer une ligne précise, puis reformuler vous-même son rôle. C’est particulièrement utile quand on apprend un langage : on garde un passage court, dont on peut vérifier chaque détail.



## 5. Décider ce que le ticket veut changer

**TL;DR :** une phrase de ticket cache parfois plusieurs comportements. Nous allons les mettre à plat avant de toucher à la fonction.

### Une remise en stock n’est pas une baisse de prix

Le ticket PRIX-1 demande de ne plus notifier un produit qui revient simplement en stock. Le fichier `TICKET.md` donne la règle complète : une notification est autorisée seulement si le produit est disponible dans le nouvel état **et** si son prix a strictement baissé par rapport à l’observation précédente.

Les prix sont des entiers en centimes. Nous comparons deux observations consécutives, dans une même devise implicite. Il n’est pas question de retrouver le prix le plus bas des six derniers mois ni de calculer une promotion.

Avant de regarder la suite, répondez à ces deux cas :

- Le produit revient en stock au même prix. Faut-il notifier ?
- Le produit revient en stock avec un prix plus bas. Faut-il notifier ?

Le premier cas doit donner **faux**, le second **vrai**. « Ne plus notifier une remise en stock » ne veut donc pas dire « ignorer tous les produits qui étaient indisponibles ». Une baisse de prix peut accompagner le retour en stock.

C’est exactement le genre de raccourci qu’il faut éclaircir dans un vrai ticket. Si personne n’a décidé comment traiter le second cas, l’agent ne devrait pas choisir discrètement à la place de l’équipe.

### Écrire la table avant les tests

Voici les cas que nous voulons distinguer :

| Ancien état | Nouvel état | Notification attendue |
| --- | --- | --- |
| 20 €, disponible | 15 €, disponible | Oui |
| 15 €, disponible | 20 €, disponible | Non |
| 20 €, disponible | 15 €, indisponible | Non |
| 20 €, indisponible | 20 €, disponible | Non |
| 20 €, indisponible | 15 €, disponible | Oui |
| 20 €, indisponible | 25 €, disponible | Non |
| 20 €, disponible | 20 €, disponible | Non |
Table: Les situations que la règle doit départager

Les trois premières correspondent déjà à nos tests de départ. Les suivantes rendent visible ce que ces tests ne contrôlaient pas.

Vous pouvez demander à l’agent de proposer cette table avant de coder les tests. Relisez alors les **résultats attendus**, pas seulement le nombre de lignes. Une longue suite de tests qui attend la mauvaise réponse reste une longue suite de tests qui attend la mauvaise réponse.

Pour une règle aussi petite, faire la table soi-même prend peu de temps. Dans un projet plus grand, l’aide peut surtout servir à retrouver les cas oubliés ou à traduire une règle déjà décidée en scénarios exécutables.

### Délimiter le changement

Ajoutons quelques limites simples à notre travail : nous conservons la fonction `notifier`, les fichiers JSON et les validations existantes. Nous n’ajoutons pas de base, d’envoi de courriel ou de système de préférences.

Pourquoi le préciser ? Parce qu’une demande d’« amélioration des notifications » pourrait facilement produire une architecture plus ambitieuse que notre besoin. Ici, le programme doit continuer à prendre deux états et à renvoyer une décision.

Les limites ne sont pas seulement des interdictions à adresser à l’agent. Elles nous servent aussi pendant la revue. Si un nouveau fichier de configuration apparaît, nous pourrons demander quel comportement du ticket le rend nécessaire.

Dans votre propre travail, gardez ce périmètre à la taille de la tâche. Un correctif d’une condition n’exige pas automatiquement un document de conception de dix pages. Il exige en revanche que les cas ambigus aient une réponse.



## 6. Faire apparaître le bug dans un test

**TL;DR :** nous ajoutons d’abord le cas oublié. Son échec nous permet de vérifier que le test distingue bien l’ancien comportement du comportement demandé.

### Écrire le premier test qui échoue

Dans `mon-suivi`, créez `test_ticket.py` :

```python
import unittest
from suivi import Etat, notifier


class TicketPrix(unittest.TestCase):
    def test_retour_en_stock_sans_baisse(self):
        self.assertFalse(
            notifier(Etat(2000, False), Etat(2000, True))
        )
```
Code: Reproduire le cas du ticket dans un test

Lancez de nouveau :

```bash
python -m unittest discover -v
```

Cette fois, vous devez obtenir **quatre tests, dont un en échec**. Le programme renvoie vrai, alors que ce cas attend faux. Nous n’avons pas cassé le projet en ajoutant un test : nous avons rendu visible le désaccord avec la nouvelle règle.

Lisez le nom du test en échec. Une erreur d’import ou une faute de syntaxe ne prouvent pas que le comportement du ticket est reproduit. Le programme doit atteindre l’assertion, puis échouer parce que sa décision ne correspond pas à celle attendue.

Si votre test passe déjà, vérifiez que vous travaillez bien dans la copie de `01-depart` et que la fonction n’a pas été corrigée par avance. Il serait dommage de conclure à une démonstration du bug sans avoir exécuté le code qui le contient.

### Ajouter les voisins du cas principal

Le cas principal est maintenant couvert. Ajoutez les autres situations de la table, notamment le retour en stock avec baisse et celui avec hausse. Pour une baisse accompagnant le retour, l’assertion doit être `assertTrue`.

Le dossier `02-test-rouge` contient une version complète de `test_ticket.py`. Vous pouvez comparer votre fichier au sien ou le recopier après avoir essayé. Il ajoute aussi les limites suivantes : une baisse d’un centime, un prix nul et des données invalides.

Avec ce fichier complet, la suite contient **treize tests**. Avant correction, **deux échouent** : le retour en stock sans baisse et le retour en stock avec hausse. Le reste passe.

![Trois états réellement exécutés : trois tests verts, puis deux échecs sur treize, puis treize tests verts](images/tests.png)
Figure: Les résultats des trois versions fournies dans l’atelier

Les tests de données invalides vérifient notamment qu’un prix négatif, un prix décimal, un booléen utilisé comme prix et une disponibilité écrite sous forme de texte sont refusés. Ils protègent un comportement existant ; ils ne décrivent pas de nouvelles fonctionnalités du ticket.

Lisez le test sur le booléen comme prix avec la validation dans `Etat`. En Python, les booléens sont un cas particulier des entiers. Le contrôle `type(...) is int` utilisé ici exclut délibérément `True`, alors qu’un simple `isinstance(..., int)` l’accepterait.[^p4-bool]

[^p4-bool]: Python, [type booléen et relation avec les entiers](https://docs.python.org/3.12/library/stdtypes.html#boolean-type-bool).

### Faire écrire les tests par l’agent

Si vous voulez lui confier cette étape, repartez de la copie initiale et donnez-lui cette consigne :

```text
À partir de TICKET.md, propose une table de cas puis écris
les tests manquants dans test_ticket.py.
Ne modifie pas suivi.py.
Lance python -m unittest discover -v.
Rapporte les noms des tests en échec et la différence
entre la valeur attendue et la valeur obtenue.
```

La séparation entre les tests et la correction nous permet d’observer le comportement initial. Vérifiez le diff après son intervention : s’il a modifié `suivi.py` en même temps, l’expérience ne montre plus aussi clairement que les nouveaux tests attrapent l’ancien comportement.

Regardez également si ses tests appellent vraiment `notifier`. Un test qui compare deux constantes ou reproduit sa propre version de la condition peut passer sans contrôler notre fonction.

Enfin, les tests sont du code exécuté sur votre ordinateur. Dans cet atelier, ils utilisent seulement nos petites fonctions. Dans un dépôt inconnu, regardez leurs imports, leurs préparatifs et les commandes proposées avant de les lancer. Le mot « test » ne garantit pas à lui seul l’absence d’écriture ou d’appel réseau.



## 7. Faire le changement et lire le diff

**TL;DR :** la règle attendue tient dans deux conditions. Nous allons enlever celle qui autorisait une notification pour une simple remise en stock.

### Relire les opérateurs

Voici la fonction initiale :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
    )
```

Lisez-la à voix haute : le produit doit être disponible maintenant, et il faut soit une baisse de prix, soit une ancienne indisponibilité.

Le second terme du `or` explique notre problème. Pour un retour en stock, `not ancien.disponible` vaut vrai. Le prix peut être identique ou même plus élevé : l’expression entre parenthèses sera tout de même vraie.

Notre ticket exige uniquement une disponibilité actuelle et une baisse stricte. La correction devient :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes
    )
```
Code: La fonction après correction

Nous conservons les parenthèses et la présentation afin que le diff porte sur le changement de comportement. Il serait possible d’écrire cette expression sur une ligne, mais cela n’est pas nécessaire pour résoudre le ticket.

N’ajoutez pas `ancien.disponible` dans la nouvelle condition. Cela empêcherait de notifier une vraie baisse au moment du retour en stock, contrairement à la règle décidée.

![Seul le cas disponible maintenant avec baisse de prix autorise une notification](images/decision.png)
Figure: La règle complète tient dans ces quatre combinaisons

### Une demande de modification précise

Pour demander cette correction à l’agent, vous pouvez utiliser :

```text
Applique le comportement décrit dans TICKET.md.
Conserve les interfaces existantes et limite la modification
au code nécessaire.
Ne change pas les réponses attendues des tests pour les faire passer.
Lance la suite avec python -m unittest discover -v.
Montre le diff et explique la condition modifiée.
Ne crée pas de commit et ne publie rien.
```
Code: Confier la correction en gardant un résultat relisible

Les verbes disent ce qui doit être fait. « Ce serait bien de vérifier les tests » laisse une intention vague ; « lance cette commande et rapporte son résultat » donne une action et une preuve à chercher.

Cela reste une consigne au modèle. Pour limiter effectivement son accès aux fichiers, au réseau ou à la publication, utilisez aussi les permissions de votre outil. Une phrase dans un prompt n’a pas le même rôle qu’un droit technique refusant l’opération.

Si l’agent propose une classe de notification, une nouvelle dépendance ou un système de règles pour cette fonction, demandez-lui quel cas du ticket le justifie. Vous pouvez rejeter ces ajouts et demander une modification plus petite. Vous n’êtes pas obligé de conserver du code parce qu’il a déjà été généré.

### Lire ce qui a vraiment changé

Un résumé de l’agent raconte ce qu’il pense avoir fait. Le diff montre les fichiers modifiés. Ouvrez celui de votre éditeur, puis cherchez le changement dans `suivi.py`.

La correction fournie retire ce morceau :

```diff
-        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
+        nouveau.prix_centimes < ancien.prix_centimes
```
Code: Le changement de comportement dans la fonction

Si Git est installé, vous pouvez aussi comparer les deux dossiers depuis leur dossier parent :

```bash
git diff --no-index 01-depart/suivi.py mon-suivi/suivi.py
```

Cette commande fonctionne sans créer de dépôt Git. Avec `--no-index`, un code de sortie égal à 1 signifie que les fichiers diffèrent ; ce n’est pas forcément un échec de la comparaison.[^p4-diff]

Regardez ensuite les autres fichiers modifiés. Les nouveaux tests sont attendus. Une modification des données d’entrée pour éviter le bug, une suppression de validation ou une réécriture de tout le programme demandent une explication.

Si vous débutez, choisissez une ligne retirée et une ligne conservée, puis expliquez leur rôle sans recopier le résumé de l’agent. Si vous n’y arrivez pas encore, revenez à la fonction. Le résultat est assez petit pour que cette lecture reste abordable.

[^p4-diff]: Git, [comparaison de fichiers avec `git diff --no-index`](https://git-scm.com/docs/git-diff).



## 8. Vérifier au-delà de la dernière ligne verte

**TL;DR :** la suite teste la fonction ; les scénarios font aussi passer les données par le chargement JSON. Nous allons examiner les deux.

### Rejouer les tests et contrôler leur nombre

Après correction, lancez :

```bash
python -m unittest discover -v
```

Avec le fichier complet de `02-test-rouge`, les **treize tests passent**. Si vous avez seulement écrit le premier nouveau test, vous en aurez quatre : ce n’est pas la même couverture, même si la dernière ligne est également `OK`.

Les noms des tests vous permettent de voir les situations réellement contrôlées. Regardez en particulier les deux qui échouaient avant la correction. Ils doivent toujours être présents et conserver leurs valeurs attendues.

Dans un rapport d’agent, cherchez la commande, son dossier d’exécution et son résultat. « Tests vérifiés » peut cacher plusieurs choses : une lecture du code des tests, une exécution partielle, ou une suite complète. Nous voulons savoir laquelle a eu lieu.

Si une dépendance manque ou qu’une commande échoue, le rapport doit le dire. Réussir à écrire les tests n’est pas la même chose que réussir à les exécuter.

### Passer par les fichiers JSON

Exécutez maintenant nos trois scénarios :

```bash
python suivi.py scenarios/retour-stock.json
python suivi.py scenarios/baisse.json
python suivi.py scenarios/rupture.json
```

Voici les décisions attendues après correction :

| Fichier | Résultat |
| --- | --- |
| `retour-stock.json` | `{"notifier": false}` |
| `baisse.json` | `{"notifier": true}` |
| `rupture.json` | `{"notifier": false}` |
Table: Les trois scénarios de recette

Nous passons cette fois par la lecture du fichier, la construction des états, la décision et l’affichage. Les tests précédents appelaient surtout les fonctions directement. Les deux vérifications se complètent.

Créez ensuite une copie de `retour-stock.json`, nommée `retour-stock-baisse.json`, et changez seulement le nouveau prix : 1 500 au lieu de 2 000. Lancez ce nouveau scénario. Le résultat doit être vrai.

Ne modifiez pas les scénarios pour les faire coïncider avec une réponse inattendue. Si un cas ne produit pas ce que la règle prévoit, conservez le fichier qui le reproduit. C’est une meilleure base de discussion qu’une capture sans ses données d’entrée.

### Vérifier qu’un test sait encore protester

Faisons une petite expérience, dans une **copie du projet corrigé**. Remplacez `<` par `<=` dans `notifier`, puis relancez la suite.

Le prix identique autorise maintenant une notification. Les tests qui attendent l’absence de notification à prix inchangé doivent échouer. S’ils ne le font pas, vérifiez que vous avez exécuté la bonne copie et que ces cas sont présents.

Rétablissez ensuite `<`, puis retirez temporairement la condition `nouveau.disponible and`. Le test de baisse sur un produit indisponible doit cette fois protester.

Ces modifications volontaires sont de petites **mutations** : nous introduisons une erreur précise pour voir si les tests la remarquent. Cela ne prouve pas qu’ils détecteront tous les bugs. Cela permet de vérifier que les cas importants ne sont pas seulement décoratifs.

Revenez enfin à la version corrigée et relancez la suite. Ne gardez pas une mutation dans votre copie de travail ; le but est de tester nos tests, pas de préparer discrètement le prochain ticket. 🙂

### Demander une seconde lecture utile

Vous pouvez maintenant faire relire le diff par un agent, en lui donnant aussi le ticket et les cas attendus :

```text
Relis le diff par rapport à TICKET.md et aux scénarios.
Pour chaque problème trouvé, donne un cas reproductible,
le comportement obtenu et celui attendu.
Ne modifie pas les fichiers pendant cette revue.
Si tu ne trouves pas de problème, indique ce que tu as vérifié
et les limites de cette vérification.
```

Cette demande évite de réduire la revue à des préférences de style. Une remarque devient plus utile lorsqu’on peut lancer le scénario qui la justifie.

Le second passage peut tout de même manquer la même erreur que le premier. Changer de session ou de modèle n’en fait pas une preuve indépendante au sens fort : les outils peuvent partager des habitudes et des angles morts. Appuyez-vous sur les scénarios, le code et les sorties observées.

Pour notre petit changement, une revue efficace peut être courte. Il n’y a aucune raison d’inventer trois problèmes pour remplir une section de rapport.



## 9. Garder un changement que l’on sait expliquer

**TL;DR :** préparez une trace courte du problème, de la correction et des vérifications. Puis choisissez où l’aide vous a réellement été utile.

### Écrire un compte rendu exploitable

Créez un fichier `COMPTE-RENDU.md` et renseignez-le avec votre propre exécution :

```markdown
# PRIX-1 — Ne plus notifier une simple remise en stock

## Problème

Le retour en stock autorisait une notification même sans baisse de prix.

## Changement

La décision exige une disponibilité actuelle et une baisse stricte.
Les interfaces et les validations des entrées sont conservées.

## Vérifications effectuées

- Commande de tests, dossier d’exécution, nombre de tests et résultat :
- Scénario retour en stock, résultat observé :
- Scénario baisse de prix, résultat observé :
- Scénario indisponible, résultat observé :

## Limites

Le programme calcule une décision. Il n’envoie pas de notification.
Il compare deux observations dans une même devise implicite.
```
Code: Une trame à compléter avec vos résultats

Les cases laissées vides ne doivent pas être remplies par une supposition. Si vous n’avez pas exécuté un scénario, écrivez-le ou lancez-le.

Ce texte peut ensuite servir de base à une description de pull request dans un vrai projet. Avant de publier, relisez les fichiers et les traces jointes : un rapport de test peut lui aussi contenir des données qu’on ne souhaite pas diffuser.

L’agent peut rédiger ce compte rendu à partir des sorties conservées. Vous gardez à vérifier que les phrases correspondent aux commandes effectivement réalisées.

### Quand on apprend encore à développer

Si vous découvrez Python, vous avez peut-être eu envie de demander directement la version finale. Vous l’auriez obtenue plus vite. Mais pourriez-vous maintenant expliquer pourquoi le `or` posait problème ?

Fermez la correction et essayez de prédire le résultat de deux cas : un retour en stock avec hausse, puis une baisse d’un centime sur un produit disponible. Vérifiez vos réponses en exécutant le programme.

Si vous vous trompez, ce n’est pas une raison de renoncer à l’aide. Demandez une explication de l’expression booléenne, construisez une table de valeurs ou réduisez l’exemple à deux booléens. Vous pouvez vous servir du modèle pour trouver une autre explication sans lui confier immédiatement toute la modification.

Pour apprendre, une bonne utilisation consiste souvent à demander un indice, un contre-exemple ou une question de vérification. Une solution complète trop tôt peut vous faire sauter exactement l’effort dont vous aviez besoin pour comprendre.

Et certains jours, le plus efficace sera de fermer l’agent et de lire la fonction tranquillement. Il n’y a rien à rentabiliser à chaque ligne.

### Trouver ses propres points de friction

Reprenez les étapes de cet atelier et demandez-vous lesquelles vous ont posé problème. Comprendre la règle ? Retrouver la fonction ? Penser aux cas limites ? Écrire la syntaxe de `unittest` ? Relire le diff ?

L’aide n’a pas le même intérêt partout. Si vous aimez écrire le code mais que préparer une recette vous prend un temps fou, vous pouvez garder le code et demander une première liste de scénarios. Si vous connaissez bien les tests mais découvrez un langage, une explication ciblée peut être plus utile qu’une implémentation complète.

Pour comparer deux façons de travailler, notez le temps total, y compris les corrections de demandes, la lecture des résultats et la validation. Le temps pendant lequel l’agent produit du texte n’est qu’une partie du travail.

N’ajoutez pas automatiquement un framework ou une série de commandes pour reproduire cet atelier. Nous avons séparé des étapes afin de voir ce qu’elles vérifient. Dans votre quotidien, regroupez ou simplifiez ce qui peut l’être, tout en conservant les contrôles nécessaires au changement.

Vous pouvez aussi conclure que l’outil ne vous aide pas sur ce type de tâche. Adapter un outil à son besoin comprend cette possibilité.



## Conclusion

La correction de notre fonction tient en peu de caractères. Le travail ne se résume pourtant pas à ces caractères : il a fallu comprendre la demande, trouver le comportement existant, choisir les cas et vérifier le résultat.

Un agent peut aider à plusieurs de ces étapes. Il peut aussi vous faire perdre du temps en élargissant le sujet, en ajoutant du code inutile ou en produisant des vérifications qui ne vérifient pas la bonne chose. Vous avez maintenant un petit projet sur lequel observer ces différences sans mettre une application réelle en jeu.

Gardez ce qui vous sert. Si vous préférez écrire vous-même la correction et demander de l’aide uniquement pour les cas de test, faites-le. Si tout l’exercice vous semble plus simple à réaliser sans IA, faites-le aussi. Votre manière de travailler n’a pas à devenir plus compliquée pour justifier l’usage d’un outil.
