# Relecture de la partie 3 — Faire tourner un modèle chez soi

Session : `2026-09-16-globale`  
Commit de départ : `102e5ccf29bff571da46bcdae0a51a5b1d089f95`  
Mode : répertoire partagé, sans commit du sous-agent

## Périmètre

Vingt-cinq sources Markdown déclarées dans `tutoriel/03-modele-local/manifest.json` ont été modifiées :

- `introduction.md` et `conclusion.md` ;
- `01-choisir/introduction.md`, `trois-pieces.md`, `fiche.md` et `machine.md` ;
- `02-installer/moteur.md`, `poids.md`, `demarrer.md` et `depanner.md` ;
- `03-dialoguer/premier-appel.md`, `requete.md`, `document.md` et `contexte.md` ;
- `04-mesurer/memoire.md`, `chronometre.md`, `lire.md` et `modifier.md` ;
- `05-juger/introduction.md`, `petite-grille.md`, `choisir-usage.md` et `local.md` ;
- `06-gpu/preparer.md`, `comparer.md` et `garder.md`.

Aucun manifest, `LECTURE.md`, atelier, résultat de référence, image, script ou ZIP n’a été modifié.

## Travail éditorial

- L’introduction présente immédiatement les trois objets que le lecteur manipulera : poids, moteur et client. Le parcours CPU reste le point de départ ; le GPU devient une comparaison à mesurer, sans gain promis avant l’expérience.
- Les étapes d’installation partent davantage du résultat visible : version du moteur, état de santé, premier message d’erreur utile et contenu de `modele.json`.
- La manipulation sur l’historique nomme désormais le fichier à créer, donne la commande à lancer et demande d’ouvrir la requête enregistrée. Même si le modèle improvise une « question précédente », le lecteur peut constater qu’aucun ancien message ne lui a été envoyé.
- Les oppositions rhétoriques répétées ont été remplacées par les conséquences observables : fichier Q8_0 plus gros que le calcul rond, mesure globale distincte du débit de décodage, droits administrateur inutiles face à un chemin erroné, etc.
- Le chapitre d’évaluation conserve sa table, mais l’introduit à partir de trois vérifications concrètes : réponse reçue, forme respectée et contenu juste. Les cinq résultats de référence restent rapportés sans les embellir.
- La conclusion distingue explicitement la réussite de courtes requêtes CPU de la qualité et du délai d’une session complète d’agent de code. Le parcours principal de la partie 4 reste hébergé ; l’expérience locale reste facultative et à évaluer séparément.

## Avant / après représentatifs

1. Avant : « Pas besoin d’une carte graphique pour commencer. »  
   Après : « Nous commencerons sur CPU, avec un petit modèle et des réponses courtes. Si vous avez une carte graphique, vous pourrez ensuite reprendre la même expérience et mesurer ce qu’elle change. »

2. Avant : « Ce choix […] ne signifie pas que ce petit modèle est un bon agent de développement. »  
   Après : « Nos cinq courtes questions ne permettront pas de juger s’il sait lire un projet, utiliser des outils et tenir une session entière. »

3. Avant : « Modifiez maintenant une question […] Lancez-la dans un nouveau fichier de messages. »  
   Après : le texte nomme `questions/historique-absent.json`, fournit la commande complète, puis fait vérifier la partie `requete` du résultat.

4. Avant : « Ce n’est pas le débit du seul décodage. »  
   Après : « La colonne s’appelle `tokens_sortie_par_seconde_globale` parce qu’elle couvre l’appel complet. Certains journaux affichent à la place le débit du seul décodage ; comparez des colonnes qui portent bien sur la même étape. »

5. Avant : « Ce premier modèle ne devient pas un agent de code utilisable simplement parce qu’on lui ajoute une interface. »  
   Après : « Nos essais prouvent que ce petit modèle répond à de courtes requêtes sur CPU. Ils ne mesurent ni la qualité ni les délais d’une session complète d’agent de code. »

## Faits, preuves et limites préservés

- Les commandes, la version b10809 de llama.cpp, le contexte de 2 048 tokens, les deux fils CPU, `--device none`, `-ngl 0`, les limites de 96 tokens et les valeurs de référence n’ont pas été changés.
- La taille reste formulée « environ 386 Mo » ; la taille exacte et l’empreinte restent dans `modele.json`.
- Les résultats annoncés correspondent aux réponses brutes présentes sous `ateliers/03-modele-local/resultats-reference/` : mardi à 10 heures, absence du dimanche reconnue, JSON valide, réponse anglaise en une phrase et réponse française interrompue à 96 tokens.
- La référence CPU existante concerne Linux x86-64, Python 3.12.14, llama.cpp b10809 et un backend CPU générique chargé explicitement. Aucun relevé de RAM ni résultat GPU n’a été ajouté.
- Les quatre illustrations ont été inspectées. Leurs flèches, valeurs, légendes et textes alternatifs concordent avec les sections ; aucune modification d’image n’est demandée.
- La page du tutoriel Vim n’a pas pu être consultée directement dans cet environnement (accès refusé puis blocage par `robots.txt`). La réécriture suit donc l’analyse détaillée et les exemples du guide de voix, sans prétendre à une nouvelle lecture du site.

## Raccords et décisions entre parties

- La fin de la partie 2 présente déjà les poids, le contexte et les logiciels entourant le modèle. L’ouverture de la partie 3 reprend seulement le chargement des poids, puis passe immédiatement à l’échelle du modèle local ; aucun changement voisin n’est nécessaire.
- Le début de la partie 4 affirme correctement qu’un petit modèle répondant sur CPU ne suffit pas à établir l’efficacité d’un agent de code. La nouvelle conclusion de la partie 3 emploie la même distinction à partir des cinq requêtes réellement évaluées. Il faut préserver ce raccord lors de l’harmonisation globale.
- La partie 4 mentionne encore « l’accès gratuit [qui] dépend de votre compte et de son quota » et un comparatif daté de septembre 2026. Ces informations changeantes relèvent de la relecture de la partie 4 ou des annexes, pas de cette partie.

## Contrôles effectués

- lecture intégrale des documents demandés, des sources du manifest, des crédits, du rapport initial, de l’atelier, des résultats de référence et des raccords avec les parties 2 et 4 ;
- comparaison des affirmations du cours avec `modele.json` et les cinq réponses de référence ;
- inspection des quatre PNG ;
- contrôle automatique : les 25 fichiers de cours modifiés sont tous déclarés par le manifest et aucune source déclarée ne manque ;
- `python -m unittest test_client.py` : 6 tests réussis ;
- recherche des motifs répétitifs demandés, puis relecture contextuelle des occurrences conservées ;
- `git diff --check` : aucune erreur.

## Vérifications restantes

- Rejouer l’installation sur le système de Hugo, qui reste à identifier.
- Refaire les cinq questions et les mesures CPU sur cette machine, puis vérifier le fonctionnement hors ligne dans ces conditions.
- Exécuter la comparaison GPU sur la RTX 3090 Ti et relever méthode, journaux, durée et VRAM ; aucun résultat GPU n’est revendiqué dans le cours.
- Vérifier Windows, macOS et le rendu après import interactif dans ZdS.
- Évaluer séparément l’expérience locale de l’annexe avec une interface de développement. Cette expérience ne devra pas devenir une promesse d’agent de code utilisable sur CPU.
