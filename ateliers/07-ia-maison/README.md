# Construire et adapter une IA maison

[Partie 7](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/07-ia-maison/README.md) · [Vérifications](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/07-ia-maison/VERIFICATION.md)

Deux expériences : retrouver des documents pour une réponse, puis adapter et entraîner un petit modèle de caractères. Les données sont fictives et créées pour cet atelier. Le petit modèle NumPy n’est ni un assistant conversationnel ni un agent de code.

## Installer

Décompressez [l’archive pratique](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-ia-maison.zip), ou ouvrez ce dossier du dépôt. Les commandes ci-dessous se lancent à côté de `recherche.py`.

Python 3.12 est la version de référence. Créez l’environnement avec `python -m venv .venv` (ou votre commande `python3` / `py -3.12`). Activez-le :

| Terminal | Commande |
| --- | --- |
| Bash/Zsh | `source .venv/bin/activate` |
| PowerShell | `.venv\Scripts\Activate.ps1` |
| Invite de commandes Windows | `.venv\Scripts\activate.bat` |

Si l’activation PowerShell est refusée, utilisez directement `.venv\Scripts\python.exe` à la place de `python`.

```bash
python -m pip install -r requirements.txt
```

NumPy et threadpoolctl servent au modèle de caractères ; la recherche et le client documentaire utilisent uniquement la bibliothèque standard. L’installation demande Internet, les entraînements du petit modèle n’en demandent pas.

## Retrouver les sources

```bash
python recherche.py "Une remise en stock à prix égal envoie-t-elle une notification ?" --sortie sorties/recherche.json
python evaluer_recherche.py --lot validation --sortie sorties/recherche-validation.json
python evaluer_recherche.py --lot test --sortie sorties/recherche-test.json
```

Le lot de validation sert à examiner les choix de recherche ; le lot test est ouvert après ces choix. Ce minuscule jeu pédagogique ne permet pas d’estimer les performances générales d’une application.

Un score TF-IDF n’est pas une probabilité de vérité. Le moteur ignore les documents archivés et recherche dans le texte des paragraphes des documents restants. Les titres sont conservés pour la lecture, mais ne participent pas au score. L’index est reconstruit en mémoire à chaque lancement.

## Préparer puis appeler le modèle local

```bash
python assistant_local.py "Quand les données de staging sont-elles réinitialisées ?" --sortie sorties/contexte.json
```

Sans `--appeler`, cette commande ne contacte aucun modèle. Le journal expose les passages et les messages préparés.

Pour la génération, relancez d’abord le serveur local de la partie 3 avec votre modèle vérifié, sur **127.0.0.1:8080**, puis ouvrez un autre terminal dans cet atelier :

```bash
python assistant_local.py "Quand les données de staging sont-elles réinitialisées ?" --appeler --sortie sorties/reponse.json
```

Le client transmet au maximum trois passages et demande jusqu’à 192 tokens de sortie. Les tokens réels, la raison d’arrêt et le texte restent dans le journal. En cas d’erreur du serveur, le contexte est enregistré avec le statut `erreur_generation` et la commande sort avec le code 2. Si aucun passage n’est retrouvé, le modèle n’est pas appelé.

Le contrôle des citations vérifie uniquement leur présence dans la sélection, pas la véracité des phrases qui les accompagnent. Relisez les documents. L’atelier ne promet pas qu’un petit modèle sur CPU répondra correctement en français.

## Examiner les données d’apprentissage

```bash
python auditer_donnees.py
```

Les corpus `base` et `adaptation` contiennent chacun 180 lignes d’entraînement, 30 de validation et 30 de test. Les identifiants de produits/tickets sont répartis avant la création des fenêtres ; les mêmes patrons de phrases restent présents dans les lots. Le jeu étudie donc un apprentissage très étroit de forme. Les journaux synthétiques ne sont pas des preuves d’exécution du service de prix.

## Adapter le modèle fourni

```bash
python petit_modele.py generer --modele resultats-reference/base/modele.npz
python petit_modele.py entrainer --base resultats-reference/base/modele.npz --mode lora --corpus adaptation --pas 800 --rang 4 --sortie sorties/lora
python petit_modele.py generer --modele resultats-reference/base/modele.npz --adaptateur sorties/lora/adaptateur.npz --debut "INFO "
python petit_modele.py entrainer --base resultats-reference/base/modele.npz --mode complet --corpus adaptation --pas 800 --sortie sorties/complet
```

LoRA ajuste uniquement deux petites matrices de la couche de sortie ; tous les tableaux de la base restent identiques. Le fichier `adaptateur.npz` contient ces facteurs et l’empreinte de la base attendue. `modele.npz` conserve également une copie complète pour faciliter les comparaisons. Ne confondez pas leurs tailles.

Le rang choisi vaut quatre et l’échelle multiplicative vaut un. Cette expérience ne reproduit pas toutes les variantes LoRA d’une bibliothèque pour grands modèles.

Évaluez **les deux corpus**, pour observer les régressions :

```bash
python petit_modele.py evaluer --modele sorties/lora/modele.npz --corpus adaptation --sortie sorties/lora-test-adaptation.json
python petit_modele.py evaluer --modele sorties/lora/modele.npz --corpus base --sortie sorties/lora-test-base.json
```

Pour comparer l’adaptation complète, remplacez `sorties/lora/modele.npz` par `sorties/complet/modele.npz` et changez les noms de sorties. Le test est lu uniquement par `evaluer` ; la boucle d’entraînement observe le lot de validation.

## Entraîner depuis zéro

```bash
python petit_modele.py entrainer --pas 1200 --sortie sorties/depuis-zero
python petit_modele.py generer --modele sorties/depuis-zero/modele.npz
python petit_modele.py evaluer --modele sorties/depuis-zero/modele.npz --corpus base --sortie sorties/depuis-zero-test.json
```

Sans `--base`, les paramètres sont initialisés aléatoirement. Le réseau prédit le caractère suivant à partir des douze précédents : embeddings, couche cachée `tanh`, sortie probabiliste. Il ne s’agit pas d’un transformer. Les poids fournis dans `resultats-reference/base` ont été obtenus avec la première commande, la graine 7 et le corpus livré.

Les sorties existantes ne sont pas écrasées : donnez un nouveau nom de fichier ou de dossier pour un nouvel essai.

## Vérifier et poursuivre

```bash
python -m unittest discover -s . -p 'test_atelier.py' -v
```

Les tests couvrent les sources, les limites de la recherche et les gradients du petit modèle comparés à des différences finies. Les résultats réellement obtenus sont dans `resultats-reference`. Les performances et les durées ne sont pas garanties sur une autre machine.

Pour préparer une expérience sur la machine de l’auteur, voir [le document de reprise](experience-gpu/PROMPT-CODEX.md). Il ne nécessite pas un GPU pour refaire les exercices NumPy. L’adaptation d’un LLM sur GPU demeure une expérience distincte, à exécuter et mesurer avant publication de résultats.

Code : GPL-3.0-only. Textes, corpus synthétiques et poids du petit modèle original : CC BY-SA 4.0, © 2026 Hugo Loiseau. Les poids tiers de SmolLM2 ne sont pas inclus dans l’archive.
