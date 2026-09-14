Nous avons vu comment plier nos fichiers afin de cacher une partie dont nous n'avions pas besoin à un moment dans le but de faciliter notre navigation.  
Les différents modes de pliage permettent de modifier les points de début et de fin d'un pli.

[[information]]
| Pour changer le mode de plis, nous avons utilisé le mode __Ligne de commande__ de Vim. Nous allons voir prochainement comment définir ce mode de manière persistante.

Voici un récapitulatif des commandes que nous avons vu:

+----------------------------------------+------------------------------------------------------------+
| Commande                               | Explication                                                |
+========================================+============================================================+
| `zo`                                   | Ouvre le pli sur lequel est le curseur                     |
+----------------------------------------+------------------------------------------------------------+
| `zc`                                   | Ferme le pli dans lequel est le curseur                    |
+----------------------------------------+------------------------------------------------------------+
| `za`                                   | Bascule entre l'état ouvert ou fermé                       |
+----------------------------------------+------------------------------------------------------------+
| `zO`                                   | Ouvre tous les plis de la hiérarchie                       |
+----------------------------------------+------------------------------------------------------------+
| `zC`                                   | Ferme tous les plis de la hiérarchie                       |
+----------------------------------------+------------------------------------------------------------+
| `zA`                                   | Ouvre ou ferme tous les plis de la hiérarchie              |
+----------------------------------------+------------------------------------------------------------+
| `zM`                                   | Ferme tous les plis du buffer                              |
+----------------------------------------+------------------------------------------------------------+
| `zR`                                   | Ouvre tous les plis du buffer                              |
+----------------------------------------+------------------------------------------------------------+
| `zm`                                   | Ferme le pli (non ouvert) le plus profond de la hiérarchie |
+----------------------------------------+------------------------------------------------------------+
| `zr`                                   | Ouvre le plus haut pli (non fermé) de la hiérarchie        |
+----------------------------------------+------------------------------------------------------------+
| `zf{[nombre] mouvement | objet texte}` | Crée un pli en méthode `manual`                            |
+----------------------------------------+------------------------------------------------------------+

[[attention | On sait maintenant:]]
| - Les différentes méthodes de pliages (`manual`, `indent`, `syntax`, `expr`, `marker`, `diff`)
| - Manipuler les plis