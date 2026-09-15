Claude Shannon étudie dès 1950 comment programmer un ordinateur pour jouer aux échecs. Le jeu fournit un terrain bien défini : on connaît les pièces, les coups autorisés et les conditions de fin de partie.[^h2s2-shannon]

Pour choisir un coup, on peut examiner les réponses possibles de l’adversaire, puis nos réponses à ces réponses. Le problème est que les possibilités se multiplient très vite.

Imaginons que chaque position n’offre que trois choix :

![Un arbre de possibilités passe de trois choix à neuf, puis à vingt-sept en trois étapes.](image:images/arbre-recherche.png)
Figure: Trois choix à chaque étape donnent 3, puis 9, puis 27 possibilités au niveau suivant. Ce ne sont pas des nombres mesurés sur une partie d’échecs.

Chaque petit cercle en bas peut encore ouvrir de nouvelles branches. Vous voyez pourquoi « il suffit de tout essayer » risque de prendre un peu de temps. 🙂

Shannon propose de limiter la recherche et d’évaluer les positions obtenues. Le programme peut, par exemple, tenir compte des pièces disponibles et de leur disposition. Il cherche ainsi un coup intéressant sans calculer toute la partie à l’avance.

Les recherches sur les jeux vont continuer pendant des décennies. Elles réunissent des questions qui concernent aussi d’autres problèmes : représenter une situation, prévoir les conséquences d’une action et choisir avec des ressources limitées.


[^h2s2-shannon]: [Claude Shannon, Programming a Computer for Playing Chess (1950)](https://www.computerhistory.org/chess/doc-431614f453dde/).
