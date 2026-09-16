# Guide de voix, de rédaction et de pédagogie — Hugo

Ce document transmet les attentes de l’auteur à une nouvelle équipe d’agents. Il s’appuie sur ses messages, ses réécritures et ses retours pendant le projet. Les exemples pédagogiques proposés ici sont des formulations de travail : ils n’ont pas tous été validés mot à mot par Hugo.

## 1. Le projet et sa destination

Nous écrivons « Comprendre l’IA et développer avec elle », un tutoriel français destiné à Zeste de Savoir. Les huit parties sont rédigées : histoire ; fonctionnement et apprentissage ; modèle local ; développement ; agents ; MCP et skills ; IA maison ; choix et conséquences des usages.

Le lecteur doit pouvoir agir, comprendre ce qu’il observe et décider ce qu’il veut reprendre. Le tutoriel s’adresse aussi aux développeurs juniors et aux personnes réticentes à l’IA. Les questions éthiques, les limites et la possibilité de s’en passer font partie du propos.

Le texte a été construit avec de l’IA et Hugo trouve encore trop de tournures artificielles. La mission de relecture comprend une vraie réécriture lorsqu’elle est nécessaire. Retoucher trois adjectifs ne répond pas à sa demande.

## 2. Les références ont des rôles différents

### La voix : les textes de Hugo

Le passage ci-dessous a été fourni par Hugo comme exemple « fait maison ». C’est notre référence principale pour la manière de s’adresser aux lecteurs. Il peut servir à lire à voix haute le passage à réécrire, puis à comparer le rythme et la posture.

> Salut !
>
> Merci d’avoir pris le temps de me lire.
>
> Ce n’est pas une mauvaise idée, mais il y a énormément de choses à dire. L’IA dans le développement est un sujet très vaste, et j’aimerais aussi aborder l’évolution de notre métier, expliquer ce qu’est réellement une IA générative, comment ces modèles sont créés aujourd’hui et quelles sont leurs limites.
>
> J’aimerais également parler des questions éthiques liées à leur utilisation, ainsi que des moyens de faire mieux que de simplement vendre son âme à quelques géants américains ou chinois.
>
> Selon moi, un tuto destiné à des développeurs juniors devrait aussi aborder ces sujets. Et surtout expliquer pourquoi, dans certains cas, un développeur junior ne devrait justement pas utiliser l’IA comme je le propose dans ce billet.
>
> Utiliser correctement ces outils demande déjà une bonne compréhension de ce que l’on fait. Sinon, on peut très vite se retrouver à générer des montagnes de code là où une seule ligne aurait suffi.
>
> Sans parler des bugs et autres problèmes qui peuvent passer entre les mailles du filet… Même si ma méthode et les skills que je décris dans ce billet permettent d’en atténuer une partie, il faut malgré tout passer un temps certain à relire, tester et valider ce qui est produit.
>
> Donc oui, l’idée me plaît beaucoup, mais un tuto de ce genre ne se fait clairement pas en cinq minutes 😅

Ce que ce passage nous apprend :

- Il part de la personne et de sa demande. Il explique pourquoi le sujet mérite du travail.
- Les phrases peuvent être longues quand elles développent une idée. Il n’écrit pas tout en slogans ou en fragments de trois mots.
- Il assume un avis, avec « selon moi », puis donne une raison concrète.
- Il parle du métier, des bugs, des tests et de la relecture. Le vocabulaire reste familier pour un développeur.
- Il peut être mordant, par exemple sur la dépendance aux grands fournisseurs. Il ne transforme pas chaque désaccord en formule consensuelle.
- L’humour vient de la situation. Le smiley termine naturellement la remarque sur le travail nécessaire.
- Il emploie une opposition lorsqu’elle sert son raisonnement. Sa critique vise leur répétition mécanique, pas la suppression de tout « mais ».

Ne reproduis pas les fautes des messages spontanés pour « faire authentique ». Nous cherchons cette voix dans un texte relu : accords, conjugaison, ponctuation et typographie corrects.

### La pédagogie : le tutoriel Vim

