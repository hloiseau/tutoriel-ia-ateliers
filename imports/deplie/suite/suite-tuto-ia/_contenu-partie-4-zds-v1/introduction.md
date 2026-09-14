Vous avez un ticket à traiter. Le projet existe déjà, les tests passent, et quelqu’un vous signale pourtant un comportement qui ne convient pas. Nous allons partir de cette situation assez ordinaire.

Un agent peut lire les fichiers, proposer une explication, ajouter des tests et modifier le code. Mais avant de lui confier le clavier, il nous faut savoir ce que nous essayons de changer. Sinon, nous risquons d’obtenir très rapidement une solution à un autre problème.

Notre projet sera assez petit pour être lu en entier. Pas de base à installer, pas de compte à créer : quelques fichiers Python, trois scénarios et une fonction qui prend une décision. Vous pourrez faire les manipulations avec votre agent habituel ou suivre les étapes vous-même.

**TL;DR**

- Nous partons d’un comportement observable et d’une règle précise.
- Nous ajoutons des tests qui échouent avant de corriger le code.
- Nous relisons le changement, puis nous vérifions le programme avec ses fichiers d’entrée.
- Nous gardons les traces des commandes réellement exécutées.
- L’objectif n’est pas d’obtenir beaucoup de code. Pour notre ticket, il faudra surtout en enlever.
