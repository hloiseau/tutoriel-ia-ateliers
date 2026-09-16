# Mission locale — partie 4, suivre un vrai atelier de développement

Applique le [prompt coordinateur](../LOCAL-COORDINATEUR.md). Lis `tutoriel/04-developpement/VERIFICATION.md`, les sept chapitres et `ateliers/04-developpement/README.md`. Les comparatifs détaillés et l’essai local facultatif sont dans `tutoriel/annexes/`.

## 1. Vérifier le parcours déterministe

Travaille dans une copie de `ateliers/04-developpement/atelier-developpement/01-depart`. Reproduis le bug et suis l’ajout des tests avant la correction. Les états fournis servent à vérifier la progression : trois tests initiaux ; suite complète de treize tests avec deux échecs avant correction ; treize réussites après correction. Si les sources ont changé depuis la rédaction de ce prompt, établis et documente la nouvelle référence au lieu de forcer ces nombres.

Rejoue les cas JSON, notamment le retour en stock avec baisse de prix. Reproduis les deux mutations prévues dans des copies distinctes. Vérifie que les tests échouent pour la bonne raison ; ne casse pas le code syntaxiquement pour obtenir un échec facile.

Vérifie la continuité du texte : outil choisi avant usage, répertoire courant, fichiers conservés d’un chapitre à l’autre, observation du premier test rouge, interprétation du diff et verdict final. Signale toute étape que tu as dû deviner.

## 2. Observer un assistant réel

Prépare une nouvelle copie de l’état initial. Donne au véritable assistant le ticket et les éléments prévus dans le chapitre. Ne lui joins pas le corrigé et ne le laisse pas lire les autres étapes du dépôt avant sa réponse. Si le produit ouvre tout le dépôt par défaut, isole le dossier de l’exercice.

Conserve la demande exacte, l’outil, le modèle si exposé, les fichiers disponibles, les actions, les commandes, les résultats des tests et le diff final. Préserve les tentatives ratées et les interventions humaines. Évalue la solution produite avec les critères du ticket et les tests prévus après sa production.

Le fait de lancer les trois états fournis ne prouve pas qu’un agent les a créés. Ton Codex local peut constituer l’assistant réellement observé, mais son résultat ne valide pas l’interface de VS Code/Copilot.

## 3. Vérifier les interfaces documentées

Si l’installation et les accès le permettent, rejoue le parcours VS Code/Copilot : session Local, passage Ask vers Agent, choix des outils, affichage des actions et comparaison documentée avec le presse-papiers. Relève les versions et noms effectivement affichés. Consulte la documentation officielle de cette version lorsqu’une étape diffère ; ne prétends pas avoir cliqué dans une interface sur la seule base de sa documentation.

Préserve les réglages existants, les comptes et les autres projets. Si une connexion humaine est nécessaire, indique l’étape puis poursuis le travail autonome. N’ouvre pas de nouvel abonnement.

L’expérience Continue avec serveur local, puis le modèle CPU proposé dans l’annexe, est facultative. Elle teste une discussion sur du code : mesure le délai et la correction de la réponse. Elle ne valide pas un agent capable de mener tout le projet sur CPU. Ne rends pas cette variante obligatoire pour suivre les chapitres.

## Livrable

Distingue dans le rapport : scripts et tests rejoués ; résolution observée par un assistant ; interfaces réellement manipulées ; variantes non exécutées. Donne les étapes corrigées et les captures utiles expurgées. Les versions et tarifs d’autres outils feront l’objet de leur propre vérification documentaire ; il n’est pas nécessaire de les installer tous pour cette mission.
