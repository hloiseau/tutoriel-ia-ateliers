Lorsque nous exécutons Vim depuis la console sans arguments nous avons un [No Name] buffer. Si nous mettons en argument le nom d'un fichier nous avons un buffer d'ouvert.  
Vim nous permet aussi d'ouvrir plusieurs buffers en donnant le nom de plusieurs fichiers.

```console
vim le_chat.txt le_chien.txt
```

Ici nous aurons deux buffers d'ouvert et verrons le buffer du chat. Si nous essayons de quitter en bas à gauche vous devriez avoir une erreur de ce type `E173: 1 more file to edit`. Cela signifie qu'il y a un autre buffer d'ouvert. Si l'on veut quitter tous les buffers ouverts, on peut utiliser la commande `:qa` (pour sauvegarder ce sera `:wa`).

[[information]]
| Lorsqu'un buffer est ouvert, on peut en ouvrir un autre avec la commande `:e <nom_du_fichier>`

Pour lister tous les buffers ouverts nous allons utiliser la commande `:ls`.
Nous devrons avoir quelque chose comme suit en bas à gauche

```console
  1 %a   "le_chat.txt"                  line 1
  2      "le_chien.txt"                 line 0
```

Le `%` signifier que c'est le buffer que nous avons actuellement devant nous.

Nous pouvons passer au buffer suivant avec la commande `:bn` (buffer next). À présent, nous sommes dont dans le buffer du chier. Si je reliste mes buffers avec `:ls` voici le résultat:

```console
  1 #    "le_chat.txt"                  line 1
  2 %a   "le_chien.txt"                 line 1
```

Maintenant un `#` est apparu devant le premier buffer. Cela signifie que c'est le dernier buffer que nous avons visité.

Nous pouvons retourner au buffer précédent avec la commande `:bp`.

Il y a d'autres commandes sur les buffers, je le ne les aient pas présenté ci-dessus car elles prennent leurs intérêts lorsque nous avons un plus grand nombre de buffers ouvert.

Voici une liste des commandes avec les buffers:

| Commande | Explication |
|:--------:|:-------------|
| `:ls` | Liste les buffers ouverts |
| `:bn` | Passe au buffer suivant |
| `:b<nombre>` | Passe au buffer portant le nombre `<nombre>` |
| `:bp` | Passe au buffer précédent |
| `:b#` | Passe au dernier buffer visité |
| `:bf` | Passe au premier buffer de la liste |
| `:bl` | Passe au dernier buffer de la liste |
| `:bm` | Passe au prochain buffer modifié |
| `:enew` | Ouvre un [No Name] buffer |

Ça en est tout sur les buffers pour le moment, nous y reviendrons surement dans un chapitre suivant.