Nous avons vu les *view* qui permettent de sauvegarder une fenêtre entre plusieurs utilisations de Vim.  
Ici nous allons parler des sessions. Ces dernières permettent de sauvegarder plus qu'une seule fenêtre. On peut sauvegarder toutes les fenêtres et tous leurs environements, c'est cela qui constitue la session.

# Crée une session

Pour créer une session on utilise la commande `:mksession`. En faisant cela Vim va créer un fichier `Session.vim` à l'endroit où vous avez ouvert Vim. Vous pouvez aussi choisir le nom du fichier en donnant un nom après la commande (ex: `:mksession ma_session.vim` sauvegardera la session dans le fichier `ma_session.vim`)

[[attention]]
| La session, une fois créée, ne peut pas être modifiée. Les sessions sont immuables. Pour sauvegarder les changements on utilise la commande `:mksession!` (ou `:mksession! ma_session.vim`)

Tout comme les *view*, lorsque l'on sauvegarde une session la configuration dans notre `.vimrc` est aussi sauvegardé pour ne pas changer les options de la session même si la configuration de Vim change.

# Ouvrir une session 

Pour rouvrir une session on utilise la commande `:source` suivie du chemin vers le fichier.  
On peut aussi directement ouvrir Vim avec notre session en utilisant l'argument `-S` (ex: `vim -S ma_session.vim`)

# Supprimer une session

Vim ne permet pas de supprimer une session. Si on n'a plus besoin de notre session il nous suffit de supprimer le fichier généré lors de la création de la session.