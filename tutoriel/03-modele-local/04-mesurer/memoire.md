Le poids du téléchargement est facile à trouver. La mémoire nécessaire pendant une réponse l’est moins.

Pour un calcul grossier, 360 millions de paramètres stockés chacun sur 16 bits représentent 720 millions d’octets. Sur 8 bits, ce serait 360 millions ; sur 4 bits, 180 millions. Ces nombres décrivent **les paramètres seuls**, en supposant ce nombre rond et une même précision partout.

![Volume théorique de 360 millions de paramètres pour trois précisions](image:images/poids.png)
Figure: Volume théorique des paramètres seuls, en Mo décimaux

Pour voir l’effet d’une précision réduite, prenons quelques nombres et arrondissons-les au quart le plus proche. Les déplacements sont visibles : nous gagnons une représentation plus grossière, mais nous perdons une partie de l’information.

![Des nombres sont ramenés au quart le plus proche](image:images/quantifier.png)
Figure: Une quantification uniforme au quart, pour observer les arrondis

Les formats de quantification des modèles emploient des méthodes plus élaborées, notamment des paramètres par blocs de valeurs. Notre arrondi permet de comprendre l’approximation ; il ne reproduit pas le format Q8_0.

Notre fichier Q8_0 fait environ 386 Mo. Il contient aussi les éléments nécessaires à son interprétation, et le stockage quantifié possède ses propres informations. Le nom « 8 bits » ne promet donc pas exactement un octet par paramètre dans le fichier final.

Pendant l’exécution, le moteur a également besoin de zones de calcul et d’un cache pour certaines représentations des tokens. La taille de ce cache dépend notamment de l’architecture, du contexte et de la précision utilisée. Charger plusieurs requêtes en parallèle peut encore changer la consommation.

Enfin, RAM et mémoire du GPU ne sont pas interchangeables. Selon le moteur et ses réglages, des données peuvent rester en RAM, être placées en mémoire vidéo ou être réparties entre les deux. Avoir 64 Go de RAM ne transforme pas une carte de 8 Go en carte de 72 Go.

Ouvrez l’outil de surveillance de votre système et relevez la mémoire du processus avant puis pendant une réponse. Notez ce que vous lisez : mémoire résidente du processus, mémoire totale utilisée ou mémoire vidéo ne désignent pas la même mesure. Sans le nom de la mesure, deux nombres risquent de ne pas être comparables.
