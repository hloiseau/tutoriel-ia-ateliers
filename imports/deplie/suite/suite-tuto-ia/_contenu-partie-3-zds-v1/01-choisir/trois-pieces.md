Dans la partie précédente, notre programme chargeait des nombres appris pendant l’entraînement. Le principe reste le même. Le modèle que nous allons utiliser possède beaucoup plus de paramètres et une architecture différente, mais ses poids ne sont pas un programme qui se lance tout seul.

Le **moteur d’inférence** réalise les calculs nécessaires à la production d’une réponse. Nous utiliserons llama.cpp. Notre **client** sera un petit script Python qui envoie des messages à ce moteur, lancé sous forme de serveur.

![Un client Python interroge un serveur local qui charge les poids depuis le disque](image:images/installation.png)
Figure: Les éléments de notre installation

Pourquoi passer par un serveur alors que tout est sur le même ordinateur ? Pour pouvoir changer le client sans recharger les poids à chaque question. Notre script, une interface web ou un autre programme peuvent demander un calcul au même processus. Le mot « serveur » décrit ici son rôle ; il ne signifie pas que nous avons acheté une machine supplémentaire.

Nous n’allons pas encore donner au modèle la possibilité de lancer des commandes ou de modifier des fichiers. Il recevra du texte et produira du texte. Les programmes qui organisent des appels d’outils ajoutent d’autres mécanismes autour de ce calcul.
