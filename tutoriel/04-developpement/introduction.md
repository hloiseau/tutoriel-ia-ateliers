**TL;DR** — Nous allons suivre un correctif de bout en bout avec l’aide d’un agent : observer le problème, l’enfermer dans un test, modifier le code puis vérifier le résultat. Nous garderons le même dossier de travail jusqu’au compte rendu final.

Les trois tests passent. Pourtant, notre suivi de prix annonce une bonne affaire… alors que le prix n’a pas baissé. Voilà un programme un peu trop enthousiaste. 😅

Nous allons lui retirer cette habitude. La correction tient presque sur un timbre-poste ; tout ce qui permet de lui faire confiance prend un peu plus de place. Nous suivrons les fichiers lus par l’agent, les tests qu’il écrit, les commandes qu’il lance et le diff qu’il nous rend.

Dans la partie précédente, nous faisions tourner un modèle chez nous. Pour cet atelier, nous utiliserons un assistant de développement avec un modèle hébergé. Vous n’avez donc pas besoin d’une grosse carte graphique. Si vous avez déjà un assistant, gardez-le ; sinon, nous décrirons une installation avec VS Code et GitHub Copilot. L’accès gratuit dépend de votre compte et de son quota.

Il vous faut savoir ouvrir un terminal, lancer un programme Python et lire une fonction simple. Le projet utilise Python 3.12 et sa bibliothèque standard. Nous expliquerons les assertions de test et la condition qui nous intéressent.

Les **sept chapitres de cette partie** suivent ce même correctif. Si vous hésitez encore entre plusieurs assistants, l’annexe [« Comparer les outils et leurs tarifs »](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/annexes/comparatif/LECTURE.md) rassemble le panorama complet, dont Pi. L’**expérience locale avec Continue** se trouve également dans les annexes. Elle reste à vérifier sur machine et porte sur une discussion avec un modèle local, pas sur une session complète d’agent de code.

Les fichiers du projet sont publics et le ticket est fictif. Nous pouvons les montrer au service choisi sans utiliser le code de notre entreprise. Si vous préférez travailler sans IA, les tests et les corrections expliquées permettent aussi de suivre l’exercice.
