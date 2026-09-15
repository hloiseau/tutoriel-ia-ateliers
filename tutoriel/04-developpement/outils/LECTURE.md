# 1. Choisir de quoi suivre l’atelier

[Sommaire de la partie](../README.md) · [Sources](.)

[Suivant : Installer l’assistant et observer le problème](../installer/LECTURE.md)

**TL;DR** — Pour l’atelier, il nous faut discuter du code, modifier un fichier et lire le résultat des tests. Gardez un assistant qui sait déjà le faire ; sinon, nous allons préparer VS Code avec Copilot.

Avant l’installation, réglons deux questions : à qui allons-nous montrer le code, et qui exécutera les commandes ?

## Où tournent le code et le modèle ?

Notre client de la partie précédente envoyait une question à `llama-server`, qui faisait calculer la réponse par le modèle. Un assistant de développement ajoute notamment les fichiers du projet à cette conversation.

Il faut distinguer **l’endroit où l’assistant agit** et **l’endroit où le modèle tourne**. Dans l’installation que nous allons utiliser, l’éditeur et les tests tournent sur notre ordinateur. Le modèle, lui, reçoit le contexte et calcule sa réponse chez le fournisseur.

| Élément | Dans l’atelier |
| --- | --- |
| Projet et tests Python | Sur notre ordinateur |
| Assistant | Dans l’éditeur, avec accès à notre copie de travail |
| Modèle et moteur d’inférence | Chez le fournisseur du modèle |
Table: Où se passe le travail ?

C’est pour cela que cette installation ne demande pas de GPU. Faire également tourner le modèle chez soi est une autre possibilité, avec des besoins de mémoire et de calcul à évaluer. Un petit modèle qui répond sur CPU ne devient pas un agent de code efficace simplement parce qu’on le branche à l’éditeur.

## Discuter, puis laisser agir

La complétion suggère du code pendant que vous tapez. Nous allons surtout utiliser deux autres fonctions :

- **La discussion** : nous montrons une fonction et demandons une explication. Nous lisons la réponse en gardant le code sous les yeux.
- **Le mode agent** : le modèle peut demander au logiciel de lire ou modifier des fichiers et de lancer des commandes. Les résultats lui reviennent, ce qui lui permet de poursuivre.

Le programme qui organise ces échanges est souvent appelé **harness**. Copilot, Codex, Claude Code, Pi et d’autres proposent leur propre manière de le faire. Nous comparerons leurs possibilités dans le chapitre de référence.

Pour commencer, nous resterons en discussion. Nous passerons au mode agent au moment d’écrire notre premier test. Vous verrez ainsi ce qui change quand l’outil peut agir sur les fichiers.

## Quel outil prendre pour commencer ?

Vous utilisez déjà un assistant capable de lire et modifier un projet ? Gardez-le. Les demandes de l’atelier portent sur des fichiers et des commandes Python ; elles ne dépendent pas d’une marque.

Sinon, nous prendrons **VS Code avec GitHub Copilot** comme exemple d’installation. D’autres possibilités figurent dans le [comparatif complet](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/04-developpement/comparatif/LECTURE.md) : éditeurs, agents en terminal, choix du modèle, prix et limites des offres. Ce comparatif est daté de septembre 2026.

Avant de vous connecter, vérifiez deux points :

- Le service peut-il recevoir ces fichiers ? Pour notre petit projet public, oui. Pour votre code professionnel, il faudra connaître les règles de votre équipe.
- Quel accès avez-vous au modèle ? Une offre gratuite peut avoir un quota. Un logiciel libre peut, lui, utiliser une API payante. Le prix du logiciel ne donne donc pas toujours le coût de la tâche.

Copilot propose une offre gratuite sous conditions et avec des limites[^p4-depart-offre]. Si elle n’est pas disponible pour votre compte, vous pouvez utiliser un autre accès que vous possédez ou suivre les corrections expliquées sans agent. Nous n’allons pas vous demander de souscrire pour ouvrir trois fichiers Python. 🙂

[^p4-depart-offre]: GitHub, [offres et limites de Copilot](https://github.com/features/copilot/plans).



---

[Suivant : Installer l’assistant et observer le problème](../installer/LECTURE.md)
