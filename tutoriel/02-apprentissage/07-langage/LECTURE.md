# 7. Produire du texte, un morceau à la fois

[Sommaire de la partie](../README.md) · [Sources](.)

Avec les chiffres, une image produisait une classe et le calcul s’arrêtait là. Pour écrire du texte, chaque sortie doit pouvoir servir à choisir la suivante.

Commençons avec un modèle de langage qui tient dans une table. Son corpus est assez court pour que nous puissions compter nous-mêmes ce qu’il apprend.

## Transformer les caractères en nombres

Ouvrez `corpus.txt`. Il contient de courtes phrases sur des animaux, des objets et du code. Ce texte est assez petit pour que vous puissiez le lire entièrement, le modifier et comprendre d’où viennent les exemples.

Dans `08_langage.py`, nous construisons un vocabulaire :

```python
vocabulaire = sorted(set(texte))
vers_id = {c: i for i, c in enumerate(vocabulaire)}
```

Chaque caractère distinct reçoit un numéro. L’espace, le point et le retour à la ligne ont eux aussi un numéro. Notre corpus contient 31 caractères distincts : notre vocabulaire comporte donc **31 tokens**.

Un **token** est une unité choisie pour représenter le texte. Ici, nous avons décidé qu’un token serait un caractère. Un modèle de langage plus grand peut utiliser des morceaux de mots, des mots fréquents, des octets ou d’autres unités. Le numéro d’un token ne désigne pas à lui seul son sens.

Dans un réseau, on associe souvent chaque numéro à un vecteur de nombres, appelé **embedding**. Ce vecteur donne au calcul une représentation modifiable pendant l’entraînement. Nous n’en avons pas besoin pour notre première table de fréquences.

Le choix du découpage compte. Avec des caractères, les séquences sont longues mais le vocabulaire est petit. Avec des morceaux de mots, une même phrase peut utiliser moins de positions, mais la table des tokens est plus grande.

## Apprendre quelles lettres se suivent

Regardons deux caractères consécutifs : `l` puis `e`, `e` puis un espace, un espace puis `c`… Nous comptons combien de fois chaque paire apparaît.

```python
comptes = np.zeros((len(vocabulaire), len(vocabulaire)))
for a, b in zip(texte, texte[1:]):
    comptes[vers_id[a], vers_id[b]] += 1
```

La table contient une ligne pour le caractère actuel et une colonne pour le suivant. Si `e` est souvent suivi d’un espace, cette case aura une grande valeur.

![Nombre d’occurrences des caractères qui suivent e dans le corpus fourni.](../images/bigrammes.png)
Figure: Comptages effectués sur `corpus.txt`.

Un modèle fondé sur deux éléments successifs s’appelle un modèle à **bigrammes**. Pour produire le prochain caractère, le nôtre regarde seulement le dernier caractère disponible.[^p2-7-compter-langage]

Si la phrase commence par « le chat » ou par « un petit rat », la dernière lettre est `t` dans les deux cas. Notre modèle utilisera la même ligne de la table. Il a déjà perdu toute la différence entre les deux débuts de phrase.

Nous n’utilisons pas de descente de gradient ici : les fréquences viennent directement des comptages. L’apprentissage d’un modèle ne passe donc pas obligatoirement par un réseau de neurones.

Modifiez une phrase du corpus, ou ajoutez-en une. Au prochain lancement, le programme recomptera les paires. C’est cette modification des comptes qui change le modèle ; écrire un autre début de phrase change seulement son entrée.


[^p2-7-compter-langage]: [Daniel Jurafsky et James H. Martin, Speech and Language Processing, N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf).

## Tirer la suite du texte

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

## Calculer une attention sur quatre positions

Notre table oublie tout sauf le dernier caractère. Les transformers disposent d’un mécanisme qui permet de combiner des informations venant de plusieurs positions : l’**attention**.

Nous pouvons effectuer ce calcul avec de petits tableaux. Dans `09_attention.py`, nous donnons à quatre positions des vecteurs choisis à la main :

```python
Q = np.array([[1., 0.], [0., 1.], [1., 1.], [1., -1.]])
K = Q.copy()
V = np.array([[1., 0.], [0., 1.], [2., 1.], [1., 2.]])
```

`Q` contient les **requêtes**, `K` les **clés** et `V` les **valeurs**. Une requête est comparée aux clés pour calculer des coefficients ; ces coefficients servent ensuite à combiner les valeurs.[^p2-7-attention-attention]

```python
scores = Q @ K.T / np.sqrt(K.shape[1])
```

Nous masquons les positions futures, puis appliquons une softmax par ligne. Enfin :

```python
resultat = attention @ V
```

Lancez :

```bash
python 09_attention.py
```

