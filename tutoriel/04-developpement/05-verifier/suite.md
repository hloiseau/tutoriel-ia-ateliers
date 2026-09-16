Après correction, lancez :

```bash
python -m unittest discover -v
```

Avec le fichier complet de `02-test-rouge`, les **treize tests passent**. Si vous avez conservé les tests de l’agent, le nombre peut être différent. Vérifiez que les cas décidés dans la table sont couverts et que ceux qui échouaient passent désormais, avec les mêmes valeurs attendues.

Les noms des tests donnent un premier inventaire des situations contrôlées. Retrouvez surtout les deux qui échouaient avant la correction : ils doivent encore être présents, avec les mêmes valeurs attendues.

Dans le rapport de l’agent, cherchez la commande, son dossier d’exécution et son résultat. La formule « tests vérifiés » est trop floue : l’agent a pu lire leur code, en lancer un seul ou exécuter la suite complète.

Une dépendance manquante ou une commande interrompue doit rester visible dans le rapport. Un fichier de test bien écrit ne nous apprend rien sur le résultat d’une exécution qui n’a pas eu lieu.
