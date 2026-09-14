Nous allons dans un premier temps parler des *View*. Elles permettent de sauvegarder des propriétés spécifiques à une fenêtre comme par exemple l'activation de la coloration syntaxique, les paramètres d'indentation, l'affichage des numéros des lignes, ...  
Si nous avons besoin de se souvenir de plus d'informations nous utiliserons une session.

[[information]]
| Ces informations ne sont pas sauvegardées dans le `.vimrc`. Tout comme les registres ou l'historique des commandes, les *views* sont sauvegardés dans le fichier `.viminfo`.

# Crée une *view*

Pour créer une *view* nous allons utiliser la commande `:mkview`. La commande va enregistrer le contenu de la fenêtre actuelle.  
La commande `:mkview` prend en argument, soit le nom de notre vue, soit un chiffre (entre 1 et 9) qui nous permettra de retrouver notre vue. Si on ne donne pas d'argument la *view* est sauvegardée de manière anonyme.

[[information]]
| Si vous avez choisi de donner un nom à votre *view* alors Vim crée un fichier (avec ce nom) dans le répertoire où vous avez ouvert Vim.

[[attention]]
| Les *views* sont indissociables de leurs fichiers. Ce n'est pas un "template" de configuration. Ouvrir une vue avec un autre fichier n'aura aucune action car Vim reconnait que la vue sauvegardée ne correspond pas au fichier ouvert.

Lors de l'enregistrement de la vue, Vim sauvegarde toute la configuration par défaut mais aussi la configuration donnée par notre `.vimrc`. Cela permet de ne pas changer les options de la vue même si la configuration de Vim change.

# Ouvrir une *view*

On ouvre une vue avec la commande `:loadview` si nous l'avons sauvegardée de manière anonyme ou si nous avons sauvegardé la vue avec un chiffre.  
Pour ouvrir une vue sauvegardée avec un nom, on utilise la commande `:source`. Vim ouvrira la vue avec le buffer correspondant au fichier.