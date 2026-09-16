# 1. Choisir ce que l’on va télécharger

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** il nous faut des poids, un logiciel capable de les lire et une tâche raisonnable. La fiche du modèle nous renseignera sur ses langues, sa licence et ses limites.

Avant de cliquer sur un fichier de plusieurs gigaoctets, faisons connaissance avec les trois pièces de notre installation.

## Le modèle, le moteur et notre programme

Dans la partie précédente, notre programme chargeait les nombres appris pendant l’entraînement. Nous allons retrouver ce principe à une autre échelle : le modèle possède beaucoup plus de paramètres et une architecture différente, tandis que ses poids restent des données à charger.

Le **moteur d’inférence** réalise les calculs nécessaires à la production d’une réponse. Nous utiliserons llama.cpp. Notre **client** sera un petit script Python qui envoie des messages à ce moteur, lancé sous forme de serveur.

![Un client Python interroge un serveur local qui charge les poids depuis le disque](../images/installation.png)
Figure: Les éléments de notre installation

Pourquoi passer par un serveur alors que tout tient sur le même ordinateur ? Parce qu’il garde le modèle chargé pendant que différents clients lui demandent des calculs. Notre script, une interface web ou un autre programme pourront ainsi l’interroger. Ici, « serveur » désigne le rôle du processus lancé sur notre machine.

Pour le moment, le modèle recevra du texte et produira du texte. Lancer des commandes ou modifier des fichiers demandera plus tard un programme capable d’organiser et de contrôler ces actions autour de lui.

## Lire la fiche avant le nom du fichier

Pour cet atelier, prenons **SmolLM2-360M-Instruct**, dans sa version GGUF Q8_0 publiée dans l’espace HuggingFaceTB. Il compte environ 360 millions de paramètres. Sa fiche le présente comme un modèle principalement anglophone et déclare une licence Apache 2.0.[^p3-smol]

Le fichier fait environ **386 Mo**, une taille raisonnable pour prendre en main l’inférence locale. La fiche annonce toutefois un modèle principalement anglophone. Quant au travail de développement, nos cinq courtes questions ne permettront pas de juger s’il sait lire un projet, utiliser des outils et tenir une session entière.

Si vous voulez essayer un autre modèle, sa fiche vous aidera à voir s’il correspond à votre usage : les langues qu’il traite, ce que sa licence permet et les limites signalées par ses auteurs.

Le suffixe **Instruct** indique une adaptation destinée à suivre des instructions. **GGUF** désigne le format de fichier utilisé ici. **Q8_0** désigne une forme de quantification : les nombres sont stockés avec une précision réduite selon ce format. Nous en observerons les conséquences sur le volume des paramètres au chapitre 4.

[^p3-smol]: HuggingFaceTB, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct) et [version GGUF](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct-GGUF). Taille et empreinte du fichier relevées le 14 septembre 2026 ; révision conservée dans `modele.json`.

## De quoi votre ordinateur a-t-il besoin ?

L’atelier utilise Python 3.12 et sa bibliothèque standard. Si vous avez suivi la partie précédente, conservez votre installation : nous n’ajouterons ni NumPy ni dépendance vers une API payante.

[Téléchargez les fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/b95165289276a45bc299d0826e3c540727e8e203/telechargements/annexes-modele-local-v1.zip), décompressez l’archive, puis ouvrez un terminal dans le dossier `atelier-local`.

Dans les commandes, `python` désigne votre Python 3.12. Selon votre installation, écrivez `python3` sous Linux ou macOS, ou `py -3.12` sous Windows. Vérifiez-le avant de poursuivre :

```bash
python --version
python inventaire.py
```
Code: Identifier l’environnement utilisé

Le second programme enregistre les informations dans `resultats/machine.json`. Il relève notamment le système, l’architecture et le nombre de processeurs logiques. S’il trouve `nvidia-smi`, il lui demande aussi le nom de la carte NVIDIA et sa mémoire. Le parcours sur CPU continue normalement lorsque cette commande est absente.

Gardez au moins quelques gigaoctets libres sur le disque pour le moteur, le modèle et les résultats. Pour la RAM, vérifiez la mémoire **disponible**, pas seulement la quantité installée : les autres applications en occupent déjà une partie. Le fichier du modèle approche 386 Mo, mais le programme aura besoin de mémoire supplémentaire.

Notre premier réglage utilisera deux fils CPU et un contexte limité à 2 048 tokens. Si la machine manque de mémoire ou devient peu réactive, arrêtez le serveur avant de modifier ses paramètres. Faire tourner un petit modèle lentement est suffisant pour comprendre la manipulation ; planter tout le bureau n’apporte pas grand-chose. 😅


