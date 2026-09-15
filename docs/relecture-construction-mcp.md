# Relecture adverse — construire le MCP

La question de départ était : un lecteur peut-il développer son serveur en suivant le chapitre, ou lui fait-on seulement manipuler un corrigé ? Cette reprise concerne le chapitre 3 de la partie 6 et ses raccords.

## Défauts corrigés

| Problème recherché ou constaté | Correction | Vérification |
| --- | --- | --- |
| Le chapitre expliquait surtout un serveur déjà terminé. | Fichier vide, puis ajouts successifs avec une commande après chaque étape. | Reconstruction des six états depuis les blocs Markdown, sans démarrer du corrigé. |
| Une commande pouvait appeler `serveur.py` alors que le lecteur modifiait son propre fichier. | Option `--serveur mon_serveur.py` et nom du fichier dans le journal. | Inventaire vide au départ, puis changement de titre visible dans la réponse ; cible par défaut contrôlée séparément. |
| Les tests de référence importaient toujours le corrigé. | Trois tests à écrire importent explicitement `mon_serveur`. | Retirer le décorateur de son outil de lecture fait échouer le test concerné. |
| Un test vérifiant seulement `isError` acceptait aussi une erreur de document absent. | Vérification de l’erreur de format et de l’inventaire des outils. | Retirer la contrainte du paramètre documentaire fait échouer le test de validation. |
| Une assertion levée à l’intérieur du client asynchrone produisait une longue `ExceptionGroup`. | Assertions placées après la fermeture du client dans les tests du lecteur. | La mutation donne un échec d’assertion lisible, puis les tests passent après restauration. |
| La suite risquait de revenir au serveur fourni, avec des explications répétées et des journaux déjà utilisés. | Chapitre 4 recentré sur les limites ; commandes et configuration gardent `mon_serveur.py` ; noms de journaux distincts. | Contrôle des commandes des chapitres suivants, des liens et des fichiers assemblés. |

## Rejeu concret

Le script `outils/verifier_construction_mcp.py` extrait l’archive pratique dans un dossier temporaire. Il lit les blocs de code du chapitre et applique les ajouts/remplacements décrits. Il compare les états obtenus aux corrigés, puis exécute les appels avec le client MCP réel.

**Six états reconstruits et 24 commandes exécutées**, dont les deux régressions volontaires. Les trois tests du lecteur et les dix tests du corrigé passent dans leur état final. La recherche sans résultat, les espaces seuls, le document absent, le fichier serveur manquant et le refus d’écraser un journal sont également exercés. Les fichiers de données restent identiques.

[Commandes et résultats](verifications-construction-mcp/executions.json). Les journaux conservent les réponses réellement obtenues ; les sorties des mutations sont des échecs attendus.

## Cohérence pédagogique retenue

1. Essayer le serveur fourni pour voir ce que nous cherchons à construire.
2. Développer le nôtre dans un fichier séparé, sans nouvelle installation ni nouveau jeu de données.
3. Vérifier une réponse observable après chaque ajout.
4. Écrire les tests, provoquer un échec, puis utiliser ce serveur dans l’assistant.
5. Examiner les limites des contrôles avant d’ajouter le skill.

Les fichiers intermédiaires servent à reprendre une étape. Leur contenu se copie dans `mon_serveur.py`, à la racine de l’atelier : ils ne sont pas annoncés comme des programmes à lancer depuis leur sous-dossier.

## Limites restantes

Ce rejeu vérifie le chemin décrit et plusieurs erreurs concrètes. Il ne prouve pas qu’un lecteur débutant comprendra chaque étape sans difficulté. Les nouveaux types et le client asynchrone sont expliqués à l’endroit où ils sont utilisés ; une relecture humaine pourra encore ajuster ces explications.

L’interface de VS Code, les autres assistants, les essais du skill avec un modèle, Windows, macOS et l’import dans l’interface ZdS restent à vérifier. Aucun succès d’un agent sur la recette n’est déduit des tests Python. Aucun GPU ni modèle sur CPU n’est nécessaire pour construire et tester le serveur ; les essais dans l’assistant utilisent le modèle habituel du lecteur.
