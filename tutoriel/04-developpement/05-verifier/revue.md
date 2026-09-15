Vous pouvez maintenant faire relire le diff par un agent, en lui donnant aussi le ticket et les cas attendus :

```text
Relis le diff par rapport à TICKET.md et aux scénarios.
Pour chaque problème trouvé, donne un cas reproductible,
le comportement obtenu et celui attendu.
Ne modifie pas les fichiers pendant cette revue.
Si tu ne trouves pas de problème, indique ce que tu as vérifié
et les limites de cette vérification.
```

Cette demande évite de réduire la revue à des préférences de style. Une remarque devient plus utile lorsqu’on peut lancer le scénario qui la justifie.

Le second passage peut tout de même manquer la même erreur que le premier. Changer de session ou de modèle n’en fait pas une preuve indépendante au sens fort : les outils peuvent partager des habitudes et des angles morts. Appuyez-vous sur les scénarios, le code et les sorties observées.

Pour notre petit changement, une revue efficace peut être courte. Il n’y a aucune raison d’inventer trois problèmes pour remplir une section de rapport.
