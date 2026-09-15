# 2. Choisir une solution adaptée à ses besoins

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR** — Un abonnement, un logiciel gratuit et une API à l’usage ne se comparent pas avec le seul prix affiché. Regardez ce qui est inclus, ce qui déclenche une dépense supplémentaire et où part votre code. Sans carte graphique dédiée, un modèle hébergé permet de commencer. L’essai avec un petit modèle local sert à explorer ses possibilités, sans présumer qu’il saura mener l’atelier.

Nous avons les noms. Maintenant, lequel installer ? Votre budget compte, mais votre façon de travailler aussi. Un outil qui vous oblige à changer d’éditeur, envoie du code que vous ne pouvez pas transmettre ou vous fait attendre trop longtemps peut être mal adapté, même s’il produit de bonnes réponses.

## Combien cela coûte-t-il ?

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

##### Prix des autres harness et environnements

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

## Où faire tourner le modèle ?

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


