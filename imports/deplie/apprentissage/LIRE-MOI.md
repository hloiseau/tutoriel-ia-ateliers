# Partie 2 — Comprendre un modèle en le construisant

## Relire

- `relecture-v2.html` : texte complet avec sommaire cliquable et images intégrées, à ouvrir dans un navigateur. Il fonctionne hors ligne.
- `relecture.md` : copie assemblée en Markdown.
- `sommaire.md` : sommaire détaillé de cette partie.
- `SOMMAIRE-GENERAL.md` : plan du tutoriel entier, avec la partie historique V3 validée et la suite prévue.
- `01-atelier` à `08-outils` : les sources Markdown découpées, référencées par le manifeste.

Le corps comprend huit chapitres. Le code complet est disponible dans une archive distincte. Les copies de lecture sont assemblées à partir des petits Markdown ; modifier seulement une copie ne modifie pas les sources importées.

## Importer dans ZdS

Sélectionnez `apprentissage-ia-zds-v2.zip` dans le champ d’archive de contenu **et le même fichier** dans le champ d’archive d’images. Le manifeste est à la racine et les treize images sont dans `images/`. Les références `image:images/…` sont destinées au remplacement par les adresses de la galerie lors de l’import.

La structure et les chemins ont été contrôlés. L’import n’a pas été exécuté sur votre compte ; vérifiez le rendu ZdS après l’import.

Cette archive présente la partie 2 seule pour la relecture. Elle ne remplace pas la partie historique validée.

## Exécuter les projets

Décompressez `annexes-atelier-ia-v1.zip`, inclus dans l’archive. Le dossier `atelier-ia` contient les sources, la grille HTML et le corpus ; `resultats-reference` conserve les modèles, graphiques et rapports obtenus. Les nouveaux calculs écriront leurs résultats dans `atelier-ia/sorties`.

L’environnement Python et ses dépendances ne sont pas inclus. L’installation nécessite Internet ; toutes les manipulations suivantes fonctionnent sur CPU, sans API distante.

Avant publication, hébergez `annexes-atelier-ia-v1.zip` à une adresse publique stable (par exemple une version publiée dans un dépôt de code). Remplacez le lien relatif de `01-atelier/installer.md` par cette URL. Le lien relatif fonctionne pour une lecture des fichiers extraits, mais ne devient pas automatiquement un téléchargement hébergé sur ZdS. La documentation des galeries décrit l’import de ZIP d’images : https://docs.zestedesavoir.com/back-end/gallery.html. Elle ne documente pas le dépôt d’une archive de code destinée aux lecteurs. Aucun téléversement public n’a été effectué.

Les figures sont contrôlées visuellement. Les scripts Python ont été exécutés sous Linux dans un environnement virtuel neuf. Les commandes Windows et macOS sont documentées mais n’ont pas été exécutées sur ces systèmes. Les gestionnaires de la page de dessin ont été testés sous Node avec un DOM simulé ; le rendu et les interactions dans un navigateur réel restent à vérifier. Le téléchargement du navigateur de test n’a pas abouti dans cet environnement.

Les journaux, versions et détails des mesures se trouvent dans `verification/`.
