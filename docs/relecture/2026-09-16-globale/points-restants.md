# Points restant réellement à vérifier

## Publication

- Importer `telechargements/zds/tutoriel-ia-complet.zip` dans un brouillon ZdS.
- Contrôler dans l’interface les niveaux du sommaire, les 46 images, les 155 notes, les tableaux, les légendes et la coloration des blocs de code.
- Ne marquer aucun conteneur `ready_to_publish` avant cette vérification et la relecture de l’auteur.

## Machine de Hugo

Le système d’exploitation reste à identifier. Les missions de `docs/prompts/local/` devront relever la configuration réelle avant d’adapter les commandes.

- Partie 2 : reprendre le parcours sur cette machine et vérifier les gestes dans un vrai navigateur.
- Partie 3 : reproduire CPU et fonctionnement hors ligne, puis comparer le même modèle sur la RTX 3090 Ti avec journaux, durée et VRAM.
- Partie 4 : observer un assistant réel et les interfaces décrites ; l’expérience locale Continue reste séparée.
- Partie 5 : recueillir outils, contexte, refus, reprise et compteurs d’une session avec modèle réel.
- Partie 6 : brancher le serveur MCP et essayer réellement la découverte du skill et les recettes PRIX-1 / PRIX-2.
- Partie 7 : reproduire les références CPU puis exécuter, si le système le permet, l’adaptation LoRA du LLM sur GPU. Le protocole préparé ne vaut pas résultat.
- Partie 8 : la comparaison humaine avec et sans IA reste facultative ; aucune mesure de productivité ou d’apprentissage ne doit être inventée.

## Autres environnements et informations changeantes

- Vérifier les variantes Windows et macOS des procédures concernées.
- Relever les libellés et versions visibles des interfaces au moment des essais.
- Réactualiser le comparatif et les tarifs si la publication s’éloigne de septembre 2026.

## Extension hors développement

La [proposition de partie sur les pipelines de travail](extension-hors-developpement.md) doit encore être discutée. Les choix structurants sont :

- insertion après MCP et skills, avec renumérotage des parties suivantes ;
- contexte du fil rouge que Hugo peut assumer dans le détail ;
- orchestrateur concret de l’atelier et place des produits commerciaux dans une annexe datée ;
- parcours entièrement local ou véritable messagerie de démonstration avec approbation avant envoi.
