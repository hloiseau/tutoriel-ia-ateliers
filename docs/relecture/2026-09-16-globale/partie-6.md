# Relecture globale — partie 6, MCP et skills

Session : `2026-09-16-globale`  
Commit de départ : `102e5ccf29bff571da46bcdae0a51a5b1d089f95`

## Périmètre relu

J’ai lu le guide de voix, la mission, le sommaire, l’état des contenus, le manifest et les 41 sources canoniques déclarées pour la partie 6. J’ai également consulté les crédits, le rapport de vérification, le README de l’atelier, les traces de vérification initiales, la passe adverse de construction du MCP et les instructions d’expérience locale. Pour les raccords, j’ai lu le dernier chapitre et la conclusion de la partie 5, puis l’introduction et le premier chapitre de la partie 7.

Le tutoriel Vim de Zeste de Savoir était inaccessible depuis l’outil de consultation (URL refusée puis domaine bloqué par `robots.txt`). La relecture applique donc l’analyse pédagogique détaillée déjà consignée dans `GUIDE-VOIX-HUGO.md`, sans prétendre à une nouvelle lecture du site.

## Fichiers modifiés

- Racine de la partie : `introduction.md`, `conclusion.md`.
- Chapitre 1 : `introduction.md`, `ticket.md`, `depanner.md`, `conclusion.md`.
- Chapitre 2 : `decouvrir.md`, `configurer.md`, `trajet.md`, `conclusion.md`.
- Chapitre 3 : `introduction.md`, `catalogue.md`, `chercher.md`, `valider.md`, `ressource.md`, `tester.md`, `conclusion.md`.
- Chapitre 4 : `introduction.md`, `parametres.md`, `ecriture.md`, `document.md`, `conclusion.md`.
- Chapitre 5 : `introduction.md`, `dossier.md`, `procedure.md`, `essayer.md`.
- Chapitre 6 : `introduction.md`, `incomplet.md`, `corriger.md`, `comparer.md`.
- Chapitre 7 : `introduction.md`, `repartir.md`, `refacto.md`, `suite.md`.
- Le présent rapport.

Les autres petits Markdown de la partie ont été relus et laissés inchangés lorsque leur progression était déjà naturelle. Aucun `LECTURE.md`, manifest, atelier, script, image ou ZIP n’a été modifié.

## Améliorations principales

La passe préserve la progression validée : premier appel, découverte, configuration, construction depuis un fichier vide, validation, ressource, tests, contrôles d’accès, skill, adaptation, puis rangement. Les commandes et blocs de code sont inchangés.

Les réserves abstraites ont été rattachées à ce que le lecteur vient d’observer : champ `isError`, inventaire des outils, transport stdio, annotation `readOnlyHint`, ticket PRIX-2 ou document piégé. Les transitions partent maintenant plus souvent du résultat précédent. Plusieurs distinctions répétées sous la forme « pas X mais Y » ont été reformulées sans perdre leur rôle technique.

Exemples représentatifs :

1. Avant : « Nous avons obtenu une donnée par MCP. Regardons maintenant… »  
   Après : « PRIX-1 est arrivé jusqu’à notre journal. Regardons maintenant comment le client a découvert l’outil… »
2. Avant : « Cela ne garantit ni que tous les assistants utilisent toutes les possibilités de MCP, ni qu’ils montrent les mêmes boutons. »  
   Après : « Chaque assistant choisit ensuite les possibilités qu’il prend en charge et la manière de les présenter dans son interface. »
3. Avant : « Il ne protège pas ces fichiers contre un autre programme lancé avec les droits de notre compte. »  
   Après : « Un assistant qui possède aussi un terminal dispose toutefois d’une autre voie vers les fichiers, avec les droits de notre compte. »
4. Avant : « Ce n’est pas au modèle de décider discrètement du comportement du produit pour que son tableau soit plus joli. »  
   Après : « Un trou visible se discute avec l’équipe ; une règle inventée au fond d’une cellule risque de devenir le comportement du produit par accident. »
5. Avant : « Notre recherche littérale atteint vite ses limites quand on ne connaît pas les mots employés dans les sources. »  
   Après : « La recherche littérale échoue déjà sur `alerte` parce que la source parle de `notification`… »

L’analogie de la recette donnée par l’ami de Hugo reste au chapitre 6. La distinction entre préparer une recette et exécuter les scénarios est rendue plus concrète, sans transformer une réponse attendue en essai réellement observé.

## Exactitude et statut des essais

Aucun fait technique, chiffre, résultat d’agent ou résultat d’expérience n’a été ajouté. La relecture conserve explicitement les limites suivantes :

- le serveur construit a été vérifié par des tests en mémoire et des appels stdio ;
- ces appels n’utilisent aucun modèle ;
- l’intégration interactive dans VS Code et les autres assistants reste à vérifier ;
- la découverte automatique du skill et son comportement avec un modèle restent à essayer ;
- demander directement la lecture de `SKILL.md` permet d’essayer la procédure, mais ne vérifie pas la découverte automatique ;
- le petit modèle local de la partie 3 n’est pas présenté comme un agent de code utilisable sur CPU ;
- une recette préparée ne constitue pas une recette exécutée.

Les liens techniques et versions proviennent des sources déjà vérifiées de la partie. Comme la passe n’a changé ni API, ni commande, ni affirmation dépendant d’une interface récente, aucune nouvelle validation externe n’a été substituée aux essais manquants.

## Raccords et répétitions entre parties

- Partie 5 vers partie 6 : le raccord reste cohérent. La partie 5 termine sur « que donne-t-on à lire, que permet-on de faire ? » ; la partie 6 répond avec le serveur MCP, ses droits et le document piégé. Aucun changement voisin n’est nécessaire.
- Partie 6 vers partie 7 : la dernière section cite maintenant l’échec concret de la recherche de `alerte` lorsque la source emploie `notification`. La partie 7 peut ainsi ouvrir sur un corpus plus grand et une recherche documentaire plus utile. Son introduction reprend déjà la distinction entre sources, procédure et poids du modèle.
- Les rappels sur le périmètre des permissions restent volontairement présents aux chapitres 3 et 4 : le premier explique l’annotation, le second montre les voies d’accès. Ils ne jouent pas le même rôle.

## Contrôles

- relecture dans l’ordre du manifest, y compris les sections laissées inchangées ;
- recherche des motifs répétitifs demandés dans la mission ;
- vérification du maintien des noms `mon_serveur.py`, `serveur.py`, `client.py`, PRIX-1 et PRIX-2 dans les passages modifiés ;
- vérification qu’aucune commande ni aucun bloc de code n’a changé ;
- vérification des sources déclarées par le manifest et des références d’images ;
- contrôle automatisé de l’existence des 41 sources déclarées par le manifest : réussi ;
- comparaison des blocs de code avec le commit de départ : aucun bloc modifié ;
- contrôle de l’existence des trois images référencées : réussi ;
- `git diff --check` : réussi.

## Points restant réellement à vérifier

La relecture éditoriale ne lève aucun des essais interactifs déjà recensés : VS Code, autres assistants, découverte du skill, réponses du modèle, Windows, macOS et import dans ZdS. Si un essai réel fait apparaître une invention ou un défaut de chargement, le chapitre 6 fournit maintenant la méthode pour conserver la trace, corriger la règle utile et rejouer PRIX-1 comme test de régression.
