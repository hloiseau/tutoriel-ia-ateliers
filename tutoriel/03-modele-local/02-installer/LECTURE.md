# 2. Installer le moteur et lancer le modèle

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** téléchargez le binaire correspondant à votre système, conservez ses bibliothèques, puis chargez le fichier GGUF. Le premier terminal restera occupé par le serveur.

## Choisir la bonne archive de llama.cpp

Ouvrez la [version b10809 de llama.cpp](https://github.com/ggml-org/llama.cpp/releases/tag/b10809). Nous fixons cette version pour pouvoir retrouver les mêmes fichiers. Les versions suivantes pourront changer leurs noms ou leurs options.[^p3-release]

Dans les fichiers proposés, choisissez celui correspondant à votre machine :

| Machine | Archive pour commencer sur CPU |
| --- | --- |
| Windows, processeur Intel ou AMD 64 bits | `llama-b10809-bin-win-cpu-x64.zip` |
| Windows sur ARM 64 bits | `llama-b10809-bin-win-cpu-arm64.zip` |
| Ubuntu sur Intel ou AMD 64 bits | `llama-b10809-bin-ubuntu-x64.tar.gz` |
| Ubuntu sur ARM 64 bits | `llama-b10809-bin-ubuntu-arm64.tar.gz` |
| Mac avec puce Apple | `llama-b10809-bin-macos-arm64.tar.gz` |
| Mac Intel | `llama-b10809-bin-macos-x64.tar.gz` |
Table: Archives présentes dans la version retenue

Décompressez l’archive dans un dossier `moteur`, à côté des scripts Python. Cherchez `llama-server`, ou `llama-server.exe` sous Windows. Selon l’archive, il peut se trouver dans un sous-dossier : gardez ce chemin pour la suite. **Conservez les bibliothèques livrées avec lui**, au lieu de déplacer seulement l’exécutable.

Sous Linux, rendez les bibliothèques de ce dossier accessibles au programme dans le terminal courant :

```bash
export LD_LIBRARY_PATH="$PWD/moteur${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
```

Adaptez `moteur` au dossier qui contient réellement les fichiers `.so`. Conservez ensuite ce terminal pour lancer le serveur. Cette commande n’installe rien dans les dossiers du système.

Sous Linux ou macOS, vérifiez la version avec le chemin trouvé :

```bash
./moteur/llama-server --version
```

Sous Windows, dans PowerShell :

```powershell
.\moteur\llama-server.exe --version
```

Si l’exécutable est dans `moteur/bin`, ajoutez simplement `bin` au chemin. Les commandes suivantes supposent qu’il est directement dans `moteur`.

Une erreur qui mentionne une bibliothèque système manquante n’est pas une erreur du modèle : le moteur n’a même pas encore pu démarrer. En particulier, un binaire Ubuntu ne garantit pas la compatibilité avec toutes les distributions Linux. Dans ce cas, utilisez les [instructions de compilation du projet](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) pour votre système, puis reprenez à `--version`. Évitez de récupérer au hasard une bibliothèque isolée pour faire disparaître le message.

[^p3-release]: ggml-org, [fichiers de la version b10809](https://github.com/ggml-org/llama.cpp/releases/tag/b10809) et [installation de llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md).

## Télécharger les poids et retrouver le même fichier

Toujours dans `atelier-local`, lancez :

```bash
python telecharger.py
```

Le programme lit `modele.json`, télécharge le fichier retenu dans `modeles/` et vérifie sa taille ainsi que son empreinte SHA-256. Le téléchargement est lié à une révision précise du dépôt ; un futur changement de sa branche principale ne changera pas silencieusement notre fichier.

Pendant le transfert, le fichier porte une extension `.part`. Il ne prend son nom définitif qu’après vérification. Si la connexion coupe, relancez la commande : ce petit script recommence le transfert, il ne sait pas le reprendre au milieu.

Vous pouvez ouvrir `modele.json`. Les informations servent à répondre à une question très pratique : « Avons-nous réellement testé le même fichier ? » Deux fichiers nommés de façon proche ne sont pas forcément identiques.

L’empreinte permet de détecter un fichier différent de celui attendu. Elle ne prouve pas que son auteur est digne de confiance ni que les données d’entraînement ont toutes été obtenues dans de bonnes conditions. Ce sont deux vérifications différentes.

## Le premier démarrage

Lancez cette commande sur une seule ligne, en adaptant le chemin du moteur :

```bash
./moteur/llama-server -m modeles/smollm2-360m-instruct-q8_0.gguf --host 127.0.0.1 --port 8080 -c 2048 -t 2 -ngl 0 --device none --parallel 1 --alias atelier-local --cors-origins http://127.0.0.1:8080
```
Code: Démarrer le serveur sur CPU sous Linux ou macOS

Sous Windows, la commande devient :

```powershell
.\moteur\llama-server.exe -m modeles/smollm2-360m-instruct-q8_0.gguf --host 127.0.0.1 --port 8080 -c 2048 -t 2 -ngl 0 --device none --parallel 1 --alias atelier-local --cors-origins http://127.0.0.1:8080
```

Le chemin après `-m` désigne les poids. Nous demandons un contexte de 2 048 tokens, deux fils CPU, aucune couche sur le GPU et une seule requête traitée à la fois. L’alias `atelier-local` sera le nom utilisé par notre client.[^p3-serveur]

Des messages apparaissent dans le terminal. Laissez-le ouvert : tant que le serveur fonctionne, il occupe ce terminal. Attendez la fin du chargement, puis ouvrez `http://127.0.0.1:8080/health` dans votre navigateur. Une réponse indiquant un état `ok` signifie que le serveur est prêt. Pendant le chargement, il peut encore répondre qu’il n’est pas disponible.

L’adresse `127.0.0.1` désigne cette machine. Nous n’ouvrons pas le service aux autres ordinateurs du réseau. L’option `--cors-origins` limite également les origines autorisées pour les appels depuis un navigateur à celle de notre service local. Pour arrêter le serveur, revenez dans son terminal et appuyez sur `Ctrl+C`.

[^p3-serveur]: ggml-org, [documentation du serveur llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md), options de lancement et route `/health`.

## Quand le serveur ne démarre pas

Avant de changer cinq options, regardez le premier message d’erreur utile.

| Ce que vous observez | Ce qu’il faut vérifier |
| --- | --- |
| Le terminal ne trouve pas `llama-server` | Le chemin de l’exécutable ; sous PowerShell, le préfixe `.\` pour un programme dans le dossier courant |
| Linux signale `libllama-server-impl.so` introuvable | La variable `LD_LIBRARY_PATH` doit désigner le dossier des bibliothèques dans le terminal où vous lancez le moteur |
| Le moteur ne trouve pas le modèle | Le dossier depuis lequel vous lancez la commande et la présence du fichier dans `modeles/` |
| Le port est déjà utilisé | Un premier serveur fonctionne peut-être encore ; arrêtez votre ancien processus avant de relancer |
| Le navigateur ne reçoit rien | Le processus est-il toujours vivant ? L’adresse et le port correspondent-ils à la commande ? |
| Le processus est arrêté pendant le chargement | Les derniers messages du moteur et la mémoire disponible ; vérifiez aussi que l’empreinte du fichier est correcte |
| Une option est inconnue | La version affichée et l’aide de **votre** exécutable avec `--help` |
Table: Quelques points de contrôle avant de réinstaller tout l’atelier

Si vous changez le port, il faudra aussi changer `BASE` dans `client.py`. Pour le premier essai, conserver `8080` évite cette manipulation supplémentaire.

Ne lancez pas le programme en administrateur pour essayer de corriger une erreur de chemin ou un manque de mémoire. Cela ne règle aucun de ces deux problèmes.

Sous Linux x86-64, si le moteur signale `no backends are loaded` alors que les bibliothèques sont présentes, vous pouvez lui indiquer explicitement la variante CPU générique fournie dans l’archive :

```bash
export GGML_BACKEND_PATH="$PWD/moteur/libggml-cpu-x64.so"
```

Adaptez là aussi le dossier. Ce réglage vise l’archive Linux x86-64 ; ne recopiez pas ce nom sur une autre architecture. Il force une variante générique, qui peut être moins rapide que celle sélectionnée automatiquement pour votre processeur. Notez-le dans les paramètres de l’expérience si vous l’utilisez.


