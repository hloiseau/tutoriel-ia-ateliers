# 1. Choisir de quoi suivre l’atelier

[Sommaire de la partie](../README.md) · [Sources](.)

[Suivant : Installer l’assistant et observer le problème](../installer/LECTURE.md)

**TL;DR** — Pour l’atelier, il nous faut discuter du code, modifier un fichier et lire le résultat des tests. Gardez un assistant qui sait déjà le faire ; sinon, nous allons préparer VS Code avec Copilot.

Avant d’ouvrir l’éditeur, suivons le trajet de notre code. Cela permettra de savoir ce qui reste sur notre machine, ce qui part vers le fournisseur du modèle et quel logiciel exécutera les commandes.

## Où tournent le code et le modèle ?

Dans la partie précédente, notre client envoyait une question à `llama-server`, puis le modèle calculait une réponse. Un assistant de développement reprend ce principe en y ajoutant du code, des résultats de commandes et parfois le droit de modifier les fichiers.

Il faut distinguer **l’endroit où l’assistant agit** et **l’endroit où le modèle tourne**. Dans l’installation que nous allons utiliser, l’éditeur et les tests tournent sur notre ordinateur. Le modèle, lui, reçoit le contexte et calcule sa réponse chez le fournisseur.

| Élément | Dans l’atelier |
| --- | --- |
| Projet et tests Python | Sur notre ordinateur |
| Assistant | Dans l’éditeur, avec accès à notre copie de travail |
| Modèle et moteur d’inférence | Chez le fournisseur du modèle |
Table: Où se passe le travail ?

Le calcul lourd ayant lieu chez le fournisseur, cette installation ne demande pas de GPU. On peut aussi faire tourner le modèle chez soi, avec des besoins de mémoire et de calcul à évaluer. Obtenir une réponse courte sur CPU ne suffit pas à établir qu’un modèle soutiendra le rythme et le contexte d’une session d’agent de code.

## Discuter, puis laisser agir

La complétion suggère du code pendant que vous tapez. Nous allons surtout utiliser deux autres fonctions :

- **La discussion** : nous montrons une fonction et demandons une explication. Nous lisons la réponse en gardant le code sous les yeux.
- **Le mode agent** : le modèle peut demander au logiciel de lire ou modifier des fichiers et de lancer des commandes. Les résultats lui reviennent, ce qui lui permet de poursuivre.

Le programme qui organise ces échanges est souvent appelé **harness**. Copilot, Codex, Claude Code, Pi et d’autres ont chacun leur manière d’assembler la conversation, les fichiers et les outils. Le détail de leurs possibilités reste dans l’annexe comparative ; notre correctif, lui, ne dépend d’aucune fonction exotique.

Nous commencerons par une discussion autour d’une fonction copiée dans le chat. Le mode agent n’arrivera qu’avec le premier test : à cet instant, l’assistant devra réellement créer un fichier et exécuter Python.

## Quel outil prendre pour commencer ?

Vous utilisez déjà un assistant capable de lire et modifier un projet ? Gardez-le. Les demandes de l’atelier portent sur des fichiers et des commandes Python ; elles ne dépendent pas d’une marque.

Sinon, nous prendrons **VS Code avec GitHub Copilot** comme exemple d’installation. Ce choix nous donne un parcours concret à décrire ; il ne change pas l’atelier en tutoriel consacré à Copilot. Le [comparatif complet](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/annexes/comparatif/LECTURE.md), daté de septembre 2026, couvre aussi des éditeurs et des agents en terminal, avec leurs modèles, leurs prix et les limites de leurs offres.

Avant de vous connecter, vérifiez deux points :

- Le service peut-il recevoir ces fichiers ? Pour notre petit projet public, oui. Pour votre code professionnel, il faudra connaître les règles de votre équipe.
- Quel accès avez-vous au modèle ? Une offre gratuite peut avoir un quota. Un logiciel libre peut, lui, utiliser une API payante. Le prix du logiciel ne donne donc pas toujours le coût de la tâche.

Copilot propose une offre gratuite sous conditions et avec des limites[^p4-depart-offre]. Si elle n’est pas disponible pour votre compte, vous pouvez utiliser un autre accès que vous possédez ou suivre les corrections expliquées sans agent. Nous n’allons pas vous demander de souscrire pour ouvrir trois fichiers Python. 🙂

[^p4-depart-offre]: GitHub, [offres et limites de Copilot](https://github.com/features/copilot/plans).



---

[Suivant : Installer l’assistant et observer le problème](../installer/LECTURE.md)
