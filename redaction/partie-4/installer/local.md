Nous allons conserver le serveur de la partie 3 et remplacer notre client Python par **Continue**.

### Retrouver le serveur

Relancez `llama-server` avec la commande qui fonctionnait sur votre machine dans la partie précédente. Pour cette première connexion, conservez le port `8080`, l’adresse `127.0.0.1`, l’alias `atelier-local` et le contexte de `2048` tokens.

Ouvrez <http://127.0.0.1:8080/health> dans le navigateur. Lorsque le modèle est chargé, ce point d’accès doit indiquer que le serveur est prêt. Vous pouvez également ouvrir <http://127.0.0.1:8080/v1/models> pour retrouver le nom exposé par le serveur[^p4-install-server].

Si rien ne répond, regardez d’abord le terminal du serveur. Installer une extension ne réparera pas un modèle qui n’a pas fini de charger.

### Ajouter Continue

Dans les extensions de VS Code, recherchez **Continue**, ou ouvrez directement [sa page officielle](https://marketplace.visualstudio.com/items?itemName=Continue.continue), puis installez l’extension[^p4-install-continue].

Ouvrez son panneau et choisissez la configuration locale. La roue dentée associée à **Local Config** permet d’ouvrir le fichier YAML. Il se trouve dans `~/.continue/config.yaml` sous Linux et macOS, ou `%USERPROFILE%\.continue\config.yaml` sous Windows[^p4-install-config].

Si vous utilisez déjà Continue, conservez une copie de votre configuration avant cet essai. Pour notre installation, utilisez ce contenu :

```yaml
name: Atelier local
version: 1.0.0
schema: v1

models:
  - name: SmolLM2 - connexion locale
    provider: openai
    model: atelier-local
    apiBase: http://127.0.0.1:8080/v1
    apiKey: local
    roles:
      - chat
    defaultCompletionOptions:
      contextLength: 2048
      maxTokens: 128
      temperature: 0
```
Code: Configuration de Continue pour le serveur de la partie 3

Ici, `provider: openai` indique le format d’API utilisé. **La destination est l’adresse de `apiBase`**, donc notre ordinateur. La valeur `local` est un remplissage pour le champ de clé ; notre serveur d’atelier n’a pas d’authentification configurée. Ce n’est pas une clé de compte OpenAI[^p4-install-compatible].

La longueur de contexte correspond à celle de notre serveur. Nous limitons aussi la réponse à 128 tokens pour ce premier essai. Le rôle `chat` nous suffit ; nous ne déclarons pas de capacité d’utilisation d’outils pour ce modèle[^p4-install-yaml].

Enregistrez, sélectionnez la configuration et le modèle locaux, puis choisissez le mode **Chat**. Envoyez une question très courte, par exemple :

> Reply with the word hello.

Ce n’est pas un test d’intelligence. Nous cherchons une réponse, même imparfaite, et une requête correspondante dans le terminal de `llama-server`. Si une erreur mentionne une clé de service distant, vérifiez le modèle sélectionné et `apiBase`.

Continue propose un réglage **Allow Anonymous Telemetry** dans les paramètres de l’extension : désactivez-le pour cet usage local[^p4-install-offline]. Les réglages réseau de VS Code et des autres extensions restent séparés. Pour vérifier que cette conversation n’a pas besoin d’Internet, vous pouvez couper la connexion après les téléchargements, ouvrir une nouvelle discussion et envoyer une autre question.

### Passer à un modèle de code

La connexion fonctionne ? Nous pouvons changer ce que le serveur charge.

Pour un premier essai sur CPU, prenons **Qwen2.5-Coder-1.5B-Instruct**, dans sa version GGUF `Q4_K_M`. C’est un petit modèle destiné au code, qui reste adapté à des demandes courtes ; nous n’en attendrons pas les capacités d’un gros agent hébergé[^p4-install-qwen].

Dans [le dépôt officiel du modèle](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/tree/main), téléchargez **`qwen2.5-coder-1.5b-instruct-q4_k_m.gguf`**, puis placez-le dans le dossier `modeles` utilisé en partie 3. Ce fichier pèse environ **1,1 Go** ; prévoyez aussi de la mémoire pour le contexte et les programmes ouverts[^p4-install-qwen-fichier].

Arrêtez le serveur précédent avec **Ctrl+C**. Dans sa commande de lancement, remplacez le chemin après `-m` par celui de ce fichier, passez le contexte de `2048` à `4096` et l’alias à `atelier-code`. Gardez les réglages de chargement des bibliothèques qui fonctionnaient déjà sur votre système.

Avec l’arborescence Linux de la partie 3, la commande devient :

```bash
./moteur/llama-server -m modeles/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf --host 127.0.0.1 --port 8080 -c 4096 -t 2 -ngl 0 --device none --parallel 1 --alias atelier-code
```
Code: Lancement du modèle de code sur CPU

Sous Windows ou macOS, reprenez votre chemin d’exécutable de la partie 3 avec ces mêmes changements. Le but est de remplacer le modèle dans une installation qui fonctionne déjà.

Remplacez ensuite la configuration Continue par :

```yaml
name: Atelier code local
version: 1.0.0
schema: v1

models:
  - name: Qwen Coder - CPU
    provider: openai
    model: atelier-code
    apiBase: http://127.0.0.1:8080/v1
    apiKey: local
    roles:
      - chat
    defaultCompletionOptions:
      contextLength: 4096
      maxTokens: 512
      temperature: 0
```
Code: Configuration de discussion avec le modèle de code

Ouvrez une nouvelle conversation après le changement de modèle. Nous allons lui montrer une fonction, pas le dépôt entier.

Si la réponse est lente, commencez par raccourcir la demande et la sortie attendue. Si la machine manque de mémoire, revenez au contexte précédent ou au petit modèle pour finir le diagnostic de connexion. Pour l’atelier, vous pouvez toujours effectuer les modifications vous-même : il n’est pas nécessaire de laisser un modèle en difficulté multiplier les tentatives.

[^p4-install-server]: llama.cpp, [documentation du serveur et des points d’accès HTTP](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).
[^p4-install-continue]: Continue, [installation de l’extension](https://docs.continue.dev/ide-extensions/install).
[^p4-install-config]: Continue, [configuration locale](https://docs.continue.dev/customize/deep-dives/configuration).
[^p4-install-compatible]: Continue, [serveurs compatibles avec l’API OpenAI](https://docs.continue.dev/customize/model-providers/top-level/openai).
[^p4-install-yaml]: Continue, [référence du fichier YAML](https://docs.continue.dev/reference).
[^p4-install-offline]: Continue, [fonctionnement sans Internet](https://docs.continue.dev/guides/running-continue-without-internet).
[^p4-install-qwen]: Qwen, [Qwen2.5-Coder-1.5B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF).
[^p4-install-qwen-fichier]: Qwen, [fichiers GGUF proposés](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/tree/main).
