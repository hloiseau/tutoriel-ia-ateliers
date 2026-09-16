Prenons trois phrases de notre atelier :

| Information | Où la conserver ? | Pourquoi ? |
| --- | --- | --- |
| « Les prix sont des entiers en centimes. » | Conventions du projet | Cela sert à plusieurs tâches sur le même code |
| « Faire apparaître les résultats encore à arbitrer. » | Skill de préparation de recette | Cela décrit une étape du travail demandé |
| « Une simple remise en stock ne déclenche pas de notification. » | Ticket et documentation métier | Cela décrit le comportement du produit |

La **base de connaissances** désigne ici l’ensemble des documents qui apportent des faits sur le projet : règles métier, décisions, contrats d’API, explications d’un service. Elle peut être constituée de Markdown dans un dépôt, de pages sur un wiki ou de données accessibles par un outil. Le terme n’impose ni base vectorielle ni logiciel particulier.

![Trois exemples rangés dans les conventions, le skill et la documentation, avec leur portée respective.](image:images/rangement.png)
Figure: Des fichiers différents parce que les informations changent pour des raisons différentes

Si la règle de notification évolue, nous corrigeons sa source métier. Si la présentation des recettes change, nous corrigeons la référence du skill. Si le projet change d’unité monétaire interne, les conventions et le code doivent être revus ensemble.

Les liens rendent cette séparation utilisable. Dans notre atelier, le ticket cite un document par son identifiant et le skill renvoie explicitement vers son format de recette. Un paragraphe déplacé dans un sous-dossier sans indication devient seulement plus difficile à retrouver.
