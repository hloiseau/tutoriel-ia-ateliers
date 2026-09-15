# 1. Suivre une demande jusqu’à l’outil

[Sommaire de la partie](../README.md) · [Sources](.)

[Suivant : Donner le contexte utile à l’étape en cours](../02-contexte/LECTURE.md)

**TL;DR** — Une demande d’outil, son autorisation et son résultat sont trois étapes distinctes. Nous allons les retrouver dans un journal avant de les chercher dans notre assistant.

## Ouvrir le banc d’essai

Récupérez le dossier [ateliers/05-agents du dépôt](https://github.com/hloiseau/tutoriel-ia-ateliers/tree/main/ateliers/05-agents), ou téléchargez [l’archive de cet atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-agents.zip). Décompressez-la dans un dossier de travail et ouvrez le terminal à côté de `banc.py`.

Le dossier `projet` contient la fonction initiale de suivi de prix et son ticket. Les fichiers de `cas` décrivent les appels que nous allons rejouer. Nous ne toucherons pas à votre correction de la partie 4.

Lancez :

```bash
python banc.py lecture --journal sorties/lecture.jsonl
```

Si nécessaire, remplacez `python` par `python3` ou par la commande qui vous servait déjà. Le programme affiche :

```text
1. lire_fichier : ok
2. lire_fichier : ok
Arrêt : fin_du_script (2 appels)
Journal : sorties/lecture.jsonl
```
Code: Deux demandes de lecture réellement exécutées par le banc

Ouvrez `sorties/lecture.jsonl`. Chaque ligne est un objet JSON : la demande, le résultat et le temps passé dans l’outil y sont conservés. Pour refaire l’essai, donnez un autre nom au journal ; le programme refuse d’écraser un journal existant.

## Qui a fait quoi ?

Ouvrez maintenant `cas/lecture.json`. Sa première demande est :

```json
{"outil": "lire_fichier", "arguments": {"chemin": "TICKET.md"}}
```

Le script choisit ici l’appel. Dans une session d’agent, c’est généralement une réponse du modèle qui demande cet outil avec ces arguments. Le logiciel reçoit la demande, effectue les contrôles nécessaires, puis appelle la fonction. Il renvoie ensuite le résultat au modèle pour poursuivre la conversation[^p5-outils].

![Une demande passe par le contrôle du programme ; elle mène à l’outil ou à un refus, puis le résultat revient à la conversation](../images/boucle.png)
Figure: La demande et son exécution sont deux moments différents

Dans le journal, retrouvez le contenu du ticket sous `resultat.contenu`. C’est cette information qu’un assistant pourrait fournir au modèle au tour suivant. La ligne « je vais lire le ticket » ne suffit pas : elle ne contient ni l’appel ni son résultat.

Notre banc s’arrête à la fin de la liste. Un agent peut, lui, choisir une autre action selon la réponse reçue, poser une question ou terminer. Le journal expose des actions et des résultats ; ce n’est pas un enregistrement de tout son raisonnement interne.

[^p5-outils]: Anthropic, [fonctionnement des appels d’outils](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview). Les noms des messages dépendent de l’API ; la demande et l’exécution restent distinctes.

## Retrouver ces étapes dans l’assistant

Revenez dans votre assistant de développement et ouvrez votre copie `mon-suivi`. Dans une nouvelle session, demandez :

```text
Lis TICKET.md et suivi.py.
Indique si la condition actuelle correspond au ticket.
Appuie ton explication sur la fonction présente dans ce dossier.
Ne modifie aucun fichier et ne lance pas les tests.
```

Dépliez les actions affichées par l’outil. Cherchez quels fichiers ont été lus et à quel moment leur contenu est revenu. Selon l’application, vous verrez les arguments complets, un extrait ou seulement une indication de lecture. Notez ce que l’interface permet réellement de vérifier.

Si l’agent répond sans lecture visible, cela ne prouve pas à lui seul qu’il invente : l’éditeur a pu joindre le fichier au contexte. Regardez les pièces jointes et les informations de session. Si vous ne pouvez pas savoir, gardez cette incertitude dans votre relevé.

Nous allons justement examiner ce que le modèle reçoit, au-delà du texte que nous tapons.



---

[Suivant : Donner le contexte utile à l’étape en cours](../02-contexte/LECTURE.md)
