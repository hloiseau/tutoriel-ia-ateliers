# Vérifications de la partie 5

Révision du 15 septembre 2026. Statut : première rédaction complète, à relire par l’auteur.

## Exécuté

- Atelier construit en ZIP, extrait dans un nouveau dossier, puis exécuté avec Python 3.12.14 sous Linux.
- Six parcours : lecture, refus, injection sans écriture, boucle limitée à trois appels, reprise avec correction du nom de fichier, injection avec écriture explicitement autorisée.
- Vérification que les refus ne produisent aucune note, que l’écriture autorisée produit le texte du script et que les fichiers du projet restent inchangés.
- Deux calculs de coût fictifs : `0.004200` puis `0.006000` avec les catégories et tarifs de l’exercice.
- Douze tests réussis : lectures, refus, lien symbolique extérieur, schéma invalide, absence de fichier, budget d’appels, contenu non exécuté et calcul du coût.
- Trois illustrations générées à partir de leur source et inspectées visuellement.

Les [commandes et sorties](../../docs/verifications-partie5/executions.json) et les [journaux de démonstration](../../docs/verifications-partie5/) sont conservés. Les durées présentes dans les journaux mesurent les fonctions Python du banc, pas l’inférence d’un modèle.

## À ne pas déduire de ces résultats

Le banc ne contient aucun modèle et n’interprète pas les documents en langage naturel. Il rejoue des demandes écrites à la main. Le document piégé ne constitue donc pas un résultat expérimental d’injection contre une IA ; il sert à tester le contrôle qui recevrait la demande.

Ses outils ne proposent ni terminal générique ni réseau. Le programme n’est pas un environnement d’isolation pour exécuter un agent hostile. Ses tests couvrent les règles de cet exercice, sans prétendre valider un mécanisme de sécurité universel.

## Restant à essayer

- Les observations de la boucle dans un assistant réel, avec la version de l’application et le modèle utilisés.
- La comparaison des deux contextes et l’essai de consigne sur les deux états du projet. Aucun avantage de qualité ou de vitesse n’est présumé.
- La reprise dans une nouvelle session à partir d’une fiche relue.
- Un relevé de tokens et de coût à partir d’un fournisseur réel. Le CSV et les tarifs fournis sont fictifs.
- Windows et macOS ; la création d’un lien symbolique peut nécessiter des droits spécifiques et son test peut être ignoré.
- Import et rendu dans un brouillon ZdS, puis relecture de l’auteur.

## Sources

Les références primaires consultées concernent les appels d’outils, le cache de prompts, les injections indirectes et l’utilisation des longs contextes. Elles figurent dans les notes des sections. Les formats JSON du banc sont propres à l’exercice, sans prétendre reproduire une API fournisseur ou MCP.
