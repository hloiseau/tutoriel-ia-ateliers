# 6. Faire évoluer le skill à partir des problèmes rencontrés

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Écrire notre premier skill](../05-skill/LECTURE.md) · [Suivant : Articuler skills, conventions et base de connaissances](../07-ranger/LECTURE.md)

**TL;DR** — PRIX-2 laisse deux décisions ouvertes. Nous allons nous en servir pour repérer une mauvaise réponse, corriger la procédure si nécessaire et vérifier que PRIX-1 fonctionne encore.

Un ami m’a proposé une comparaison qui me plaît bien :

> Les skills sont comme une recette de cuisine, on peut enlever du sel ou du sucre pour l’adapter à notre régime.

On peut reprendre une bonne base sans tout garder. Pour un skill, cela peut vouloir dire retirer une étape qui ne nous sert pas, ajouter une vérification qui manque ou remplacer une étape prévue pour un outil que l’on n’utilise pas. C’est à la procédure de s’adapter à notre manière de travailler.

C’est souvent là que les choses deviennent intéressantes : PRIX-1 peut donner un résultat convaincant, puis PRIX-2 révèle tout ce que la procédure ou le ticket n’avaient pas précisé.

## Un ticket qui ne dit pas tout

Consultez le second ticket :

```bash
python client.py ticket PRIX-2 --serveur mon_serveur.py --journal sorties/adaptation-prix-2.json
```

Il demande de limiter les notifications trop rapprochées. Deux questions restent ouvertes : quelle durée définit un intervalle court, et une baisse plus importante peut-elle contourner cette limite ?

Ouvrez une nouvelle conversation, chargez le même skill et demandez la préparation de PRIX-2. Une nouvelle conversation évite que vos corrections précédentes soient les seules à expliquer un bon résultat : nous voulons voir ce que les fichiers permettent de refaire.

La réponse devrait faire apparaître les deux questions. Elle peut déjà identifier des familles de cas : une notification juste avant la limite, une autre juste après, une nouvelle baisse pendant l’intervalle. En revanche, « dix minutes » ou « une forte baisse passe toujours » seraient des règles inventées pour remplir les cases.

La documentation de PRIX-1 ne résout pas cette ambiguïté. Elle dit quand une baisse rend une notification pertinente ; PRIX-2 ajoute une condition de temporisation encore à définir. Des sources vraies peuvent donc rester insuffisantes pour répondre.

Une recette avec deux résultats « à arbitrer » peut être plus utile qu’un tableau entièrement rempli. Elle montre précisément les décisions dont nous avons besoin pour poursuivre. Un trou visible se discute avec l’équipe ; une règle inventée au fond d’une cellule risque de devenir le comportement du produit par accident.

## Changer la règle qui a réellement manqué

Si votre assistant choisit malgré tout une durée, commencez par ouvrir les fichiers qu’il a lus. A-t-il chargé le bon skill ? Le ticket complet ? Est-ce une ancienne copie de la procédure qui est encore utilisée ? Ajouter une nouvelle consigne dans un fichier jamais lu ne réglera pas le problème.

Si le skill a bien été chargé, vous pouvez demander une correction précise :

> Sur PRIX-2, tu as choisi une durée alors que le ticket la laisse ouverte. Modifie le skill pour laisser ce résultat à arbitrer et présenter la question. Garde la préparation possible pour les cas déjà décidés. Montre-moi le diff avant de réessayer.

Relisez le diff. La modification devrait décrire le comportement manquant de manière générale. Si elle ajoute seulement PRIX-2 comme cas particulier, le prochain ticket incomplet risque de déclencher la même invention.

Notre version fournie contient déjà la consigne sur les décisions manquantes. Si votre assistant la suit, ne rajoutez pas une deuxième formulation pour le principe. Gardez plutôt ce cas dans vos essais futurs.

Après une modification, rejouez PRIX-2 **et** PRIX-1 dans des conversations neuves. Une règle trop large, comme « s’arrêter dès qu’il manque une information », pourrait empêcher toute préparation de PRIX-1 sous prétexte que notre jeu ne fournit pas d’interface de staging. Nous voulons préparer ce qui est déterminé et nommer ce qui manque pour l’exécution.

C’est du *trial and error*, avec des traces pour comprendre ce qui a changé. L’IA peut nous aider à modifier les fichiers ; la décision sur le comportement voulu nous revient toujours.

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

Nos deux tickets et le document piégé fournissent déjà de quoi mettre la procédure à l’épreuve. Lorsqu’un nouvel incident apparaît dans votre travail, ajoutez un exemple réduit qui le reproduit avec des données partageables ; vous pourrez alors vérifier si la correction tient au prochain changement.

Les tests Python de l’atelier contrôlent le serveur. Le skill doit être essayé séparément, car son résultat dépend aussi du modèle, du contexte et du produit qui charge les fichiers. Un seul passage réussi nous donne une trace utile, aucun taux de fiabilité.

Nous pouvons également comparer l’effort avec une préparation manuelle. Si la réponse demande plus de temps à réparer qu’à écrire, le skill n’a pas encore trouvé sa place pour cette tâche. Et si vous n’aimez pas déléguer le code, rien n’oblige à aller plus loin que cette aide à la recette.

La procédure commence à correspondre à une manière de travailler. Reste à la maintenir sans finir avec un fichier géant qui mélange les règles du projet, les données métier et toutes les erreurs de l’année.

---

[Précédent : Écrire notre premier skill](../05-skill/LECTURE.md) · [Suivant : Articuler skills, conventions et base de connaissances](../07-ranger/LECTURE.md)
