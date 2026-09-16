# Annexes

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Revenez au comparatif pour choisir ou changer d’assistant. L’expérience locale, elle, relie un éditeur au serveur de la partie 3. Ces deux annexes restent facultatives et se consultent selon vos besoins.

## Annexe A. Comparer les outils et leurs tarifs

**TL;DR** — Cette référence compare les interfaces, les possibilités et les coûts des outils. Vous pouvez y revenir pour changer d’assistant sans recommencer l’atelier.

Le relevé est une photographie de septembre 2026. Un éditeur, un harness et un abonnement à un modèle couvrent des besoins et des dépenses différents. Pour les comparer, partez des tâches que vous voulez réaliser dans votre projet.

### Les éditeurs et les agents

Commençons par les outils que vous pouvez rencontrer dans un éditeur, un terminal ou un service distant. Le tableau donne une carte de départ pour l’atelier ; la section suivante l’élargira aux harness extensibles, dont Pi. Les produits y sont regroupés par porte d’entrée et par usage, sans classement des modèles.

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

Pour commencer l’atelier, revenez au chapitre « Installer l’assistant et observer le problème ». L’expérience Continue avec notre serveur local se trouve dans l’annexe suivante.

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

Avec le même modèle, deux agents peuvent donc se comporter différemment : chacun prépare son contexte, choisit les outils disponibles et organise la boucle à sa manière.

###### Pi, et les autres possibilités à connaître

**Pi** mérite qu’on s’y arrête. Il propose un agent en terminal que l’on peut étendre et intégrer à ses propres outils. Sa conception laisse une grande place aux extensions et aux modèles de consignes, plutôt que de fournir par défaut toutes les étapes d’une méthode de développement. Il dispose aussi d’interfaces permettant de le piloter depuis un programme[^p4-h-pi].

Pi illustre une question qui nous suivra dans le tutoriel : jusqu’où pouvons-nous adapter l’outil à notre manière de travailler ?

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

Cette liberté demande de prévoir les protections adaptées. Le dépôt de Pi précise que le programme s’exécute avec les droits du processus qui le lance, sans système intégré de restriction des accès aux fichiers, aux processus ou au réseau. Une isolation supplémentaire relève de l’environnement dans lequel on l’exécute[^p4-h-pi-droits]. C’est une différence concrète à connaître lorsqu’on compare deux harness.

###### Les noms que vous trouverez dans d’anciens comparatifs

**Roo Code** a sa place dans l’histoire de ces outils, mais son dépôt officiel est archivé depuis le **15 mai 2026**. Les anciennes procédures qui l’utilisent demandent donc une attention particulière[^p4-h-roo].

**Gemini CLI** mérite aussi d’être nommé explicitement. Le changement annoncé par Google concerne notamment les parcours gratuits et les abonnements individuels transférés vers Antigravity ; les usages professionnels et les autres modalités d’accès suivent leurs propres conditions[^p4-h-gemini].

Les noms, les offres et parfois les dépôts changent. Ce comparatif photographie leur état en septembre 2026. Les étoiles GitHub peuvent aider à repérer un projet connu ; pour choisir, il faudra surtout essayer sa manière de travailler sur les tâches de votre équipe.

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

### Les prix et les limites des offres

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

« Gratuit » peut donc désigner deux choses : un service qui vous accorde un petit quota, ou un logiciel que vous installez sans payer, mais auquel il faut fournir un modèle. Avec une API payante, le logiciel reste gratuit tandis que chaque réponse peut être facturée.

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



## Annexe B. Expérimenter une discussion avec un modèle local

**TL;DR** — Expérience facultative : relier Continue au serveur de la partie 3, puis examiner la réponse d’un petit modèle de code. Cette configuration reste à exécuter et à mesurer. Le parcours s’arrête à une courte discussion ; les capacités d’un agent de code sur CPU restent à établir.

### Relier Continue à notre serveur

Vous voulez essayer de discuter avec notre modèle depuis l’éditeur ? Nous allons conserver le serveur de la partie 3 et remplacer notre client Python par **Continue**. Gardez sous la main la commande de lancement du serveur qui fonctionnait en partie 3.

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

