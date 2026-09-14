La génération d’images suit également plusieurs pistes. En 2014, les **GAN**, ou réseaux antagonistes génératifs, proposent d’entraîner deux modèles ensemble : l’un produit des exemples, l’autre cherche à distinguer ces productions des données utilisées pour l’entraînement.[^h6s4-gan]

Vous pouvez imaginer un dessinateur et un examinateur, à condition de garder en tête qu’il s’agit de calculs. Le générateur est ajusté pour produire des exemples qui trompent davantage l’autre modèle ; celui-ci est ajusté pour mieux les distinguer.

Les **modèles de diffusion** suivent une autre idée. Une famille de méthodes apprend à inverser progressivement un processus d’ajout de bruit. Les travaux de Ho, Jain et Abbeel en 2020 constituent un repère important de cette approche.[^h6s4-diffusion]

![Une forme devient progressivement bruitée ; une flèche inverse illustre le principe d’un débruitage appris.](image:images/diffusion.png)
Figure: Illustration du bruit ajouté à une forme. La rangée ne représente pas les sorties d’un modèle entraîné ; elle sert à expliquer le principe.

Sur l’image, la forme devient de moins en moins visible quand on ajoute du bruit. Pendant l’apprentissage, le modèle est entraîné à estimer comment revenir vers des données moins bruitées. Lors de la génération, des méthodes utilisent cette capacité pour construire progressivement une image à partir de bruit.

Les versions guidées par du texte ajoutent des informations sur ce que l’on souhaite obtenir. On ne peut donc pas résumer toute la génération d’images à un modèle qui choisit le prochain mot.


[^h6s4-gan]: [Goodfellow et ses collègues, Generative Adversarial Networks (2014)](https://arxiv.org/abs/1406.2661).
[^h6s4-diffusion]: [Ho, Jain et Abbeel, Denoising Diffusion Probabilistic Models (2020)](https://arxiv.org/abs/2006.11239).
