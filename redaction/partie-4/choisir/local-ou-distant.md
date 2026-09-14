Pour un service hébergé, votre ordinateur doit surtout faire tourner l’éditeur et le projet. Le fournisseur effectue les calculs du modèle. Vous avez besoin d’un accès au service et d’une connexion réseau, mais pas d’une grosse carte graphique.

En local, vous fournissez aussi la mémoire et le calcul. Cela permet de garder l’inférence sur votre machine et de travailler sans accès au fournisseur une fois les éléments nécessaires téléchargés. En échange, il faut choisir un modèle qui tient en mémoire et dont le temps de réponse vous convient.

| Situation | Point de départ possible |
| --- | --- |
| Petit ordinateur, priorité à une installation simple | Offre hébergée gratuite, si l’envoi du code est acceptable |
| Envoi du code exclu, aucune carte graphique dédiée | Petit modèle de code sur CPU et demandes courtes |
| Machine disposant de davantage de mémoire et d’un GPU compatible | Même principe local, puis essais de modèles plus volumineux |
| Assistant déjà fourni par votre équipe | Commencer avec cet outil, dans les conditions d’usage de l’équipe |
Table: Plusieurs chemins pour le même atelier

Notre SmolLM2 de la partie 3 nous a servi à comprendre l’inférence. Il ne faut pas attendre de lui qu’il explore un dépôt et corrige un ticket tout seul. Nous allons d’abord l’utiliser pour vérifier la connexion, puis proposer un petit modèle spécialisé dans le code.

Une grosse carte graphique donnera davantage de possibilités, mais elle ne sera pas le ticket d’entrée du tutoriel. Avec un modèle modeste, on peut discuter d’une fonction, demander un exemple et appliquer soi-même une proposition. Les manipulations sur le programme resteront les mêmes.

Reste la question des données. Une API personnelle peut vous laisser choisir votre fournisseur, sans rendre l’inférence locale. Et une option « ne pas utiliser mes données pour l’entraînement » ne signifie pas que le code ne quitte jamais l’ordinateur : elle porte sur un usage des données après leur transmission.

Pour notre atelier, nous utiliserons des fichiers publics et un ticket fictif. Pour votre travail, il faudra savoir ce que votre équipe autorise à transmettre. Nous reviendrons plus largement sur ces choix ; ils comptent déjà au moment d’installer l’outil.
