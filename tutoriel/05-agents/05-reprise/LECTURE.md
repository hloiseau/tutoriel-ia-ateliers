# 5. Arrêter une boucle et reprendre sans perdre le fil

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Observer un refus qui ne dépend pas du modèle](../04-permissions/LECTURE.md) · [Suivant : Mesurer ce que la session nous a coûté](../06-couts/LECTURE.md)

**TL;DR** — Nous allons arrêter des lectures répétées avec un budget d’appels, puis corriger une demande refusée. Pour une vraie session, nous conserverons l’état des fichiers et la prochaine action à vérifier.

## Trois appels, puis on s’arrête

Lancez :

```bash
python banc.py boucle --limite 3 --journal sorties/boucle.jsonl
```

Le fichier `cas/boucle.json` contient huit demandes de lecture identiques. Le journal n’enregistre que trois appels, puis un arrêt pour `budget_appels`. Le quatrième appel n’est pas exécuté.

Ouvrez la fonction `rejouer` : c’est le programme qui compte les appels et arrête la boucle. Il ne demande pas au modèle de décider s’il a suffisamment dépensé. Le test associé vérifie aussi que les demandes refusées consomment ce budget.

Dans un véritable agent, une limite peut porter sur les tours, les tokens, la durée ou une dépense. Il faut savoir ce qui est compté. Notre limite d’appels ne borne pas le temps d’un outil bloqué ni la durée d’une requête au modèle ; il faudrait des délais d’expiration pour cela.

Relire un fichier n’est pas toujours inutile : il peut avoir changé. En revanche, lire trois fois le même contenu sans nouvelle question doit nous inciter à regarder ce qui manque, plutôt qu’à attendre le quatrième passage. 😅

## Corriger la cause du refus

Rejouez cet autre cas :

```bash
python banc.py reprise --journal sorties/reprise.jsonl
```

La première demande cherche `ticket.md`, qui ne figure pas dans la liste des chemins autorisés. La seconde demande `TICKET.md` et réussit. Le script montre une correction de paramètre, pas une ouverture générale des droits.

Dans votre assistant, commencez de la même façon : quelle demande a échoué, avec quels arguments, et quel résultat est revenu ? « Permission refusée », « fichier absent » et « test en échec » demandent des réponses différentes.

Avant de relancer une écriture, regardez aussi si elle a pu avoir lieu. Un délai dépassé ne prouve pas que le serveur n’a rien fait. Pour un envoi de notification ou la création d’un ticket, répéter aveuglément peut produire un doublon. L’opération doit avoir une manière de vérifier son état ou d’éviter les doublons ; « réessaie » ne suffit pas.

Pour notre exercice de la partie 4, inspectez le fichier et le diff avant de demander une nouvelle correction. On repartira ainsi de l’état présent, pas du récit de la dernière tentative.

## Préparer la prochaine session

L’atelier fournit `REPRISE-exemple.md`. C’est une trame, pas le compte rendu de votre session. Adaptez-la à `mon-suivi` :

```markdown
# Reprise du ticket

## But
Le comportement demandé, en une phrase.

## État présent
Le dossier de travail et les fichiers modifiés à examiner.

## Décisions
Les cas ambigus qui ont été tranchés.

## Vérifications
Les commandes réellement exécutées, leurs résultats et leurs journaux.

## Suite
Le blocage éventuel et la prochaine action à vérifier.
```

Fermez la conversation et essayez de reprendre avec cette fiche dans une session neuve. Demandez d’abord de vérifier l’état des fichiers et de relever ce qui manque pour continuer.

Si la fiche dit « les tests passent », mais ne donne ni commande ni résultat conservé, complétez-la. Si elle contient trente paragraphes d’hypothèses abandonnées, retirez ce qui ne guide plus la suite. Gardez en revanche la raison d’une solution rejetée si elle risque de revenir.

Le modèle peut préparer ce résumé. Relisez les décisions et les faits avant de vous en servir : une erreur recopiée dans une fiche de reprise peut devenir très convaincante à force d’être répétée.



---

[Précédent : Observer un refus qui ne dépend pas du modèle](../04-permissions/LECTURE.md) · [Suivant : Mesurer ce que la session nous a coûté](../06-couts/LECTURE.md)
