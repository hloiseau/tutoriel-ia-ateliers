# Expériences à reprendre sur la machine de l’auteur

Ce fichier décrit les validations locales restantes. Il n’est pas un chapitre à importer sur ZdS.

## 1. État de la machine

Relever le système, sa version, l’architecture, le CPU, Python et les outils existants. Confirmer la carte, le pilote et la mémoire disponible. Vérifier l’espace disque avant de télécharger. Conserver l’environnement de travail utilisé ; ne pas enregistrer de secrets ou de noms de dossiers personnels inutiles au rapport.

## 2. Partie 2 — atelier d’apprentissage

Utiliser `ateliers/02-apprentissage/atelier-ia/`. Rejouer les commandes dans un environnement Python isolé. Les versions de référence sont dans `docs/verifications-initiales/02-apprentissage/`.

- Refaire les entraînements et vérifier les nombres d’images et le découpage.
- Ouvrir réellement la grille HTML dans un navigateur : dessiner, effacer, exporter, charger le dessin dans le classifieur.
- Vérifier les commandes propres au système de l’auteur.
- Conserver les résultats différents ; ne pas modifier les données pour retrouver artificiellement les chiffres de référence.

Déjà fait ici : entraînements CPU, gradients, évaluations, parcours depuis l’archive et logique de la page sous DOM simulé. Non fait ici : interactions et rendu dans un vrai navigateur ; Windows et macOS.

## 3. Partie 3 — modèle local sur CPU

Suivre les chapitres dans l’ordre, sans lire seulement le README du code. Cela vérifie aussi les transitions entre les fichiers et les terminaux.

- Installer le binaire adapté ; vérifier son dossier et les bibliothèques associées.
- Télécharger le modèle avec `telecharger.py` et contrôler son empreinte.
- Lancer le serveur et attendre `/health`.
- Rejouer les cinq fichiers de questions et enregistrer les réponses.
- Faire une série avec échauffement et trois appels, deux fils CPU et contexte 2 048.
- Relever la mémoire en indiquant la définition de la mesure utilisée.
- Si pertinent, changer seulement le nombre de fils, puis seulement la capacité de contexte. Distinguer ce dernier essai d’un allongement de l’entrée.
- Vérifier la manipulation hors ligne après téléchargement.

Déjà fait ici : Linux x86-64, moteur b10809, modèle vérifié par SHA-256, serveur réel sur CPU, cinq questions et série de mesures. Une variante CPU générique a été chargée explicitement dans cet environnement. Les chiffres sont un repère de cette exécution, pas ceux de l’ordinateur de l’auteur.

## 4. Partie 3 — variante RTX 3090 Ti

Réutiliser le même modèle, les mêmes questions et les mêmes limites de génération. Préparer le moteur adapté au pilote et au système. Contrôler `--list-devices` et les messages d’affectation des couches ; ne pas conclure au calcul GPU à partir de la seule option passée.

Comparer les réponses, la durée globale et la mémoire vidéo. Noter les autres charges de la machine et les versions. Ne pas confondre un débit de décodage du serveur avec le rapport global du client. Sur ce minuscule modèle, les résultats ne permettent pas de prévoir tous les gains sur de grands modèles.

Choisir ensuite une éventuelle expérience plus grande à partir d’un besoin : français, code, documents. Examiner la fiche, la licence et la mémoire disponible avant le téléchargement. Aucun entraînement massif n’est nécessaire pour valider ces chapitres.

## 5. Partie 4 — parcours de développement

Copier `ateliers/04-developpement/atelier-developpement/01-depart`, suivre les nouveaux tests puis la correction. Vérifier la suite de 3 tests, le premier test rouge, la suite complète de 13 tests avec 2 échecs avant correction, puis 13 réussites. Rejouer les JSON, le retour en stock avec baisse et les deux mutations dans des copies.

On peut réaliser le parcours à la main. Pour tester les consignes avec un agent réel, conserver le nom de l’outil, sa version ou le modèle si exposé, la demande exacte, le diff et les commandes réalisées. Ne pas prendre les trois étapes prédéfinies pour une preuve qu’un agent les a produites.

## 6. Préparer la publication

Reconstruire les lectures et les archives avec `python outils/assembler_tutoriel.py --exports ../exports-zds`, puis importer dans un brouillon ZdS lorsque l’auteur le demande. Vérifier les images, notes, tableaux, coloration et légendes. Les liens des archives de code pointent désormais vers les fichiers publics du dépôt GitHub.

## 7. Installation des assistants

Rejouer le parcours principal VS Code/Copilot et, séparément, l’expérience facultative Continue avec le serveur local, puis Qwen sur CPU. Pour cette dernière, mesurer le délai, conserver la réponse et vérifier son exactitude ; ne pas en déduire une capacité à mener l’atelier comme agent. Consigner les versions, la connexion effective, le contexte utilisé et les erreurs. Voir `tutoriel/04-developpement/VERIFICATION.md`.
