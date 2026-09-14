Pour voir les marque-pages que nous avons créés on utilise la commande `:marks`.  
La commande nous affiche un résultat similaire à la commande `:reg` (cf. le chapitre sur les registres). Nous avons sur chaque ligne:

-  le nom du marque-page
-  la ligne où il se situe
-  la colonne de ce dernier
-  et la ligne complète du marque-page (ou le fichier dans lequel il est si ce n'est pas celui du *buffer* courant)

[[information]]
| On remarque qu'il y a des marque-pages numérotés de 0 à 9. Le 0 est le dernier endroit où nous étions lorsque nous avons quitté Vim. 1 est l'avant-dernier, 2 l'antépénultième, ...  
| On ne peut pas assigner ces marque-pages nous-mêmes.

Lorsque vous listez vos marque-pages, vous allez aussi sûrement en voir d'autre que ceux avec des chiffres ou des lettres.  
Voici leurs noms et ce qu'ils réfèrent:


| Marque-page | Signification |
| ------- | -------- |
| `'`     | Marque la ligne du *buffer* courant d'où le curseur provient |
| `` ` `` | Marque la position du *buffer* courant d'où le curseur provient |
| `.`     | Marque la position dans le *buffer* courant du dernier changement |
| `"`     | Marque la position du curseur la dernière fois que nous avons quitté le *buffer* |
| `[`     | Marque la position de début des derniers changements |
| `]`     | Marque la position de fin des derniers changements |
| `<`     | Marque la position de début de la dernière sélection visuelle |
| `>`     | Marque la position de fin de la dernière sélection visuelle |