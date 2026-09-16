# 7. Construire ses propres critères de choix

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Alternatives, logiciels libres et possibilités de s’en passer](../06-alternatives/LECTURE.md)

**TL;DR** — Une décision courte relie un besoin, des contraintes, une validation et une façon de revenir en arrière. Les critères bloquants passent avant la comparaison des options.

L’équipe aimerait « mettre de l’IA ». Demandons-lui quelque chose d’un peu plus utile : sur quelle tâche, pour quel résultat ?

## Ce qui se discute et ce qui bloque

Reprenez `cas/equipe.md`. Les incidents contiennent des données de clients ; aucun envoi vers un prestataire externe n’a été autorisé dans ce scénario. L’essai devra donc employer d’autres données, une autre configuration ou un autre périmètre, quelle que soit la vitesse annoncée.

![Des exigences bloquantes filtrent d’abord les options. Les options restantes sont comparées sur leurs résultats, leur coût complet et leurs effets sur l’apprentissage.](../images/decision.png)
Figure: Une contrainte ne disparaît pas dans une moyenne

Notre fiche commence donc par les exigences bloquantes, sans note sur cent à « l’éthique ». Une formule qui additionnerait prix, confidentialité et confort pourrait masquer une condition que l’équipe juge indispensable.

Écrivez d’abord les exigences : données autorisées, résultat vérifiable, budget de l’essai, personne capable de valider et possibilité de reprendre sans l’outil. Comparez ensuite les options qui restent. Les informations inconnues doivent apparaître comme telles, avec leur conséquence sur la décision.

Un désaccord peut porter sur une valeur plutôt que sur un chiffre manquant. Certaines personnes ne souhaitent pas utiliser un service pour des raisons liées au travail humain ou aux contenus employés. Écoutons ces raisons pour ce qu’elles sont : un benchmark de code ne leur répond pas.

## Écrire une décision que l’on peut appliquer

Ouvrez `fiches/decision.md`. Le document tient en quelques rubriques : besoin, option retenue, données, validation, limites, solution de repli et raison de réexaminer le choix.

Pour le catalogue, nous pouvons choisir les contrôles déterministes fournis dans `catalogue.py`. Lancez `python catalogue.py` : le fichier fictif contient trois lignes invalides et la commande sort avec le code 1 en indiquant les raisons. Le corrigé `corriges/catalogue.md` explique comment préparer une copie valide pour comparer. Pour la recette manuelle, nous pouvons essayer une aide à la rédaction sur les documents fictifs, en gardant une relecture et les arbitrages humains. Pour les incidents clients, nous pouvons reporter l’essai tant que le trajet des données et les droits nécessaires ne sont pas établis.

Le script, l’aide à la rédaction et le report de l’essai répondent à trois besoins différents. Vous trouverez cette proposition développée dans `corriges/decision.md` ; d’autres choix peuvent être défendables si leurs conditions sont explicites.

La décision doit aussi dire quand s’arrêter : si l’on ne sait pas vérifier le résultat, si la sortie exige plus de réparation que la procédure habituelle, ou si les données nécessaires dépassent le périmètre accepté. Écrire ces conditions à l’avance évite la boucle de demandes supplémentaires simplement parce que nous avons déjà passé l’après-midi dessus.

Enfin, choisissez ce qui déclenchera une nouvelle lecture de la décision : changement de modèle, de contrat, de données ou problème observé. Inutile de suivre chaque annonce ; surveillez ce qui change réellement votre usage.

## Garder la méthode que l’on peut expliquer

Au début du tutoriel, l’IA pouvait ressembler à une seule grande boîte. Nous avons ouvert plusieurs morceaux : des données, des calculs, un entraînement, un serveur, des outils, des procédures et des personnes qui vérifient le résultat.

Nous pouvons ainsi discuter des critiques sans les balayer. Comprendre le fonctionnement d’un modèle laisse entière la question de sa production et de sa commercialisation. On peut également critiquer cette organisation tout en expérimentant un petit réseau chez soi, en contribuant à un logiciel libre ou en utilisant ponctuellement une aide que l’on juge utile.

Ma méthode n’a pas vocation à devenir votre nouvelle obligation. Votre contexte, votre équipe et ce que vous aimez faire comptent. Vous pouvez reprendre une idée, modifier un skill, garder seulement un outil de recherche ou fermer l’assistant.

Si une expérience vous sert, gardez les fichiers et la raison de ce choix. Si elle échoue, gardez aussi ce qu’elle vous a appris. Dans les deux cas, nous aurons fait un peu mieux que choisir notre organisation de travail au nombre d’étoiles sur GitHub. 🙂

La fiche tient en quelques rubriques, mais elle conserve l’essentiel : l’usage précis, les personnes concernées, la façon de vérifier et les conditions d’arrêt. Refermons maintenant le tutoriel avec ce que ces huit parties nous permettent de choisir.

---

[Précédent : Alternatives, logiciels libres et possibilités de s’en passer](../06-alternatives/LECTURE.md)
