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
