# Relecture globale — partie 7

Session : `2026-09-16-globale`  
Commit de départ : `102e5ccf29bff571da46bcdae0a51a5b1d089f95`  
Mode : répertoire partagé, sans commit ni régénération

## Périmètre relu

Lecture intégrale du guide de voix, de la mission, du sommaire, de l’état des contenus, du manifest de la partie 7, de ses quarante-deux sources canoniques, de ses crédits, de son rapport de vérification et du README de l’atelier. Les résultats documentaires, rapports d’entraînement et consignes de l’expérience GPU ont été confrontés aux affirmations du cours. La fin de la partie 6 et le début de la partie 8 ont été lus en voisinage.

Les quatre illustrations ont été ouvertes. Les schémas correspondent au parcours et le graphique reprend bien les six pertes enregistrées. La page du tutoriel Vim n’a pas pu être chargée depuis cet environnement ; la relecture s’est donc appuyée sur l’analyse détaillée fournie dans `GUIDE-VOIX-HUGO.md`, sans prétendre à une nouvelle consultation du site.

## Fichiers modifiés

Trente-neuf petits Markdown déclarés par le manifest :

- `introduction.md`, `conclusion.md` ;
- `01-choisir/{introduction,besoin,separer}.md` ;
- `02-rechercher/{introduction,score,limites,conclusion}.md` ;
- `03-evaluer/{introduction,lots,absence,citations,conclusion}.md` ;
- `04-application/{introduction,contexte,programme,reponses,conclusion}.md` ;
- `05-donnees/{introduction,corpus,lots,base,conclusion}.md` ;
- `06-adaptateurs/{introduction,principe,entrainer,resultats,conclusion}.md` ;
- `07-entrainer/{introduction,reseau,boucle,generation,conclusion}.md` ;
- `08-comparer/{introduction,materiel,gpu,choix,conclusion}.md`.

Les trois sources déjà naturelles (`01-choisir/installer.md`, `01-choisir/conclusion.md` et `02-rechercher/paragraphes.md`) ont été laissées intactes. Le manifest, les lectures générées, les images, l’atelier, les scripts et les ZIP n’ont pas été modifiés.

## Changements principaux

- La progression s’appuie désormais plus souvent sur un objet observable : formulation manquée, passage envoyé, nombre inventé, pertes mesurées et génération incohérente.
- La coupure entre SmolLM2 et le petit réseau de caractères est annoncée dès l’entrée du chapitre 5. Le lecteur ne risque plus de prendre l’adaptation NumPy pour la suite de l’essai documentaire.
- Les résultats CPU sont nommés précisément : recherche, trois appels documentaires et trois entraînements. Le protocole RTX 3090 Ti est explicitement présenté comme non exécuté, sur un système encore inconnu.
- Les transitions des chapitres 4 à 8 partent des limites de l’étape précédente, au lieu de résumer mécaniquement le plan.
- Les anciennes tâches et les sorties ratées restent visibles : régression LoRA de `0,48` à `8,77`, dix minutes inventées et génération qui se détériore.
- Les listes et tableaux utiles ont été conservés ; la réécriture n’a pas transformé la partie en nouvelle succession de fiches.

## Avant / après représentatifs

1. Recherche documentaire :
   - Avant : « Une base vectorielle n’est pas un passage obligé pour retrouver dix paragraphes. »
   - Après : « Avec dix paragraphes, nous pouvons commencer par une recherche que nous savons lire de bout en bout. Nous verrons son premier échec avant d’envisager une base vectorielle. »

2. Réponse inventée :
   - Avant : « Le passage transmis dit pourtant qu’aucune durée n’est validée. »
   - Après : « Ouvrez `reponse-delai.json` : `temporisation#2` figure bien dans les passages et dit qu’aucune durée chiffrée n’est validée. La recherche a fait son travail ; les dix minutes viennent du modèle. »

3. Changement d’expérience :
   - Avant : « Entraîner un grand modèle n’est pas nécessaire pour voir comment un réseau apprend. »
   - Après : « Les réponses précédentes venaient du modèle local de la partie 3. Pour observer un entraînement sans carte graphique, nous passons maintenant à un autre réseau, beaucoup plus petit. »

4. Régression mesurée :
   - Avant : « Notre adaptateur améliore donc la prédiction du nouveau format, mais dégrade fortement celle des anciennes phrases. »
   - Après : « Sur les lignes `INFO`, la perte passe de 6,08 à 0,95 avec LoRA. Sur les anciennes phrases, elle bondit de 0,48 à 8,77. »

5. Expérience GPU :
   - Avant : « Avant de choisir une recette d’entraînement, il faudra vérifier son système, ses pilotes et la mémoire réellement disponible. »
   - Après : « Nous n’avons pas encore identifié son système ni exécuté l’adaptation. Avant de choisir une recette d’entraînement, il faudra vérifier le système, les pilotes et la mémoire réellement disponible. »

## Exactitude et points restant à vérifier

Aucune nouvelle expérience ni nouvelle mesure n’a été ajoutée. Les chiffres repris viennent des JSON de référence et concordent avec `VERIFICATION.md`. Les erreurs grammaticales des réponses du modèle sont conservées mot pour mot dans les citations. Les blocs de code et les commandes sont inchangés.

Restent réellement à vérifier :

- l’adaptation d’un LLM sur la RTX 3090 Ti, après identification du système, des pilotes et de la mémoire disponible ;
- Windows et macOS ;
- l’import interactif dans ZdS ;
- tout résultat qui découlerait d’un autre modèle documentaire ou d’une autre méthode de recherche.

Le tutoriel Vim était inaccessible depuis cet environnement. Aucune affirmation n’a été ajoutée à son sujet.

## Coordination avec les parties voisines

La fin de la partie 6 mène naturellement vers la question « où l’information doit-elle vivre ? », reprise au chapitre 1. La conclusion de la partie 7 ouvre désormais explicitement sur les données, les dépendances et les conséquences, ce qui rejoint l’introduction actuelle de la partie 8 sans exiger de changement voisin.

Une amélioration d’image est à arbitrer par le coordinateur : `images/recherche.png` contient encore la formule « Une source pertinente ne garantit pas une réponse juste », précisément le motif rhétorique que la passe réduit dans le texte. Comme les images étaient hors périmètre, elle n’a pas été régénérée. Proposition de libellé : « Le modèle peut encore contredire les passages retenus. »

## Contrôles effectués

- relecture des sources dans l’ordre du manifest ;
- confrontation des affirmations aux trois journaux documentaires et aux rapports `base`, `lora` et `complet` ;
- inspection visuelle des quatre images ;
- recherche des motifs répétitifs demandés dans la mission ;
- comparaison des blocs de code avec le commit de départ : aucun changement ;
- `git diff --check -- tutoriel/07-ia-maison` : succès.
