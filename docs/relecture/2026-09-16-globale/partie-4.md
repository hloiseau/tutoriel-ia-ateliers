# Relecture de la partie 4 — Développer avec une IA

Session : `2026-09-16-globale`  
Commit de départ : `102e5ccf29bff571da46bcdae0a51a5b1d089f95`

## Périmètre lu

Lecture intégrale du guide de voix, de la mission, du sommaire, de l’état des contenus, du manifest de la partie 4 et de ses 39 petits Markdown canoniques. J’ai également lu `README.md`, `CREDITS.md`, `VERIFICATION.md`, le README et les états de l’atelier, les deux rapports d’exécution de la partie 4, le prompt local pertinent, la fin de la partie 3 et le début de la partie 5.

La référence Vim n’a pas été consultée directement pendant cette passe. Je me suis appuyé sur l’analyse détaillée conservée dans `GUIDE-VOIX-HUGO.md` et sur la relecture pédagogique du 15 septembre.

## Fichiers modifiés

Trente et un petits Markdown déclarés par `tutoriel/04-developpement/manifest.json` :

- `introduction.md` et `conclusion.md` ;
- `outils/introduction.md`, `outils/trois-morceaux.md`, `outils/usages.md`, `outils/choisir.md` ;
- `installer/projet.md`, `installer/heberge.md`, `installer/observer.md`, `installer/lire.md` ;
- `02-demande/introduction.md`, `02-demande/regle.md`, `02-demande/cas.md`, `02-demande/limites.md` ;
- `03-tests/agent.md`, `03-tests/rouge.md`, `03-tests/completer.md` ;
- `04-corriger/introduction.md`, `04-corriger/demander.md`, `04-corriger/condition.md`, `04-corriger/diff.md` ;
- `05-verifier/introduction.md`, `05-verifier/suite.md`, `05-verifier/recette.md`, `05-verifier/casser.md`, `05-verifier/revue.md` ;
- `06-garder-la-main/introduction.md`, `06-garder-la-main/rapport.md`, `06-garder-la-main/apprendre.md`, `06-garder-la-main/choisir.md`, `06-garder-la-main/conclusion.md`.

Le présent rapport est le seul autre fichier créé. Aucun manifest, `LECTURE.md`, atelier, script, index, image ou ZIP n’a été modifié. Aucun commit n’a été créé.

## Améliorations principales

- Le fil est désormais annoncé et repris avec les mêmes objets : `mon-suivi`, le scénario fautif, le premier test rouge, les deux échecs de référence, le diff, les scénarios JSON et le compte rendu.
- Les explications partent davantage d’une sortie ou d’un fichier observé. Les formulations générales sur le contrôle, les limites et les tests ont été ramenées au cas du ticket PRIX-1.
- Les interfaces Copilot sont explicitement présentées comme un parcours documenté dont les libellés peuvent évoluer. Aucun essai d’interface ou résultat d’agent n’est ajouté.
- La place des alternatives reste claire : le parcours concret utilise VS Code et Copilot, le comparatif détaillé reste en annexe, l’exercice peut se suivre sans IA et l’essai local ne devient pas une promesse d’agent utilisable sur CPU.
- La transition vers la partie 5 nomme maintenant les trois éléments que celle-ci va séparer : demande d’outil, autorisation du logiciel et résultat renvoyé au modèle.

## Avant / après représentatifs

1. Avant : « La correction sera petite, ce qui nous laissera le temps de comprendre ce que l’agent fait autour. »  
   Après : « La correction tient presque sur un timbre-poste ; tout ce qui permet de lui faire confiance prend un peu plus de place. » Le paragraphe enchaîne ensuite sur les fichiers, commandes et diff réellement suivis.

2. Avant : « Il n’est pas question de retrouver le prix le plus bas des six derniers mois ni de calculer une promotion. »  
   Après : « L’historique des six derniers mois et le calcul d’une promotion restent hors du programme. » La limite est formulée directement, sans corriger par avance une interprétation du lecteur.

3. Avant : « Une longue suite de tests qui attend la mauvaise réponse reste une longue suite de tests qui attend la mauvaise réponse. »  
   Après : « Dix tests persuadés qu’une hausse mérite une alerte ne rendraient pas cette idée plus juste. 😅 » L’humour repose sur le cas métier et mène à la relecture des valeurs attendues.

