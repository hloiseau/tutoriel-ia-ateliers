Vous êtes en train d’écrire une fonction. L’éditeur suggère la fin de la ligne : c’est de la **complétion**. Vous décidez si vous la gardez.

Un peu plus loin, vous tombez sur une condition difficile à lire. Vous sélectionnez ces lignes et demandez une explication : c’est une **discussion avec du contexte**. Vous n’avez pas besoin que l’outil puisse modifier le dépôt pour vous aider.

Vous pouvez aussi demander une **modification ciblée** : ajouter un cas de test, simplifier une fonction ou proposer un autre nom. L’assistant prépare alors du code ou un diff, que vous relisez.

Enfin, un **agent** peut enchaîner plusieurs actions : chercher le fichier concerné, le lire, le modifier, lancer les tests, lire l’erreur et recommencer. Il lui faut un modèle, mais aussi un programme qui exécute les actions et lui renvoie leurs résultats.

| Votre besoin | Fonction à chercher |
| --- | --- |
| Écrire moins de code répétitif au clavier | Complétion dans l’éditeur |
| Comprendre une fonction ou une erreur | Discussion avec sélection de code |
| Obtenir une proposition facile à relire | Modification ciblée et affichage du diff |
| Faire avancer une tâche dans plusieurs fichiers | Agent avec accès au projet et au terminal |
| Confier une tâche pendant que vous faites autre chose | Exécution en arrière-plan, locale ou distante |
Table: Partir du travail à faire pour choisir une fonction

Ces fonctions peuvent cohabiter dans un même produit. Cela ne vous oblige pas à toutes les activer.

Si votre difficulté actuelle est d’imaginer des cas de test, commencez par là. Vous pouvez écrire le code vous-même et demander à l’assistant quels comportements vous avez oubliés. Vous pouvez aussi préférer déboguer seul et ne lui demander qu’une explication de documentation. Il n’y a pas de formule complète à adopter pour avoir le droit de s’en servir. 🙂
