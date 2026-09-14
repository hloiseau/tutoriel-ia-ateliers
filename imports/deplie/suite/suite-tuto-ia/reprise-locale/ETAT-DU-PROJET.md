# État du projet — 14 septembre 2026

## Livrables

| Partie | État | Fichiers |
| --- | --- | --- |
| 1 — Histoire de l’IA | V3 validée par l’auteur | `parties-precedentes/histoire-ia-zds-v3.zip` |
| 2 — Comprendre un modèle en le construisant | Version complète, retours favorables ; annexes séparées | `parties-precedentes/apprentissage-ia-zds-v2.zip` |
| 3 — Faire tourner un modèle chez soi | Nouveau brouillon complet : 6 chapitres, 21 sections, 4 illustrations | `partie-3/`, `partie-3-zds-v1.zip` |
| 4 — Développer avec une IA | Nouveau brouillon complet : 6 chapitres, 19 sections, 3 illustrations | `partie-4/`, `partie-4-zds-v1.zip` |
| 5 à 8 | Plan à développer ; pas de chapitres complets revendiqués | `reprise-locale/SOMMAIRE-GENERAL.md` |

Les chapitres des parties 3 et 4 sont rédigés, sans sections vides à remplir ultérieurement. Les manipulations sur le GPU de l’auteur et le contrôle sur son système restent à faire. Les résultats actuellement conservés viennent de l’environnement Linux de rédaction.

## Lire et modifier

Ouvrir `partie-3/relecture.html` ou `partie-4/relecture.html` dans un navigateur. Les images sont intégrées. Pour modifier, utiliser les petits Markdown référencés par `manifest.json`, pas seulement la copie `relecture.md`.

Les dossiers `atelier` contiennent le code décompressé et modifiable. Les ZIP d’annexes sont assemblés à partir de ces dossiers ; les poids et les exécutables de llama.cpp sont exclus.

L’outil `reprise-locale/assembler.py` reconstruit les lectures, l’archive d’annexes et l’archive ZdS de chacune des **parties 3 et 4**. Il ne remplace pas les outils spécifiques des parties précédentes.

```bash
python -m pip install Markdown==3.10.3
python reprise-locale/assembler.py partie-3
python reprise-locale/assembler.py partie-4
```

Installer la dépendance dans un environnement virtuel si elle n’est pas déjà disponible. Les scripts des ateliers eux-mêmes utilisent seulement la bibliothèque standard de Python.

## Limites déjà connues

- Les réponses du petit modèle sont réelles, mais elles ne constituent pas un benchmark général. En français, une réponse est maladroite et atteint la limite de sortie.
- Les six tests du client HTTP utilisent des réponses factices ; ils sont distincts des appels réels au modèle, qui ont aussi été exécutés.
- Le parcours de développement, les scénarios et les deux mutations ont été exécutés. Aucun produit d’agent externe n’a été évalué : les prompts sont des consignes proposées, pas des traces attribuées à Claude Code, Cursor ou Codex.
- Windows, macOS, la 3090 Ti et l’import sur le compte ZdS de l’auteur n’ont pas été testés ici.
- Le HTML a été contrôlé structurellement et les illustrations inspectées. Un rendu complet dans un navigateur réel reste à contrôler.
- Les liens relatifs des ZIP d’annexes fonctionnent dans les dossiers extraits ; ils doivent être remplacés par les liens publics réels avant publication.

## Prochaine étape

La priorité locale est la validation pratique décrite dans `EXPERIENCES-A-LANCER.md`. La rédaction peut continuer en parallèle logique sur les parties 5 et 6, mais les expériences non exécutées doivent rester identifiées comme telles dans les dossiers de travail. Les principes validés par l’auteur ne sont pas à renégocier à chaque chapitre.
