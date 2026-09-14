**TL;DR**

- Nous allons entraîner un programme à reconnaître des chiffres, puis lui soumettre nos propres dessins. Tout fonctionne sur CPU, sans abonnement ni carte graphique dédiée.
- Un modèle reçoit des nombres, calcule une réponse et ajuste ses paramètres pendant l’entraînement. Nous écrirons ces calculs avec NumPy.
- Nous garderons des images à part pour vérifier les résultats. Le modèle pourra réussir ses exercices et se tromper sur un chiffre légèrement décalé. 😅
- Un second petit projet produira du texte. Nous manipulerons les tokens, le choix du caractère suivant et un calcul d’attention, avant de regarder où interviennent les outils d’un agent.

Prenez un crayon et écrivez un trois. Vous avez probablement fait deux courbes, sans mesurer exactement leur position. Écrivez-en un deuxième : il ne sera pas identique au premier, mais vous le reconnaîtrez quand même.

Pour un programme, nous allons devoir préciser ce qui entre, ce qui sort et comment décider qu’une réponse est correcte. Les images feront huit pixels de côté. C’est petit, mais suffisant pour commencer à lui donner du travail.

Vous aurez besoin de savoir lancer une commande et de connaître les bases de Python : variables, fonctions, boucles et listes. Les calculs sur des tableaux seront expliqués au moment où nous les utiliserons.
