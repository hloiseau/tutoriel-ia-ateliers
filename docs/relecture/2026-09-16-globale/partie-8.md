# Relecture de la partie 8 — Choisir la place de l’IA

Session : `2026-09-16-globale`  
Commit de départ : `102e5ccf29bff571da46bcdae0a51a5b1d089f95`  
Mode : répertoire partagé, sans commit ni régénération

## Périmètre

Trente-six sources canoniques déclarées dans `tutoriel/08-choisir/manifest.json` ont été modifiées :

- la racine : `introduction.md` et `conclusion.md` ;
- chapitre 1 : `remonter.md`, `personnes.md`, `selection.md` et `conclusion.md` ;
- chapitre 2 : `introduction.md`, `objets.md`, `libertes.md`, `fiche.md` et `conclusion.md` ;
- chapitre 3 : `introduction.md`, `perimetre.md`, `calcul.md`, `usage.md` et `conclusion.md` ;
- chapitre 4 : `introduction.md`, `trajet.md`, `sortie.md`, `collectif.md` et `conclusion.md` ;
- chapitre 5 : `introduction.md`, `comprendre.md`, `exercice.md`, `metier.md` et `conclusion.md` ;
- chapitre 6 : `introduction.md`, `solutions.md`, `comparer.md`, `etudes.md` et `conclusion.md` ;
- chapitre 7 : `introduction.md`, `contraintes.md`, `decision.md`, `continuer.md` et `conclusion.md` ;
- le présent rapport.

Les autres petits Markdown ont été relus et conservés. Aucun manifest, `LECTURE.md`, atelier, résultat de référence, image, script, index ou ZIP n’a été modifié. Aucun commit plus récent que le commit de départ ne concernait ce périmètre au début de la passe.

## Améliorations principales

- Les conclusions de chapitre partent désormais d’un objet obtenu pendant le parcours — fiche de provenance, calcul à 100 Wh, carte des trajets, exercice repris le lendemain, bilan complet — au lieu d’enchaîner « nous avons vu » et « passons maintenant ».
- Les distinctions nécessaires restent explicites, mais les séries de « ce n’est pas X » ont été remplacées par leur conséquence concrète. La licence du moteur, celle du modèle et les conditions de l’interface sont ainsi rattachées aux fichiers qu’elles couvrent ; les Wh restent rattachés au périmètre mesuré.
- Le travail humain ne disparaît plus derrière une formule générale : le témoignage conserve sa portée exacte, les inconnues restent visibles, et la position de Hugo sur l’accord des créateurs et le partage de la valeur demeure assumée.
- La dépendance technique est suivie comme un trajet. Le texte précise ce que répond l’option « non utilisé pour l’entraînement », puis renvoie la conservation, l’accès de tiers et la localisation aux engagements de l’offre concernée.
- Le chapitre sur l’apprentissage parle aussi aux développeurs expérimentés et place l’exercice après fermeture de l’outil. La possibilité de se passer de l’IA reste présente dans les solutions comme dans la conclusion.
- La conclusion du chapitre 7 est devenue un raccord procédural. La conclusion de partie porte seule la fermeture du tutoriel, avec un rappel des huit parties, l’opinion de Hugo et trois issues possibles : garder, adapter ou abandonner l’outil.

## Avant / après représentatifs

1. Avant : « Cela ne veut pas dire que tout calcul est inutile. »  
   Après : « Un périmètre étroit, correctement annoncé, reste utile pour comparer deux essais. Sa légende doit simplement rester avec le résultat. »

2. Avant : « “Non utilisé pour l’entraînement” ne signifie pas forcément “jamais conservé”. »  
   Après : « Une option “non utilisé pour l’entraînement” répond à une question précise. Pour connaître la durée de conservation des journaux, l’accès de tiers et la localisation du traitement, il reste à lire les engagements applicables. »

3. Avant : « Ce n’est pas un examen à envoyer à quelqu’un. »  
   Après : « Personne ne ramassera la copie. 🙂 Observez plutôt ce que vous savez encore expliquer et modifier après avoir fermé l’outil. »

