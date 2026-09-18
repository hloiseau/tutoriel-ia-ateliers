# Exemple : notre application documentaire locale

Dans la configuration testée en partie 8, `assistant_local.py` lit les documents du dossier, construit les messages puis contacte `127.0.0.1:8080`. Les messages comprennent la question et les passages retenus. Le serveur de cette expérience utilise des poids déjà téléchargés. Le journal local conserve question, passages, requête et réponse.

Ces observations portent sur ce programme et cette configuration. Elles ne démontrent pas que tout logiciel installé localement fonctionne sans service extérieur, ni que l’ensemble de la machine est exempt d’autres communications. Le téléchargement initial du modèle est distinct de l’appel local.

En cas d’arrêt du modèle, la recherche seule reste utilisable. Le texte des règles et les tests sont lisibles sans compte. Changer le moteur ou les poids demanderait de vérifier l’interface et surtout de rejouer les questions ; une API compatible ne garantit pas les mêmes réponses.

Pour un assistant tiers, compléter la fiche avec sa configuration et ses conditions actuelles. L’atelier ne fournit pas de conclusion inventée sur la conservation de ses journaux.
