# 3. Écrire des consignes que l’on peut contrôler

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Donner le contexte utile à l’étape en cours](../02-contexte/LECTURE.md) · [Suivant : Observer un refus qui ne dépend pas du modèle](../04-permissions/LECTURE.md)

**TL;DR** — Une consigne utile nomme l’action, les limites et le résultat à examiner. Nous allons transformer une demande vague, puis vérifier son effet sur un petit cas.

## De « fais attention » à une action précise

Voici une demande difficile à contrôler :

> Regarde le code, fais attention aux cas limites et assure-toi que tout est bon.

À quel résultat reconnaîtrons-nous que le travail est terminé ? Avec cette seule phrase, le modèle peut produire un commentaire très rassurant sans avoir inspecté le bon cas.

Pour notre projet, nous pouvons écrire :

```text
Lis la fonction notifier et les tests qui l’appellent.
Cherche si le retour en stock avec hausse de prix est couvert.
S’il existe, cite le test et sa valeur attendue.
Sinon, propose un test qui appelle notifier sur ce cas.
Ne modifie pas les fichiers. Ne prétends pas avoir exécuté la suite.
```

Les verbes sont impératifs, le cas est nommé et le résultat se vérifie dans les fichiers. L’agent doit retrouver un test précis ou en proposer un ; il n’a plus à deviner ce que « tout est bon » voulait dire.

Gardez les demandes courtes tant que le travail l’est. Dix interdictions héritées d’un autre ticket finiraient par cacher la seule règle qui compte ici.

## Essayer la consigne sur deux états du projet

Faites l’essai sur `01-depart`, puis sur la version contenant les tests de `02-test-rouge`, dans deux copies séparées si votre assistant doit ouvrir un dossier. Ces versions se trouvent dans les fichiers fournis avec la partie 4. Utilisez une session neuve pour chaque essai.

Dans la première version, le test du retour avec hausse est absent. Dans la seconde, vous pouvez retrouver `test_retour_en_stock_avec_hausse`. Vérifiez dans le fichier si la réponse de l’agent correspond à l’état que vous lui avez montré.

Le même texte devrait mener à deux constats différents, puisque les fichiers diffèrent. Nous vérifions ainsi que la réponse correspond au projet ouvert, au lieu de nous contenter d’y retrouver les mots de la consigne.

S’il se trompe, notez la demande, le modèle choisi, le fichier réellement ouvert et la réponse. Puis changez un élément à la fois : une pièce jointe manquait-elle ? L’assistant avait-il gardé le contexte d’une autre copie ? La consigne demandait-elle vraiment de lire les tests ?

Au bout de ces deux essais, gardez le cas, l’état de départ et le résultat. Vous pourrez les rejouer après avoir changé la consigne ou le modèle. Deux réussites resteraient deux observations, bien loin d’une fiabilité « à 100 % ».

## Quand les règles se contredisent

Imaginons que le fichier général du projet dise « crée un commit après chaque tâche », tandis que votre demande exige de voir le changement avant tout commit. Une troisième phrase en majuscules ajouterait surtout du bruit à ce désaccord.

Ouvrez les consignes chargées par votre assistant. Cherchez les règles qui portent sur cette étape, leur portée et l’ordre de priorité documenté par l’outil. Les fichiers et leurs noms diffèrent selon les produits, et leur simple présence dans le dépôt ne dit pas quand l’assistant les charge.

Pour votre propre organisation, placez une règle générale là où elle s’applique réellement, puis retirez les copies contradictoires. Les détails d’un ticket ont leur place avec le ticket. La procédure réutilisable de revue ou de préparation des tests pourra devenir un skill dans la partie suivante.

Ces consignes aident le modèle à choisir. Dès qu’une action doit être interdite, le programme doit prendre le relais. Voyons donc ce qu’il autorise réellement.

Une consigne précise rend le résultat observable et rejouable. Elle ne peut toutefois pas retirer au processus un droit qu’il possède déjà : pour cela, quittons le texte des prompts et passons aux contrôles du programme.

---

[Précédent : Donner le contexte utile à l’étape en cours](../02-contexte/LECTURE.md) · [Suivant : Observer un refus qui ne dépend pas du modèle](../04-permissions/LECTURE.md)
