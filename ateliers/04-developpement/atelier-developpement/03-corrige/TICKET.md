# PRIX-1 — Ne plus notifier une simple remise en stock

Une notification est autorisée seulement si le produit est disponible dans le nouvel état et si son prix a strictement baissé par rapport à l’observation précédente.

- Un prix identique ne déclenche aucune notification, même après une rupture.
- Une hausse ne déclenche aucune notification, même après une rupture.
- Une baisse accompagnant un retour en stock déclenche une notification.
- Une baisse alors que le produit reste indisponible ne déclenche aucune notification.
- On compare deux observations consécutives, dans la même devise, avec des prix entiers en centimes.

Ne pas ajouter d’envoi de courrier, de base de données ni de framework. La validation des entrées existante reste en place.
