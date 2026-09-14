Regardons deux caractères consécutifs : `l` puis `e`, `e` puis un espace, un espace puis `c`… Nous comptons combien de fois chaque paire apparaît.

```python
comptes = np.zeros((len(vocabulaire), len(vocabulaire)))
for a, b in zip(texte, texte[1:]):
    comptes[vers_id[a], vers_id[b]] += 1
```

La table contient une ligne pour le caractère actuel et une colonne pour le suivant. Si `e` est souvent suivi d’un espace, cette case aura une grande valeur.

![Nombre d’occurrences des caractères qui suivent e dans le corpus fourni.](image:images/bigrammes.png)
Figure: Comptages effectués sur `corpus.txt`.

Un modèle fondé sur deux éléments successifs s’appelle un modèle à **bigrammes**. Pour produire le prochain caractère, le nôtre regarde seulement le dernier caractère disponible.[^p2-7-compter-langage]

Si la phrase commence par « le chat » ou par « un petit rat », la dernière lettre est `t` dans les deux cas. Notre modèle utilisera la même ligne de la table. Il a déjà perdu toute la différence entre les deux débuts de phrase.

Nous n’utilisons pas de descente de gradient ici : les fréquences viennent directement des comptages. L’apprentissage d’un modèle ne passe donc pas obligatoirement par un réseau de neurones.

Modifiez une phrase du corpus, ou ajoutez-en une. Au prochain lancement, le programme recomptera les paires. C’est cette modification des comptes qui change le modèle ; écrire un autre début de phrase change seulement son entrée.


[^p2-7-compter-langage]: [Daniel Jurafsky et James H. Martin, Speech and Language Processing, N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf).
