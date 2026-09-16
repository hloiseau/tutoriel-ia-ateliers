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

Si une erreur mentionne une bibliothèque système manquante, le moteur n’a pas encore démarré et le modèle n’est pas en cause. Les binaires Ubuntu peuvent aussi rencontrer des incompatibilités sur une autre distribution Linux. Suivez alors les [instructions de compilation du projet](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) pour votre système, puis reprenez à `--version`. Télécharger au hasard une bibliothèque isolée ne ferait que masquer le diagnostic.

[^p3-release]: ggml-org, [fichiers de la version b10809](https://github.com/ggml-org/llama.cpp/releases/tag/b10809) et [installation de llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md).
