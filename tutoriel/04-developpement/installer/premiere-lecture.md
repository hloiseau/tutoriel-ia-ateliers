Dans `suivi.py`, repérez la fonction `notifier`. Copiez-la dans la discussion, avec la définition de `Etat` juste au-dessus. Dans Continue, vous pouvez aussi sélectionner le code et utiliser **Ctrl+L**, ou **Cmd+L** sur macOS, pour l’ajouter à la conversation[^p4-install-chat].

Ajoutez cette demande :

> Explique ce que représente un état et dans quels cas cette fonction renvoie vrai. Appuie-toi uniquement sur cet extrait. Ne modifie aucun fichier et ne propose pas encore de correction.

Nous n’attendons pas une réponse mot pour mot. Le code doit permettre de retrouver deux informations : un état contient un prix en centimes et une disponibilité ; la fonction décide de notifier lorsque le produit est disponible et qu’au moins une des deux conditions de la parenthèse est vraie.

Lisez l’explication en gardant le code ouvert. Si le modèle parle d’un envoi de courriel ou d’une base de données, cherchez ce qui lui permet de l’affirmer dans l’extrait. Vous ne trouverez rien : cette fonction renvoie seulement un booléen.

Votre modèle local répond mal en français ? Vous pouvez essayer la même demande en anglais :

> Explain what an Etat represents and when notifier returns True. Use only this snippet. Do not change any files or suggest a fix yet.

L’objectif reste de comprendre la fonction. Si l’explication ne vous aide pas, revenez au code et décomposez la condition vous-même. Nous allons justement le faire dans le chapitre suivant.

### Et pour les modifications ?

Avec un assistant disposant d’un mode agent, vous pourrez ensuite lui demander de préparer les changements, puis examiner le diff et les résultats des tests.

L’expérience locale s’arrête ici : une réponse sur une fonction ne valide pas la capacité du modèle à modifier le projet. Si vous voulez poursuivre en mode Chat, vous pourrez examiner ses propositions et les appliquer vous-même, mais nous n’avons pas vérifié que ce petit modèle saura suivre les demandes des chapitres suivants.

Les exercices Python peuvent aussi se faire sans IA. Les corrigés vous permettront de vérifier votre travail ; cela ne remplacera pas l’expérience de piloter un agent.

Gardez votre dossier `mon-suivi` : nous allons maintenant y lancer les tests et comprendre pourquoi un programme dont les tests passent peut tout de même avoir besoin d’une correction.

[^p4-install-chat]: Continue, [discussion et sélection de code](https://docs.continue.dev/ide-extensions/chat/quick-start).