4. Avant : « Le bilan ne choisit pas à notre place. Il rend simplement visibles des éléments que la vitesse d’apparition du code pouvait cacher. »  
   Après : « Le bilan fait apparaître la préparation, les corrections, l’attente et l’état du résultat derrière la vitesse d’apparition du code. »

5. Avant : « Nous n’avons pas à réorganiser notre métier autour d’un agent simplement parce qu’il sait générer beaucoup de code. »  
   Après : « Générer beaucoup de code ne suffit pas à justifier que nous réorganisions le métier autour d’un agent. Si l’outil nous éloigne de ce que nous livrons au point de ne plus pouvoir l’expliquer, il a raté sa place. »

## Raccords et décisions entre parties

- La fin actuelle de la partie 7 annonce les données, les personnes, la dépendance et les ressources. L’introduction de la partie 8 reprend ces critères en ajoutant les licences et l’apprentissage. Le raccord est cohérent ; lors de l’harmonisation globale, éviter d’allonger encore ces deux énumérations.
- `07-decider/continuer.md` rappelle déjà la boîte ouverte, le droit d’expérimenter et celui de fermer l’assistant. La conclusion générale reprend l’ensemble du parcours et formule le dernier choix. Le coordinateur devra préserver la brièveté de `07-decider/conclusion.md` pour ne pas recréer une seconde morale.
- La conclusion mentionne l’assistant documentaire de la partie 7, sans présenter l’expérience GPU préparée comme exécutée. Aucun résultat sur la RTX 3090 Ti n’est ajouté.
- Le souhait de futurs chapitres sur les usages hors développement mérite un travail de structure séparé. La présente partie fournit déjà des critères réutilisables — provenance, trajets, sortie, coût complet et décision — mais son cas fil rouge reste une équipe logicielle. Il serait préférable de ne pas greffer à sa conclusion un catalogue de produits ou de pipelines qui daterait vite.

## Faits, sources et limites

Aucun chiffre, résultat d’expérience, témoignage ou comportement d’interface n’a été ajouté. Les nombres fictifs restent explicitement signalés : 200 W pendant 30 minutes donnent 100 Wh ; le bilan fictif donne 23 et 28 minutes. Les affirmations sur Anthropic, l’OIT, METR, l’ADEME, l’OSI, la CNIL et le témoignage d’Oskarina Veronica Fuentes Anaya conservent leurs notes et leur portée initiales.

La page du tutoriel Vim a été demandée à l’outil de consultation, qui a refusé l’URL dans cet environnement. La réécriture s’appuie donc sur l’analyse détaillée et les exemples conservés dans `GUIDE-VOIX-HUGO.md`, sans prétendre à une nouvelle lecture du site.

Restent réellement à vérifier :

- une comparaison menée par l’auteur avec et sans assistance, en conservant les résultats incomplets ;
- toute mesure électrique sur sa machine, avec le périmètre de l’instrument ;
- l’effet pédagogique auprès de lecteurs ;
- Windows, macOS et l’import interactif dans ZdS.

## Contrôles effectués

- lecture intégrale du guide de voix, de la mission, du sommaire, de l’état des contenus, du manifest, de toutes les sources canoniques, des crédits, du README, de `VERIFICATION.md`, de `sources.json`, du README de l’atelier, de la fin de la partie 7 et de la conclusion générale vide ;
- lecture de la passe adverse existante et vérification des fichiers d’atelier cités dans le cours ;
- relecture continue des sources dans l’ordre du manifest ;
- recherche contextuelle des motifs « ce n’est pas », « ne signifie pas », « nous allons », « passons maintenant », « voyons maintenant », « il est important » et « en résumé » ;
- contrôle de la présence des quatre images référencées et des douze définitions de notes ;
- contrôle du périmètre des 36 fichiers modifiés ;
- `git diff --check` sur la partie : réussi.

Les tests techniques n’ont pas été relancés : aucune commande, aucun script, aucun contrat d’exercice et aucun résultat attendu n’a changé. Les générateurs communs n’ont pas été exécutés, conformément à la mission.
