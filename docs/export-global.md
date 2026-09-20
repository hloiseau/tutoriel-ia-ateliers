# Assembler les exports pour ZdS

Le [guide d’import](../telechargements/zds/README.md) donne les deux fichiers : `tutoriel-ia-complet.zip` pour le contenu et `tutoriel-ia-complet-images.zip` pour les images.

```bash
python outils/assembler_tutoriel.py --exports telechargements/zds/parties
python outils/assembler_global.py
python -m unittest discover -s outils -p 'test_assembler*.py' -v
```

## Sources et transformations

Les petits Markdown référencés par les manifests des neuf parties sont les sources canoniques. `tutoriel/introduction.md` est l’introduction générale ; la conclusion de la partie 9 termine le parcours. Le manifeste global et les lectures GitHub sont générés.

Les exports emploient le manifeste ZdS 2.1, de type `TUTORIAL`, avec le code de licence `CC BY-SA`. Les images quittent le ZIP de contenu pour une archive dédiée. Les liens utilisent `archive:`. Dans l’export global, chaque chemin d’image et chaque identifiant de note reçoit le préfixe de sa partie. Les blocs de code sont conservés.

Les dates ZIP sont fixes : les mêmes sources produisent les mêmes octets. Les [statistiques et empreintes](structure-globale.json) décrivent les deux fichiers reconstruits. Les notes éditoriales, prompts, archives historiques et lectures générées sont exclus des imports. Les ateliers sont des téléchargements séparés.

## Contrôles et limites

Les contrôles couvrent les sources manquantes, les images, les notes non résolues, les collisions entre parties, les sorties de dossiers et les exemples dans les blocs de code. Le test des deux archives vérifie la correspondance entre les chemins cités et les images livrées. Le manifeste respecte la hiérarchie contenu → parties → chapitres → sections.

Le contrôle local du parseur officiel ne lance ni le site, ni sa base de données, ni le rendu Markdown. Un premier import du contenu a été signalé par l’auteur, sans images ; l’export d’images séparé accompagne désormais le contenu. L’import complet avec images et son rendu restent à confirmer dans ZdS.

Les conteneurs restent marqués `ready_to_publish: false`. La relecture et les expériences pratiques restent suivies dans [l’état des contenus](etat-des-contenus.md).
