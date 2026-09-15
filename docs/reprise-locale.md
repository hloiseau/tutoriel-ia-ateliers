# Reprendre avec Codex sur la machine de l’auteur

Ouvrir une session dans un clone à jour de `hloiseau/tutoriel-ia-ateliers`, puis lui donner ce texte :

---

Nous écrivons le tutoriel français « Comprendre l’IA et développer avec elle » pour ZdS. Ce dépôt est la source courante du travail.

Lis `SOMMAIRE.md`, `docs/etat-des-contenus.md`, `docs/cadre-redaction.md`, `docs/experiences-a-lancer.md` et les rapports de vérification des ateliers. Les parties 1 à 4 sont sous `tutoriel/` ; le code pratique est sous `ateliers/`. La partie historique V3 a été validée : ne change pas son ton.

L’auteur possède une RTX 3090 Ti de 24 Go et 64 Go de DDR4 3200. Relève le système, le CPU, le pilote et les outils installés avant de choisir les commandes adaptées. Préserve les installations et les projets présents ; utilise un dossier d’expériences dédié.

Rejoue d’abord les parcours CPU des parties 2 et 3. En partie 4, distingue le parcours hébergé de l’expérience facultative de discussion locale sur CPU. Cette dernière ne valide pas un parcours d’agent de code. Pour chaque essai, consigne le temps avant la première réponse, la durée totale, la mémoire, la réponse complète et ses erreurs. Ne recommande une configuration pour l’atelier qu’après l’avoir éprouvée sur ses tâches. Vérifie aussi la session Local avec les modèles Copilot, le passage Ask → Agent, l’affichage des actions et la comparaison avec le presse-papiers dans VS Code. Ces manipulations documentées n’ont pas été rejouées. Inspecte les fichiers avant de lancer leurs commandes et respecte les restrictions de l’environnement.

Conserve versions, commandes, sorties, codes de retour, réponses brutes et mesures dans un nouveau dossier daté. Ne remplace pas les résultats de référence. Distingue exécution réelle, réponse factice de test et déduction. Corrige les procédures à partir des erreurs effectivement rencontrées.

Modifie les petits Markdown déclarés dans les manifests, puis lance `python outils/assembler_tutoriel.py --exports ../exports-zds`. Les `LECTURE.md` sont générés. Le tutoriel reste indépendant d’un fournisseur, accessible sans grosse carte graphique et attentif aux enjeux éthiques et à l’apprentissage.

Prépare des modifications relisibles dans Git. Cette reprise ne demande pas à elle seule une publication sur ZdS. La rédaction peut avancer sans attendre les retours des lecteurs.
