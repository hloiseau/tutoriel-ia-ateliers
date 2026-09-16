Faites l’essai sur `01-depart`, puis sur la version contenant les tests de `02-test-rouge`, dans deux copies séparées si votre assistant doit ouvrir un dossier. Ces versions se trouvent dans les fichiers fournis avec la partie 4. Utilisez une session neuve pour chaque essai.

Dans la première version, le test du retour avec hausse est absent. Dans la seconde, vous pouvez retrouver `test_retour_en_stock_avec_hausse`. Vérifiez dans le fichier si la réponse de l’agent correspond à l’état que vous lui avez montré.

Le même texte devrait mener à deux constats différents, puisque les fichiers diffèrent. Nous vérifions ainsi que la réponse correspond au projet ouvert, au lieu de nous contenter d’y retrouver les mots de la consigne.

S’il se trompe, notez la demande, le modèle choisi, le fichier réellement ouvert et la réponse. Puis changez un élément à la fois : une pièce jointe manquait-elle ? L’assistant avait-il gardé le contexte d’une autre copie ? La consigne demandait-elle vraiment de lire les tests ?

Au bout de ces deux essais, gardez le cas, l’état de départ et le résultat. Vous pourrez les rejouer après avoir changé la consigne ou le modèle. Deux réussites resteraient deux observations, bien loin d’une fiabilité « à 100 % ».
