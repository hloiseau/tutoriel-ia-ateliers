# 3. Écrire des consignes que l’on peut contrôler

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Donner le contexte utile à l’étape en cours](../02-contexte/LECTURE.md) · [Suivant : Observer un refus qui ne dépend pas du modèle](../04-permissions/LECTURE.md)

**TL;DR** — Une consigne utile nomme l’action, les limites et le résultat à examiner. Nous allons transformer une demande vague, puis vérifier son effet sur un petit cas.

## De « fais attention » à une action précise

Voici une demande difficile à contrôler :

> Regarde le code, fais attention aux cas limites et assure-toi que tout est bon.

Qu’est-ce qui nous permettra de dire que le travail est terminé ? Le modèle peut répondre par un commentaire très rassurant sans avoir fait ce que nous attendions.

Pour notre projet, nous pouvons écrire :

```text
Lis la fonction notifier et les tests qui l’appellent.
Cherche si le retour en stock avec hausse de prix est couvert.
S’il existe, cite le test et sa valeur attendue.
Sinon, propose un test qui appelle notifier sur ce cas.
Ne modifie pas les fichiers. Ne prétends pas avoir exécuté la suite.
```

Les verbes sont impératifs et le résultat est vérifiable. L’agent doit retrouver un cas précis ou en proposer un. Il n’a pas à deviner ce que « tout est bon » voulait dire.

Gardez les demandes courtes tant que le travail l’est. Une longue liste d’interdictions sans rapport rend aussi plus difficile la lecture de ce qui compte.

## Essayer la consigne sur deux états du projet

Faites l’essai sur `01-depart`, puis sur la version contenant les tests de `02-test-rouge`, dans deux copies séparées si votre assistant doit ouvrir un dossier. Ces versions se trouvent dans les fichiers fournis avec la partie 4. Utilisez une session neuve pour chaque essai.

Dans la première version, le test du retour avec hausse est absent. Dans la seconde, vous pouvez retrouver `test_retour_en_stock_avec_hausse`. Vérifiez dans le fichier si la réponse de l’agent correspond à l’état que vous lui avez montré.

Le même texte doit donc mener à deux constats différents. C’est plus instructif que de vérifier seulement si l’agent reprend les mots de la consigne.

S’il se trompe, notez la demande, le modèle choisi, le fichier réellement ouvert et la réponse. Puis changez un élément à la fois : une pièce jointe manquait-elle ? L’assistant avait-il gardé le contexte d’une autre copie ? La consigne demandait-elle vraiment de lire les tests ?

Nous n’en déduirons pas qu’un prompt est « fiable à 100 % ». Nous aurons un cas qui passe ou échoue, et une manière de le rejouer après une modification.

## Quand les règles se contredisent

Imaginons que le fichier général du projet dise « crée un commit après chaque tâche » et que votre demande dise « montre-moi le changement avant tout commit ». Ajouter une troisième phrase en majuscules ne résout pas proprement ce désaccord.

Ouvrez les consignes chargées par votre assistant. Cherchez les règles qui portent sur cette étape, leur portée et l’ordre de priorité documenté par l’outil. Les fichiers et leurs noms diffèrent selon les produits. Une instruction présente quelque part dans le dépôt n’est pas forcément chargée à chaque tour.

Pour votre propre organisation, placez une règle générale là où elle s’applique réellement, puis retirez les copies contradictoires. Les détails d’un ticket ont leur place avec le ticket. La procédure réutilisable de revue ou de préparation des tests pourra devenir un skill dans la partie suivante.

Une consigne explicite reste adressée à un modèle. Pour une action qui doit être interdite, il nous faut maintenant regarder ce que le programme autorise réellement.



---

[Précédent : Donner le contexte utile à l’étape en cours](../02-contexte/LECTURE.md) · [Suivant : Observer un refus qui ne dépend pas du modèle](../04-permissions/LECTURE.md)
