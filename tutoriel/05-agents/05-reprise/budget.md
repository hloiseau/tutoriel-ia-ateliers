Lancez :

```bash
python banc.py boucle --limite 3 --journal sorties/boucle.jsonl
```

Le fichier `cas/boucle.json` contient huit demandes de lecture identiques. Le journal enregistre les trois premières, puis un arrêt pour `budget_appels`. La quatrième reste dans le scénario et n’atteint jamais l’outil.

Ouvrez la fonction `rejouer` : le compteur et l’arrêt appartiennent au programme. Le test associé vérifie aussi que les demandes refusées consomment ce budget. Une boucle de refus peut donc atteindre la limite aussi vite qu’une boucle de succès.

Dans un véritable agent, une limite peut porter sur les tours, les tokens, la durée ou une dépense. Vérifiez l’unité choisie : trois appels d’outils ne disent rien sur la taille des réponses du modèle. Notre compteur ne borne pas non plus le temps d’un outil bloqué ni la durée d’une requête au modèle ; ces risques demandent des délais d’expiration.

Un fichier peut changer et mériter une seconde lecture. Après trois lectures du même contenu sans nouvelle question, mieux vaut chercher ce qui manque que parier sur l’illumination au quatrième passage. 😅
