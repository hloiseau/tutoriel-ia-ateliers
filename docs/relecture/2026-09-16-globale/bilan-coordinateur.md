# Bilan de la réécriture globale

Session : `2026-09-16-globale`  
Commit de départ : `102e5ccf29bff571da46bcdae0a51a5b1d089f95`  
Branche : `relecture-globale-2026-09-16`

## Résultat

Huit missions distinctes ont réécrit les huit parties dans leurs sources canoniques. Le coordinateur a relu l’introduction générale, repris les annexes, harmonisé les raccords et intégré deux passes adverses sur les transitions.

La structure reste inchangée : huit parties, 56 chapitres, deux annexes, 196 sections et 46 illustrations. Les choix déjà validés, les données d’expérience, les commandes et les opinions de l’auteur sont conservés. La conclusion de la partie 8 ferme toujours le parcours ; `tutoriel/conclusion.md` reste vide.

La passe porte principalement sur :

- les oppositions rhétoriques répétées, remplacées par une action, une observation ou une formulation directe ;
- les transitions automatiques, désormais rattachées au problème qui motive l’étape suivante ;
- le statut des preuves : banc sans modèle, serveur MCP, appel réel, résultat CPU et protocole GPU restent distincts ;
- les manipulations : dossiers, fichiers, état de départ et résultats à regarder sont nommés plus clairement ;
- la continuité du fil rouge entre développement, agents, MCP, skills, recherche documentaire et décision d’usage ;
- les conclusions de chapitres, notamment dans la partie 5, qui étaient souvent vides ou trop générales.

L’introduction générale était déjà proche de la voix attendue. Elle a été relue et préservée. Les annexes ont reçu une passe ciblée sur la comparaison des outils et sur la frontière entre une discussion locale et un agent de code utilisable.

## Quelques avant / après

### Partir du geste

Avant : « Un modèle qui produit une commande n’a pas, pour autant, exécuté cette commande. »

Après : « Supposons qu’un modèle produise la commande `pytest`. Pour qu’elle soit réellement exécutée, un programme autour de lui doit lire cette proposition, autoriser l’appel, lancer l’outil et lui transmettre le résultat. »

### Garder l’humour dans la situation

Avant : « Nous allons lui retirer cette habitude. La correction sera petite […] »

Après : « La correction tient presque sur un timbre-poste ; tout ce qui permet de lui faire confiance prend un peu plus de place. »

### Montrer la preuve

Avant : « La recherche n’a pas toujours retrouvé le bon passage. »

Après : « La recherche a manqué une formulation. Le modèle documentaire a inventé une durée malgré la bonne source placée dans son contexte. »

### Clarifier les objets techniques

Avant : « Nous allons les brancher avec MCP. »

Après : « Dans la partie suivante, nous retrouverons les mêmes questions avec un serveur MCP, puis nous décrirons une procédure réutilisable dans un skill. »

### Fermer sans slogan

Avant : « Regardez ce qui vous pose problème aujourd’hui. […] gardez, adaptez ou abandonnez l’outil. »

Après : « Partez du problème qui vous occupe aujourd’hui. Essayez quelque chose d’assez petit pour en comprendre le résultat. Gardez l’outil s’il vous aide, adaptez-le s’il prend trop de place, ou abandonnez-le si une solution plus simple fait mieux le travail. »

## Décisions de coordination

- Le rappel CPU entre les parties 3 et 4 reste volontairement présent : une courte réponse locale ne prouve pas la faisabilité d’une session d’agent de code.
- La partie 5 distingue désormais `mon-suivi`, conservé pour l’assistant, du dossier séparé qui contient `banc.py`.
- La conclusion de la partie 6 reprend l’échec `alerte` / `notification` pour mener vers la recherche documentaire.
- La partie 8 inventorie séparément le banc, le serveur MCP, le skill et l’assistant documentaire, sans attribuer toutes ces preuves à un agent réel.
- Le schéma `recherche.png` a été régénéré depuis `outils/illustrer_ia_maison.py` avec une formulation directe : « Le modèle peut encore contredire les passages retenus. »
- Les usages hors développement font l’objet d’une [proposition séparée](extension-hors-developpement.md). Aucune neuvième partie n’a été greffée pendant cette passe.

## Référence Vim et format ZdS

L’accès direct au tutoriel Vim a été refusé par l’environnement puis bloqué par `robots.txt`. La réécriture s’appuie donc sur l’analyse détaillée conservée dans `GUIDE-VOIX-HUGO.md`, sans prétendre avoir relu la page en ligne. Le guide de rédaction ZdS était accessible et les conventions du dépôt ont été conservées.

## Contrôles et archive

Les lectures et les neuf imports séparés ont été régénérés, puis le ZIP global a été construit. Il contient 394 entrées et son empreinte SHA-256 est :

```text
7bdbbb8d88d9b2aa76021f2e17579732970de938b45ba67206e5a3d4e1bed744
```

Les quatre tests de l’assembleur global réussissent. `unzip -t` ne relève aucune erreur. Les contrôles rapides rejouent aussi les 6 tests du client local, les étapes de la partie 4 avec leurs 2 échecs attendus avant correction, puis les 12 tests du banc d’agents.

L’import interactif dans ZdS reste non effectué. Aucun téléchargement massif, entraînement GPU, API payante ou essai d’agent réel n’a été lancé pendant cette passe éditoriale.

## Relecture conseillée à Hugo

Pour une première lecture efficace, concentrer l’attention sur :

1. `tutoriel/04-developpement/introduction.md` et `05-verifier/casser.md`, pour le ton et la correction de la mutation ;
2. `tutoriel/05-agents/introduction.md` et `conclusion.md`, pour la séparation entre assistant et banc ;
3. `tutoriel/06-mcp-skills/conclusion.md` puis `tutoriel/07-ia-maison/introduction.md`, pour le raccord MCP → recherche documentaire ;
4. `tutoriel/07-ia-maison/04-application/reponses.md` et la conclusion de la partie, pour les erreurs réelles et le statut GPU ;
5. `tutoriel/08-choisir/introduction.md` et `conclusion.md`, pour la position finale et le niveau de fermeté ;
6. les annexes, dont les informations commerciales restent une photographie datée du 14 septembre 2026.

Les huit rapports détaillés se trouvent dans ce dossier, avec les deux passes adverses sur les transitions.
