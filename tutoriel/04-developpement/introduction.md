**TL;DR** — Nous allons corriger un petit programme avec l’aide d’un agent : observer le problème, écrire un test qui le reproduit, faire la modification et vérifier le résultat. Un seul dossier de travail nous suivra jusqu’au bout.

Les trois tests passent. Pourtant, notre suivi de prix annonce une bonne affaire… alors que le prix n’a pas baissé. Voilà un programme un peu trop enthousiaste. 😅

Nous allons lui retirer cette habitude. La correction sera petite, ce qui nous laissera le temps de comprendre ce que l’agent fait autour : les fichiers qu’il lit, les tests qu’il écrit et les commandes qu’il lance.

Dans la partie précédente, nous faisions tourner un modèle chez nous. Pour cet atelier, nous utiliserons un assistant de développement avec un modèle hébergé. Vous n’avez donc pas besoin d’une grosse carte graphique. Si vous avez déjà un assistant, gardez-le ; sinon, nous décrirons une installation avec VS Code et GitHub Copilot. L’accès gratuit dépend de votre compte et de son quota.

Il vous faut savoir ouvrir un terminal, lancer un programme Python et lire une fonction simple. Le projet utilise Python 3.12 et sa bibliothèque standard. Nous expliquerons les assertions de test et la condition qui nous intéressent.

Les **sept premiers chapitres** suivent l’atelier. Le chapitre [« Référence — comparer les outils et leurs tarifs »](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/04-developpement/comparatif/LECTURE.md) rassemble le panorama complet, dont Pi : vous pouvez le consulter dès maintenant pour choisir votre outil, puis revenir à l’installation. L’**expérience locale avec Continue**, à la fin, est facultative et reste à vérifier sur machine ; elle ne remplace pas un parcours d’agent validé.

Les fichiers du projet sont publics et le ticket est fictif. Nous pouvons les montrer au service choisi sans utiliser le code de notre entreprise. Si vous préférez travailler sans IA, les tests et les corrections expliquées permettent aussi de suivre l’exercice.
