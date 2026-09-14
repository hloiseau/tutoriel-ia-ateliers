# État de la centralisation

État au **14 septembre 2026**. Cet inventaire distingue les fichiers récupérés des textes seulement identifiés dans les échanges.

## Disponible sur main

| Contenu | Emplacement | État |
| --- | --- | --- |
| Plan global | [SOMMAIRE.md](../SOMMAIRE.md) | Plan de travail ; découpage des premières parties à reprendre de leurs archives |
| Choix éditoriaux et pédagogiques | [cadre-redaction.md](cadre-redaction.md) | Synthèse des décisions de l’auteur |
| Ateliers d’apprentissage | [Partie 2](../ateliers/02-apprentissage/) | Code, données et résultats de référence |
| Atelier de modèle local | [Partie 3](../ateliers/03-modele-local/) | Code, configuration et résultats CPU |
| Atelier de développement | [Partie 4](../ateliers/04-developpement/) | Départ, tests rouges, correction et consignes |
| Nouveau début de la partie 4 | [Textes](../tutoriel/04-developpement/README.md) | Trois chapitres rédigés, à relire ; nouvelles installations non rejouées |
| Archives pratiques | [Téléchargements](../telechargements/) | Trois archives d’ateliers ; ce ne sont pas les textes complets du tutoriel |

Les textes du nouveau début de la partie 4 proviennent du commit `7ce9ee7333fdc0e367e18fe26db15de7a2a048a6`. Le panorama a ensuite été étendu aux harness, dont Pi, à la demande de l’auteur. Ils sont centralisés sous `tutoriel/04-developpement/` ; leur présence sur `main` n’ajoute aucune validation éditoriale ou technique.

## Sources écrites à récupérer

| Fichier identifié dans les échanges | Ce qu’il doit apporter | État connu |
| --- | --- | --- |
| `histoire-ia-zds-v3.zip` | Partie 1 et illustrations | Version validée par l’auteur ; contenu non récupérable dans la session de centralisation |
| `apprentissage-ia-zds-v2.zip` | Partie 2 et illustrations | Texte rédigé ; contenu non récupérable dans cette session |
| `tutoriel-ia-suite-parties-3-4.zip` | Partie 3, six chapitres initiaux de la partie 4 et illustrations | Texte rédigé ; contenu non récupérable dans cette session |
| Dernier export du billet « Fabriquer sa méthode de dev avec un agent, plutôt que copier celle des autres » | Sources du billet publié et éléments associés | Plusieurs versions ont circulé ; prendre le dernier export ZdS |

Le dépôt ne contient pas ces quatre exports. Les trois premiers sont nécessaires pour terminer la centralisation du tutoriel. Le dernier complète celle du billet à l’origine du projet.

## À faire lors de la récupération

1. Importer les vrais Markdown, manifests et images, en conservant leurs crédits.
2. Comparer les variantes éventuelles avec les versions identifiées ci-dessus avant de choisir.
3. Compléter la partie 4 avec les six chapitres existants, puis appliquer les raccords déjà préparés.
4. Vérifier les liens, les images, les notes et l’ordre des chapitres.
5. Préparer les archives ZdS depuis les sources du dépôt et vérifier leur import.
6. Mettre cet inventaire à jour et retirer les mentions « à récupérer » résolues.

## Parties suivantes

Les parties 5 à 8 figurent au plan. Aucun texte complet de ces parties n’a été récupéré ou identifié comme déjà livré dans le contexte disponible. Ne pas confondre les décisions sur leur contenu avec des chapitres rédigés.