4. Avant : « Nous n’avons pas cassé le projet en ajoutant un test : nous avons rendu visible le désaccord avec la nouvelle règle. »  
   Après : « Cet échec est le résultat recherché : il relie le ticket au comportement fautif avant que nous changions le code. » L’échec sert immédiatement la progression rouge → correction.

5. Avant : « Changer de session ou de modèle n’en fait pas une preuve indépendante au sens fort. »  
   Après : « Une nouvelle session, même avec un autre modèle, peut retrouver les mêmes habitudes et les mêmes angles morts. Les scénarios, le code et les sorties observées restent nos pièces les plus solides. »

## Correction technique issue de la relecture

L’étape de mutation disait de remplacer `<` par `<=` dans `suivi.py`. Ce fichier contient aussi `prix_centimes < 0` dans la validation. Le rapport `docs/relecture-partie4-execution.json` montre qu’une substitution trop large a rendu le prix zéro invalide et ajouté une erreur sans rapport avec la mutation visée.

La consigne cible maintenant uniquement la comparaison de `notifier` :

```python
nouveau.prix_centimes < ancien.prix_centimes
```

devient :

```python
nouveau.prix_centimes <= ancien.prix_centimes
```

Les exécutions de référence initiales conservent déjà le résultat attendu de cette mutation ciblée : deux tests à prix identique échouent. Aucun code d’atelier ni résultat de référence n’a été changé.

## Répétitions et raccords à traiter au niveau global

- Le raccord courant avec la partie 3 est aligné : modèle hébergé pour le parcours principal, expérience locale facultative et aucune promesse d’agent de code sur CPU. La partie 4 reprend ensuite le programme, le ticket et les tests annoncés.
- La fin de `06-garder-la-main/conclusion.md` et la conclusion de partie jouent toutes deux le raccord vers les outils, permissions et contexte. Les formulations ont été différenciées, mais le coordinateur peut encore décider si la conclusion de partie doit rester aussi brève.
- Le début courant de la partie 5 reprend bien le diff et les vérifications, puis distingue l’assistant du banc déterministe. Plus loin, le lecteur rouvrira `mon-suivi` pour observer son assistant ; le raccord de la partie 4 n’annonce donc pas un changement de projet exclusif.

## Faits et vérifications

- Aucun nouveau prix, quota, comportement d’interface, résultat de modèle ou résultat d’agent n’a été ajouté.
- Les nombres conservés correspondent aux résultats enregistrés : 3 tests au départ ; 13 tests dont 2 échecs avant correction ; 13 réussites après correction ; scénarios `false`, `true`, `false`.
- Les affirmations sur VS Code/Copilot restent rattachées aux deux sources Microsoft déjà citées et au relevé documentaire du 14 septembre 2026. L’installation et les libellés visibles restent à vérifier sur la machine de l’auteur.
- L’expérience Continue et le parcours d’agent avec un modèle réel restent non exécutés. Le texte ne les présente pas comme réussis.
- Les expériences locales préparées pour la RTX 3090 Ti ne sont pas utilisées dans cette partie et restent à exécuter.

## Contrôles réalisés

- Relecture continue des sources dans l’ordre du manifest, avec contrôle du dossier courant, des noms de fichiers, des nombres de tests et des raccords.
- Recherche des motifs répétitifs « ce n’est pas », « il est important », « nous allons voir », « en résumé » dans les sources canoniques de la partie.
- Contrôle du périmètre des fichiers modifiés.
- `git diff --check` : réussi après le dernier contrôle.

## Restant réellement à vérifier

- Parcours VS Code/Copilot sur une interface réelle : connexion, libellés **Local**, **Ask** et **Agent**, affichage des actions et comparaison avec le presse-papiers.
- Réponses et actions d’un agent réel aux prompts de l’atelier, en conservant ses écarts et les interventions humaines.
- Rendu des tableaux, notes, blocs de code et figures après régénération, puis import interactif dans un brouillon ZdS.
- Expérience locale facultative avec Continue, sans en déduire la faisabilité d’une session d’agent sur CPU.
