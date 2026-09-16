Vous croiserez souvent le mot **harness** dans les discussions sur les agents. Il désigne le programme qui organise leur fonctionnement : préparer le contexte, appeler le modèle, exécuter ses demandes d’outils et poursuivre la conversation avec les résultats.

Dans notre premier client Python, nous envoyions une question et recevions du texte. Un harness peut ajouter la boucle suivante : le modèle demande à lire un fichier, le programme le lit et lui renvoie le contenu, puis le modèle choisit la prochaine action. La gestion des sessions, des permissions et des modifications appartient aussi à cet entourage logiciel.

Avec le même modèle, deux agents peuvent donc se comporter différemment : chacun prépare son contexte, choisit les outils disponibles et organise la boucle à sa manière.

### Pi, et les autres possibilités à connaître

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

### Les noms que vous trouverez dans d’anciens comparatifs

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
