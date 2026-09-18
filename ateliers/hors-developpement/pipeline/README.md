# Préparer le point dans le navigateur

Ouvrez `index.html` directement dans un navigateur récent. Gardez les fichiers `index.html`, `donnees.js`, `moteur.js` et `interface.js` ensemble. Aucune installation, aucun compte et aucun serveur ne sont nécessaires. L’application utilise des scripts classiques, fonctionne avec une adresse `file://` et ne fait aucune requête réseau.

Elle est conçue pour le dossier fictif « Les ateliers du quartier », lot `quartier-01`. Elle refuse un autre lot. Elle n’est pas un outil général de gestion d’inscriptions.

## Essayer le parcours

1. Cliquez sur **Charger l’exemple fictif**. L’origine indique `exemple_fictif` : cette extraction a été préparée pour l’exercice, sans appel à un modèle. Vous pouvez aussi coller votre extraction manuelle ou celle d’un assistant, avec l’origine correspondante.
2. Cliquez sur **Contrôler et préparer**. M001, M002 et M005 sont nouveaux ; M004 figure déjà dans le suivi initial. La copie de M001 reste documentée.
3. Comparez le **Point proposé** aux **Sources consultables**. Tous les courriels, les deux comptes rendus, le suivi initial et les règles sont lisibles dans l’application. Corrigez le point si nécessaire. Un extrait authentique ne garantit pas que les champs sont fidèles : si vous donnez l’atelier Reliure à Léo dans l’extraction, le contrôle de format peut réussir, alors que M002 ne précise aucun atelier.
4. Cochez « J’ai comparé ce point aux sources, vérifié les informations manquantes et les décisions laissées ouvertes. », puis **Approuver cette version**. Le bouton reste indisponible sans cette confirmation. L’accord porte uniquement sur le point interne.
5. Modifiez une phrase du point : **Exporter le point** redevient indisponible. Relisez, cochez et approuvez à nouveau. Si vous modifiez l’extraction, le contrôle doit lui aussi être refait ; l’ancien accord est annulé immédiatement, même avant ce nouveau contrôle.
6. Cliquez sur **Exporter le point** pour télécharger `point-quartier-01.md`. M001, M002 et M005 deviennent alors des messages pris en compte dans le rapport. Aucune place n’est confirmée, aucun tableau partagé n’est modifié et aucun message n’est envoyé.
7. Cliquez sur **Exporter l’état** pour télécharger `etat-quartier-01.json`. Rechargez la page, puis choisissez ce fichier avec **Reprendre un état**. Cliquez de nouveau sur **Contrôler et préparer** : ce lot ne contient plus de message nouveau et aucun second point ne peut être exporté.

**Contrôler et préparer** reconstruit le point à partir de l’extraction : les retouches du point sont remplacées. Conservez celles que vous souhaitez garder avant de recommencer.

## Ce que l’application contrôle

Le noyau refuse les champs absents ou inconnus, les versions et lots inconnus, les identifiants absents ou répétés, les types et ateliers inconnus, ainsi que les quantités qui ne sont ni des entiers positifs ni `null`. Les champs `date_evenement` et `horaire_cartographie` doivent rester à `null` dans ce lot non arbitré. M005 reste une question sans place supplémentaire.

Chaque source doit être le chemin attendu pour son identifiant, depuis `entrees/`. Chaque extrait doit être une sous-chaîne exacte du fichier correspondant, retours à la ligne compris. Ce test ne démontre pas que l’extrait justifie chaque valeur extraite. La case de relecture engage la personne qui clique ; l’application ne sait pas si elle a réellement lu les documents.

Les contrôles propres à ce jeu de données ne remplacent pas des règles métier ou une décision de l’équipe. Un point librement modifié peut contenir des erreurs : elles restent à repérer avant de l’approuver.

## Ce que sauvegarde l’état

L’état contient les identifiants connus, les rapports exportés avec leur extraction, les deux zones de brouillon et les 200 derniers événements du journal. Le journal indique l’ordre des opérations. Aucun accord n’y est réactivé lors d’une reprise : les brouillons doivent être contrôlés et approuvés à nouveau.

Exporter l’état ne traite aucun nouveau message. Seul le déclenchement du téléchargement du point marque ses identifiants comme pris en compte. Le navigateur ne sait pas si vous avez ensuite annulé le téléchargement ou supprimé le fichier : dans ce cas, le marquage reste effectif pendant la séance. Le texte du point est conservé dans les rapports du fichier d’état.

Si vous avez annulé le téléchargement, copiez le texte encore présent dans **Point proposé** vers un fichier `point-quartier-01.md`, puis sauvegardez l’état. Si vous aviez déjà sauvegardé l’état après l’export, le reprendre restaure aussi le brouillon : copiez ce point avant de relancer **Contrôler et préparer**, qui le remplacerait par le constat d’un lot déjà traité.

L’import refuse les formats inattendus, les références incohérentes et les identifiants sans rapport correspondant. Un import refusé laisse la séance actuelle intacte. Le fichier d’état reste modifiable par toute personne qui le possède ; son contenu textuel est affiché comme du texte et aucune instruction qu’il contient n’est exécutée. Ces vérifications ne prouvent pas l’authenticité du fichier et ne constituent pas un mécanisme de sécurité pour plusieurs utilisateurs.

Aucune sauvegarde automatique n’est effectuée. Deux onglets ouverts séparément ont deux états indépendants. Fermer ou recharger un onglet sans exporter son état perd le travail de cette séance.

## Pour maintenir l’exercice

Le navigateur n’a besoin ni de Node.js ni de Python. Les commandes suivantes servent seulement aux personnes qui maintiennent l’atelier, depuis la racine du dépôt :

```sh
node ateliers/hors-developpement/pipeline/generer-donnees.cjs
node --test ateliers/hors-developpement/pipeline/test-moteur.cjs
```

Le générateur intègre les neuf sources fournies dans `donnees.js`, puis ajoute une extraction de démonstration explicitement fictive. Les tests comparent les sources intégrées aux vrais fichiers et vérifient les refus de format, le contre-exemple sémantique, l’approbation d’une version exacte, l’invalidation, la reprise et le rejeu sans doublon. Ils n’appellent aucun modèle et n’envoient rien.
