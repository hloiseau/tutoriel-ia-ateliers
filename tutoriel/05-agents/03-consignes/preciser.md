Voici une demande difficile à contrôler :

> Regarde le code, fais attention aux cas limites et assure-toi que tout est bon.

À quel résultat reconnaîtrons-nous que le travail est terminé ? Avec cette seule phrase, le modèle peut produire un commentaire très rassurant sans avoir inspecté le bon cas.

Pour notre projet, nous pouvons écrire :

```text
Lis la fonction notifier et les tests qui l’appellent.
Cherche si le retour en stock avec hausse de prix est couvert.
S’il existe, cite le test et sa valeur attendue.
Sinon, propose un test qui appelle notifier sur ce cas.
Ne modifie pas les fichiers. Ne prétends pas avoir exécuté la suite.
```

Les verbes sont impératifs, le cas est nommé et le résultat se vérifie dans les fichiers. L’agent doit retrouver un test précis ou en proposer un ; il n’a plus à deviner ce que « tout est bon » voulait dire.

Gardez les demandes courtes tant que le travail l’est. Dix interdictions héritées d’un autre ticket finiraient par cacher la seule règle qui compte ici.
