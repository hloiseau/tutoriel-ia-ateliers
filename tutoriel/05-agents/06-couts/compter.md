Le journal du banc compte les outils appelés et le temps passé dans chaque fonction Python. La colonne des tokens y brille par son absence : aucun modèle n’a été appelé.

Dans une vraie session, le modèle reçoit un contexte, produit une réponse et peut demander plusieurs outils. Leurs résultats alimentent parfois un nouvel appel au modèle, avec un contexte plus long. Deux appels d’outils peuvent ainsi tenir dans un seul tour du modèle ou provoquer plusieurs tours : leur nombre ne suffit pas à calculer les tokens ni le prix final.

Une partie du contexte peut être réutilisée d’un tour à l’autre. Selon le fournisseur, le cache change la manière dont ces tokens sont traités et facturés ; sa lecture et parfois son écriture ont des conditions propres[^p5-cache]. Ne multipliez pas simplement la taille de la conversation affichée par le prix d’entrée.

Pour un relevé réel, partez des compteurs d’usage exposés par le fournisseur ou l’application. Regardez ce qu’ils incluent : entrée totale, entrée en cache, sortie, éventuels tokens de raisonnement et outils facturés séparément. Si l’entrée totale inclut déjà le cache, ne comptez pas celui-ci une deuxième fois.

Avec un abonnement, distinguez aussi l’argent débité en plus et la part consommée d’un quota déjà payé. Une session peut afficher zéro dépense supplémentaire tout en rapprochant votre équipe d’une limite mensuelle.

[^p5-cache]: Anthropic, [fonctionnement et tarification du cache de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Les conditions de cette documentation ne s’appliquent pas automatiquement aux autres fournisseurs.
