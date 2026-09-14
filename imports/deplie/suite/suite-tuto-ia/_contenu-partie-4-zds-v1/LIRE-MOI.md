# Partie 4 — relire et importer

Ouvrir `relecture.html` dans un navigateur. Les images sont intégrées et la lecture fonctionne hors ligne. `sommaire.md` donne le plan détaillé. Les petits Markdown indiqués dans `manifest.json` sont les sources à modifier.

## Import ZdS

Utiliser `partie-4-zds-v1.zip`, avec le manifeste à la racine. Sélectionner la même archive dans les champs d’import du contenu et des images. Les références `image:images/...` servent à l’import des images dans la galerie.

L’archive représente cette partie seule. L’import n’a pas été réalisé sur le compte de l’auteur ; contrôler son rendu dans un brouillon avant publication. Les images sont toutes inférieures à 1 Mo.

## Annexes de code

Le ZIP d’annexes est inclus dans l’archive ZdS et à côté de cette lecture. Les programmes complets sont aussi disponibles dans le dossier `atelier` de la livraison générale.

Avant publication, remplacer le lien relatif du ZIP par son adresse publique stable. La documentation ZdS consultée décrit l’import de ZIP d’images, pas un dépôt public générique d’archives de code : https://docs.zestedesavoir.com/back-end/gallery.html. Aucun lien d’hébergement n’a été inventé et aucun téléversement public n’a été effectué.

Les résultats de référence sont distincts des sorties produites par le lecteur. Les journaux et la portée des contrôles sont dans `verification/`.

Pour reconstruire cette partie, voir `reprise-locale/assembler.py` dans la livraison générale.
