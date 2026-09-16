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

Des messages apparaissent dans le terminal. Laissez-le ouvert : le serveur y restera jusqu’à son arrêt. Attendez la fin du chargement, puis ouvrez `http://127.0.0.1:8080/health` dans votre navigateur. Tant que le modèle se charge, la route peut signaler qu’il est indisponible ; l’état `ok` annonce que nous pouvons envoyer notre première question.

L’adresse `127.0.0.1` désigne cette machine. Nous n’ouvrons pas le service aux autres ordinateurs du réseau. L’option `--cors-origins` limite également les origines autorisées pour les appels depuis un navigateur à celle de notre service local. Pour arrêter le serveur, revenez dans son terminal et appuyez sur `Ctrl+C`.

[^p3-serveur]: ggml-org, [documentation du serveur llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md), options de lancement et route `/health`.
