Les buffers sont donc une copie du fichier présent sur le disque. On peut voir un buffer au travers de plusieurs fenêtres (que nous allons voir au chapitre suivant). Les buffers sont synchronisés entre eux, leur contenu est donc toujours cohérent.

[[attention | On sait maintenant:]]
| - Vim ne travaille pas directement sur le fichier mais avec une *copie*, le buffer
| - Les différents types de buffers (Le buffer, le [No Name] buffer, le scratch buffer)
| - Se déplacer entre les buffers