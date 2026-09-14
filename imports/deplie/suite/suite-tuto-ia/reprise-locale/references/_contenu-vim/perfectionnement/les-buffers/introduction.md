Depuis le début de ce tutoriel, nous avons manipulé des buffers sans nous en rendre compte.

Lorsque nous éditions un fichier, ce dernier n'est pas modifié sur le disque à chaque changement que nous faisons. Vim s'occupe de copier le fichier disque dans la RAM de notre ordinateur. C'est ce fichier chargé en RAM que nous appelons **buffer**.  
Lorsque nous modifions notre buffer, la version du fichier sur le disque reste inchangée. C'est quand nous décidons d'écrire le buffer (avec la commande `:w`) que le fichier sur le disque sera changé.

L'utilisation des buffers plutôt que l'utilisation du fichier du disque permet notamment qu'il soit affiché dans plusieurs **fenêtres** (nous verrons les viewport ou window au chapitre suivant) avec un contenu toujours cohérent entre les uns et les autres. Ils sont synchronisés.  
Si votre fichier est grand, les buffers (accompagnés des viewport) vous permettront d'avoir le début de votre buffer ainsi de la fin l'un à côté de l'autre.