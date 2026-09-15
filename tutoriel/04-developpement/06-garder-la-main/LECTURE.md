# 7. Garder un changement que l’on sait expliquer

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Vérifier au-delà de la dernière ligne verte](../05-verifier/LECTURE.md)

**TL;DR :** préparez une trace courte du problème, de la correction et des vérifications. Puis choisissez où l’aide vous a réellement été utile.

## Écrire un compte rendu exploitable

Créez un fichier `COMPTE-RENDU.md` et renseignez-le avec votre propre exécution :

```markdown
# PRIX-1 — Ne plus notifier une simple remise en stock

## Problème

Le retour en stock autorisait une notification même sans baisse de prix.

## Changement

La décision exige une disponibilité actuelle et une baisse stricte.
Les interfaces et les validations des entrées sont conservées.

## Vérifications effectuées

- Commande de tests, dossier d’exécution, nombre de tests et résultat :
- Scénario retour en stock, résultat observé :
- Scénario baisse de prix, résultat observé :
- Scénario indisponible, résultat observé :

## Limites

Le programme calcule une décision. Il n’envoie pas de notification.
Il compare deux observations dans une même devise implicite.
```
Code: Une trame à compléter avec vos résultats

Indiquez « non exécuté » pour les scénarios que vous n’avez pas lancés.

Ce texte peut ensuite servir de base à une description de pull request dans un vrai projet. Avant de publier, relisez les fichiers et les traces jointes : un rapport de test peut lui aussi contenir des données qu’on ne souhaite pas diffuser.

L’agent peut rédiger ce compte rendu à partir des sorties conservées. Vous gardez à vérifier que les phrases correspondent aux commandes effectivement réalisées.

## Quand on apprend encore à développer

Si vous découvrez Python, vous avez peut-être eu envie de demander directement la version finale. Mais pourriez-vous ensuite expliquer pourquoi le `or` posait problème ?

Fermez la correction et essayez de prédire le résultat de deux cas : un retour en stock avec hausse, puis une baisse d’un centime sur un produit disponible. Vérifiez vos réponses en exécutant le programme.

Si vous vous trompez, ce n’est pas une raison de renoncer à l’aide. Demandez une explication de l’expression booléenne, construisez une table de valeurs ou réduisez l’exemple à deux booléens. Vous pouvez vous servir du modèle pour trouver une autre explication sans lui confier immédiatement toute la modification.

Pour apprendre, une bonne utilisation consiste souvent à demander un indice, un contre-exemple ou une question de vérification. Une solution complète trop tôt peut vous faire sauter exactement l’effort dont vous aviez besoin pour comprendre.

Et certains jours, le plus efficace sera de fermer l’agent et de lire la fonction tranquillement. Il n’y a rien à rentabiliser à chaque ligne.

## Trouver ses propres points de friction

Reprenez les étapes de cet atelier et demandez-vous lesquelles vous ont posé problème. Comprendre la règle ? Retrouver la fonction ? Penser aux cas limites ? Écrire la syntaxe de `unittest` ? Relire le diff ?

L’aide n’a pas le même intérêt partout. Si vous aimez écrire le code mais que préparer une recette vous prend un temps fou, vous pouvez garder le code et demander une première liste de scénarios. Si vous connaissez bien les tests mais découvrez un langage, une explication ciblée peut être plus utile qu’une implémentation complète.

Pour comparer deux façons de travailler, notez le temps total, y compris les corrections de demandes, la lecture des résultats et la validation. Le temps pendant lequel l’agent produit du texte n’est qu’une partie du travail.

N’ajoutez pas automatiquement un framework ou une série de commandes pour reproduire cet atelier. Nous avons séparé des étapes afin de voir ce qu’elles vérifient. Dans votre quotidien, regroupez ou simplifiez ce qui peut l’être, tout en conservant les contrôles nécessaires au changement.

Vous pouvez aussi conclure que l’outil ne vous aide pas sur ce type de tâche. Adapter un outil à son besoin comprend cette possibilité.

Notre correction tient en peu de caractères, mais nous savons maintenant quel cas elle change et comment le vérifier. Gardez votre copie de travail et votre compte rendu.

L’atelier s’arrête ici. Le comparatif qui suit sert à choisir d’autres outils ; l’expérience locale permet d’explorer une autre installation. Dans la prochaine partie, nous regarderons plus précisément comment les agents choisissent leurs actions et comment encadrer ce travail.

---

[Précédent : Vérifier au-delà de la dernière ligne verte](../05-verifier/LECTURE.md)
