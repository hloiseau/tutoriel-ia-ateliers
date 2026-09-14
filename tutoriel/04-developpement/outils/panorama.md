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
