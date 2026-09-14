# Comprendre l’IA et développer avec elle

## 1. Une histoire de l’IA — V3 validée

1. Les origines de l’intelligence artificielle
2. Des règles pour raisonner
3. Apprendre à partir de données : les premières approches
4. Promesses, systèmes experts et hivers de l’IA
5. Le tournant du deep learning
6. Des transformers à l’IA générative
7. Où en sommes-nous aujourd’hui ?

## 2. Comprendre un modèle en le construisant — rédigé

1. Installer notre petit atelier
2. Des pixels à une première réponse
3. Faire apprendre le modèle
4. Lire les résultats sans se raconter d’histoires
5. Faire reconnaître nos propres dessins
6. Ajouter une couche… et voir ce que cela change
7. Produire du texte, un morceau à la fois
8. Du modèle aux outils qui l’entourent

Pratique : chiffres manuscrits sur CPU, dessin personnel, entraînement et évaluation, génération par bigrammes, attention et appel d’un outil. Sources et résultats dans une archive séparée.

## 3. Faire tourner un modèle chez soi — rédigé dans cette livraison

1. Choisir ce que l’on va télécharger
2. Installer le moteur et lancer le modèle
3. Envoyer une question et conserver la réponse
4. Mesurer sans mélanger les résultats
5. Décider si le résultat nous sert
6. Essayer une carte graphique, si vous en avez une

Pratique : petit modèle GGUF, serveur local, client Python, cinq cas d’évaluation, mesures reproductibles et comparaison CPU/GPU. Serveur et appels CPU réellement exécutés ; variante GPU à vérifier sur la machine de l’auteur.

## 4. Développer avec une IA, du problème au changement vérifié — rédigé dans cette livraison

1. Ouvrir un projet que l’on peut comprendre
2. Décider ce que le ticket veut changer
3. Faire apparaître le bug dans un test
4. Faire le changement et lire le diff
5. Vérifier au-delà de la dernière ligne verte
6. Garder un changement que l’on sait expliquer

Pratique : suivi de prix, ticket, tests rouges puis verts, diff, fichiers de recette et mutations. Code Python sans dépendances ; consignes utilisables avec différents agents ou parcours à la main.

## 5. Comprendre et encadrer les agents de code — à rédiger

1. Ce qui se passe entre une demande et une action
2. Organiser le contexte, les recherches et l’historique
3. Donner des consignes explicites et vérifier leur effet
4. Distinguer permissions, validations et instructions au modèle
5. Reprendre après une erreur et limiter les actions risquées
6. Mesurer les coûts et le temps réel de vérification

Pratique envisagée : boucle d’agent limitée à un petit répertoire, journal des décisions et des outils, incident reproductible, tests de refus au niveau du programme. Distinguer outil disponible, autorisation et réussite effective.

## 6. Les MCP et les skills en pratique — à rédiger

1. Ce que MCP apporte et ce qu’il ne fait pas
2. Utiliser un serveur MCP et observer les échanges
3. Construire un petit serveur MCP en lecture seule
4. Contrôler les paramètres et traiter les réponses comme des données
5. Écrire un skill adapté à une tâche réelle
6. Faire évoluer ses fichiers par essais, erreurs et refacto
7. Articuler skills, conventions et base de connaissances

Pratique envisagée : faux tickets et documentation locale, recherche via MCP, tests des outils et d’un refus d’écriture, skill de préparation de tests ou de revue. Garder le protocole, le client et les politiques d’accès distincts. Ne pas supposer que tous les produits chargent les descriptions au même moment.

## 7. Construire et adapter son IA maison — à rédiger

1. Choisir entre contexte, recherche documentaire, adaptation et entraînement
2. Construire une recherche dans ses documents
3. Évaluer la réponse et retrouver les passages utilisés
4. Construire une application autour du modèle local
5. Préparer ses données et adapter un modèle existant
6. Expérimenter les adaptateurs et leurs limites
7. Entraîner un petit modèle de langage plus élaboré
8. Comparer les besoins matériels et les résultats

Pratique envisagée : documents fictifs, application locale, corpus créé ou libre, entraînement minuscule sur CPU et variantes GPU optionnelles. Pas de promesse d’entraîner un modèle géant à la maison. Évaluer sur des exemples distincts de l’entraînement et conserver aussi les régressions.

## 8. Choisir la place de l’IA — à rédiger

1. D’où viennent les données et le travail humain ?
2. Licences, transparence et possibilités de vérification
3. Coûts, énergie, matériel et environnement
4. Dépendances techniques et économiques
5. Apprendre et exercer notre métier
6. Alternatives, logiciels libres et possibilités de s’en passer
7. Construire ses propres critères de choix

Pratique envisagée : analyser une fiche de modèle, inventorier ce que révèle un outil, comparer une tâche avec et sans IA en incluant la relecture. Les questions éthiques et l’apprentissage des juniors apparaissent dès les autres parties ; elles ne sont pas reportées ici pour être évitées ailleurs.
