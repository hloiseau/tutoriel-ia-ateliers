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
