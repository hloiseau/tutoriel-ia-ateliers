# 5. Écrire notre premier skill

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Refuser ce que le serveur ne doit pas faire](../04-controler/LECTURE.md) · [Suivant : Faire évoluer le skill à partir des problèmes rencontrés](../06-adapter/LECTURE.md)

**TL;DR** — Nous allons mettre une procédure de préparation de recette dans un dossier lisible et modifiable. Le skill guidera l’usage des sources déjà accessibles par MCP.

Demander « prépare-moi les tests » laisse encore beaucoup de place à l’interprétation. Quels tests ? Avec quelles données ? Et que faire si le ticket ne décide pas du résultat attendu ?

## Donner un nom à une tâche précise

Ouvrez `skills/preparer-recette/SKILL.md`. Le début ressemble à ceci :

```yaml
---
name: preparer-recette
description: Préparer des scénarios de recette à partir d’un ticket et de sa documentation, en séparant les comportements décidés des questions encore ouvertes. À utiliser pour préparer les tests manuels, sans exécuter la recette ni implémenter le ticket.
license: CC-BY-SA-4.0
---
```
Code: Métadonnées du skill fourni

Le nom désigne la tâche. La description aide l’assistant à reconnaître quand ce dossier peut servir. Avec « un super expert du développement », il aurait encore fallu deviner à quel moment charger une procédure de recette.

Le format Agent Skills prévoit un dossier contenant `SKILL.md`, avec des métadonnées YAML puis les instructions en Markdown. On peut y joindre des scripts, des références ou des modèles de documents.[^p6-format-skill] Notre dossier ne contient que la procédure et une référence de présentation.

| Fichier | Ce qu’il apporte ici |
| --- | --- |
| `SKILL.md` | Quand préparer la recette et comment traiter les sources |
| `references/format-recette.md` | La forme du résultat à présenter |

Un produit peut proposer notre skill sous la forme d’une commande dans son interface. Un plugin peut, lui, distribuer plusieurs skills avec des outils. Ces mots décrivent des objets qui se recouvrent parfois, mais notre point de départ reste très simple : un fichier de procédure que nous pouvons lire et modifier.

[^p6-format-skill]: [Spécification du format Agent Skills](https://agentskills.io/specification).

## Décrire le travail à faire

Le corps du skill commence par demander la lecture du ticket. Il fait ensuite charger les documents cités, préparer les cas décidés et faire apparaître les questions ouvertes. Voici la consigne qui nous intéresse particulièrement :

> Si une décision manque ou que les sources se contredisent, expose la question et laisse le résultat concerné indéterminé. Ne choisis pas discrètement à la place de l’équipe.

Nous écrivons à l’impératif parce que nous décrivons la procédure attendue. « Tu pourrais peut-être vérifier les questions » ressemble à une possibilité parmi d’autres. Ici, leur examen fait partie du travail.

L’impératif rend notre attente claire ; il ne transforme pas le texte en programme déterministe. Nous devrons vérifier ce que le modèle en fait, comme nous avons relu les tests proposés dans la partie 4.

Le skill ne contient pas la règle « notifier si le prix baisse et si le produit est disponible ». Cette information appartient au ticket et à sa documentation. En la recopiant dans la procédure, nous créerions une deuxième version à mettre à jour lors du prochain changement métier.

Enfin, le skill demande de lire `references/format-recette.md` au moment de présenter le résultat. Ce fichier précise les colonnes : cas, préconditions, action, résultat attendu et source. L’assistant peut ainsi charger ce format au moment de rédiger, après avoir découvert PRIX-1 et examiné ses sources.

Le chargement progressif dépend de l’implémentation du client. Cette séparation le rend possible ; vérifiez dans votre outil quels fichiers sont réellement chargés et à quel moment.[^p6-chargement]

[^p6-chargement]: Agent Skills, [prise en charge et chargement par les clients](https://agentskills.io/client-implementation/adding-skills-support).

## Préparer la recette de PRIX-1

Dans VS Code, copiez le dossier complet `skills/preparer-recette` dans `.github/skills/`, à la racine du dossier d’atelier ouvert. Vous devez obtenir `.github/skills/preparer-recette/SKILL.md`, avec son sous-dossier `references` à côté. Cet emplacement est pris en charge pour les skills de projet.[^p6-vscode-skill]

Si `/preparer-recette` apparaît dans le chat, sélectionnez-le puis demandez :

> Prépare la recette de PRIX-1 avec le MCP atelier-tickets. Présente-la dans la conversation.

Avec un autre assistant, utilisez son emplacement de skills ou demandez explicitement la lecture du fichier fourni. Dans ce second cas, vous essayez bien les instructions, mais pas la découverte automatique du dossier par le produit.

Dans la réponse, cherchez des cas concrets. Le retour en stock à prix égal doit être distingué du retour en stock accompagné d’une baisse. L’indisponibilité nouvelle doit aussi être couverte. Un tableau très long qui répète seulement « le système fonctionne correctement » ne nous aide pas beaucoup. 😅

Comparez la proposition avec `attendus-recette.md`. Ce document contient des cas rédigés pour l’exercice. Les données y sont en centimes, comme dans nos conventions. Il explique aussi ce qui manque pour exécuter une vraie recette : notre jeu ne décrit ni interface de staging ni compte ni moyen d’observer un envoi.

À ce stade, nous avons préparé des scénarios. Pour annoncer leurs résultats, il faudrait encore disposer de l’application et les exécuter. Gardons cette différence dans le vocabulaire : une jolie recette ne fait toujours pas cuire le gâteau. 🙂

[^p6-vscode-skill]: [Utiliser les skills dans VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills).

Nous avons une première procédure et des critères pour relire ce qu’elle produit. Essayons-la maintenant sur un ticket qui ne permet pas de remplir toutes les cases.

---

[Précédent : Refuser ce que le serveur ne doit pas faire](../04-controler/LECTURE.md) · [Suivant : Faire évoluer le skill à partir des problèmes rencontrés](../06-adapter/LECTURE.md)
