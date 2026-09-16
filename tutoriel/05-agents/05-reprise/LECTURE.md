# 5. Arrêter une boucle et reprendre sans perdre le fil

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Observer un refus qui ne dépend pas du modèle](../04-permissions/LECTURE.md) · [Suivant : Mesurer ce que la session nous a coûté](../06-couts/LECTURE.md)

**TL;DR** — Nous allons arrêter des lectures répétées avec un budget d’appels, puis corriger une demande refusée. Pour une vraie session, nous conserverons l’état des fichiers et la prochaine action à vérifier.

## Trois appels, puis on s’arrête

Lancez :

```bash
python banc.py boucle --limite 3 --journal sorties/boucle.jsonl
```

Le fichier `cas/boucle.json` contient huit demandes de lecture identiques. Le journal enregistre les trois premières, puis un arrêt pour `budget_appels`. La quatrième reste dans le scénario et n’atteint jamais l’outil.

Ouvrez la fonction `rejouer` : le compteur et l’arrêt appartiennent au programme. Le test associé vérifie aussi que les demandes refusées consomment ce budget. Une boucle de refus peut donc atteindre la limite aussi vite qu’une boucle de succès.

Dans un véritable agent, une limite peut porter sur les tours, les tokens, la durée ou une dépense. Vérifiez l’unité choisie : trois appels d’outils ne disent rien sur la taille des réponses du modèle. Notre compteur ne borne pas non plus le temps d’un outil bloqué ni la durée d’une requête au modèle ; ces risques demandent des délais d’expiration.

Un fichier peut changer et mériter une seconde lecture. Après trois lectures du même contenu sans nouvelle question, mieux vaut chercher ce qui manque que parier sur l’illumination au quatrième passage. 😅

## Corriger la cause du refus

Rejouez cet autre cas :

```bash
python banc.py reprise --journal sorties/reprise.jsonl
```

La première demande cherche `ticket.md`, absent de la liste des chemins autorisés. La seconde utilise le nom exact `TICKET.md` et réussit. Le droit de lecture n’a pas changé ; seul l’argument a été corrigé.

Dans votre assistant, commencez par les mêmes questions : quelle demande a échoué, avec quels arguments, et quel résultat est revenu ? « Permission refusée », « fichier absent » et « test en échec » appellent des corrections différentes.

Avant de relancer une écriture, vérifiez si elle a pu avoir lieu. Après un délai dépassé, le serveur a peut-être terminé l’action sans que la réponse vous parvienne. Renvoyer une notification ou recréer un ticket peut alors produire un doublon. Prévoyez un moyen de consulter l’état de l’opération ou de reconnaître une répétition.

Pour l’exercice de la partie 4, inspectez le fichier et le diff avant de demander une nouvelle correction. La reprise partira de l’état présent des fichiers, plus fiable que le récit de la dernière tentative.

## Préparer la prochaine session

L’atelier fournit `REPRISE-exemple.md`, une trame à compléter avec les faits de votre session sur `mon-suivi` :

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

Fermez la conversation, puis repartez dans une session neuve avec cette fiche. Demandez d’abord de vérifier l’état des fichiers et de relever ce qui manque pour continuer. Vous verrez vite si la fiche porte le travail ou si elle s’appuyait encore sur des souvenirs de l’ancienne conversation.

Si la fiche dit « les tests passent », mais ne donne ni commande ni résultat conservé, complétez-la. Si elle contient trente paragraphes d’hypothèses abandonnées, retirez ce qui ne guide plus la suite. Gardez en revanche la raison d’une solution rejetée si elle risque de revenir.

Le modèle peut préparer ce résumé. Relisez les décisions et les faits avant de vous en servir : une erreur recopiée dans une fiche de reprise gagne vite l’apparence d’une vieille vérité.

Une limite arrête la boucle ; le journal explique où elle s’est arrêtée ; la fiche rassemble l’état nécessaire pour repartir. Cette reprise consomme toutefois du temps, des appels et parfois un quota payant. Nous allons les compter séparément.

---

[Précédent : Observer un refus qui ne dépend pas du modèle](../04-permissions/LECTURE.md) · [Suivant : Mesurer ce que la session nous a coûté](../06-couts/LECTURE.md)
