# Relecture de la partie 1 — Une histoire de l’IA

Session : `2026-09-16-globale`  
Commit de départ : `102e5ccf29bff571da46bcdae0a51a5b1d089f95`  
Mode : répertoire partagé, sans commit ni régénération

## Fichiers modifiés

- `tutoriel/01-histoire/introduction.md`
- `tutoriel/01-histoire/01-origines/introduction.md`
- `tutoriel/01-histoire/01-origines/babbage-lovelace.md`
- `tutoriel/01-histoire/01-origines/dartmouth.md`
- `tutoriel/01-histoire/01-origines/conclusion.md`
- `tutoriel/01-histoire/02-regles/logique.md`
- `tutoriel/01-histoire/02-regles/eliza.md`
- `tutoriel/01-histoire/03-apprendre/introduction.md`
- `tutoriel/01-histoire/03-apprendre/apprentissage.md`
- `tutoriel/01-histoire/03-apprendre/plusieurs-couches.md`
- `tutoriel/01-histoire/04-promesses/limites.md`
- `tutoriel/01-histoire/04-promesses/experts.md`
- `tutoriel/01-histoire/04-promesses/cycles.md`
- `tutoriel/01-histoire/05-deep-learning/deep-blue.md`
- `tutoriel/01-histoire/05-deep-learning/autres-methodes.md`
- `tutoriel/01-histoire/05-deep-learning/imagenet.md`
- `tutoriel/01-histoire/05-deep-learning/alexnet.md`
- `tutoriel/01-histoire/06-generatif/attention.md`
- `tutoriel/01-histoire/06-generatif/langage.md`
- `tutoriel/01-histoire/06-generatif/donnees.md`
- `tutoriel/01-histoire/07-aujourdhui/agents.md`
- `tutoriel/01-histoire/07-aujourdhui/mcp-skills.md`
- `tutoriel/01-histoire/07-aujourdhui/modeles-locaux.md`
- `tutoriel/01-histoire/07-aujourdhui/raisonnement.md`
- `tutoriel/01-histoire/07-aujourdhui/choisir.md`
- `tutoriel/01-histoire/conclusion.md`

Le présent rapport est le seul autre fichier modifié. Aucun `LECTURE.md`, manifest, crédit, image, script ou ZIP n’a été touché.

## Améliorations majeures

La structure, les dates, les illustrations et la progression de la V3 validée ont été conservées. La passe intervient à l’échelle de phrases et de raccords : elle rend les objets historiques plus présents, retire plusieurs réserves formulées mécaniquement et évite de raconter l’histoire comme une suite de remplacements complets d’une méthode par une autre.

Exemples représentatifs :

- Avant : « Les recherches n’ont pas toutes commencé cet été-là, mais elles sont réunies sous un nom et un projet commun. »  
  Après : « Plusieurs des recherches qu’elle rassemble existaient déjà ; elles disposent désormais d’un nom et d’un projet commun. »
- Avant : « Cela ne veut pas dire que tous les laboratoires ferment ni que tous les chercheurs s’arrêtent. »  
  Après : « Le froid n’atteint pas tous les laboratoires de la même manière : à Édimbourg, des travaux et des enseignements se poursuivent… »
- Avant : « Le résultat ne signifie pas que Deep Blue peut discuter de n’importe quel sujet… »  
  Après : le passage nomme d’abord la performance — gagner un match d’échecs — puis précise que le match n’évalue ni la discussion générale ni l’apprentissage d’un métier.
- Avant : « Un modèle qui produit une commande n’a pas, pour autant, exécuté cette commande. »  
  Après : « Supposons qu’un modèle produise la commande `pytest`. » Le texte suit ensuite les opérations concrètes nécessaires à son exécution.
- Avant : la partie se terminait sur les composants des systèmes actuels.  
  Après : la conclusion annonce l’image de huit pixels, les poids et le petit modèle que le lecteur entraînera dans la partie 2.

Autres changements notables :

- l’exemple musical de Babbage et Lovelace reste explicitement hypothétique ;
- la généralisation est introduite à partir des fruits gardés à part, sans prendre la forme d’une maxime abstraite ;
- le travail humain d’ImageNet et des systèmes experts apparaît dans les actions réalisées ;
- les distinctions utiles restent présentes : scripts d’ELIZA et modèles de langage, distillation et quantification, poids disponibles et autres éléments d’ouverture, exécution et entraînement ;
- les positions de l’auteur sur les juniors et la possibilité de se passer d’IA gardent leur netteté.

## Raccords et répétitions entre parties

- Le nouveau dernier paragraphe de la partie 1 rejoint précisément l’ouverture de la partie 2 (image de huit pixels, poids, calcul d’une réponse). Il faut conserver ce raccord lors de l’harmonisation globale.
- Le chapitre 7 introduit volontairement les agents, MCP, skills et modèles locaux avant leurs parties pratiques. Les parties 3, 5 et 6 peuvent entrer rapidement dans l’usage au lieu de refaire leur historique ; la courte définition donnée ici doit rester un repère, pas devenir un second mode d’emploi.
- La mise en garde destinée aux juniors apparaît déjà dans `07-aujourdhui/choisir.md` et dans l’introduction générale. Elle est légitime ici parce qu’elle tire une conséquence de l’histoire, mais le coordinateur peut surveiller sa répétition mot pour mot dans les parties 4, 5 et 8.

## Faits, sources et vérifications restantes

Aucune date, attribution ou portée historique n’a été corrigée pendant cette passe. Les notes existantes et `sources.json` ont été conservés. Les reformulations de Deep Blue, Dartmouth, ImageNet et des hivers de l’IA restent dans le périmètre exact des sources déjà citées.

La distinction entre distillation et quantification est désormais formulée positivement : la première fait intervenir un modèle pour en aider un autre pendant son entraînement ; la seconde réduit la précision numérique des poids. Cette modification explicite une distinction technique déjà présente, sans attribuer une nouvelle expérience au tutoriel.

La page publique du tutoriel Vim a été demandée à l’outil de consultation, mais l’accès à cette URL était restreint dans l’environnement. La relecture s’appuie donc sur l’analyse détaillée et les exemples du `GUIDE-VOIX-HUGO.md`, pas sur une prétendue nouvelle lecture du tutoriel en ligne.

Reste à vérifier au niveau global : l’import interactif dans ZdS et le rendu après régénération. Aucun besoin de modification d’image, de manifest ou de code n’a été relevé pour cette partie.

## Contrôles réalisés

- lecture intégrale du guide de voix, de la mission, du sommaire, de l’état des contenus et du manifest ;
- lecture intégrale de toutes les sources canoniques de la partie dans l’ordre du manifest, de `README.md`, `CREDITS.md` et `sources.json` ;
- lecture de l’introduction générale, de l’introduction de la partie 2 et du début de son premier chapitre ;
- relecture du diff et recherche des motifs répétitifs demandés ; une occurrence humoristique naturelle de « ne fait pas grand-chose… mais » a été conservée dans le passage sur le neurone de 1943 ;
- contrôle que tous les fichiers de cours modifiés sont déclarés par `tutoriel/01-histoire/manifest.json` ;
- `git diff --check -- tutoriel/01-histoire` : succès.

Les lectures et archives n’ont pas été régénérées, conformément à la répartition de la mission.

## Points bloquants

Aucun point bloquant pour l’intégration. Le seul contrôle impossible dans cet environnement est la consultation directe du tutoriel Vim ; cela ne nécessite pas de suspendre la réécriture, puisque le guide en consigne déjà les enseignements utiles.
