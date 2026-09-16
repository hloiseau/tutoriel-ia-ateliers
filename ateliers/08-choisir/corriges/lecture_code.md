# Lire puis modifier la règle

La fonction de départ utilise `<=`, ce qui accepte aussi le prix égal. Le cas 2500 → 2500 avec disponibilité vraie renvoie donc vrai alors que la règle demande faux. Le corriger en `<` rend les quatre cas cohérents avec la baisse stricte et la disponibilité.

Pour la variante, la baisse vaut `ancien_prix - nouveau_prix`. Elle doit atteindre au moins 100 centimes : `disponible and ancien_prix - nouveau_prix >= 100`. Les baisses de 99, 100 et 101 donnent respectivement faux, vrai et vrai si le produit est disponible. Une hausse ou un produit indisponible ne notifie pas.

Ces fonctions supposent les types validés en amont. Les scripts testent les frontières utiles, pas toute l’application de production. Pouvoir expliquer la différence entre les deux seuils compte autant que recopier la ligne du corrigé.
