# Point d’équipe — référence de l’exercice

Corrigé rédigé à partir de données fictives. Ce document n’est pas une sortie observée d’assistant. Aucun message n’a été envoyé et aucune demande n’a été ajoutée au tableau initial.

## Demandes nouvelles

| Message | Objet | Informations à garder | Source |
| --- | --- | --- | --- |
| M001 — Nora | Inscription | Deux places en Reliure, demande à examiner ; inscription non confirmée | `entrees/courriels/01-nora.txt` |
| M002 — Léo | Inscription | Deux places ; atelier non précisé, question à préparer | `entrees/courriels/02-leo.txt` |
| M005 — Nora | Question | Demande de l’heure de début de Cartographie ; aucune inscription supplémentaire | `entrees/courriels/05-question-nora.txt` |

Les trois messages sont nouveaux par rapport au suivi initial. Deux concernent des demandes d’inscription et un pose une question. Les deux messages distincts de Nora doivent être conservés.

## Suivi déjà connu

La demande de Samir pour une place en Reliure est déjà enregistrée sous `D001`, avec l’identifiant `<M004@atelier.example>`, dans `entrees/suivi-initial.csv`. Le courriel `entrees/courriels/04-samir.txt` apporte le même message. Garder la ligne existante sans en créer une deuxième. Le statut reste `demande_enregistree`, sans confirmation de place.

## Décisions et informations manquantes

La date est à clarifier avec Camille :

- le 10 octobre 2026 est retenu dans `entrees/reunions/01-preparation.md`, section « Date de la journée » (CR01), avec la disponibilité de la salle encore à vérifier ;
- le 17 octobre 2026 figure dans le projet d’affiche mentionné par `entrees/reunions/02-communication.md`, section « Projet d’affiche » (CR02).

Le second compte rendu n’établit pas de décision qui remplace le premier. Demander à Camille quelle date retenir, puis conserver la décision avant de l’annoncer.

L’horaire propre à Cartographie est absent : les horaires restent à préciser dans CR01, section « Ateliers », et ne sont pas renseignés dans CR02, section « Programme ». La question de Nora ne permet pas de les déduire.

L’atelier souhaité par Léo est absent de M002. Le nombre de places, lui, est connu : deux. Lui demander de choisir l’atelier.

## Brouillons, sans envoi

À Léo :

> Bonjour Léo,
>
> Votre demande porte sur deux places. Pour quel atelier souhaitez-vous vous inscrire : Reliure ou Cartographie ?
>
> Merci !

À Camille, pour le point interne :

> Le compte rendu du 7 septembre retient le 10 octobre, tandis que les notes du 14 septembre mentionnent le 17 sur le projet d’affiche. Quelle date devons-nous retenir ? Il nous manque aussi l’heure de début de Cartographie pour répondre à Nora. Peux-tu consigner ces décisions avant les confirmations ?

Ces brouillons ne confirment ni date, ni horaire, ni inscription. Leur formulation peut varier ; les questions doivent rester présentes.

## Comptage et copie

Cinq fichiers de courriel correspondent à quatre messages distincts. `entrees/courriels/03-copie-nora.txt` reproduit exactement M001. Retenir `01-nora.txt` comme référence principale, signaler la copie et conserver les deux fichiers.

Après rapprochement avec le suivi initial, trois messages sont nouveaux. Le lot ajoute des propositions de traitement ; le tableau de référence et les documents reçus restent intacts.
