# 6. Vérifier au-delà de la dernière ligne verte

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Faire le changement et lire le diff](../04-corriger/LECTURE.md) · [Suivant : Garder un changement que l’on sait expliquer](../06-garder-la-main/LECTURE.md)

**TL;DR** — Une suite verte couvre la fonction avec les cas que nous avons écrits. Les scénarios JSON feront ensuite parcourir au programme tout le chemin observé au début.

## Rejouer les tests et contrôler leur nombre

Après correction, lancez :

```bash
python -m unittest discover -v
```

Avec le fichier complet de `02-test-rouge`, les **treize tests passent**. Si vous avez conservé les tests de l’agent, le nombre peut être différent. Vérifiez que les cas décidés dans la table sont couverts et que ceux qui échouaient passent désormais, avec les mêmes valeurs attendues.

Les noms des tests donnent un premier inventaire des situations contrôlées. Retrouvez surtout les deux qui échouaient avant la correction : ils doivent encore être présents, avec les mêmes valeurs attendues.

Dans le rapport de l’agent, cherchez la commande, son dossier d’exécution et son résultat. La formule « tests vérifiés » est trop floue : l’agent a pu lire leur code, en lancer un seul ou exécuter la suite complète.

Une dépendance manquante ou une commande interrompue doit rester visible dans le rapport. Un fichier de test bien écrit ne nous apprend rien sur le résultat d’une exécution qui n’a pas eu lieu.

## Passer par les fichiers JSON

Exécutez maintenant nos trois scénarios :

```bash
python suivi.py scenarios/retour-stock.json
python suivi.py scenarios/baisse.json
python suivi.py scenarios/rupture.json
```

Voici les décisions attendues après correction :

| Fichier | Résultat |
| --- | --- |
| `retour-stock.json` | `{"notifier": false}` |
| `baisse.json` | `{"notifier": true}` |
| `rupture.json` | `{"notifier": false}` |
Table: Les trois scénarios de recette

Cette fois, les données traversent la lecture du fichier, la construction des états, la décision puis l’affichage. Les tests précédents appelaient surtout les fonctions directement. Ensemble, ces deux niveaux couvrent la règle et son chemin d’entrée principal.

Créez ensuite une copie de `retour-stock.json`, nommée `retour-stock-baisse.json`, et changez seulement le nouveau prix : 1 500 au lieu de 2 000. Lancez ce nouveau scénario. Le résultat doit être vrai.

Si un cas produit une réponse inattendue, conservez le fichier qui le reproduit. Modifier ensuite ses données pour obtenir du vert effacerait précisément l’information dont nous avons besoin. Un scénario complet vaut mieux qu’une capture privée de ses entrées.

## Vérifier qu’un test sait encore protester

Cette expérience est facultative. Copiez le dossier corrigé `mon-suivi` dans un dossier voisin nommé **`mon-suivi-mutations`**. Depuis le terminal placé dans `mon-suivi`, entrez dans cette nouvelle copie :

```bash
cd ../mon-suivi-mutations
```

Ouvrez **le fichier `suivi.py` de cette copie**. Dans la fonction `notifier` uniquement, remplacez la comparaison `nouveau.prix_centimes < ancien.prix_centimes` par `nouveau.prix_centimes <= ancien.prix_centimes`. Enregistrez, puis relancez `python -m unittest discover -v` dans ce terminal.

Le prix identique autorise maintenant une notification. Les tests qui attendent l’absence de notification à prix inchangé doivent échouer. S’ils ne le font pas, vérifiez la copie exécutée et la présence de ces cas.

Rétablissez ensuite `<`, puis retirez temporairement la condition `nouveau.disponible and`. Le test de baisse sur un produit indisponible doit cette fois protester.

Ces modifications volontaires sont de petites **mutations** : nous introduisons une erreur précise pour voir si les tests la remarquent. Nous vérifions ainsi que les cas importants savent protester. D’autres bugs restent évidemment possibles ; deux mutations ne dressent pas un bouclier magique autour de la fonction.

Rétablissez la condition dans `mon-suivi-mutations`, puis revenez à notre copie de travail restée intacte :

```bash
cd ../mon-suivi
python -m unittest discover -v
```

Le but est de tester nos tests, pas de préparer discrètement le prochain ticket. 🙂

## Demander une seconde lecture utile

Pour un second avis, vous pouvez faire relire le changement par un agent. C’est facultatif pour terminer l’atelier. Fournissez-lui le diff obtenu dans la comparaison, le contenu de `TICKET.md` et la table des cas attendus :

```text
Relis le diff par rapport à TICKET.md et aux scénarios.
Pour chaque problème trouvé, donne un cas reproductible,
le comportement obtenu et celui attendu.
Ne modifie pas les fichiers pendant cette revue.
Si tu ne trouves pas de problème, indique ce que tu as vérifié
et les limites de cette vérification.
```

Cette demande ramène la revue aux comportements. Une remarque devient utile lorsqu’elle s’accompagne d’un scénario que l’on peut lancer.

Le second passage peut manquer la même erreur que le premier. Une nouvelle session, même avec un autre modèle, peut retrouver les mêmes habitudes et les mêmes angles morts. Les scénarios, le code et les sorties observées restent nos pièces les plus solides.

Pour notre petit changement, une revue efficace peut tenir en quelques lignes. Inutile d’inventer trois problèmes pour donner du volume au rapport.



---

[Précédent : Faire le changement et lire le diff](../04-corriger/LECTURE.md) · [Suivant : Garder un changement que l’on sait expliquer](../06-garder-la-main/LECTURE.md)
