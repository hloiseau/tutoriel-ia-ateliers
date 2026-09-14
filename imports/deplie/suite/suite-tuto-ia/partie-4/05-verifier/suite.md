Après correction, lancez :

```bash
python -m unittest discover -v
```

Avec le fichier complet de `02-test-rouge`, les **treize tests passent**. Si vous avez seulement écrit le premier nouveau test, vous en aurez quatre : ce n’est pas la même couverture, même si la dernière ligne est également `OK`.

Les noms des tests vous permettent de voir les situations réellement contrôlées. Regardez en particulier les deux qui échouaient avant la correction. Ils doivent toujours être présents et conserver leurs valeurs attendues.

Dans un rapport d’agent, cherchez la commande, son dossier d’exécution et son résultat. « Tests vérifiés » peut cacher plusieurs choses : une lecture du code des tests, une exécution partielle, ou une suite complète. Nous voulons savoir laquelle a eu lieu.

Si une dépendance manque ou qu’une commande échoue, le rapport doit le dire. Réussir à écrire les tests n’est pas la même chose que réussir à les exécuter.
