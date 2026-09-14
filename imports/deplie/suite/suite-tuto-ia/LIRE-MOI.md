# Comprendre l’IA et développer avec elle — suite de la rédaction

## Commencer par la lecture

- **Partie 3 :** `partie-3/relecture.html` — faire tourner un modèle chez soi.
- **Partie 4 :** `partie-4/relecture.html` — développer avec une IA, du problème au changement vérifié.

Ces deux lectures regroupent douze chapitres, quarante sections et sept illustrations. Les images sont intégrées dans les HTML. Les petits Markdown restent les sources à modifier ; les lectures complètes sont des copies assemblées.

## Importer dans ZdS

Les fichiers `partie-3-zds-v1.zip` et `partie-4-zds-v1.zip` sont les archives d’import de chacune des nouvelles parties. **La grande archive qui contient ce README est le dossier de travail, pas une archive à importer telle quelle dans ZdS.**

Chaque archive de partie contient son manifeste à la racine et ses images. Sélectionner le même ZIP dans le champ du contenu et celui des images. Contrôler le rendu dans un brouillon avant publication ; aucun import sur le compte de l’auteur n’a été effectué ici.

## Récupérer les exercices

Les ZIP d’annexes sont dans les dossiers de chaque partie. Les dossiers `atelier` contiennent aussi leurs sources décompressées. Les poids et le moteur de llama.cpp sont à télécharger séparément ; ils ne sont pas inclus dans cette livraison.

Les annexes doivent être hébergées à une adresse publique stable pour les lecteurs de ZdS. Les liens relatifs actuels fonctionnent dans les dossiers extraits ; les remplacer par les adresses publiées avant la mise en ligne. Aucun hébergement public n’a été effectué.

## Reprendre sur la machine de l’auteur

Ouvrir une session locale dans ce dossier et lui donner le texte de `reprise-locale/PROMPT-REPRISE.md`. Ce passage de relais repose sur les fichiers ; il ne suppose pas que l’application locale puisse récupérer cette conversation.

`ETAT-DU-PROJET.md`, `CHARTE-REDACTION.md`, `SOMMAIRE-GENERAL.md` et `EXPERIENCES-A-LANCER.md` conservent les choix et les vérifications restantes. La référence Vim et les fichiers du guide ZdS fournis sont dans `reprise-locale/references`.

Les deux parties précédentes sont préservées sous `parties-precedentes` : histoire V3 validée et apprentissage V2 avec annexes séparées.

## Ce qui a été vérifié

Le petit modèle a été téléchargé, son empreinte vérifiée et ses appels réellement exécutés sur CPU sous Linux. Les sorties brutes et mesures sont conservées. L’atelier de développement, ses scénarios et deux mutations ont été exécutés. Les archives ont aussi été extraites dans un nouveau dossier pour contrôler leur contenu et rejouer le client ainsi que le parcours de développement.

Les variantes Windows, macOS et GPU, le rendu dans un vrai navigateur et l’import ZdS restent à vérifier. Aucun résultat obtenu sur la 3090 Ti de l’auteur n’est revendiqué.
