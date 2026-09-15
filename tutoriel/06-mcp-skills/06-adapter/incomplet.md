Consultez le second ticket :

```bash
python client.py ticket PRIX-2 --journal sorties/prix-2.json
```

Il demande de limiter les notifications trop rapprochées. Deux questions restent ouvertes : quelle durée définit un intervalle court, et une baisse plus importante peut-elle contourner cette limite ?

Ouvrez une nouvelle conversation, chargez le même skill et demandez la préparation de PRIX-2. Une nouvelle conversation évite que vos corrections précédentes soient les seules à expliquer un bon résultat : nous voulons voir ce que les fichiers permettent de refaire.

Que doit contenir la réponse ? Des questions, justement. On peut déjà identifier des familles de cas : une notification juste avant la limite, une autre juste après, une nouvelle baisse pendant l’intervalle. Mais choisir « dix minutes » ou décider qu’une forte baisse passe toujours inventerait une règle.

La documentation de PRIX-1 ne résout pas cette ambiguïté. Elle dit quand une baisse rend une notification pertinente ; PRIX-2 ajoute une condition de temporisation encore à définir. Des sources vraies peuvent donc rester insuffisantes pour répondre.

Une recette avec deux résultats « à arbitrer » peut être plus utile qu’un tableau entièrement rempli. Elle montre précisément les décisions dont nous avons besoin pour poursuivre. Ce n’est pas au modèle de décider discrètement du comportement du produit pour que son tableau soit plus joli.
