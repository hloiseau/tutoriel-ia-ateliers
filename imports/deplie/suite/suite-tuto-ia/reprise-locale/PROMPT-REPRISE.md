# Prompt à donner à Codex sur la machine de l’auteur

Copier le texte ci-dessous dans une session ouverte à la racine du dossier extrait `suite-tuto-ia`.

---

Nous écrivons un tutoriel français complet pour Zeste de Savoir : « Comprendre l’IA et développer avec elle ». Les sources et l’état du travail sont dans ce dossier.

Lis d’abord `reprise-locale/ETAT-DU-PROJET.md`, `reprise-locale/CHARTE-REDACTION.md`, `reprise-locale/SOMMAIRE-GENERAL.md` et `reprise-locale/EXPERIENCES-A-LANCER.md`. Consulte ensuite les Markdown des parties concernées et les fichiers de leurs ateliers. Ne t’appuie pas sur un supposé historique de conversation : ce dossier est le point de reprise.

L’auteur possède une RTX 3090 Ti de 24 Go et 64 Go de DDR4 3200. Le système et le processeur exacts restent à relever. Commence par les identifier et par lire les installations existantes. Préserve les projets et environnements déjà présents. Utilise un dossier de travail dédié ; les archives de code ne contiennent pas les poids du modèle.

Ton objectif immédiat est de rejouer les parcours des parties 2, 3 et 4 sur cette machine, puis d’ajuster les instructions à partir des problèmes réellement rencontrés. Fais d’abord fonctionner la voie CPU. La comparaison GPU vient ensuite et ne doit pas devenir un prérequis du lecteur. Inspecte les fichiers avant de lancer leurs commandes. Pour une installation nécessitant une élévation ou une modification du système, explique le besoin concret avant d’agir ; ne contourne pas les restrictions de ton environnement.

Conserve les commandes, les versions, stdout, stderr, les codes de sortie et les réponses brutes dans un nouveau dossier d’expériences daté. Ne remplace pas les résultats de référence. Identifie clairement les mesures CPU, GPU, les tests avec réponses factices et les exécutions réelles d’un modèle. Ne transforme pas une déduction en mesure. Si une opération échoue, conserve l’erreur utile et corrige la procédure ; n’écris pas qu’elle a réussi.

Relis aussi la progression : où le lecteur ouvre son terminal, où il trouve chaque fichier, ce qu’il doit obtenir et ce qui doit le faire revenir à l’étape précédente. Il doit pouvoir suivre sans carte graphique dédiée, sans abonnement et sans envoyer son exercice à l’auteur pour correction.

Modifie les petits Markdown déclarés dans les manifestes, puis reconstruis les lectures et les archives avec `reprise-locale/assembler.py`. Pour les parties 3 et 4, les ateliers décompressés sont déjà sous `partie-3/atelier` et `partie-4/atelier`. Les parties 1 et 2 sont conservées dans `parties-precedentes` sous forme d’archives ; extrais-les avant de travailler dessus. Ne réécris pas la partie historique validée pour changer son ton.

Le tutoriel reste général : différents agents de code peuvent servir aux exercices. Les parties ultérieures doivent traiter les agents, les MCP, les skills, l’adaptation et la création d’un modèle, ainsi que les enjeux éthiques et l’apprentissage des juniors. Ne réduis pas le projet à un tutoriel Claude Code ou à une présentation de llama.cpp.

Aucun import sur ZdS ni publication de dépôt n’est demandé dans cette reprise. Prépare des résultats relisibles et les archives correspondantes. Avance sur ce qui est vérifiable sans attendre des retours de lecteurs.
