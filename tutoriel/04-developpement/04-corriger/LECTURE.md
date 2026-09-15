# 7. Faire le changement et lire le diff

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** la règle attendue tient dans deux conditions. Nous allons enlever celle qui autorisait une notification pour une simple remise en stock.

## Relire les opérateurs

Voici la fonction initiale :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
    )
```

Lisez-la à voix haute : le produit doit être disponible maintenant, et il faut soit une baisse de prix, soit une ancienne indisponibilité.

Le second terme du `or` explique notre problème. Pour un retour en stock, `not ancien.disponible` vaut vrai. Le prix peut être identique ou même plus élevé : l’expression entre parenthèses sera tout de même vraie.

Notre ticket exige uniquement une disponibilité actuelle et une baisse stricte. La correction devient :

```python
def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes
    )
```
Code: La fonction après correction

Nous conservons les parenthèses et la présentation afin que le diff porte sur le changement de comportement. Il serait possible d’écrire cette expression sur une ligne, mais cela n’est pas nécessaire pour résoudre le ticket.

N’ajoutez pas `ancien.disponible` dans la nouvelle condition. Cela empêcherait de notifier une vraie baisse au moment du retour en stock, contrairement à la règle décidée.

![Seul le cas disponible maintenant avec baisse de prix autorise une notification](../images/decision.png)
Figure: La règle complète tient dans ces quatre combinaisons

## Une demande de modification précise

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

## Lire ce qui a vraiment changé

Un résumé de l’agent raconte ce qu’il pense avoir fait. Le diff montre les fichiers modifiés. Ouvrez celui de votre éditeur, puis cherchez le changement dans `suivi.py`.

La correction fournie retire ce morceau :

```diff
-        nouveau.prix_centimes < ancien.prix_centimes or not ancien.disponible
+        nouveau.prix_centimes < ancien.prix_centimes
```
Code: Le changement de comportement dans la fonction

Si Git est installé, vous pouvez aussi comparer les deux dossiers depuis leur dossier parent :

```bash
git diff --no-index 01-depart/suivi.py mon-suivi/suivi.py
```

Cette commande fonctionne sans créer de dépôt Git. Avec `--no-index`, un code de sortie égal à 1 signifie que les fichiers diffèrent ; ce n’est pas forcément un échec de la comparaison.[^p4-diff]

Regardez ensuite les autres fichiers modifiés. Les nouveaux tests sont attendus. Une modification des données d’entrée pour éviter le bug, une suppression de validation ou une réécriture de tout le programme demandent une explication.

Si vous débutez, choisissez une ligne retirée et une ligne conservée, puis expliquez leur rôle sans recopier le résumé de l’agent. Si vous n’y arrivez pas encore, revenez à la fonction. Le résultat est assez petit pour que cette lecture reste abordable.

[^p4-diff]: Git, [comparaison de fichiers avec `git diff --no-index`](https://git-scm.com/docs/git-diff).


