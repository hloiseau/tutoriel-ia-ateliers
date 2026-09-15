Pour un service hébergé, votre ordinateur doit surtout faire tourner l’éditeur et le projet. Le fournisseur effectue les calculs du modèle. Vous avez besoin d’un accès au service et d’une connexion réseau, mais pas d’une grosse carte graphique.

En local, vous fournissez aussi la mémoire et le calcul. Cela permet de garder l’inférence sur votre machine et de travailler sans accès au fournisseur une fois les éléments nécessaires téléchargés. En échange, il faut choisir un modèle qui tient en mémoire et dont le temps de réponse vous convient.

| Situation | Point de départ possible |
| --- | --- |
| Petit ordinateur, priorité à une installation simple | Offre hébergée gratuite, si l’envoi du code est acceptable |
| Envoi du code exclu, aucune carte graphique dédiée | Essai local limité ; aucun parcours d’agent validé ici pour cette configuration |
| Machine disposant de davantage de mémoire et d’un GPU compatible | Tester un modèle local sur les tâches visées, puis mesurer le délai et vérifier le résultat |
| Assistant déjà fourni par votre équipe | Commencer avec cet outil, dans les conditions d’usage de l’équipe |
Table: Choisir selon ses contraintes

Notre SmolLM2 de la partie 3 nous a servi à comprendre l’inférence. Il ne faut pas attendre de lui qu’il explore un dépôt et corrige un ticket tout seul. Nous allons d’abord l’utiliser pour vérifier la connexion, puis proposer un petit modèle spécialisé dans le code.

Il faut distinguer deux choses : **le logiciel de l’agent peut tourner sur votre ordinateur pendant que son modèle tourne chez un fournisseur**. Dans ce cas, vous n’avez pas besoin d’une grosse carte graphique. Faire aussi tourner le modèle chez vous pose une autre question.

llama.cpp permet l’inférence sur CPU[^p4-cpu-moteur]. Mais charger un modèle et obtenir une réponse ne prouve pas qu’il sera utile pour développer. Un agent doit exploiter le code qu’il lit, choisir ses actions, comprendre les résultats des commandes et poursuivre la tâche. Le temps de traitement du contexte s’ajoute à celui des réponses, à chaque étape. Il faut vérifier tout cela sur une tâche réelle.

Notre essai avec Qwen2.5-Coder à 1,5 milliard de paramètres n’a pas été exécuté dans cette configuration. Nous ne savons donc pas encore s’il apporte une aide utile sur cet atelier, ni combien de temps il demande. Continue cite d’ailleurs un modèle Qwen Coder de cette taille pour la complétion, et d’autres modèles pour le travail d’agent[^p4-cpu-roles]. Ce sont des usages différents.

Si vous ne pouvez ni envoyer votre code à un service ni utiliser un modèle local adapté, vous pouvez faire les exercices Python vous-même. Vous apprendrez à reproduire le problème et à vérifier la correction ; l’utilisation d’un agent restera à expérimenter avec une configuration qui le permet.

Reste la question des données. Une API personnelle peut vous laisser choisir votre fournisseur, sans rendre l’inférence locale. Et une option « ne pas utiliser mes données pour l’entraînement » ne signifie pas que le code ne quitte jamais l’ordinateur : elle porte sur un usage des données après leur transmission.

Pour notre atelier, nous utiliserons des fichiers publics et un ticket fictif. Pour votre travail, il faudra savoir ce que votre équipe autorise à transmettre. Nous reviendrons plus largement sur ces choix ; ils comptent déjà au moment d’installer l’outil.

[^p4-cpu-moteur]: llama.cpp, [moteur d’inférence et plateformes prises en charge](https://github.com/ggml-org/llama.cpp).
[^p4-cpu-roles]: Continue, [configuration et modèles recommandés pour le mode Agent](https://docs.continue.dev/ide-extensions/agent/model-setup).
