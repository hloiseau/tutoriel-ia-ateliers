Lancez :

```bash
python 08_langage.py
```

```text
Corpus : 1010 caractères ; vocabulaire : 31 tokens
Contexte utilisé : 1 caractère ; température : 1.0
le sess à s lessta mateneust la rix ja chelerilere r.
lelere.
le mmme.
le le chelere s.
le chare ege ctrifévindata e.
lenegis lamblapaure.
ler leure fin suis rbories.
leroive décalust
```

Nous avons des morceaux qui ressemblent à du français, et beaucoup de charabia. Le modèle connaît les enchaînements de caractères de son petit corpus, mais il ne conserve qu’un caractère de contexte. Ce serait assez optimiste de lui demander un roman. 🙂

À chaque étape, le programme sélectionne une ligne de comptages, la transforme en probabilités, tire un caractère et l’ajoute au résultat :

```python
frequences = comptes[vers_id[resultat[-1]]]
```

Le dernier caractère de la nouvelle séquence sera utilisé au tour suivant. Les comptes, eux, restent inchangés pendant la génération.

Nous pouvons régler la **température**, qui modifie la répartition utilisée pour le tirage :

```bash
python 08_langage.py --temperature 0.5
```

Une température plus basse favorise davantage les continuations fréquentes. Une température plus haute rend la répartition moins concentrée. Le modèle n’apprend rien de nouveau dans les deux cas.

Voici le début réellement obtenu avec `0.5` :

```text
le re paure leist de sst ure la prre la le le e re pa are re chisore le le s.
```

La température ne répare donc pas la limite de contexte. Elle change la manière de choisir parmi les possibilités disponibles.

Essayez aussi :

```bash
python 08_langage.py --debut "la " --graine 7 --longueur 100
```

`--graine` règle le générateur pseudo-aléatoire du tirage. Avec les mêmes fichiers, la même version de NumPy, les mêmes options et la même graine, vous pouvez refaire le même essai. Avec une autre graine, les choix peuvent changer.

Le résultat est écrit dans `sorties/texte-genere.txt`. La table de comptes et son vocabulaire sont sauvegardés dans `sorties/bigrammes.npz`.
