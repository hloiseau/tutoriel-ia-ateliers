**TL;DR** — Notre réseau prédit le prochain caractère à partir des douze précédents. Nous allons initialiser ses 15 055 paramètres au hasard, les entraîner sur CPU, puis comparer la baisse de perte au texte réellement généré.

Tout le modèle tient dans `petit_modele.py`. Sa seule tâche consiste à prédire un caractère ; il ne possède ni outils ni mémoire documentaire. Cette taille volontairement modeste nous permet de lire ses calculs et de rejouer son entraînement sur CPU.
