# Données et outils utilisés

## Chiffres manuscrits

E. Alpaydin et C. Kaynak (1998), *Optical Recognition of Handwritten Digits*, UCI Machine Learning Repository : https://doi.org/10.24432/C50P49, sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

La partie 2 utilise les 1 797 images fournies par `sklearn.datasets.load_digits`. Les graphiques de référence en contiennent des visualisations ; certains montrent une version décalée d’un pixel. Les modèles `.npz` de cette partie sont les petits modèles entraînés pendant l’atelier.

## Modèle de langage local

[SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct), HuggingFaceTB, et [sa version GGUF](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct-GGUF), licence déclarée Apache 2.0. Les poids ne sont pas inclus dans ce dépôt. Le fichier `modele.json` contient la révision, la taille et l’empreinte du téléchargement retenu.

[llama.cpp](https://github.com/ggml-org/llama.cpp) sert de moteur d’inférence. Ses exécutables ne sont pas inclus.

Les corpus courts, scénarios, tickets fictifs et scripts d’exercice ont été préparés pour ce tutoriel. Les résultats de référence ne sont pas des données d’entreprise.

## Petit modèle de la partie 7

Les corpus de caractères, les illustrations et les poids originaux de `ateliers/07-ia-maison/resultats-reference` sont créés pour ce tutoriel : © 2026 Hugo Loiseau, CC BY-SA 4.0. Il s’agit des poids du petit réseau NumPy, pas de poids SmolLM2. Le code est sous GPL-3.0-only. Les réponses documentaires enregistrées proviennent d’appels réels au modèle SmolLM2 mentionné plus haut.
