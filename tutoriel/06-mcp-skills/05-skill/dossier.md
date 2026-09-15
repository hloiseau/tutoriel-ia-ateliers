Ouvrez `skills/preparer-recette/SKILL.md`. Le début ressemble à ceci :

```yaml
---
name: preparer-recette
description: Préparer des scénarios de recette à partir d’un ticket et de sa documentation, en séparant les comportements décidés des questions encore ouvertes. À utiliser pour préparer les tests manuels, sans exécuter la recette ni implémenter le ticket.
license: CC-BY-SA-4.0
---
```
Code: Métadonnées du skill fourni

Le nom désigne la tâche. La description aide l’assistant à reconnaître quand ce dossier peut servir. « Un super expert du développement » ne lui dirait pas grand-chose sur le moment où charger une procédure de recette.

Le format Agent Skills prévoit un dossier contenant `SKILL.md`, avec des métadonnées YAML puis les instructions en Markdown. On peut y joindre des scripts, des références ou des modèles de documents.[^p6-format-skill] Notre dossier ne contient que la procédure et une référence de présentation.

| Fichier | Ce qu’il apporte ici |
| --- | --- |
| `SKILL.md` | Quand préparer la recette et comment traiter les sources |
| `references/format-recette.md` | La forme du résultat à présenter |

Les mots *skill*, *commande* et *plugin* ne désignent donc pas exactement la même chose. Un produit peut proposer notre skill comme commande dans son interface. Un plugin peut distribuer plusieurs skills avec des outils. Notre procédure reste un fichier que nous pouvons lire et modifier sans adopter l’organisation complète d’un plugin.

[^p6-format-skill]: [Spécification du format Agent Skills](https://agentskills.io/specification).
