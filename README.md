# Les ateliers du tutoriel sur l’IA

Les fichiers pratiques du tutoriel « Comprendre l’IA et développer avec elle », en cours de rédaction pour Zeste de Savoir.

On commence sur CPU, sans abonnement à une API. Une carte graphique peut servir à des variantes, mais elle n’est pas nécessaire pour suivre les premiers ateliers.

## Choisir un atelier

| Partie | Ce que l’on fait | Dossier de départ |
| --- | --- | --- |
| 2 — Comprendre un modèle | Reconnaître des chiffres, entraîner un petit réseau, produire du texte et calculer une attention | [Atelier d’apprentissage](ateliers/02-apprentissage/atelier-ia/README.md) |
| 3 — Modèle local | Charger un petit modèle, lui envoyer des messages et mesurer les appels | [Atelier local](ateliers/03-modele-local/atelier-local/README.md) |
| 4 — Développement | Reproduire un bug, écrire les tests, corriger et vérifier un suivi de prix | [Atelier de développement](ateliers/04-developpement/README.md) |

Chaque README indique le dossier dans lequel ouvrir le terminal et les commandes à lancer. Python 3.12 est utilisé pour les exécutions de référence.

Les répertoires `resultats-reference` contiennent des résultats réellement obtenus. Les scripts écrivent vos essais dans leurs propres dossiers de sortie. Les réponses et durées peuvent différer sur votre machine.

## Télécharger

Vous pouvez cloner ce dépôt ou télécharger son archive ZIP depuis GitHub. Les [archives des trois ateliers](telechargements/) permettent de télécharger un atelier séparément. Le chapitre peut pointer vers une révision précise du dépôt pour conserver les mêmes fichiers au fil des corrections. Les fichiers de poids du modèle local et les exécutables de llama.cpp se téléchargent séparément.

## État des vérifications

Les ateliers ont été exécutés sous Linux sur CPU. L’atelier local a été interrogé avec un vrai modèle ; les tests unitaires du client utilisent, eux, des réponses factices. Les scripts de développement et leurs mutations ont été exécutés. Les prompts fournis ne sont pas des traces attribuées à un agent particulier.

Les essais GPU, Windows, macOS et les interactions dans un vrai navigateur restent à vérifier. Voir [les résultats et leurs limites](docs/verification.md).

## Préparer les archives des ateliers

```bash
python outils/assembler_annexes.py
```

Les trois ZIP sont écrits dans `telechargements/`. Ils contiennent le code, les résultats de référence et les mentions de licence.

Pour exécuter les contrôles rapides sans téléchargement de modèle :

```bash
python outils/verifier.py
```

Ces contrôles ne relancent pas les entraînements de la partie 2 ni le serveur de la partie 3.

Les sources des données et du modèle sont recensées dans [CREDITS.md](CREDITS.md).

## Licences

Copyright © 2026 Hugo Loiseau.

- **Code et page de dessin : GPLv3**, voir [LICENSE](LICENSE).
- **Textes de documentation et illustrations originales : CC BY-SA 4.0**, voir [LICENCE-TEXTES.md](LICENCE-TEXTES.md).
- **Éléments tiers :** les licences et attributions précisées dans [CREDITS.md](CREDITS.md) restent applicables.
