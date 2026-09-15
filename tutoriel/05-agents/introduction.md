**TL;DR** — Nous allons suivre les appels d’outils, choisir ce qui entre dans le contexte et observer ce qui arrête réellement une action. Puis nous préparerons une reprise de session et un relevé de coût.

Dans la partie précédente, nous avons demandé à un agent d’ajouter des tests et de corriger une fonction. Il a fallu lire ce qu’il produisait. Maintenant, regardons aussi ce qui se passe **entre notre demande et les fichiers modifiés**.

Quand l’agent annonce qu’il va lancer les tests, qui les lance ? Quand il lit une consigne dans un fichier, doit-il la suivre ? Et s’il répète la même action sans avancer, combien de temps le laissons-nous continuer ?

Nous garderons l’assistant choisi pour la partie 4. Pour les incidents que nous voulons reproduire à coup sûr, nous utiliserons aussi un petit banc Python : il rejoue des demandes d’outils écrites à la main. Il ne contient pas de modèle. Nous pourrons donc observer un refus ou une limite d’appels sans attendre qu’une IA se trompe exactement comme prévu.

Il faut Python 3.12 et savoir lire les petits fichiers de l’atelier précédent. Aucun nouveau service ni GPU n’est nécessaire pour le banc. Les observations avec votre assistant utilisent, elles, votre accès au modèle habituel.
