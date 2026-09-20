# Importer le tutoriel dans Zeste de Savoir

Ces fichiers servent à l’auteur pour importer le cours. Pour suivre un exercice, utilisez les [archives des ateliers](../README.md).

## Les deux fichiers à télécharger

| Champ du formulaire ZdS | Fichier à sélectionner |
| --- | --- |
| **Archive de votre contenu** | [tutoriel-ia-complet.zip](tutoriel-ia-complet.zip?raw=true) |
| **Archive des images** | [tutoriel-ia-complet-images.zip](tutoriel-ia-complet-images.zip?raw=true) |

Le premier ZIP contient le manifeste et les textes des neuf parties et des annexes. Le second contient les 49 illustrations, aux chemins exacts utilisés dans les textes. Gardez les deux ZIP compressés pour l’import.

Dans « Importer un nouveau contenu », ou « Importer une nouvelle version » si le brouillon existe, remplissez **les deux champs**. Un import du contenu seul ne charge pas les images. Pour reprendre un import sans images, sélectionnez à nouveau le ZIP du contenu et ajoutez le ZIP des images.

Après l’import, vérifiez le sommaire, les illustrations, les notes, les tableaux et les blocs de code dans le brouillon. La mise en bêta se fait ensuite dans ZdS. Les vérifications automatiques ne remplacent pas ce contrôle du rendu.

## Imports par partie

Les [exports séparés](parties/README.md) proposent également un ZIP de contenu et un ZIP d’images pour chaque partie.

## Reconstruire les fichiers

Depuis la racine du dépôt :

```bash
python outils/assembler_tutoriel.py --exports telechargements/zds/parties
python outils/assembler_global.py
```

Le manifeste utilise la version numérique `2.1`, le type `TUTORIAL` et le code de licence `CC BY-SA`. Les textes sources et crédits précisent les versions et attributions applicables. Les liens d’images de l’export utilisent `archive:`. Les conteneurs restent marqués `ready_to_publish: false` pour la relecture.

[Détails des transformations](../../docs/export-global.md) · [Documentation officielle de l’import](https://docs.zestedesavoir.com/back-end/contents.html#import-de-contenus)
