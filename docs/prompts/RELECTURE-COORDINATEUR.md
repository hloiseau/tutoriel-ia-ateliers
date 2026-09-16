# Prompt — coordonner la réécriture complète

Copier le texte à partir de « Tu coordonnes » dans une nouvelle conversation, avec un clone du dépôt ouvert. Il est volontairement détaillé : il remplace le contexte des échanges de rédaction.

---

Tu coordonnes la réécriture du tutoriel français **« Comprendre l’IA et développer avec elle »**, par Hugo Loiseau, pour Zeste de Savoir. Le dépôt `hloiseau/tutoriel-ia-ateliers` est la source de vérité. Huit parties sont rédigées. L’auteur veut maintenant une vraie passe de rédaction et de pédagogie sur l’ensemble, avec une voix naturelle et cohérente.

**Utilise une flotte de sous-agents : un sous-agent responsable de chacune des huit parties.** Tu restes responsable de l’ensemble, de l’introduction générale, des annexes et de l’intégration. Si ta plateforme limite la concurrence, lance les missions par vagues ; garde bien huit missions distinctes. Si elle ne permet réellement pas de déléguer, explique cette limite et effectue les missions successivement. N’invente pas une relecture indépendante qui n’a pas eu lieu.

Il faut modifier les textes, pas seulement rendre un audit. Avance sans demander une validation après chaque paragraphe. L’auteur relira le résultat dans GitHub et dans ZdS. Il ne corrigera pas les exercices des lecteurs et nous n’attendons pas leurs retours pour terminer.

## 1. Comprendre la commande avant de déléguer

Lis entièrement :

- `docs/prompts/GUIDE-VOIX-HUGO.md` : voix, références, exemples avant/après, refus exprimés par l’auteur ;
- `SOMMAIRE.md`, `tutoriel/introduction.md`, `docs/etat-des-contenus.md` ;
- `docs/cadre-redaction.md`, `docs/verification.md`, `docs/experiences-a-lancer.md` ;
- `docs/prompts/MISSION-PARTIE.md` et les manifests des parties ;
- les instructions applicables du dépôt et l’état Git.

Le guide reprend un texte réellement écrit par Hugo. La référence pédagogique est le tutoriel Vim : https://zestedesavoir.com/tutoriels/3575/vim/. Le guide décrit ce qui en a été retenu après lecture de son archive. Consulte des passages de cette référence si elle est accessible, sans recopier sa prose. Si son accès échoue, utilise l’analyse disponible et signale ce qui n’a pas été revu.

Pour ZdS, appuie-toi sur https://zestedesavoir.com/tutoriels/249/rediger-sur-zds/ et sur les fichiers existants. Ne transforme pas les encarts ZdS en syntaxe GitHub inventée. N’installe pas une autre chaîne de publication.

La demande récente prime sur les habitudes du premier jet : Hugo trouve encore trop de formulations du type « c’est ceci, pas cela ». Il demande une réécriture réelle, y compris dans les parties ayant reçu un accord antérieur. Préserve leurs décisions, leurs exemples utiles et les faits validés. Un accord sur le fond n’interdit pas d’améliorer une phrase.

## 2. Préparer un travail intégrable

Inspecte `git status`, la branche, le commit de départ et les modifications présentes. Préserve tout travail de l’auteur. Crée une branche de relecture dédiée ou un worktree si cela permet de l’isoler sans conflit. Ne réinitialise pas une branche, ne supprime pas des fichiers non suivis, ne force pas un push.

Choisis un identifiant de session, par exemple la date suivie d’un suffixe. Les rapports iront dans `docs/relecture/<session>/`. Ce dossier contient des notes de travail, jamais du texte destiné au lecteur du tutoriel.

Définis avant le lancement :

1. le périmètre de chaque agent ;
2. le mode de partage du dépôt ;
3. les propriétaires des fichiers communs ;
4. l’endroit où chaque agent rend son rapport et son diff ;
5. les conventions déjà tranchées dans le guide.

Dans un répertoire partagé, chaque agent ne modifie que les sources de sa partie et son rapport. Dans des worktrees séparés, il remet un commit à intégrer. Ne mélange pas ces deux modes sans prévenir les agents. Aucun agent de partie ne régénère les `LECTURE.md`, les ZIP, le manifest global, les index ou les statistiques : tu le feras une fois les changements réunis.

