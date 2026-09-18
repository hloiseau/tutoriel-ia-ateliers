# Voir le pipeline dans n8n

Cette variante facultative reprend le lot fictif « Les ateliers du quartier ». Elle permet de suivre les données dans un éditeur de workflows et de provoquer quelques erreurs. Vous pouvez poursuivre tout le parcours avec l’application locale `pipeline/index.html` sans installer n8n.

Le fichier `point-equipe.json` fournit quatre nœuds :

1. **Lancer manuellement** démarre à votre demande.
2. **Extraction fictive ou collée** fournit un objet JSON écrit pour l’exercice.
3. **Contrôler le lot** vérifie sa structure et ses références.
4. **Préparer le point interne** produit une proposition dans la sortie du nœud.

Aucun modèle n’intervient dans la démonstration fournie. Le workflow ne contient ni clé, ni connexion à une messagerie, ni nœud d’envoi, ni requête réseau. Il porte `active: false` et son seul déclencheur est manuel. n8n lui-même reste un logiciel installé ou un service hébergé : l’absence de requête dans ce workflow ne décrit pas tous les échanges de votre instance.

## Importer et regarder le résultat

Utilisez une instance n8n dont vous disposez déjà. Les [possibilités d’hébergement](https://docs.n8n.io/choose-how-to-use-n8n/) sont présentées dans la documentation officielle ; l’installation et l’administration d’un serveur sortent de cet exercice.

Dans l’éditeur, créez un workflow vide. Ouvrez le menu à trois points, choisissez **Import from File**, puis sélectionnez `point-equipe.json`. L’import de fichiers JSON est décrit dans [Export and import](https://docs.n8n.io/build/manage-workflows/export-and-import/).

Vérifiez que les quatre nœuds ci-dessus apparaissent, puis utilisez **Execute Workflow**. Le [Manual Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger/) sert précisément à cette exécution à la demande. Il n’est pas nécessaire d’activer ou de publier le workflow pour le lancer manuellement.

Ouvrez **Préparer le point interne**, puis sa sortie **Output**, en vue JSON. Le champ `point_interne` contient le texte du point. Les autres champs permettent de vérifier ce qui s’est passé :

| Champ | Valeur attendue avec la démonstration |
| --- | --- |
| `origine` | `exemple_fictif` |
| `statut` | `proposition_interne_non_approuvee` |
| `nouveaux` | `M001`, `M002`, `M005` |
| `deja_connus` | `M004` |
| `action_exterieure` | `false` |
| `persistance` | `false` |

Léo demande deux places, mais son atelier reste « non précisé ». Nora pose une question dans M005 ; elle ne s’inscrit pas une seconde fois. La date et l’horaire restent à clarifier. Le tableau reprend les valeurs de l’extraction : si vous lui donnez une quantité fausse mais bien formée, elle peut apparaître dans le point.

Cette variante s’arrête à la proposition. Elle ne contient pas les boutons d’approbation et d’export de l’application locale, et ne mémorise pas les messages retenus lors d’une exécution précédente. Relancer le workflow avec le même JSON produit le même point depuis le suivi initial. Cela ne constitue pas un mécanisme de déduplication entre exécutions.

## Remplacer la démonstration par une réponse réelle

Réalisez d’abord l’extraction avec la [consigne fournie](../consignes/extraction.md), les règles et les entrées de l’atelier. Gardez la réponse réellement obtenue dans vos fichiers d’essai.

Ouvrez **Extraction fictive ou collée**. C’est un nœud [Edit Fields (Set)](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/) en mode **JSON Output**. Dans le champ JSON, conservez le mode **Fixed** et remplacez tout l’objet par l’extraction obtenue. Collez du JSON seul, sans les balises Markdown qui l’entourent parfois. Le contenu de la réponse va dans ce champ de données ; les nœuds Code n’ont pas à être modifiés.

L’extraction d’un assistant doit porter `"origine": "assistant"`. Utilisez `"origine": "manuel"` si vous avez vous-même saisi l’extraction. Si vous avez retouché une réponse, conservez également l’original et notez ces corrections dans le compte rendu de l’essai : ce champ d’origine ne constitue pas une preuve de provenance.

Relancez le workflow complet. Une erreur de format JSON bloque le nœud d’entrée ; une erreur de contrat bloque **Contrôler le lot**. La proposition suivante n’est produite que si les contrôles passent. Ne demandez pas à n8n de poursuivre malgré l’erreur pour obtenir tout de même un compte rendu.

## Faire tomber les contrôles

Gardez une copie de votre extraction avant ces essais. Dans **Extraction fictive ou collée**, changez une seule valeur, puis relancez :

| Modification | Ce que vous devez observer |
| --- | --- |
| Mettre `"places": "2"` dans M001 | Refus : la quantité est devenue du texte. |
| Remplacer l’extrait de M001 par `"Je réserve neuf places."` | Refus : cette citation n’existe pas dans le message source. |
| Utiliser le fichier de Léo comme `source` de M001 | Refus : la source ne correspond pas à l’identifiant. |
| Dupliquer M001 à la place de M002 | Refus : un identifiant est répété. |
| Donner `"2026-10-17"` à `date_evenement` | Refus : la date de ce lot n’a pas été arbitrée. |
| Mettre `"places": 9` dans M001 en gardant la vraie citation | Le contrôle passe, alors que le message demande deux places. |

Le dernier cas mérite qu’on s’y arrête. Retrouver un extrait dans le bon fichier prouve que la citation existe. Le programme ne comprend pas que « deux personnes » contredit le nombre 9. La relecture reste nécessaire. De même, affecter Cartographie à Léo passe les vérifications de structure, alors que son message ne nomme aucun atelier.

Le contrôleur est volontairement lié à ce petit lot : il connaît les quatre identifiants, leur fichier de référence, les messages complets et M004 déjà présent dans le suivi. Il refuse une date ou un horaire non nul pour ce dossier non arbitré. L’appliquer à de nouvelles demandes exige de fournir un nouveau corpus de référence et des règles adaptées. Une liste d’identifiants figée dans le code ne remplace pas le suivi d’une équipe.

## Faire appeler un modèle par n8n : une étape distincte

Le copier-coller suffit pour vérifier la séparation entre extraction et traitement. Pour expérimenter ensuite un appel direct, dupliquez le workflow et gardez son déclencheur manuel. Cette adaptation est à configurer et à tester dans votre installation ; elle n’est pas incluse dans l’export fourni.

Vous pouvez utiliser le nœud officiel [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm/) avec un nœud de modèle de conversation compatible :

1. Remplacez le nœud **Extraction fictive ou collée** par **Basic LLM Chain**, relié au déclencheur. Reliez le modèle choisi au connecteur de modèle de la chaîne et configurez son accès selon sa documentation.
2. Dans **Prompt**, choisissez **Define below**. Placez dans **Prompt (User Message)** la consigne d’extraction, puis le texte de `regles-equipe.md` et des fichiers de `entrees/`, séparés par leur nom. Ne fournissez pas le corrigé. Pour ce premier essai, ce contenu reste fixe et fictif.
3. Exécutez cette étape seule et regardez sa sortie réelle. Elle peut contenir une chaîne de caractères ou un objet selon le modèle et les options utilisés. Le nœud **Contrôler le lot** attend directement l’objet d’extraction, sans enveloppe supplémentaire.
4. Ajoutez un nœud de transformation entre la chaîne et le contrôleur pour sélectionner le champ observé et, s’il contient du texte, le convertir avec `JSON.parse`. Conservez les erreurs de conversion. Ne faites jamais exécuter la réponse comme du JavaScript.
5. Vérifiez `origine`, les valeurs et les extraits, puis lancez l’enchaînement complet. Conservez la réponse brute, les corrections éventuelles, le nom du modèle, la date, la configuration et le coût observé.

L’option **Require Specific Output Format** de la chaîne permet de raccorder un **Structured Output Parser**. Elle peut aider à obtenir un objet conforme, mais elle ne remplace pas nos contrôles de références, ni la relecture des quantités et des décisions manquantes. Évitez pour ce premier essai un mécanisme de réparation qui rappelle automatiquement le modèle : vous voulez voir l’erreur initiale et compter les appels effectués.

Un service de modèle peut facturer les appels indépendamment de votre formule n8n. Chaque nouvelle exécution de la chaîne peut produire un nouvel appel ; surveillez aussi les reprises et la taille des entrées. Un modèle local demande un serveur accessible depuis l’instance n8n et des ressources adaptées. Le tutoriel ne suppose pas que votre ordinateur puisse faire tourner n’importe quel modèle. Aucun de ces appels n’a été exécuté pour valider cet export.

## Ce qui a été vérifié

Le 17 septembre 2026, les 15 tests JavaScript passent avec Node.js 24.19.0 : structure de l’export, corpus incorporé, résultat fictif, erreurs de format et de provenance, limites sémantiques, absence de suivi durable. Les tests lisent directement le code contenu dans les deux nœuds de `point-equipe.json` ; ils l’exécutent hors du moteur n8n.

Depuis la racine du dépôt :

```bash
node --test ateliers/hors-developpement/n8n/test_workflow.js
```

Depuis le dossier de l’atelier décompressé :

```bash
node --test n8n/test_workflow.js
```

L’import dans une interface n8n, l’exécution par son moteur et l’appel réel d’un modèle restent à vérifier. Aucun résultat de ces opérations n’est annoncé ici. Le JSON utilise Manual Trigger version 1, Edit Fields version 3.4 et Code version 2 ; notez la version de votre instance dans votre compte rendu d’import.

Les deux nœuds [Code](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/) utilisent JavaScript, en mode **Run Once for All Items**, sans dépendance externe. Ils échangent un tableau contenant un objet `json`, conformément à la [structure des données n8n](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure/).

Textes et données fictives : CC BY-SA 4.0. Code de l’export et tests : GPL-3.0-only. Ces licences concernent les fichiers de l’atelier, pas le logiciel n8n.
