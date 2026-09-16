# Étendre le tutoriel au travail hors développement

## Recommandation

Ajouter une partie d’application consacrée au travail documentaire et aux pipelines, après les agents, MCP et skills, puis avant l’IA maison et la partie sur les choix d’usage. Les notions techniques seraient ainsi apprises une fois, puis appliquées à deux familles de tâches : le développement et le travail de bureau.

Cette insertion demanderait de renuméroter les deux dernières parties. Elle vaut mieux qu’un chapitre isolé en annexe : l’objectif est d’élargir réellement le public, pas d’ajouter un catalogue de produits à la fin du parcours.

Avant ce chantier, quelques raccords courts pourraient déjà annoncer que les boucles d’agent, les permissions, MCP et les skills servent aussi à travailler sur des documents, des tableaux ou une veille. La réécriture actuelle n’effectue pas ce changement de structure.

## Fil rouge proposé

Chaque semaine, une petite équipe reçoit :

- quelques demandes fictives par courriel ;
- un tableur de suivi ;
- des notes de réunion ;
- une procédure qui indique ce qui peut être traité automatiquement et ce qui demande une décision.

Le lecteur construit un parcours qui rassemble les entrées, extrait des faits dans un format défini, repère les informations manquantes, prépare un compte rendu et demande une validation avant toute action extérieure. Le résultat reste vérifiable sans compte d’entreprise ni données personnelles.

Ce cas permet de montrer une automatisation utile et imparfaite. Une date absente doit rester absente ; un montant trouvé dans une pièce jointe doit garder sa provenance ; un brouillon peut être préparé automatiquement, tandis que l’envoi reste soumis à une personne.

## Découpage possible

1. **Définir le travail avant de l’automatiser** — Entrées, livrable attendu, règles stables et cas qui demandent une décision.
2. **Produire un document à partir de plusieurs sources** — Notes, tableur et pièces jointes ; citations et informations manquantes.
3. **Passer de la conversation au pipeline** — Déclencheur, étapes déterministes, appel de modèle, branche d’erreur et reprise.
4. **Relier les outils avec des permissions limitées** — Fichiers, messagerie, tableur, MCP ou intégrations ; lecture séparée de l’écriture.
5. **Placer la validation humaine au bon endroit** — Préparer un brouillon, approuver un changement, refuser un envoi et conserver la décision.
6. **Planifier, observer et corriger** — Exécutions récurrentes, journaux, coût, doublons, changements de format et reprise après erreur.
7. **Comparer les voies possibles** — Espace de travail agentique, orchestrateur visuel, script local ou absence d’IA ; choisir selon la tâche.

Chaque chapitre peut partir d’un incident visible : une colonne mal interprétée, une information inventée, deux courriels traités deux fois ou un envoi bloqué faute d’approbation. Les concepts arrivent alors pour résoudre un problème rencontré, dans l’esprit pédagogique déjà retenu pour le tutoriel.

## Produits et indépendance

Le cours devrait parler d’abord de catégories :

- espaces de travail agentiques capables de produire des documents, tableaux et présentations ;
- orchestrateurs de workflows, visuels ou programmables ;
- intégrations directes, MCP et skills ;
- automatisations planifiées ;
- validations humaines et journaux d’exécution.

Les produits servent ensuite d’exemples datés. Au 16 septembre 2026, la documentation officielle présente notamment ChatGPT Work pour transformer un objectif, des fichiers et du contexte en livrables ; Anthropic indique que Claude Cowork est en cours d’intégration dans Claude ; Microsoft propose Copilot Cowork ; n8n représente la famille des orchestrateurs visuels et permet de placer une approbation humaine devant certains appels d’outils.

Sources consultées :

- OpenAI, [ChatGPT Work](https://learn.chatgpt.com/), consulté le 16 septembre 2026 ;
- Anthropic, [Claude Cowork](https://claude.com/product/cowork), consulté le 16 septembre 2026 ;
- Microsoft, [Copilot Cowork](https://www.microsoft.com/en-us/copilot/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/), consulté le 16 septembre 2026 ;
- n8n, [validation humaine des appels d’outils](https://docs.n8n.io/changelog#human-in-the-loop-for-ai-tool-calls), consulté le 16 septembre 2026.

Les interfaces et les noms changent vite. Une annexe datée peut comparer ChatGPT Work, Claude, Microsoft 365 Copilot, n8n et d’autres solutions. Les chapitres principaux doivent rester valables lorsque l’un de ces écrans change.

## Atelier reproductible

Préparer un petit dossier de données entièrement fictives, avec :

- cinq courriels en texte brut, dont un doublon et une demande incomplète ;
- un tableur de suivi contenant une ligne déjà traitée ;
- deux comptes rendus qui se contredisent sur une date ;
- une procédure courte avec les règles d’approbation ;
- un résultat attendu et plusieurs erreurs volontaires.

Le parcours de référence doit pouvoir s’exécuter sans envoyer de courriel réel. L’action finale écrit un brouillon dans un dossier de sortie. Une variante connectée peut montrer l’envoi ou la mise à jour d’un outil, avec un compte de démonstration et une approbation explicite.

Il faudra conserver les entrées, sorties et journaux, puis vérifier au minimum : provenance des faits, absence d’invention pour les champs manquants, gestion du doublon, arrêt devant la contradiction et absence d’action extérieure avant validation.

## Points à trancher avec Hugo

- Accepter ou non le renumérotage des parties 7 et 8 pour insérer ce parcours après MCP et skills.
- Choisir le métier du fil rouge : suivi d’association, préparation d’un point d’équipe, traitement de demandes clients ou autre contexte que Hugo connaît assez pour en assumer les détails.
- Choisir l’outil concret de l’atelier. n8n offre une voie visuelle et auto-hébergeable ; un espace de travail agentique simplifie le premier essai, mais lie davantage les captures et la procédure à un fournisseur.
- Décider si l’atelier montre une vraie intégration à une messagerie de test ou reste entièrement local dans sa première version.
