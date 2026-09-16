# Imports ZdS

Archives reconstruites depuis les sources courantes du tutoriel. Chaque ZIP contient son manifest à la racine, les sections et les illustrations. Les ateliers restent dans leurs archives séparées.

- **[Tutoriel complet — huit parties et annexes](tutoriel-ia-complet.zip)**

- [Partie 1 — Histoire](01-histoire.zip)
- [Partie 2 — Apprentissage](02-apprentissage.zip)
- [Partie 3 — Modèle local](03-modele-local.zip)
- [Partie 4 — Développement](04-developpement.zip)
- [Partie 5 — Agents, contexte et permissions](05-agents.zip)
- [Partie 6 — MCP et skills](06-mcp-skills.zip)
- [Partie 7 — IA maison](07-ia-maison.zip)
- [Partie 8 — Choisir la place de l’IA](08-choisir.zip)
- [Annexes — Comparatif et expérience locale](annexes.zip)

Les contrôles de structure ne remplacent pas la relecture dans un brouillon ZdS ni les validations pratiques restantes.

Pour reconstruire après une modification, depuis la racine du dépôt :

```bash
python outils/assembler_tutoriel.py --exports telechargements/zds
python outils/assembler_global.py
```

[Sommaire et lectures sur GitHub](../../SOMMAIRE.md)

[Structure, transformations et limites de l’export global](../../docs/export-global.md).
