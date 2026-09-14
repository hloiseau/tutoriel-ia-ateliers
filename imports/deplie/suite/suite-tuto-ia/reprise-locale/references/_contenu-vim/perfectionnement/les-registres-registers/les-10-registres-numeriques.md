Il existe 10 registres numériques (`"0`, `"1`, `"2`, `"3`, `"4`, `"5`, `"6`, `"7`, `"8`, et `"9`).

Ces registres sont peuplés et gérés automatiquement par Vim. Néanmoins il est possible d'écrire dedans, ils ne sont pas en lecture seule.

# Le fonctionnement des registres numérique

Pour toutes actions de copie, en plus de remplir le registre sans nom (`""`), la sélection sera aussi mise dans le registre 0 (`"0`).  
On aura donc les registres `""` et `"0` qui auront le même contenus.

Pour toutes actions de coupe, en plus de remplir le registre sans nom (`""`), la sélection sera aussi mise dans le registre 1 (`"1`).  
Cependant, avant de bêtement écraser ce qu'il y avait dans le registre `"1`, Vim met le contenu dans le registre `"2`. Et le contenu du registre `"2` dans le registre `"3`. Et ce jusqu'au registre `"9`. Le contenu du registre `"9` est quant à lui perdu car il est remplacé par celui du registre `"8`.

Les registres `"1` à `"9` sont peuplé de la sorte de toujours avoir les 9 dernières sélections coupées.

Je vous invite à essayer de couper et copier du texte en faisant la commande `:reg` entre chaque étape afin d'observer le fonctionnement des registres numérique.