```text
Poids d'attention :
[[1.    0.    0.    0.   ]
 [0.33  0.67  0.    0.   ]
 [0.248 0.248 0.503 0.   ]
 [0.266 0.065 0.131 0.539]]
Valeurs combinées :
[[1.    0.   ]
 [0.33  0.67 ]
 [1.255 0.752]
 [1.066 1.273]]
```

Ouvrez `sorties/attention.png` :

![Matrice de quatre lignes et quatre colonnes : chaque position combine seulement sa propre valeur et les valeurs précédentes.](../images/attention.png)
Figure: Poids calculés à partir des tableaux Q, K et V du programme.

Les zéros au-dessus de la diagonale correspondent aux positions futures. La première position ne peut consulter qu’elle-même. La dernière peut combiner les quatre valeurs. Chaque ligne a une somme égale à un, à l’arrondi près.

Sur la deuxième ligne, les coefficients sont environ `0,330` et `0,670`. Les deux valeurs accessibles sont `[1, 0]` et `[0, 1]`. Leur combinaison donne :

```text
0,330 × [1, 0] + 0,670 × [0, 1] = [0,330, 0,670]
```

C’est la deuxième ligne du tableau « Valeurs combinées ». Les coefficients d’attention indiquent comment mélanger les valeurs ; ils ne sont pas eux-mêmes les valeurs à transmettre.

Essayez maintenant une autre requête. **Après la définition de `V`**, ajoutez cette ligne, avant le calcul de `scores` :

```python
Q[3] = [0., 1.]
```

Nous la plaçons après `K = Q.copy()` pour conserver les clés d’origine. Relancez le programme : la dernière ligne d’attention devient environ `[0.180, 0.365, 0.365, 0.089]`. Les trois autres lignes restent identiques.

Vous venez de changer ce que recherche la dernière position, en conservant les informations qu’elle peut consulter. Retirez ensuite cette ligne pour retrouver le calcul de départ.

Ces vecteurs ne proviennent pas d’un entraînement : nous les avons définis pour faire le calcul. Dans un transformer, des projections apprises produisent notamment les requêtes, clés et valeurs à partir des représentations disponibles. Plusieurs têtes d’attention, des transformations supplémentaires et des informations de position sont combinées dans les couches du modèle.[^p2-7-attention-transformer]

Le masque utilisé ici est **causal** : pour prédire la suite, on ne donne pas au modèle les caractères futurs. D’autres usages, comme l’analyse d’un texte déjà entièrement disponible, peuvent employer une attention sans ce masque.


[^p2-7-attention-attention]: [Dive into Deep Learning, Queries, Keys, and Values](https://d2l.ai/chapter_attention-mechanisms-and-transformers/queries-keys-values.html).

[^p2-7-attention-transformer]: [Vaswani et ses collègues, Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762).

## Pourquoi cela ne fait pas encore un assistant

Notre bigramme produit du texte. Notre calcul d’attention combine des vecteurs. Nous n’avons pourtant pas un programme capable de répondre utilement à une demande.

Pour entraîner un modèle de langage autorégressif, on peut lui fournir une séquence et lui demander de prédire les tokens suivants. Le texte fournit alors lui-même une cible d’apprentissage : nul besoin d’écrire manuellement une étiquette pour chaque caractère. On parle notamment d’apprentissage **auto-supervisé**.

Un modèle préentraîné à poursuivre du texte peut ensuite être adapté avec des exemples de consignes et de réponses, ainsi qu’avec d’autres méthodes d’optimisation. Les travaux sur InstructGPT illustrent cette distinction entre le préentraînement et l’entraînement destiné à mieux suivre des instructions.[^p2-7-reponse-instructions]

La prédiction de la suite produit parfois une réponse utile, parfois une formule familière ou un dialogue qui part dans la mauvaise direction. La capacité à suivre une consigne se travaille et s’évalue comme un usage à part entière.

Et une réponse bien écrite peut être fausse. Nous avons déjà vu notre classifieur produire une mauvaise réponse avec un score élevé. Pour le langage, les erreurs prennent d’autres formes : une référence inexistante, une explication plausible mais incorrecte, une API inventée.

Nous n’avons pas mesuré les erreurs des grands modèles avec notre corpus de mille caractères. L’expérience rend seulement visibles deux mécanismes que l’on retrouve chez eux : produire une sortie à partir d’un contexte et sélectionner des possibilités selon des scores. Leur fiabilité doit ensuite être évaluée sur la tâche qui nous intéresse.


[^p2-7-reponse-instructions]: [Ouyang et ses collègues, Training language models to follow instructions with human feedback (2022)](https://arxiv.org/abs/2203.02155).

Le corpus fixe les comptages de notre bigramme, le début fournit son contexte et la température modifie le tirage. L’attention nous a ensuite permis de combiner plusieurs positions. Gardons ces rôles en tête avant d’ajouter des outils autour du modèle.
