# 7. Garder un changement que l’on sait expliquer

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Vérifier au-delà de la dernière ligne verte](../05-verifier/LECTURE.md)

**TL;DR** — Gardez une trace courte du problème, du diff et des vérifications réellement exécutées. Vous pourrez ensuite décider à quelles étapes l’aide vous a servi.

## Écrire un compte rendu exploitable

Créez un fichier `COMPTE-RENDU.md` dans `mon-suivi` et renseignez-le avec votre propre exécution :

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

Ce texte peut servir de base à une description de pull request dans un vrai projet. Avant de publier, relisez les fichiers et les traces jointes : un rapport de test peut lui aussi contenir des données qu’on ne souhaite pas diffuser.

L’agent peut rédiger ce compte rendu à partir des sorties conservées. Comparez ensuite chaque affirmation aux commandes effectivement réalisées ; « treize tests passent » réclame une sortie de treize tests, pas un souvenir de la consigne.

## Quand on apprend encore à développer

Si vous découvrez Python, la version finale donnée tout de suite est tentante. Fermez-la un instant : pourriez-vous expliquer pourquoi le `or` autorisait une alerte lorsque le prix montait ?

Fermez la correction et essayez de prédire le résultat de deux cas : un retour en stock avec hausse, puis une baisse d’un centime sur un produit disponible. Vérifiez vos réponses en exécutant le programme.

En cas d’erreur, demandez une explication de l’expression booléenne, construisez une table de valeurs ou réduisez l’exemple à deux booléens. Le modèle peut proposer un autre angle sans recevoir aussitôt la modification entière.

Pour apprendre, une bonne utilisation consiste souvent à demander un indice, un contre-exemple ou une question de vérification. Une solution complète trop tôt peut vous faire sauter exactement l’effort dont vous aviez besoin pour comprendre.

Et certains jours, le plus efficace sera de fermer l’agent et de lire la fonction tranquillement. Vous n’avez rien à rentabiliser à chaque ligne.

## Trouver ses propres points de friction

Reprenez les étapes de cet atelier et demandez-vous lesquelles vous ont posé problème. Comprendre la règle ? Retrouver la fonction ? Penser aux cas limites ? Écrire la syntaxe de `unittest` ? Relire le diff ?

L’aide n’a pas le même intérêt partout. Vous pouvez aimer écrire le code et détester préparer une recette : dans ce cas, gardez l’implémentation et demandez une première liste de scénarios. Si vous connaissez les tests mais découvrez le langage, une explication ciblée vous apprendra souvent davantage qu’une implémentation complète.

Pour comparer deux façons de travailler, notez le temps total, y compris les corrections de demandes, la lecture des résultats et la validation. Le temps pendant lequel l’agent produit du texte n’est qu’une partie du travail.

N’ajoutez pas automatiquement un framework ou une série de commandes pour reproduire cet atelier. Nous avons séparé des étapes afin de voir ce qu’elles vérifient. Dans votre quotidien, regroupez ou simplifiez ce qui peut l’être, tout en conservant les contrôles nécessaires au changement.

Vous pouvez aussi conclure que l’outil ne vous aide pas sur ce type de tâche. S’en passer est encore une manière parfaitement valable d’adapter sa méthode.

Notre correction tient en peu de caractères. Nous pouvons pourtant expliquer le bug, montrer le test qui l’a fait apparaître, lire le diff et citer les vérifications exécutées. Gardez `mon-suivi` et son compte rendu : la partie suivante repartira de ce projet.

Les annexes restent disponibles pour comparer d’autres outils ou préparer l’expérience locale. Dans la prochaine partie, nous reprendrons l’agent au moment où il demande à lire un fichier ou lancer une commande. Nous pourrons alors séparer sa demande, l’autorisation du logiciel et le résultat renvoyé au modèle.

---

[Précédent : Vérifier au-delà de la dernière ligne verte](../05-verifier/LECTURE.md)
