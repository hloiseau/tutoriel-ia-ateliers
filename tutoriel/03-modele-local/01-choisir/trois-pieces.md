Dans la partie précédente, notre programme chargeait les nombres appris pendant l’entraînement. Nous allons retrouver ce principe à une autre échelle : le modèle possède beaucoup plus de paramètres et une architecture différente, tandis que ses poids restent des données à charger.

Le **moteur d’inférence** réalise les calculs nécessaires à la production d’une réponse. Nous utiliserons llama.cpp. Notre **client** sera un petit script Python qui envoie des messages à ce moteur, lancé sous forme de serveur.

![Un client Python interroge un serveur local qui charge les poids depuis le disque](image:images/installation.png)
Figure: Les éléments de notre installation

Pourquoi passer par un serveur alors que tout tient sur le même ordinateur ? Parce qu’il garde le modèle chargé pendant que différents clients lui demandent des calculs. Notre script, une interface web ou un autre programme pourront ainsi l’interroger. Ici, « serveur » désigne le rôle du processus lancé sur notre machine.

Pour le moment, le modèle recevra du texte et produira du texte. Lancer des commandes ou modifier des fichiers demandera plus tard un programme capable d’organiser et de contrôler ces actions autour de lui.
