# Assembler le tutoriel pour ZdS

Le [ZIP global](../telechargements/zds/tutoriel-ia-complet.zip) regroupe l’introduction générale, les huit parties et les annexes. La hiérarchie reprend celle de l’archive du tutoriel Vim fournie par l’auteur : un contenu, ses parties, leurs chapitres, puis leurs sections.

Depuis la racine du dépôt :

```bash
python outils/assembler_tutoriel.py --exports telechargements/zds
python outils/assembler_global.py
python -m unittest discover -s outils -p 'test_assembler_global.py' -v
```

La première commande régénère les lectures et les imports séparés. La deuxième produit `tutoriel/manifest.json`, `telechargements/zds/tutoriel-ia-complet.zip` et `docs/structure-globale.json`. Le manifest global est généré : modifier les manifests des parties pour changer leur structure, puis reconstruire.

## Sources et transformations

Les petits Markdown déclarés dans les manifests des parties restent les sources canoniques. `tutoriel/introduction.md` est l’introduction générale. `tutoriel/conclusion.md` reste vide : la conclusion de la partie 8 termine déjà le parcours.

Dans l’archive globale seulement, les chemins d’images reçoivent le préfixe de leur partie. Les identifiants internes des notes reçoivent également un préfixe, pour éviter les collisions entre parties. Les blocs de code sont préservés. Ces transformations ne modifient ni le texte source ni les imports séparés.

L’archive contient les sources référencées, leurs images, les crédits et les mentions de licence. Les ateliers, prompts d’assistant, rapports éditoriaux et lectures générées en sont exclus. Les archives d’ateliers restent des téléchargements séparés. Il n’y a pas de nouveau document monolithique de lecture : le sommaire GitHub conserve les liens par chapitre.

## Vérifications et limites

L’assembleur contrôle les fichiers et images référencés, les notes manquantes ou dupliquées, les chemins sortant des dossiers et les entrées ZIP en double. Tous les conteneurs restent marqués `ready_to_publish: false`. Les dates internes du ZIP sont fixes afin que la reconstruction soit reproductible.

Les tests couvrent deux parties utilisant le même nom d’image et de note, la préservation des exemples dans les blocs de code, une image manquante, une note non résolue et une tentative de sortie du dossier. Le [rapport structurel](structure-globale.json) donne les nombres et l’empreinte de l’archive réellement construite.

**L’import interactif dans ZdS n’a pas été effectué.** Dans un brouillon, il reste à vérifier le sommaire, les niveaux de titres, les 46 images, les notes, les tableaux et leurs légendes, ainsi que les blocs de code. Une acceptation par l’assembleur ne prouve pas le rendu du site. Le détail des contrôles de structure est disponible sans prétendre que les nouvelles expériences locales ont été réalisées.