## 3. Répartir les huit missions

| Agent | Sources canoniques confiées | Vigilance particulière |
| --- | --- | --- |
| 1 | `tutoriel/01-histoire/` | Garder l’histoire en ouverture, les illustrations et la progression ; éviter une succession scolaire de dates. Vérifier les raccourcis historiques contre les sources. |
| 2 | `tutoriel/02-apprentissage/` | Faire observer les effets des expériences ; expliquer les notions au moment où elles servent. Préserver les jeux de données, les découpages et les résultats réellement mesurés. |
| 3 | `tutoriel/03-modele-local/` | Accompagner installation, chargement et premiers appels ; distinguer capacité à lancer un petit modèle et utilité pratique. Aucune promesse d’agent de code performant sur CPU. |
| 4 | `tutoriel/04-developpement/` | Rendre la progression lisible de bout en bout : choix de l’outil, premier bug, tests, correction, validation. Réduire les répétitions. Les comparatifs détaillés restent dans les annexes. |
| 5 | `tutoriel/05-agents/` | Rendre les appels d’outils, le contexte, les permissions et les coûts concrets. Le banc Python sans modèle n’est pas une trace d’un véritable agent. |
| 6 | `tutoriel/06-mcp-skills/` | Garder la construction pas à pas d’un MCP, les vérifications et les skills. Conserver l’analogie de la recette adaptable au passage sur les skills, là où elle explique quelque chose. |
| 7 | `tutoriel/07-ia-maison/` | Relier recherche documentaire, application et adaptation. Distinguer expériences CPU exécutées et LLM sur GPU encore à éprouver. Garder les erreurs réelles du modèle. |
| 8 | `tutoriel/08-choisir/` | Traiter concrètement données, travail humain, droits, environnement, dépendances et apprentissage. Assumer qu’on peut choisir de se passer de l’IA. Ne pas moraliser chaque geste. |

Pour chaque mission, utilise `docs/prompts/MISSION-PARTIE.md`. Donne le chemin exact, l’identifiant de session, le commit de départ et les limites d’écriture. Fournis le guide complet ou son chemin avec instruction de le lire intégralement. Un résumé du style en trois adjectifs ne suffit pas.

Chaque agent lit aussi les conclusions et introductions des parties voisines, en lecture seule. Il peut signaler un raccord à améliorer chez le voisin ; il ne le modifie pas lui-même. Tu arbitres ensuite.

Tu prends directement en charge `tutoriel/introduction.md`, `tutoriel/annexes/`, les raccords entre parties et les index. La conclusion de la partie 8 ferme actuellement le parcours ; `tutoriel/conclusion.md` est volontairement vide pour éviter de la répéter. N’ajoute pas une deuxième morale générale.

## 4. Ce que doit produire la réécriture

Garde un texte utile, précis, plaisant à suivre. Les critères détaillés et les exemples sont dans le guide. Les priorités immédiates sont :

- une situation concrète avant une explication abstraite quand le lecteur peut essayer ;
- des commandes accompagnées du dossier courant, de l’état de départ et d’une observation interprétable ;
- des transitions qui expliquent pourquoi l’étape suivante devient utile ;
- des phrases développées naturellement, plutôt qu’une série de slogans ;
- des limites placées au bon endroit, sans répéter la même précaution après chaque exemple ;
- de vrais schémas ou captures lorsqu’ils apportent une information ; conserver les crédits ;
- des smileys Unicode occasionnels, selon le passage ;
- des TL;DR utiles au début des parties et chapitres, sans recopier ensuite le même résumé trois fois.

Conserve la voix de l’auteur : « trial and error », « refacto » ou « planter le bureau » peuvent être adaptés au lectorat sans devenir une langue administrative. Les opinions fortes restent des opinions assumées et argumentées. N’atténue pas automatiquement chaque affirmation.

Le « je » désigne Hugo. Tu ne peux pas lui attribuer tes propres essais, une anecdote inventée ou une mesure réalisée sur une autre machine. Les modèles, prompts et résultats fictifs restent identifiés. Les comparatifs de marché portent une date de vérification réelle : une photographie de septembre 2026 n’autorise pas à inventer ce qui n’a pas été consulté.

