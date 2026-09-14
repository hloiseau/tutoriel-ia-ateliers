Pour demander cette correction à l’agent, vous pouvez utiliser :

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

Les verbes disent ce qui doit être fait. « Ce serait bien de vérifier les tests » laisse une intention vague ; « lance cette commande et rapporte son résultat » donne une action et une preuve à chercher.

Cela reste une consigne au modèle. Pour limiter effectivement son accès aux fichiers, au réseau ou à la publication, utilisez aussi les permissions de votre outil. Une phrase dans un prompt n’a pas le même rôle qu’un droit technique refusant l’opération.

Si l’agent propose une classe de notification, une nouvelle dépendance ou un système de règles pour cette fonction, demandez-lui quel cas du ticket le justifie. Vous pouvez rejeter ces ajouts et demander une modification plus petite. Vous n’êtes pas obligé de conserver du code parce qu’il a déjà été généré.
