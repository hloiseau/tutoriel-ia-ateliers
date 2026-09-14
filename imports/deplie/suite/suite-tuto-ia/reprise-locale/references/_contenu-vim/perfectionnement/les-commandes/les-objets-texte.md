Je l'ai évoqué à la section précédente, les commandes peuvent agir sur un objet texte. Voici les objets texte de Vim.

# Les mots (Word)

Les mots sont [défini](http://vimdoc.sourceforge.net/htmldoc/motion.html#word) comme étant une suite de chiffres, lettres et underscores **ou** par une séquence de caractères non vide.

L'objet mot est identifié par `w`.

Exemple:

Ici Vim voit 3 mots: `un-deux`, `un deux trois`, `un,deux`, `un---deux`  
Ici il n'en voit qu'un seul: `un_deux_trois`

On peut le vérifier facilement en faisant la commande `dw` pour "delete word".

# Les phrases (Sentence)

Les phrases sont [défini](http://vimdoc.sourceforge.net/htmldoc/motion.html#sentence) comme finissant à un point ("."), un point d'exclamation ("!") ou d'intérrogation ("?")

L'objet phrase est identifié par `s`.

# Les paragraphes (Paragraph)

Les paragraphes sont [défini](http://vimdoc.sourceforge.net/htmldoc/motion.html#paragraph) comme commençant après une ligne vide.

L'objet paragraphe est identifié pas `p`.

# Les balises (Tag)

Les balises sont [défini](http://vimdoc.sourceforge.net/htmldoc/tagsrch.html#tag) de la même manière qu'elles le sont dans la norme XML (et HTML).

L'objet balise est identifié par `t`.

# Les citations (Quote)

Les quotes sont définies comme étant le contenu entre les caractères `"`, `'`, ou `` ` ``.

Les objets citations sont identifiés par `"`, `'`, ou `` ` ``.

Exemple:

Mon texte est `Le 'petit "chien" bleu' est ici` et que mon curseur est sur le "i" de chien.

Si je fais la commande `da"` ma phrase sera `Le 'petit bleu' est ici`.  
Tandis que si j'utilise la commande `da'` le résultat sera `Le est ici`

# Les blocs (Block)

Les blocs sont définis comme étant le contenu entre les caractères `( ) `, `[ ]`, `{ }`, et `< >`

Les objets bloques sont identifiés par, `(`, `)`, `[`, `]`, `{`, `}`, `<`, et `>`.  
Ils fonctionnent de la même manière que les blocs de citations.

---

Les objets texte peuvent être précédés d'un mouvement spécial. `i` et `a` signifiant `inside` et `around`.

Prenons un exemple, imaginons la situation suivante:

->![](/media/galleries/11359/e6ac72a0-6f55-4196-a8e1-3233ad241901.png)<-

Je souhaite supprimer le mot "deux", je peux donc essayer la commande `dw` pour "delete word".  
Mais voici le résultat:

->![](/media/galleries/11359/b217414b-e8cc-4211-95c5-b01d4cd72ba9.png)<-

Ce n'est pas vraiment le résultat que nous espérions. Ici Vim à supprimer la fin de notre mot jusqu'au début du suivant, en incluant l'espace.

Pour supprimer **tout** le mot, nous allons essayer la commande `diw` pour "delete inside word".  
Voici le résultat:

->![](/media/galleries/11359/eef5d052-00fc-4aa5-95e7-adfdd45fe9bb.png)<-

C'est plutôt bien, cependant nous avons deux espaces entre les mots "un" et "trois", ça aurait été ce que nous étions en insertion, pour ajouter du contenu entre les deux mots.

[[secret|Si nous avions voulu insérer]]
| Dans le cas où nous aurions voulu insérer un autre mot entre "un" et "trois" nous aurions utilisé la commande `ciw`.

Pour supprimer cet espace en trop nous pourrions tout simplement utiliser la commande `x`. Cependant, cela nous fait deux commandes. Pour pallier cela, nous devons utiliser le `a` à la place de `i` dans notre commande.  
Essayons maintenant avec la commande `daw`.

->![](/media/galleries/11359/e6db0b15-468b-404f-a685-e998924c2b46.png)<-

Et voilà !  :D  
Nous avons supprimé le mot "deux" en une commande tout en ne laissant qu'un seul espace entre "un" et "trois".

En conclusion, les mouvements spéciaux des objets texte ne sont qu'une lettre dans la commande (`i` ou `a`), mais changent grandement le résultat de notre action.