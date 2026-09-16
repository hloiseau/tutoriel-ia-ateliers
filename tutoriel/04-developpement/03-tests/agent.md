Gardez `mon-suivi` ouvert : il contient encore la fonction initiale et ses trois tests. Nous allons demander à l’agent d’ajouter **un seul test**, celui de la remise en stock au même prix.

Dans la session **Local** de VS Code, passez du rôle **Ask** au rôle **Agent** avec le sélecteur de la discussion. D’après la documentation consultée, Agent dispose des outils de lecture, d’édition et d’exécution ; Ask nous servait à discuter[^p4-premier-agent]. Avec un autre assistant, activez son mode de modification du projet. Gardez les demandes d’autorisation pour les commandes : nous voulons voir ce qui va réellement être lancé.

Envoyez :

```text
Dans mon-suivi, lis TICKET.md, suivi.py et test_suivi.py.
Crée test_ticket.py avec unittest.
Ajoute uniquement test_retour_en_stock_sans_baisse :
notifier(Etat(2000, False), Etat(2000, True)) doit renvoyer False.
Ne modifie ni suivi.py ni les tests existants.
Lance python -m unittest discover -v depuis mon-suivi.
Rapporte le résultat obtenu et l’assertion en échec.
Ne crée pas de commit et ne publie rien.
```
Code: Notre première demande qui modifie un fichier

Adaptez `python` si vous avez utilisé une autre commande au chapitre précédent. Quand l’outil vous demande d’autoriser une commande, regardez le dossier et la commande affichés. Cet exercice ne demande ni installation de paquet ni accès réseau.

Observez les actions annoncées par l’interface : lecture des fichiers, création du test, lancement de la suite. Si l’agent corrige aussi `suivi.py`, arrêtez-le et remettez **ce seul fichier** dans son état initial à partir de `01-depart`. Gardez le nouveau test : son échec doit précéder la correction.

Si vous travaillez sans agent, créez le test décrit dans la section suivante. Dans les deux cas, nous continuons dans le même dossier.

[^p4-premier-agent]: Microsoft, [rôles disponibles dans une session Local](https://code.visualstudio.com/docs/agents/run/agent-harnesses).
