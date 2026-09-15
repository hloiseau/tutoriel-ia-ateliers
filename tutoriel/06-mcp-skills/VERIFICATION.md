# Vérifications de la partie 6

Sous Linux, Python **3.12.14**, SDK MCP **2.2.0**. Les données de l’atelier sont fictives ; aucun modèle n’est appelé par les scripts de vérification.

## Parcours courant : construire le serveur

Le chapitre 3 a été rejoué depuis ses **blocs Markdown**, avec les fichiers d’une archive extraite. Chaque ajout et remplacement décrit dans le texte reconstruit le fichier `mon_serveur.py`. Les six états obtenus correspondent aux corrigés fournis, jusqu’au serveur complet.

Les appels stdio vérifient l’inventaire vide, le premier ticket, le changement visible de son titre, les questions de PRIX-2, la recherche et la lecture documentaires, les paramètres et la ressource. Le journal identifie le fichier serveur lancé.

Les **trois tests du lecteur** passent. Retirer l’exposition du premier outil, puis retirer la validation du paramètre documentaire, fait échouer le test concerné. Les tests repassent après restauration. Les **dix tests du corrigé** passent également.

Le refus d’écraser un journal, un chemin de serveur absent, la sélection du corrigé par défaut et la configuration visant `mon_serveur.py` ont été exercés. Les données sont inchangées à l’issue des essais.

- [Relecture adverse et corrections](../../docs/relecture-construction-mcp.md)
- [Commandes, sorties réelles et empreinte de l’archive](../../docs/verifications-construction-mcp/executions.json)
- [Script de rejeu depuis le Markdown](../../outils/verifier_construction_mcp.py)

Pour rejouer depuis la racine du dépôt, avec le Python de l’environnement MCP :

```bash
python outils/verifier_construction_mcp.py
```

Le script extrait l’archive dans un dossier temporaire, sans remplacer les fichiers du lecteur. Il met à jour les traces de vérification dans `docs/verifications-construction-mcp`.

## Première exécution du serveur fourni

Les [journaux initiaux](../../docs/verifications-partie6/) concernent la version publiée au [commit b921fc8](https://github.com/hloiseau/tutoriel-ia-ateliers/commit/b921fc867bb4babf4a4eb4eda2cf53c884a500d9). Ils conservent dix échanges stdio, dix tests et l’empreinte de l’archive de cette version. Le protocole observé était `2026-07-28`.

La structure du skill et les trois illustrations avaient également été vérifiées. Ces fichiers restent inchangés dans la reprise du chapitre de construction.

## Essais restants

L’installation interactive dans VS Code, les autres assistants, la découverte du skill et son comportement avec un modèle restent à essayer. Les étapes VS Code suivent les documentations officielles citées. Windows et macOS n’ont pas été exécutés. L’import dans l’interface ZdS reste à vérifier.

Les attendus de recette sont rédigés pour l’exercice ; ils ne sont pas des réponses attribuées à une IA. Le serveur n’expose pas d’écriture, mais son processus n’est pas un bac à sable : un autre outil de l’assistant peut donner un autre accès aux fichiers.
