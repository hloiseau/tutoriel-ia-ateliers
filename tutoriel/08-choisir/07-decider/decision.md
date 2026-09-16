Ouvrez `fiches/decision.md`. Le document tient en quelques rubriques : besoin, option retenue, données, validation, limites, solution de repli et raison de réexaminer le choix.

Pour le catalogue, nous pouvons choisir les contrôles déterministes fournis dans `catalogue.py`. Lancez `python catalogue.py` : le fichier fictif contient trois lignes invalides et la commande sort avec le code 1 en indiquant les raisons. Le corrigé `corriges/catalogue.md` explique comment préparer une copie valide pour comparer. Pour la recette manuelle, nous pouvons essayer une aide à la rédaction sur les documents fictifs, en gardant une relecture et les arbitrages humains. Pour les incidents clients, nous pouvons reporter l’essai tant que le trajet des données et les droits nécessaires ne sont pas établis.

Le script, l’aide à la rédaction et le report de l’essai répondent à trois besoins différents. Vous trouverez cette proposition développée dans `corriges/decision.md` ; d’autres choix peuvent être défendables si leurs conditions sont explicites.

La décision doit aussi dire quand s’arrêter : si l’on ne sait pas vérifier le résultat, si la sortie exige plus de réparation que la procédure habituelle, ou si les données nécessaires dépassent le périmètre accepté. Écrire ces conditions à l’avance évite la boucle de demandes supplémentaires simplement parce que nous avons déjà passé l’après-midi dessus.

Enfin, choisissez ce qui déclenchera une nouvelle lecture de la décision : changement de modèle, de contrat, de données ou problème observé. Inutile de suivre chaque annonce ; surveillez ce qui change réellement votre usage.
