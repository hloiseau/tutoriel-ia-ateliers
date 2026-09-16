# 3. Évaluer les sources avant les réponses

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Construire une recherche dans nos documents](../02-rechercher/LECTURE.md) · [Suivant : Assembler notre assistant documentaire](../04-application/LECTURE.md)

**TL;DR** — Nous allons séparer trois questions : le passage utile a-t-il été retrouvé, la réponse est-elle juste, et ses citations la soutiennent-elles ?

Une seule note de « qualité de l’IA » cacherait l’endroit où l’application échoue. Nous allons donc tester séparément la recherche, la réponse et l’usage des citations.

## Garder des questions de côté

Le fichier `questions-validation.json` rassemble des questions dont nous connaissons les sources attendues. Il sert à examiner nos choix de recherche. Lancez :

```bash
python evaluer_recherche.py --lot validation --sortie sorties/recherche-validation.json
```

Le rapport indique quels identifiants ont été retrouvés. Il compte la présence d’au moins une source pertinente parmi les trois passages retenus. Il ne mesure ni la précision de chaque passage ni la qualité d’une réponse générée.

Une fois vos choix fixés, lancez le lot de test :

```bash
python evaluer_recherche.py --lot test --sortie sorties/recherche-test.json
```

Dans notre exécution, une source pertinente est présente pour trois des quatre questions de test qui en ont une. La question sur la « purge des fixtures » est manquée. La question hors corpus ne retourne aucun passage.

Avec cinq exemples, nous cherchons des erreurs concrètes plutôt qu’un score général. Si nous ajoutons des synonymes spécialement pour corriger la question ratée, elle devient un exemple de développement. Pour évaluer la modification, il nous faudra alors de nouvelles questions qu’elle n’aura pas déjà rencontrées — autrement, nous lui soufflerions le sujet de l’examen. 😅

## Dire ce que l’on n’a pas trouvé

Il y a deux cas à distinguer dans nos documents. Pour l’horaire de staging, la réponse existe mais peut être mal retrouvée. Pour la temporisation de PRIX-2, le document est trouvé et dit précisément que la durée reste à décider.

Dans le premier cas, notre application peut seulement dire « aucun passage retrouvé » : le document est bien là, hors de portée de cette formulation. Dans le second, le passage remonte et la réponse attendue est une décision ouverte. Ajouter un nombre pour remplir la phrase contredirait la source.

Un seuil de recherche ne tranche pas cette différence. Un score élevé peut rapprocher une question d’un paragraphe qui décrit le problème sans donner la solution. C’est ce qui rend utile le champ `reponse_attendue` du jeu de questions : un humain peut comparer le sens de la réponse aux sources.

Gardez également les questions auxquelles le système devrait s’abstenir. Un jeu rempli uniquement de réponses présentes dans le corpus passerait sous silence son comportement lorsque les documents sont insuffisants.

## Une citation peut être vraie et mal utilisée

Une réponse pourrait écrire « la durée est de dix minutes [temporisation#2] ». L’identifiant existe, tandis que le passage dit qu’aucun délai chiffré n’est validé. La référence mène donc tout droit à la preuve que la phrase est fausse.

Notre petit contrôle automatique sait repérer un identifiant qui ne fait pas partie des passages transmis. Il ne sait pas décider si chaque phrase est soutenue par le texte cité. Pour relire une réponse, ouvrez donc la source et comparez l’affirmation exacte, notamment les nombres, les négations et les conditions.

| Observation | Ce qu’elle permet de dire |
| --- | --- |
| Le passage attendu est sélectionné | La recherche a fourni une source utile |
| L’identifiant cité appartient à la sélection | La référence n’a pas été inventée hors de cette sélection |
| La phrase correspond au contenu de la source | Cette affirmation est soutenue par ce passage |
| La source est ancienne ou incomplète | Il reste à vérifier qu’elle s’applique à la question |

Les deux premiers contrôles s’automatisent facilement. Pour les suivants, il faut encore confronter chaque affirmation au passage cité. Notre modèle local va justement nous fournir un cas très parlant.

Nous savons maintenant dire si l’échec vient de la recherche avant d’accuser le modèle de langage. Relions les deux, tout en conservant dans le journal les passages que le modèle a réellement reçus.

---

[Précédent : Construire une recherche dans nos documents](../02-rechercher/LECTURE.md) · [Suivant : Assembler notre assistant documentaire](../04-application/LECTURE.md)
