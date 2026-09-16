# Modèle de mission pour un sous-agent

Le coordinateur remplace les champs entre accolades, puis transmet cette mission. Les chemins de référence sont relatifs à la racine du dépôt.

---

Tu es responsable de la réécriture de la **partie {NUMERO} : {TITRE}**, dans `tutoriel/{DOSSIER}/`, du tutoriel « Comprendre l’IA et développer avec elle » de Hugo Loiseau.

Session : `{SESSION}`. Commit de départ : `{COMMIT}`. Mode de travail : `{REPERTOIRE_PARTAGE_OU_WORKTREE}`. Rapport attendu : `docs/relecture/{SESSION}/partie-{NUMERO}.md`.

## Lecture obligatoire

Lis intégralement `docs/prompts/GUIDE-VOIX-HUGO.md`. Il contient le texte maison de Hugo, ses corrections explicites, l’analyse de la pédagogie du tutoriel Vim et des exemples avant/après. Applique-le réellement aux paragraphes, pas seulement aux introductions.

Lis ensuite `SOMMAIRE.md`, `docs/etat-des-contenus.md`, le manifest de ta partie, ses sources canoniques, ses crédits, son éventuel `VERIFICATION.md` et le README de l’atelier associé. Lis en lecture seule la fin de la partie précédente et le début de la suivante. Consulte les nouveaux rapports locaux pertinents s’ils existent.

## Périmètre d’écriture

Tu modifies les petits fichiers Markdown déclarés par le manifest de **ta partie uniquement**, ainsi que ton rapport. Les autres parties, les ateliers, les index, les scripts, les ZIP et les `LECTURE.md` sont hors de ton périmètre. Le coordinateur possède les fichiers communs et les régénérations.

Si un changement de manifest, d’image ou de code est nécessaire, signale-le au coordinateur avec la raison et le changement précis proposé. Obtiens une attribution claire avant d’éditer un fichier partagé. Ne supprime jamais le travail d’un autre agent. Dans un dossier partagé, ne committe pas ses fichiers ; dans un worktree, rends ton propre commit selon les consignes du coordinateur.

## Travail demandé

Réécris les passages qui en ont besoin, sans attendre une approbation paragraphe par paragraphe. Préserve les passages déjà naturels. Le but n’est ni une réduction arbitraire du nombre de mots ni une transformation en fiche de cours.

1. Suis l’expérience du lecteur : que sait-il en arrivant, que fait-il, qu’observe-t-il, que comprend-il ensuite ?
2. Corrige les introductions abstraites, les transitions artificielles, les répétitions et les oppositions rhétoriques systématiques.
3. Garde la précision technique et les opinions de l’auteur. Le vocabulaire de développeur a sa place ; explique ce qui est nouveau sans expliquer chaque mot courant.
4. Vérifie que l’on sait dans quel dossier exécuter une commande et avec quel état initial. Un résultat fourni n’est pas forcément une sortie réellement obtenue : lis sa provenance.
5. Préserve les exemples, figures et crédits utiles. Propose une illustration manquante avec une intention précise ; n’insère pas un faux emplacement « image ici » dans le texte final.
6. Réserve les encarts aux informations que le lecteur doit pouvoir retrouver. Supprime les panneaux qui commentent la méthode de rédaction ou prennent le lecteur de haut.
7. Garde les TL;DR et quelques smileys Unicode bien placés. Ne rajoute pas un smiley dans chaque section pour simuler le ton Vim.
8. Termine la partie par un raccord concret avec la suite ; signale au coordinateur les changements nécessaires chez le voisin.

Ne prête pas à Hugo une expérience que tu as inventée ou réalisée toi-même. N’invente pas un chiffre, une citation, un essai, une source ou une réponse d’agent. Une documentation d’interface ne prouve pas que l’interface a été essayée. Pour les erreurs factuelles que tu peux vérifier, consulte la source primaire et conserve le lien dans ton rapport. Les changements techniques non vérifiables restent signalés, sans promesse de fonctionnement ajoutée.

## Autocontrôle

Relis la partie d’une traite dans ses sources, en suivant le manifest. Contrôle les définitions, les pronoms, les noms de fichiers, les références aux figures et les notes. Cherche quelques motifs répétitifs (« ce n’est pas », « il est important », « nous allons voir », « en résumé »), puis juge chaque occurrence ; ne les remplace pas mécaniquement par des synonymes.

Vérifie les fichiers modifiés et `git diff --check`. Ne lance pas les générateurs communs. Les tests techniques ne sont nécessaires que si une modification de procédure le justifie et si le coordinateur t’en confie le périmètre.

## Rapport à remettre

Donne au coordinateur :

- les fichiers effectivement modifiés et le commit si applicable ;
- les améliorations majeures avec trois à cinq courts avant/après représentatifs ;
- les répétitions et transitions qui nécessitent une décision entre parties ;
- les faits corrigés, leurs sources et ce qui reste à vérifier ;
- les contrôles réellement faits ;
- les éventuels points bloquants avec une proposition concrète.

N’annonce pas une partie « validée par Hugo » après ta propre relecture. Une fois ton travail intégré, le coordinateur peut te demander de relire une autre partie en adversaire ; fais alors remonter les problèmes observables, pas une préférence pour ta propre façon de rédiger.
