# Révision de la transition entre les parties 3 et 4

[Lire les ajouts dans l’ordre](LECTURE.md) · [Sommaire corrigé](SOMMAIRE.md)

Cette révision ajoute trois chapitres avant le premier ticket. Elle conserve les six chapitres de développement existants et repousse toujours les MCP et les skills aux parties suivantes.

Les textes et les tableaux utilisent le Markdown de ZdS : extraits séparés, appels de notes et légendes `Table:` / `Code:`. Les notes restent dans leurs extraits. GitHub affiche les légendes comme du texte ordinaire.

## Fichiers à intégrer

| Fichier | Destination |
| --- | --- |
| `transition-partie-3.md` | À la fin de la conclusion de la partie 3 |
| `introduction.md` | Remplace l’introduction de la partie 4 |
| `outils/`, `choisir/`, `installer/` | Trois nouveaux chapitres, avant les six existants |
| `chapitres-a-inserer.json` | Trois objets à insérer au début de `children` dans le manifest de la partie 4 |
| `raccord-01-projet.md` | Remplace le premier extrait d’installation de l’ancien chapitre 1 ; nouveau titre : « Lancer les tests du projet » |

Les noms des anciens dossiers n’ont pas besoin de changer. Leur ordre d’affichage vient du manifest.

## Préparer l’archive ZdS depuis les sources existantes

Le dépôt ne contient pas encore les sources complètes des parties 3 et 4. L’ancienne archive n’était plus accessible pendant cette révision. Aucun ZIP complet mis à jour n’est donc annoncé ici.

Le script fourni prépare une **nouvelle copie** de la partie 4, conserve ses six chapitres et ses images, insère les ajouts, puis crée un ZIP avec le manifest à la racine :

```bash
python redaction/partie-4/integrer.py --partie4 /chemin/vers/partie-4 --sortie /chemin/vers/partie-4-revisee
```

Le dossier source doit être celui qui contient le `manifest.json` de la partie 4. Le dossier de sortie et le ZIP correspondant ne doivent pas déjà exister. Le script s’arrête si la structure attendue ne correspond pas.

Pour la partie 3, ajouter séparément `transition-partie-3.md` à sa conclusion. Les fichiers `README.md`, `LECTURE.md`, `SOMMAIRE.md`, le rapport et le script ne sont pas inclus par ce script dans l’import de la partie 4.

**Le script d’intégration n’a pas été exécuté dans cette session.** Il doit être lancé sur les vraies sources avant d’importer le résultat dans ZdS. Voir [l’état des vérifications](VERIFICATION.md).

Textes : CC BY-SA 4.0, Hugo Loiseau. Code du script et configurations : GPL-3.0-only, selon les licences du dépôt.
