# Relecture de la partie 5 — Comprendre et encadrer les agents de code

## Périmètre

Session : `2026-09-16-globale`

Commit de départ annoncé : `102e5ccf29bff571da46bcdae0a51a5b1d089f95`

Mode : répertoire partagé, sans commit

Les changements portent uniquement sur les petits Markdown déclarés dans `tutoriel/05-agents/manifest.json` et sur ce rapport. Les manifests, `LECTURE.md`, images, ateliers, scripts et archives n’ont pas été modifiés ni régénérés.

Fichiers de cours modifiés :

- `tutoriel/05-agents/introduction.md` et `tutoriel/05-agents/conclusion.md` ;
- `tutoriel/05-agents/01-boucle/appel.md`, `conclusion.md`, `installer.md` et `observer.md` ;
- `tutoriel/05-agents/02-contexte/comparer.md`, `conclusion.md`, `historique.md` et `selectionner.md` ;
- `tutoriel/05-agents/03-consignes/conclusion.md`, `preciser.md`, `ranger.md` et `verifier.md` ;
- `tutoriel/05-agents/04-permissions/conclusion.md`, `introduction.md`, `limites.md`, `piege.md` et `refuser.md` ;
- `tutoriel/05-agents/05-reprise/budget.md`, `conclusion.md`, `fiche.md` et `reprendre.md` ;
- `tutoriel/05-agents/06-couts/calculer.md`, `compter.md`, `conclusion.md`, `introduction.md` et `temps.md`.

Les six conclusions de chapitre, auparavant vides, portent maintenant le raccord vers la question suivante. Les introductions de chapitre déjà efficaces et les commandes ont été préservées.

## Améliorations majeures

- Le statut du banc est annoncé sans ambiguïté dès l’introduction : les demandes viennent des fichiers JSON, aucun modèle n’est appelé et les traces prouvent uniquement l’exécution du script.
- La progression part plus souvent de ce que le lecteur voit : clé `secondes_outil`, contenu de `resultat.contenu`, trois motifs de refus, quatrième appel absent du journal, compteurs du CSV.
- Les explications sur le contexte, le *drifting* et les consignes ont été réécrites en paragraphes continus, avec moins d’oppositions automatiques et de réserves en série.
- Les permissions sont distinguées concrètement : consigne adressée au modèle, confirmation donnée par l’interface, restriction imposée par le système. L’autorisation d’écrire un fichier ne valide pas la phrase écrite.
- Les coûts séparent désormais plus nettement appels d’outils, tours de modèle, catégories de tokens, quota d’abonnement, temps écoulé et attention humaine.
- Deux touches d’humour restent liées aux manipulations : le terminal absent qui ne surgit pas « par magie » et la quatrième lecture attendue comme une illumination.

## Avant / après représentatifs

1. **Statut du banc**
   - Avant : « Il ne contient pas de modèle. Nous pourrons donc observer un refus ou une limite d’appels… »
   - Après : « Ce banc n’appelle aucun modèle : ses traces montrent l’exécution du script, jamais le comportement d’un agent réel. »
2. **Comparaison des contextes**
   - Avant : « Ce ne serait pas un échec de l’exercice : cet exemple ne promet pas qu’ajouter du texte fait systématiquement échouer le modèle. »
   - Après : « Vous obtiendrez peut-être deux bonnes réponses. Très bien : l’exercice n’a pas été truqué pour garantir une erreur. »
3. **Permissions**
   - Avant : « Une consigne, une confirmation et une restriction du système ne jouent pas le même rôle. »
   - Après : « Une consigne guide le modèle, une confirmation vous rend la décision, une restriction du système bloque l’action. »
4. **Budget**
   - Avant : « Il ne demande pas au modèle de décider s’il a suffisamment dépensé. »
   - Après : « Le compteur et l’arrêt appartiennent au programme. […] Une boucle de refus peut donc atteindre la limite aussi vite qu’une boucle de succès. »
5. **Mesure du coût**
   - Avant : « Le nombre d’outils ne permet donc pas de déduire directement le nombre de tokens, ni le prix final. »
   - Après : « Deux appels d’outils peuvent ainsi tenir dans un seul tour du modèle ou provoquer plusieurs tours : leur nombre ne suffit pas à calculer les tokens ni le prix final. »

