# 6. Faire évoluer le skill à partir des problèmes rencontrés

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Écrire notre premier skill](../05-skill/LECTURE.md) · [Suivant : Articuler skills, conventions et base de connaissances](../07-ranger/LECTURE.md)

**TL;DR** — PRIX-2 laisse deux décisions ouvertes. Nous allons nous en servir pour repérer une mauvaise réponse, corriger la procédure si nécessaire et vérifier que PRIX-1 fonctionne encore.

C’est souvent là que les choses deviennent intéressantes : le premier exemple marchait, le suivant révèle ce que nous n’avions pas précisé.

## Un ticket qui ne dit pas tout

Consultez le second ticket :

```bash
python client.py ticket PRIX-2 --serveur mon_serveur.py --journal sorties/adaptation-prix-2.json
```

Il demande de limiter les notifications trop rapprochées. Deux questions restent ouvertes : quelle durée définit un intervalle court, et une baisse plus importante peut-elle contourner cette limite ?

Ouvrez une nouvelle conversation, chargez le même skill et demandez la préparation de PRIX-2. Une nouvelle conversation évite que vos corrections précédentes soient les seules à expliquer un bon résultat : nous voulons voir ce que les fichiers permettent de refaire.

Que doit contenir la réponse ? Des questions, justement. On peut déjà identifier des familles de cas : une notification juste avant la limite, une autre juste après, une nouvelle baisse pendant l’intervalle. Mais choisir « dix minutes » ou décider qu’une forte baisse passe toujours inventerait une règle.

La documentation de PRIX-1 ne résout pas cette ambiguïté. Elle dit quand une baisse rend une notification pertinente ; PRIX-2 ajoute une condition de temporisation encore à définir. Des sources vraies peuvent donc rester insuffisantes pour répondre.

Une recette avec deux résultats « à arbitrer » peut être plus utile qu’un tableau entièrement rempli. Elle montre précisément les décisions dont nous avons besoin pour poursuivre. Ce n’est pas au modèle de décider discrètement du comportement du produit pour que son tableau soit plus joli.

## Changer la règle qui a réellement manqué

Si votre assistant choisit malgré tout une durée, commencez par ouvrir les fichiers qu’il a lus. A-t-il chargé le bon skill ? Le ticket complet ? Est-ce une ancienne copie de la procédure qui est encore utilisée ? Ajouter une nouvelle consigne dans un fichier jamais lu ne réglera pas le problème.

Si le skill a bien été chargé, vous pouvez demander une correction précise :

> Sur PRIX-2, tu as choisi une durée alors que le ticket la laisse ouverte. Modifie le skill pour laisser ce résultat à arbitrer et présenter la question. Garde la préparation possible pour les cas déjà décidés. Montre-moi le diff avant de réessayer.

Relisez le diff. Une bonne modification décrit le comportement manquant. Une mauvaise modification peut simplement ajouter PRIX-2 comme cas particulier, puis inventer une durée sur le prochain ticket.

Notre version fournie contient déjà la consigne sur les décisions manquantes. Si votre assistant la suit, ne rajoutez pas une deuxième formulation pour le principe. Gardez plutôt ce cas dans vos essais futurs.

Après une modification, rejouez PRIX-2 **et** PRIX-1 dans des conversations neuves. Une règle trop large, comme « s’arrêter dès qu’il manque une information », pourrait empêcher toute préparation de PRIX-1 sous prétexte que notre jeu ne fournit pas d’interface de staging. Nous voulons préparer ce qui est déterminé et nommer ce qui manque pour l’exécution.

C’est du *trial and error*, avec des traces qui permettent de comprendre ce qui a changé. L’IA peut nous aider à modifier les fichiers ; nous gardons la décision sur le comportement voulu.

## Garder des essais que l’on peut comparer

Conservez une petite fiche par essai :

| Élément | Exemple à noter |
| --- | --- |
| Version des fichiers | Commit du dépôt ou copie du skill essayé |
| Outil et modèle | Ceux réellement sélectionnés dans l’interface |
| Demande | Texte envoyé pour PRIX-1 ou PRIX-2 |
| Sources | Appels observés et documents effectivement lus |
| Résultat | Réponse conservée, avec les erreurs éventuelles |
| Décision | Modification à garder, à revoir ou à abandonner |

Ces éléments permettent de comparer autre chose qu’une impression. Un meilleur résultat après avoir changé à la fois le modèle, le ticket et le skill ne nous apprend pas quelle modification a aidé.

Il n’est pas nécessaire d’attendre les retours d’autres lecteurs pour avancer. Nos deux tickets et le document piégé fournissent déjà de quoi mettre la procédure à l’épreuve. Si un nouvel incident apparaît dans votre travail, ajoutez un exemple réduit qui le reproduit, avec des données partageables.

Les tests Python de l’atelier ne vérifient pas cette partie : ils contrôlent le serveur. Pour le skill, le résultat dépend aussi du modèle, du contexte et du produit qui charge les fichiers. Un passage réussi n’est pas un taux de fiabilité.

Nous pouvons également comparer l’effort avec une préparation manuelle. Si la réponse demande plus de temps à réparer qu’à écrire, le skill n’a pas encore trouvé sa place pour cette tâche. Et si vous n’aimez pas déléguer le code, rien n’oblige à aller plus loin que cette aide à la recette.

La procédure commence à correspondre à une manière de travailler. Reste à la maintenir sans finir avec un fichier géant qui mélange les règles du projet, les données métier et toutes les erreurs de l’année.

---

[Précédent : Écrire notre premier skill](../05-skill/LECTURE.md) · [Suivant : Articuler skills, conventions et base de connaissances](../07-ranger/LECTURE.md)