Le tutoriel doit couvrir le développement avec l’IA, MCP et skills compris, tout en traitant la compréhension des modèles, l’histoire, les usages locaux et les enjeux humains. Ne supprime pas une de ces dimensions sous prétexte de raccourcir. Réduis d’abord les répétitions et les détours inutiles.

## 5. Vérifier le fond sans fabriquer d’expérience

Pour les affirmations douteuses ou les informations changeantes, consulte les sources primaires : documentation officielle, article de recherche, contrat ou fiche du modèle. Note les URL et dates dans le rapport. Ne cherche pas à documenter chaque correction de ponctuation.

Distingue une correction rédactionnelle d’un changement de protocole. Un code modifié doit être vérifié par le parcours concerné. Ne change pas une commande, un nom de fichier ou un résultat attendu uniquement pour rendre le paragraphe plus élégant. Si une correction technique dépasse le périmètre de l’agent, fais-la remonter et prends-en la responsabilité.

Consulte les rapports d’essais locaux nouvellement disponibles dans `docs/experiences-locales/`, s’ils existent. Un prompt préparé n’est pas une expérience exécutée. En leur absence, conserve honnêtement les réserves connues. N’ajoute pas « testé sur la 3090 Ti » sans trace correspondante.

Ne lance pas un téléchargement massif, un entraînement GPU ou une API payante pour cette seule passe de prose. Les prompts de ces travaux sont dans `docs/prompts/LOCAL-COORDINATEUR.md`.

## 6. Intégrer et faire la passe transversale

Attends les livrables des huit missions, inspecte les diffs et résous leurs conflits. Les agents peuvent avancer par vagues sans attendre une réponse de Hugo. Vérifie toi-même des passages substantiels de chaque partie ; leur rapport ne remplace pas la lecture.

Lis ensuite les introductions, conclusions et transitions dans l’ordre global. Cherche notamment : notions définies plusieurs fois, notion supposée connue avant son introduction, changements d’outil sans explication, promesses jamais tenues, variations du projet fil rouge, coûts ou capacités contredits ailleurs.

Fais une relecture adverse après intégration. Si possible, confie à un agent disponible la lecture d’une autre partie que la sienne et à un autre le parcours des transitions ; respecte les limites de concurrence. Cette seconde passe teste la cohérence et la pédagogie, elle ne doit pas uniformiser mécaniquement toute la prose. Traite les problèmes concrets qu’elle trouve.

Régénère les lectures et les imports depuis la racine du dépôt :

```bash
python outils/assembler_tutoriel.py --exports telechargements/zds
python outils/assembler_global.py
python -m unittest discover -s outils -p 'test_assembler_global.py' -v
```

Si du code d’atelier a effectivement changé, exécute ses vérifications pertinentes et reconstruis son archive avec `outils/assembler_annexes.py`, selon son aide. Inutile de relancer tous les entraînements pour un accord corrigé. Vérifie les liens locaux, les images, les notes, les tableaux, les légendes et les manifests. Ne revendique pas un rendu validé dans ZdS si personne n’a effectué l’import interactif.

## 7. Rendre un résultat relisible

Mets à jour `docs/etat-des-contenus.md` sans transformer la relecture en validation de l’auteur. Prépare dans `docs/relecture/<session>/` :

- les huit rapports de partie ;
- un bilan du coordinateur avec les principaux changements et quelques avant/après ;
- les points techniques encore ouverts, chacun avec son emplacement et la preuve manquante ;
- les contrôles réellement exécutés et leur résultat ;
- les fichiers où Hugo devrait concentrer sa propre relecture.

Les rapports sont des documents de travail. Ne les ajoute pas aux ZIP ZdS. Dans le message final, donne les liens vers le résultat, le bilan et l’archive ; annonce clairement les limites restantes. N’ajoute pas un nouveau tour de validation obligatoire avant de terminer les corrections déjà demandées.

Respecte les droits de publication disponibles dans la session. Hugo a demandé de centraliser le projet sur GitHub : prépare un commit relisible et publie la branche de travail si l’accès est autorisé ; n’écrase aucun travail concurrent et n’importe rien sur ZdS sans demande. Si le dépôt distant a changé, intègre ses changements proprement avant de proposer le résultat.
