Consultez le second ticket :

```bash
python client.py ticket PRIX-2 --serveur mon_serveur.py --journal sorties/adaptation-prix-2.json
```

Il demande de limiter les notifications trop rapprochées. Deux questions restent ouvertes : quelle durée définit un intervalle court, et une baisse plus importante peut-elle contourner cette limite ?

Ouvrez une nouvelle conversation, chargez le même skill et demandez la préparation de PRIX-2. Une nouvelle conversation évite que vos corrections précédentes soient les seules à expliquer un bon résultat : nous voulons voir ce que les fichiers permettent de refaire.

La réponse devrait faire apparaître les deux questions. Elle peut déjà identifier des familles de cas : une notification juste avant la limite, une autre juste après, une nouvelle baisse pendant l’intervalle. En revanche, « dix minutes » ou « une forte baisse passe toujours » seraient des règles inventées pour remplir les cases.

La documentation de PRIX-1 ne résout pas cette ambiguïté. Elle dit quand une baisse rend une notification pertinente ; PRIX-2 ajoute une condition de temporisation encore à définir. Des sources vraies peuvent donc rester insuffisantes pour répondre.

Une recette avec deux résultats « à arbitrer » peut être plus utile qu’un tableau entièrement rempli. Elle montre précisément les décisions dont nous avons besoin pour poursuivre. Un trou visible se discute avec l’équipe ; une règle inventée au fond d’une cellule risque de devenir le comportement du produit par accident.
