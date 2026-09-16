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

Les droits d’administrateur ne corrigent ni un chemin erroné ni un manque de mémoire. Gardez les permissions normales et revenez au premier message utile.

Sous Linux x86-64, si le moteur signale `no backends are loaded` alors que les bibliothèques sont présentes, vous pouvez lui indiquer explicitement la variante CPU générique fournie dans l’archive :

```bash
export GGML_BACKEND_PATH="$PWD/moteur/libggml-cpu-x64.so"
```

Adaptez là aussi le dossier. Ce réglage vise l’archive Linux x86-64 ; ne recopiez pas ce nom sur une autre architecture. Il force une variante générique, qui peut être moins rapide que celle sélectionnée automatiquement pour votre processeur. Notez-le dans les paramètres de l’expérience si vous l’utilisez.
