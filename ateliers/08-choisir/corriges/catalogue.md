# Contrôle du catalogue fictif

La ligne 1 est valide. La ligne 2 contient un prix négatif ; la ligne 3 n’a pas d’identifiant ; la ligne 4 emploie `true` comme prix. En Python, un booléen se comporte aussi comme un entier dans certains contrôles : ici, `type(prix) is int` l’exclut explicitement.

Pour tester une copie valide, donner à B le prix entier 50, à la ligne 3 l’identifiant C et à D le prix entier 100. Ce sont des valeurs d’exercice, pas une méthode pour deviner des prix manquants en production. Le contrôle doit alors afficher zéro ligne invalide et sortir avec le code 0.

Dans un vrai traitement, une donnée incorrecte doit être corrigée depuis une source autorisée ou rejetée selon la règle du projet. Remplacer silencieusement un prix négatif par sa valeur absolue pourrait masquer un autre problème.
