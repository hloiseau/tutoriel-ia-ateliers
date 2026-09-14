Comme exercice pour manipuler les macros je vous propose de transformer ce contenu:

```txt
1. donut au chocolat
2. chausson aux pommes
3. pain au raisin
4. far breton
```

en celui-ci:

```txt
1. DONUT au chocolat
2. CHAUSSON aux pommes
3. PAIN au raisin
4. FAR breton
```

[[secret | Solution]]
| On se place sur une ligne (peu importe)
| 1. `qa` pour démarrer l'enregistrement d'une macro dans le registre `a`
| 2. `0` pour placer le curseur au début de la ligne
| 3. `2w` pour se placer sur le premier mot de notre liste
| 4. `viw` pour sélectionner tout le mot
| 5. `U` pour mettre la sélection en majuscule
| 6. `q` pour quitter l'enregistrement de la macro
|
| À présent que la macro est enregistrée on peut la réutiliser sur les autres lignes en faisant `@a`