# 3. Installer notre premier assistant

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR** — Préparez une copie du projet, puis choisissez un seul des deux parcours. Avec Copilot, le modèle est hébergé. Avec Continue, nous allons réutiliser notre serveur local, puis essayer un petit modèle de code. Dans les deux cas, la première demande portera sur la lecture d’un extrait.

Nous allons maintenant faire apparaître l’assistant à côté de notre code. Il n’a encore rien à corriger : commençons par vérifier que nous savons ce que nous lui envoyons et d’où vient sa réponse.

## Ouvrir notre copie du projet

Téléchargez [les fichiers de l’atelier de développement](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/b95165289276a45bc299d0826e3c540727e8e203/telechargements/annexes-developpement-v1.zip), puis décompressez l’archive. Vous pouvez aussi les récupérer dans [le dépôt](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/b95165289276a45bc299d0826e3c540727e8e203/ateliers/04-developpement).

Dans `atelier-developpement`, copiez le dossier `01-depart` dans un nouveau dossier nommé `mon-suivi`, **en dehors du dépôt téléchargé**. Gardez les autres dossiers à côté pour plus tard : ils contiennent les étapes de correction.

Installez [Visual Studio Code](https://code.visualstudio.com/download), si vous ne l’avez pas déjà, puis utilisez **Fichier → Ouvrir le dossier** pour ouvrir `mon-suivi`. L’explorateur doit afficher `suivi.py`, les tests et le dossier `scenarios`. Il ne doit pas afficher `02-test-rouge` et `03-corrige` : autant éviter de poser une devinette à l’agent en lui laissant la réponse sous le nez. 🙂

Pour le moment, ouvrez simplement `suivi.py`. Nous lancerons les tests dans le chapitre consacré au projet.

Si vous utilisez déjà Cursor, Codex, Claude Code ou un autre assistant, vous pouvez garder votre outil et ouvrir cette même copie. La demande de lecture en fin de chapitre sera identique.

## Utiliser un service hébergé

Dans ce parcours, nous utilisons **GitHub Copilot dans VS Code**, avec un compte GitHub et l’offre gratuite si votre compte y est éligible. Le modèle tournera chez le fournisseur ; le code ajouté à la conversation lui sera transmis.

Dans la barre d’état de VS Code, ouvrez le menu de l’icône Copilot, choisissez **Use AI Features**, puis suivez la connexion à GitHub. Un compte sans abonnement peut être inscrit à Copilot Free. Le tableau de bord Copilot, accessible depuis la barre d’état, permet de suivre l’usage[^p4-install-copilot].

Ouvrez la vue de discussion. Pour cette première demande, choisissez une session **Copilot** et le rôle **Ask**, qui permet de poser des questions sans modifier le code. Choisissez un modèle disponible dans votre offre, ou **Auto** si cette option est proposée[^p4-install-roles].

Nous ne lançons pas encore de tâche en arrière-plan. Nous voulons une réponse que nous puissions comparer à quelques lignes sous nos yeux.

Si l’interface vous demande de souscrire pour continuer, vérifiez le compte connecté, son éligibilité et le quota restant. Le parcours local reste disponible ; vous n’avez pas besoin de payer pour accéder aux fichiers et faire l’atelier.

Une fois la discussion ouverte, passez à la section « Notre première demande de lecture ». L’installation locale ci-dessous constitue l’autre parcours.

[^p4-install-copilot]: Microsoft, [configuration de Copilot dans VS Code](https://code.visualstudio.com/docs/setup/copilot).
[^p4-install-roles]: Microsoft, [choix de l’agent, du rôle et du modèle](https://code.visualstudio.com/docs/agents/run/agent-harnesses).

## Relier l’éditeur à notre modèle local

Nous allons conserver le serveur de la partie 3 et remplacer notre client Python par **Continue**.

##### Retrouver le serveur

Relancez `llama-server` avec la commande qui fonctionnait sur votre machine dans la partie précédente. Pour cette première connexion, conservez le port `8080`, l’adresse `127.0.0.1`, l’alias `atelier-local` et le contexte de `2048` tokens.

Ouvrez <http://127.0.0.1:8080/health> dans le navigateur. Lorsque le modèle est chargé, ce point d’accès doit indiquer que le serveur est prêt. Vous pouvez également ouvrir <http://127.0.0.1:8080/v1/models> pour retrouver le nom exposé par le serveur[^p4-install-server].

Si rien ne répond, regardez d’abord le terminal du serveur. Installer une extension ne réparera pas un modèle qui n’a pas fini de charger.

##### Ajouter Continue

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

##### Passer à un modèle de code

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

## Notre première demande de lecture

Dans `suivi.py`, repérez la fonction `notifier`. Copiez-la dans la discussion, avec la définition de `Etat` juste au-dessus. Dans Continue, vous pouvez aussi sélectionner le code et utiliser **Ctrl+L**, ou **Cmd+L** sur macOS, pour l’ajouter à la conversation[^p4-install-chat].

Ajoutez cette demande :

> Explique ce que représente un état et dans quels cas cette fonction renvoie vrai. Appuie-toi uniquement sur cet extrait. Ne modifie aucun fichier et ne propose pas encore de correction.

Nous n’attendons pas une réponse mot pour mot. Le code doit permettre de retrouver deux informations : un état contient un prix en centimes et une disponibilité ; la fonction décide de notifier lorsque le produit est disponible et qu’au moins une des deux conditions de la parenthèse est vraie.

Lisez l’explication en gardant le code ouvert. Si le modèle parle d’un envoi de courriel ou d’une base de données, cherchez ce qui lui permet de l’affirmer dans l’extrait. Vous ne trouverez rien : cette fonction renvoie seulement un booléen.

Votre modèle local répond mal en français ? Vous pouvez essayer la même demande en anglais :

> Explain what an Etat represents and when notifier returns True. Use only this snippet. Do not change any files or suggest a fix yet.

L’objectif reste de comprendre la fonction. Si l’explication ne vous aide pas, revenez au code et décomposez la condition vous-même. Nous allons justement le faire dans le chapitre suivant.

##### Et pour les modifications ?

Les deux parcours ne donneront pas exactement la même expérience. Avec un agent, vous pourrez lui demander de préparer les changements puis examiner le diff. Avec notre configuration locale en mode Chat, vous pourrez demander une proposition et l’appliquer vous-même après lecture. Nous n’avons pas configuré ce petit modèle pour piloter le terminal.

Dans les chapitres suivants, une consigne destinée à un agent pourra donc aussi servir à obtenir du code dans la discussion. Vous exécuterez alors vous-même les commandes indiquées et lui montrerez seulement la sortie utile. Le programme et les critères de réussite seront identiques.

Gardez votre dossier `mon-suivi` : nous allons maintenant y lancer les tests et comprendre pourquoi un programme dont les tests passent peut tout de même avoir besoin d’une correction.

[^p4-install-chat]: Continue, [discussion et sélection de code](https://docs.continue.dev/ide-extensions/chat/quick-start).


