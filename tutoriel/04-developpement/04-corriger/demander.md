Les tests reproduisent le problème ; la fonction est encore dans son état initial. Dans la même session, demandez maintenant :

```text
Applique le comportement décrit dans TICKET.md.
Conserve les interfaces existantes et limite la modification
au code nécessaire.
Ne change pas les réponses attendues des tests pour les faire passer.
Lance la suite avec python -m unittest discover -v.
Montre le diff et explique la condition modifiée.
Ne crée pas de commit et ne publie rien.
```
Code: Confier la correction en gardant un résultat relisible

La demande décrit le comportement sans souffler la ligne de correction. Regardez la solution proposée et les fichiers touchés. Si vous faites l’exercice à la main, essayez votre modification avant de lire la section suivante.

Cela reste une consigne au modèle. Pour limiter effectivement son accès aux fichiers, au réseau ou à la publication, utilisez aussi les permissions de votre outil. Une phrase dans un prompt n’a pas le même rôle qu’un droit technique refusant l’opération.

Si l’agent propose une classe de notification, une nouvelle dépendance ou un système de règles pour cette fonction, demandez-lui quel cas du ticket le justifie. En l’absence de réponse concrète, revenez à une modification plus petite. Le temps déjà passé à générer du code ne lui donne aucune valeur particulière.