Ici, `provider: openai` indique le format d’API utilisé. **La destination est l’adresse de `apiBase`**, donc notre ordinateur. La valeur `local` remplit le champ de clé attendu par l’extension ; notre serveur d’atelier ne vérifie aucune clé et aucun compte OpenAI n’intervient[^p4-install-compatible].

La longueur de contexte correspond à celle de notre serveur. Nous limitons aussi la réponse à 128 tokens pour ce premier essai. Nous déclarons le rôle `chat`, puis nous sélectionnerons le mode **Chat** dans l’interface. Les permissions d’outils se règlent ailleurs ; ce rôle décrit seulement l’usage prévu du modèle[^p4-install-yaml].

Enregistrez, sélectionnez la configuration et le modèle locaux, puis choisissez le mode **Chat**. Envoyez une question très courte, par exemple :

> Reply with the word hello.

Ici, nous vérifions simplement la connexion. Cherchez une réponse, même imparfaite, et la requête correspondante dans le terminal de `llama-server`. Si une erreur mentionne une clé de service distant, vérifiez le modèle sélectionné et `apiBase`.

Continue propose un réglage **Allow Anonymous Telemetry** dans les paramètres de l’extension : désactivez-le pour cet usage local[^p4-install-offline]. Les réglages réseau de VS Code et des autres extensions restent séparés. Pour vérifier que cette conversation n’a pas besoin d’Internet, vous pouvez couper la connexion après les téléchargements, ouvrir une nouvelle discussion et envoyer une autre question.

###### Passer à un modèle de code

La connexion fonctionne ? Nous pouvons changer ce que le serveur charge.

Pour un premier essai sur CPU, prenons **Qwen2.5-Coder-1.5B-Instruct**, dans sa version GGUF `Q4_K_M`. C’est un petit modèle destiné au code. Sa fiche décrit ses usages prévus ; notre extrait court nous montrera ce qu’il produit ici, sur notre machine[^p4-install-qwen].

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

Ouvrez une nouvelle conversation après le changement de modèle. Copiez la définition de `Etat` et la fonction `notifier` depuis **la version initiale** `01-depart/suivi.py`. Posez la même question que dans le chapitre de lecture : pour `Etat(2000, False)` puis `Etat(2000, True)`, quelles valeurs prennent les conditions et que renvoie la fonction ?

Chronométrez le temps avant le début de la réponse et sa durée totale. Conservez le texte obtenu, puis vérifiez-le contre le code : le résultat initial est vrai. Une réponse rapide mais fausse ne nous aide pas davantage qu’une réponse juste qui arrive trop tard pour notre usage.

Si la réponse est lente, commencez par raccourcir la demande et la sortie attendue. Si la machine manque de mémoire, revenez au contexte précédent ou au petit modèle pour finir le diagnostic de connexion. Vous pouvez aussi poursuivre l’atelier à la main, plutôt que de laisser un modèle en difficulté multiplier les tentatives.

[^p4-install-server]: llama.cpp, [documentation du serveur et des points d’accès HTTP](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).
[^p4-install-continue]: Continue, [installation de l’extension](https://docs.continue.dev/ide-extensions/install).
[^p4-install-config]: Continue, [configuration locale](https://docs.continue.dev/customize/deep-dives/configuration).
[^p4-install-compatible]: Continue, [serveurs compatibles avec l’API OpenAI](https://docs.continue.dev/customize/model-providers/top-level/openai).
[^p4-install-yaml]: Continue, [référence du fichier YAML](https://docs.continue.dev/reference).
[^p4-install-offline]: Continue, [fonctionnement sans Internet](https://docs.continue.dev/guides/running-continue-without-internet).
[^p4-install-qwen]: Qwen, [Qwen2.5-Coder-1.5B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF).
[^p4-install-qwen-fichier]: Qwen, [fichiers GGUF proposés](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/tree/main).

Une connexion réussie montre que l’éditeur peut parler au serveur. Pour savoir si cette installation vous aide à développer, examinez ensuite ses réponses et ses délais sur vos propres tâches. Cette expérience s’arrête à la discussion avec un petit modèle ; elle ne valide aucun parcours d’agent sur CPU.

## Conclusion