## Raccords et répétitions à arbitrer

- La fin actuelle de la partie 4 annonce déjà le contexte, les permissions et le coût, puis son dernier chapitre décrit encore la séparation entre demande, autorisation et résultat. L’introduction de la partie 5 reprend volontairement le projet `mon-suivi`, mais évite désormais une seconde formule « ouvrir le capot ».
- La conclusion de la partie 5 raccorde directement le banc au serveur MCP et au skill. L’introduction actuelle de la partie 6 reprend ce mouvement avec « accès précis » puis distingue serveur et procédure ; les deux textes sont cohérents. Lors de l’assemblage global, vérifier simplement que les conclusions générale et de dernier chapitre de la partie 4 ne forment pas un doublon successif.
- Le rapport de la partie 4 (`COMPTE-RENDU.md`) et la fiche de reprise de la partie 5 remplissent des rôles proches. La partie 5 conserve la différence utile : la fiche sert à redémarrer une session et commence par vérifier l’état présent des fichiers.
- La distinction « banc sans modèle / essai dans un assistant » réapparaît à plusieurs endroits. Elle est conservée dans l’introduction, l’injection et les coûts parce qu’elle change l’interprétation de chacune de ces expériences ; les formulations ont été variées et rattachées à la trace locale.

## Exactitude, sources et vérifications restantes

Les affirmations ont été comparées à `banc.py`, `mesurer.py`, aux cas JSON, aux tests, au CSV et à `VERIFICATION.md`. Aucun résultat de modèle n’a été ajouté. En particulier :

- `secondes_outil` mesure la fonction Python du banc ; aucune durée d’inférence n’est revendiquée ;
- le scénario d’injection contient lui-même la demande d’écriture ; il ne montre pas un modèle trompé par le document ;
- les valeurs `0.004200` et `0.006000` restent les résultats du calcul sur tokens et tarifs fictifs ;
- la limite de trois porte sur les demandes d’outils du banc, y compris les refus ; elle ne borne ni les tokens, ni la requête au modèle, ni le temps d’un outil bloqué ;
- aucun essai sur l’assistant du lecteur, aucune comparaison de contexte réelle et aucun coût fournisseur ne sont présentés comme exécutés.

Les quatre notes techniques existantes ont été conservées : documentation d’appels d’outils et du cache d’Anthropic, article *Lost in the Middle*, fiche OWASP sur les injections. Aucun fait dépendant d’une interface ou d’un tarif courant n’a été ajouté. La référence Vim sur ZdS a été demandée au navigateur, mais son URL était inaccessible dans cet environnement ; la réécriture s’appuie donc sur l’analyse détaillée du guide de voix, sans prétendre à une nouvelle lecture du tutoriel.

Restent à vérifier en conditions réelles, comme l’indique déjà `VERIFICATION.md` :

- l’affichage des actions et permissions dans chaque assistant retenu, avec sa version ;
- les deux réponses aux contextes `cible.txt` et `complet.txt` ;
- la consigne sur les états `01-depart` et `02-test-rouge` ;
- la reprise dans une session neuve ;
- les compteurs de tokens, quotas et coûts d’un fournisseur réel ;
- le rendu après assemblage et import dans un brouillon ZdS.

## Contrôles effectués

- lecture intégrale du guide de voix, de la mission, du sommaire, de l’état des contenus, du manifest et de toutes les sources canoniques de la partie 5 ;
- lecture de `README.md`, `CREDITS.md`, `VERIFICATION.md`, de l’atelier pertinent et de ses scripts, données et tests ;
- lecture de la fin actuelle de la partie 4 et du début actuel de la partie 6 ;
- inspection visuelle des trois schémas, cohérents avec leurs textes alternatifs, légendes et parcours ;
- relecture complète des petits Markdown dans l’ordre du manifest ;
- recherche des motifs répétitifs demandés et contrôle des notes, noms de fichiers, commandes, chiffres et pronoms ;
- `git diff --check` sur l’ensemble du répertoire partagé, puis contrôle des espaces de fin de ligne dans ce rapport encore non suivi : réussis.

Les tests techniques n’ont pas été relancés : aucun code ni contrat de commande n’a changé, et la mission interdit de régénérer les artefacts communs. Aucun point bloquant n’empêche l’intégration éditoriale.
