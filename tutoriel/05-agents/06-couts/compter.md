Le journal du banc nous dit combien d’outils ont été appelés et combien de temps chacun a pris. Il ne contient aucun token de modèle : nous n’en avons appelé aucun.

Dans une vraie session, le modèle reçoit un contexte, produit une réponse et peut demander plusieurs outils. Leurs résultats peuvent alimenter un nouvel appel au modèle. Le nombre d’outils ne permet donc pas de déduire directement le nombre de tokens, ni le prix final.

Une partie du contexte peut être réutilisée d’un tour à l’autre. Selon le fournisseur, le cache change la manière dont ces tokens sont traités et facturés ; sa lecture et parfois son écriture ont des conditions propres[^p5-cache]. Ne multipliez pas simplement la taille de la conversation affichée par le prix d’entrée.

Pour un relevé réel, partez des compteurs d’usage exposés par le fournisseur ou l’application. Regardez ce qu’ils incluent : entrée totale, entrée en cache, sortie, éventuels tokens de raisonnement et outils facturés séparément. Si l’entrée totale inclut déjà le cache, ne comptez pas celui-ci une deuxième fois.

Un abonnement ajoute une autre question : avez-vous dépensé de l’argent supplémentaire ou consommé une partie d’un quota déjà payé ? Les deux informations sont utiles, mais elles ne se lisent pas de la même façon.

[^p5-cache]: Anthropic, [fonctionnement et tarification du cache de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Les conditions de cette documentation ne s’appliquent pas automatiquement aux autres fournisseurs.