Référence explicite : [Vim sur ZdS](https://zestedesavoir.com/tutoriels/3575/vim/). Hugo en a fourni une archive pendant la rédaction ; elle n’est pas redistribuée dans ce dépôt.

L’archive a notamment été examinée pour l’introduction, le premier chapitre d’édition et un exercice sur les commandes. Le premier apprentissage repose sur des gestes et des observations : lancer Vim, savoir le quitter, essayer d’écrire, observer le mode, sauvegarder et comprendre un refus de quitter après modification. Les captures se placent à côté des états à reconnaître. L’humour accompagne une difficulté concrète.

À reprendre dans notre tutoriel :

1. Une action que le lecteur comprend et peut essayer tout de suite.
2. Le résultat visible : message, fichier, capture, graphique ou sortie.
3. Une explication qui répond à ce que l’on vient d’observer.
4. Une variation ou un incident qui donne une raison d’apprendre la suite.
5. Un repère pour reprendre lorsqu’une étape échoue.

À ne pas recopier : les phrases originales, les fautes, les raccourcis anciens, les émoticônes ASCII et la multiplication des panneaux. Les demandes plus récentes de Hugo priment : smileys Unicode, peu d’encarts et aucun commentaire méta inutile. Ne fais pas de cette référence un prétexte pour importer des contenus ou illustrations tiers sans vérifier leurs droits.

Si tu peux consulter la référence, lis quelques passages en contexte. Si le site est inaccessible, utilise l’analyse précise ci-dessus et signale cette limite dans le rapport de travail. N’invente pas une lecture que tu n’as pas faite.

### Le format : le guide ZdS

Référence : [Rédiger sur ZdS](https://zestedesavoir.com/tutoriels/249/rediger-sur-zds/). Les fichiers du dépôt utilisent un manifest et des petits Markdown ; les lectures et archives sont générées. La section 9 de ce guide donne les conventions utiles.

## 3. Posture et pronoms

Le texte s’adresse au lecteur avec « vous ». « Nous » accompagne une manipulation commune. « Je » peut exprimer une expérience ou une opinion de Hugo lorsque le contexte la justifie.

Évite de passer sans raison de « vous » à « tu », ou de donner au narrateur le rôle d’un formateur qui contrôle ses élèves. Le lecteur est capable de réfléchir ; nous lui donnons les informations et les exemples pour le faire.

Faits biographiques disponibles : Hugo développe sur une flotte de microservices en Go ; il utilise un agent au quotidien ; il adapte les fichiers et procédures par trial and error ; il possède une RTX 3090 Ti de 24 Go et 64 Go de RAM DDR4. Son système d’exploitation n’est pas établi dans la conversation d’origine. Ne lui attribue ni résultat GPU, ni incident, ni souvenir supplémentaire.

Écrire « dans notre essai enregistré » à propos d’un journal vérifiable convient. Écrire « j’ai observé sur ma 3090 Ti » serait faux tant que l’essai local correspondant n’existe pas. Pour une nouvelle prise de position non documentée, propose-la dans le rapport au lieu de la glisser comme une conviction déjà exprimée par l’auteur.

## 4. Le problème de ton signalé en dernier

Hugo trouve trop de phrases de la forme « c’est ceci, pas cela », ainsi que leurs variantes : « ce n’est pas X, c’est Y », « l’enjeu n’est pas X mais Y », « X ne signifie pas Y », « pas une promesse », « pas une garantie ». Leur accumulation donne l’impression qu’un assistant corrige le lecteur avant même de l’avoir laissé essayer.

Pour les reprendre :

- Formule directement l’idée utile quand la comparaison ne sert à rien.
- Remplace une abstraction par ce qui arrive dans l’exemple.
- Garde les distinctions nécessaires, mais explique-les une fois au bon endroit.
- Regroupe des limites identiques au lieu de conclure chaque paragraphe par une réserve.
- Laisse les preuves conduire à la conclusion : un modèle qui invente une durée se comprend mieux avec son entrée et sa réponse qu’avec plusieurs avertissements généraux.

Ne supprime pas une distinction technique indispensable. Préparer une recette et l’exécuter ont des résultats différents. Un banc déterministe et un modèle réel ne donnent pas les mêmes preuves. Un coût fictif ne doit jamais devenir une mesure observée. Le travail consiste à trouver une manière naturelle de l’expliquer, puis à avancer.

## 5. Exemples de réécriture

Les formulations « avant » ci-dessous sont des exemples de défauts à chercher ; elles ne sont pas toutes des citations du tutoriel. Les formulations « après » illustrent une direction. Adapte-les à la section, sans les répéter partout.

### A. Une opposition qui n’apporte rien

Avant : « L’objectif n’est pas de faire confiance à l’IA, mais de garder le contrôle. »

Après : « Avant de garder la modification, ouvrez le diff et relancez les tests. Nous allons vérifier ce que l’agent a changé. »

La deuxième version donne quelque chose à faire et dit à quoi cela sert.

### B. Une distinction nécessaire, rendue concrète

Avant : « Une source pertinente ne garantit pas une réponse correcte. »

Après : « Le document laisse la durée à décider. Pourtant, le modèle répond “dix minutes”. Ouvrons le journal : le bon passage était bien présent dans les messages envoyés. »

Cette réécriture exige un journal qui montre réellement ces faits. La partie 7 en possède un ; ne fabrique pas le même incident ailleurs pour obtenir un effet de style.

### C. Une limite répétée

Avant : « Ce résultat ne constitue pas un benchmark, ne garantit pas les performances sur votre machine et ne permet pas de généraliser à tous les modèles. »

Après : « Ces essais nous aident à comparer nos réglages sur cette machine. Pour retrouver l’expérience, gardez le modèle, sa version et les paramètres du lancement. »

Si la section contient une extrapolation dangereuse, corrige-la explicitement. La réécriture ne doit pas effacer le périmètre d’une mesure.

### D. Une procédure trop scolaire

Avant : « Ouvrez la fiche et cherchez quatre informations. Si l’une manque, notez son absence. »

Après : « Nous voulons utiliser ce modèle pour répondre en français. Regardons les langues indiquées dans sa fiche, puis essayons notre question sur la remise en stock. Cela nous donnera déjà un premier point de comparaison. »

Le lecteur voit pourquoi il consulte ce document. Une fiche de suivi peut rester utile dans l’atelier ; elle n’a pas à devenir le rythme de tous les paragraphes.

### E. Une transition automatique

Avant : « Nous avons vu X. Voyons maintenant Y. Il est important de comprendre Z. »

Après : « Notre fonction passe les tests, mais le ticket prévoit aussi le retour en stock. Essayons ce cas avant de garder la correction. »

La transition naît d’une question concrète. Ne remplace pas tous les raccords par le même exemple de test.

### F. Un panneau qui commente le cours

Avant : un encart expliquant que le schéma est simplifié, que les exemples sont fictifs et que les sources sont en notes.

Après : retirer le panneau. Donner dans la légende la précision nécessaire à la lecture du schéma ; identifier le jeu fictif lorsqu’il apparaît ; laisser les appels de notes près des affirmations sourcées.

Une limite technique utile peut rester dans une phrase ordinaire : « Dans ce premier calcul, les deux entrées favorisent l’activation. » Inutile d’ajouter un discours général sur la complexité du cerveau si la manipulation ne l’utilise pas.

### G. Un terme que Hugo emploie

Avant : « Nous suivons une démarche d’amélioration itérative des instructions opérationnelles. »

Après : « Il y a eu du trial and error. Quand l’agent prenait un raccourci ou répétait une erreur, je lui demandais de modifier les fichiers. »

Ce souvenir est présent dans les messages de Hugo. Il peut donc être repris. On peut aussi expliquer le terme à sa première apparition, en une phrase, sans le supprimer partout.

### H. Une consigne affaiblie

Avant : « Vous pourriez inviter l’agent à préférer le Makefile. »

Après : « Écrivez la consigne directement : “Ne lance jamais `go test` directement ; utilise la cible du Makefile du projet.” »

Hugo veut montrer pourquoi il formule des instructions impératives et précises. Conserve cette intention. Les droits et contrôles exécutables, lorsqu’ils sont nécessaires, doivent être expliqués dans le passage consacré à leur rôle. N’attribue pas à une phrase un pouvoir de blocage que le code n’assure pas.

### I. Une précision numérique sans utilité

Avant : « Le fichier pèse 386 404 992 octets, soit 386 Mo ou 369 Mio. »

Après : « Le téléchargement fait environ 386 Mo. »

L’empreinte et la taille exacte peuvent rester dans le manifest de téléchargement. Une taille de tenseur, un seuil métier ou une mesure à comparer doit en revanche conserver sa précision utile.

### J. Une opinion diluée

Avant : « Il pourrait être pertinent d’envisager l’éventualité d’adapter certaines méthodes selon votre contexte. »

Après : « Votre équipe a ses outils et ses habitudes. Adaptez les fichiers à cette manière de travailler, plutôt que de réorganiser le projet autour du framework. »

Hugo assume ce point de vue. Garde sa force, sans inventer des défauts factuels à un produit.

### K. Un humour plaqué

Avant : « Attention, petit padawan de l’IA, voilà un piège sournois ! 😉 »

Après : « Le modèle vient de proposer une durée que personne n’a décidée. On va éviter de transformer son imagination en règle métier. 😅 »

Même la seconde phrase doit servir le passage. S’il n’y a pas de place naturelle pour une plaisanterie, écris simplement l’observation.

### L. Une explication après coup trop abstraite

Avant : « La qualité des données est un enjeu essentiel de la performance globale du système. »

Après : « Notre dossier contient encore l’ancienne règle de notification. Si la recherche la retrouve, le modèle recevra deux consignes contradictoires. Retirons-la de l’index courant, puis reposons la même question. »

L’exemple suppose que l’archive, le statut et le programme correspondent. Vérifie les fichiers avant de proposer la manipulation.

## 6. Un passage complet : le rythme attendu

Exemple de départ trop mécanique :

> Notre modèle n’est pas un expert. Il est un outil probabiliste. La présence d’une source ne garantit pas sa fidélité. Il convient donc de procéder à une vérification rigoureuse de la réponse. Cette approche permet de conserver un contrôle humain.

Proposition de travail, appuyée sur l’essai documentaire de la partie 7 :

> Posons maintenant la question sur la temporisation. Le ticket laisse la durée à décider ; nous attendons donc que l’assistant le signale.
>
> Dans notre essai, il répond pourtant : « Délai de temporisation validé : 10 minutes. »
>
> Ouvrez le journal. Le passage envoyé au modèle dit bien qu’aucun délai n’est validé. La recherche a retrouvé l’information, mais la réponse invente tout de même un nombre.
>
> Gardons cette question dans nos essais. Si nous changeons le modèle ou les consignes, elle nous permettra de voir si le problème revient. Pour le ticket, la durée reste à arbitrer avec les personnes concernées.

Ce passage contient encore un « mais » utile. Il suit un événement, montre la preuve et mène à une action. Il n’accumule pas des maximes sur l’IA.

## 7. Construire une progression qui se retient

Un chapitre peut alterner explication, manipulation, exemple, illustration et récapitulatif selon son sujet. N’impose pas une grille identique à tous les chapitres : l’histoire de l’IA n’est pas un tutoriel d’installation.

Pour une manipulation, vérifie ces éléments :

- Le dossier dans lequel le lecteur travaille est identifiable.
- Les fichiers à créer ou à modifier sont nommés.
- Le code montré correspond à l’état du projet à cet endroit.
- Le lecteur sait quel résultat regarder et ce qui constitue une erreur attendue.
- Les prérequis apparaissent avant la commande qui les utilise.
- Une étape ne suppose pas que l’assistant ait lu une annexe encore inconnue du lecteur.
- Les corrections sont accessibles et expliquées, sans demander à Hugo de corriger des copies.

Pour un concept, pars d’une question ou d’un objet concret. Montre ce que la notion permet de comprendre. Présente le terme au moment où il devient utile. Une analogie doit éclairer une relation précise ; elle ne remplace pas toute l’explication technique.

Pour l’histoire, conserve des objets, des personnes, des dates et des expériences identifiables. Évite une succession de « tournants majeurs » et de « révolutions » sans expliquer ce qui a changé.

Les TL;DR restent au début des parties et des chapitres. Ils orientent la lecture en quelques lignes. Ils ne doivent pas répéter toutes les conclusions ni devenir des avertissements standardisés.

## 8. Illustrations et humour

Hugo a explicitement demandé de vraies illustrations. Ne remplace pas les images existantes par « ajouter un schéma ici ». Inspecte l’image avant de commenter sa qualité. Vérifie la relation entre ses flèches, son texte alternatif, sa légende et les calculs du chapitre.

- Une capture montre un état réellement observé ; elle n’est pas une interface inventée présentée comme un résultat.
- Un schéma doit expliquer un mécanisme, une relation ou un choix.
- Un graphique reprend les valeurs enregistrées, avec unités et périmètre.
- Un exemple fictif reste identifié, dans son fichier et sa légende.
- Les crédits et les conditions de réutilisation restent accessibles.

Les figures existantes sont des fichiers PNG ou des images référencées par l’export. Conserve ce parcours d’import. N’introduis pas une dépendance à un rendu Mermaid supposé sur ZdS sans l’avoir vérifié et sans prévoir une illustration compatible.

Utilise des smileys Unicode avec mesure : 🙂, 😅, etc. Pas de quota par chapitre. Évite les clins d’œil répétitifs, les mascottes qui parlent et le vocabulaire infantilisant.

## 9. Conventions ZdS à respecter

Modifier les petits fichiers déclarés dans les manifests. Les `LECTURE.md`, le manifest global et les ZIP se régénèrent avec les scripts du dépôt.

Pour une source :

```markdown
Le résultat concerne cette expérience précise.[^p8-experience]

[^p8-experience]: Auteur, [titre de la source primaire](https://example.org/source), date.
```

L’URL de cet exemple est un emplacement illustratif : ne l’insère pas comme source du cours. Place les notes près de l’affirmation soutenue ; chaque référence doit réellement correspondre au propos.

Pour une image :

```markdown
![Description informative du contenu de l’image.](image:images/exemple.png)
Figure: Ce que l’on doit regarder dans cette illustration
```

Pour le code et les tableaux : indiquer la langue du bloc et employer les légendes `Code:` ou `Table:` lorsque leur ajout aide à identifier l’exemple. Garder les en-têtes des tableaux distincts ; ne pas fusionner leur texte dans la première cellule.

Les blocs `[[information]]`, `[[attention]]` et autres existent sur la plateforme. Hugo demande d’en limiter l’usage. Réserver un panneau à une information qui mérite réellement d’interrompre le parcours. Le rappel « le modèle peut se tromper » n’a pas à devenir un panneau dans chaque chapitre.

Corriger espaces, apostrophes, accents, accords et ponctuation sans changer les commandes, identifiants ou valeurs de code. Respecter les intitulés observés des outils lorsque leur graphie aide le lecteur à les retrouver.

## 10. Vocabulaire et contenu à préserver

- **MCP**, pas « connecteur » pour renommer le protocole ou ses serveurs.
- **Skill**, avec une explication concrète lors de son introduction. L’analogie de la recette de cuisine se trouve en partie 6, chapitre 6 ; elle vient d’un ami de Hugo.
- **Trial and error**, **refacto**, **tokens**, **agent** : conserver les termes qui servent le propos et les expliquer lorsqu’ils arrivent.
- **Drifting** : illustrer une dérive observée dans une session ; éviter de donner ce nom à toutes les erreurs possibles d’un modèle.
- Le tutoriel couvre plusieurs outils. Claude Code, Cursor et Codex sont des exemples, pas un changement de sujet vers un tutoriel consacré à un produit.
- Le comparatif des outils se trouve en annexe. Pi doit rester présent. Ne présenter aucune liste comme exhaustive ni aucune popularité comme une mesure de qualité.
- Les premiers ateliers doivent rester praticables sans grosse carte graphique. Une réponse courte sur CPU n’établit pas la faisabilité d’une session d’agent de code.

La thèse de Hugo : adapter les outils à ses besoins et à son équipe. On peut reprendre une idée, modifier une recette, utiliser l’IA seulement pour une tâche pénible ou s’en passer entièrement. La relecture ne doit pas transformer cette position en argumentaire commercial pour l’adoption de l’IA.

## 11. Exactitude et preuves

Aucun chiffre ne doit être ajouté pour donner du poids au texte. Une ancienne proportion de 78 % avait été inventée dans le billet par un modèle : Hugo l’a explicitement rejetée. Les résultats viennent des fichiers, des expériences ou d’une source retrouvée.

Les prix, interfaces, modèles disponibles et bibliothèques changent. Vérifier les informations nécessaires dans les sources officielles, noter la date et distinguer consultation documentaire et exécution. Pour les faits historiques, juridiques ou les études, conserver la portée exacte des sources.

Ne transformer aucune de ces situations en une autre :

| Ce que nous avons | Ce que le texte peut affirmer |
| --- | --- |
| Test unitaire avec réponse factice | Le client gère le cas essayé |
| Banc sans modèle | Le scénario programmé donne cette trace |
| Appel réel au modèle | Cette réponse a été obtenue avec ces paramètres |
| Observation d’interface | Ce parcours a été vu dans cette version |
| Mesure locale | Ce résultat correspond à ce matériel et ce périmètre |
| Protocole préparé | L’expérience reste à exécuter |

Déplacer les longues listes de validations restantes dans les rapports. Conserver dans le cours les informations dont le lecteur a besoin pour interpréter une commande ou un résultat. Les données fictives et les limites qui changent le sens du résultat doivent rester visibles.

## 12. Statut des textes et degré de réécriture

Les parties 1 et 6 ont été validées par Hugo ; la partie 7 a reçu un accord global. La partie 8 a reçu un avis global favorable, accompagné d’une critique du ton. Ces repères n’interdisent pas la nouvelle passe explicitement demandée. Ils indiquent où préserver davantage la progression et les décisions déjà prises.

Le coordinateur peut réécrire les phrases nécessaires dans toutes les parties. Il doit isoler les changements de fond : une nouvelle expérience, la suppression d’un chapitre, une modification du contrat d’un exercice ou un changement de conclusion technique demandent un motif précis et une vérification adaptée.

Ne fige pas les formulations de ce guide comme un nouveau style automatique. Après une réécriture, lis plusieurs paragraphes d’affilée. Si les débuts de phrases, les oppositions et les conclusions se ressemblent, reprends le passage dans son ensemble.

## 13. Relecture finale d’un passage

Avant de le rendre, pose-toi ces questions :

1. Est-ce que la première phrase donne une idée ou une action concrète ?
2. Est-ce que les phrases suivantes développent cette idée, avec une raison de passer à la suite ?
3. Le lecteur rencontre-t-il un résultat, un exemple ou un objet qui l’aidera à se souvenir du propos ?
4. Ai-je conservé une opinion de Hugo ou l’ai-je affaiblie sans raison ?
5. Ai-je supprimé une réserve qui était nécessaire à l’exactitude ?
6. Ai-je ajouté une expérience, une mesure ou un fait que les sources ne donnent pas ?
7. Le passage donne-t-il envie d’essayer sans infantiliser le lecteur ?
8. Une illustration, un tableau ou quelques puces rendraient-ils la relation plus claire ?
9. Le texte ressemble-t-il encore au même auteur que les pages voisines ?
10. Est-ce que je peux retirer une phrase qui explique simplement comment le tutoriel a été fabriqué ?

Le rapport de travail peut expliquer toutes tes décisions. Le chapitre doit rester agréable à lire.
