Avant de manipuler les fonctions de pliage de Vim, nous devons nous attarder sur les différentes méthodes que nous avons à disposition.

- `manual` → Les plis sont définis en entrant une commande
- `indent` → Groupe les lignes qui ont le même niveau d'indentation pour un pli
- `syntax` → Les plis sont définis par la coloration syntaxique
- `expr` → Les plis sont définis par une expression que l'utilisateur indique
- `marker` → Plis selon des caractères spéciaux qui définissent le début et la fin du pli
- `diff` → Plis le texte qui n'est pas changé lorsque regarde les différences entre fichiers (utile dans le mode diff)

La différence entre ces modes de pliage ne change que le début et la fin des plis. Autrement, les commandes sont toutes le même indifféremment du mode.