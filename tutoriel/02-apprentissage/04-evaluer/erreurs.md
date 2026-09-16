Ouvrez maintenant `sorties/lineaire-erreurs.png` :

![Huit erreurs réelles du modèle linéaire, avec la réponse attendue, la réponse choisie et son score.](image:images/lineaire-erreurs.png)
Figure: Premières erreurs dans l’ordre du jeu de test. Données d’E. Alpaydin et C. Kaynak, UCI, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Regardez d’abord un chiffre sans lire son étiquette. Êtes-vous certain de votre propre réponse ? Certaines images deviennent ambiguës avec seulement 64 pixels.

Regardez ensuite les scores. Une mauvaise réponse peut recevoir un score élevé. Le modèle répartit ses probabilités entre les dix classes disponibles ; il ne possède pas une onzième classe « je ne reconnais pas ce dessin ».

Une image complètement noire passera aussi dans les calculs. Si tous les pixels sont nuls, les scores du modèle linéaire se réduisent à ses biais. Il choisira quand même un chiffre.

Une règle pourrait refuser les scores trop faibles. Avant de l’adopter, il faudrait compter les erreurs qu’elle évite et les bonnes réponses qu’elle rejette. Un seuil choisi au hasard déplacerait simplement le problème.
