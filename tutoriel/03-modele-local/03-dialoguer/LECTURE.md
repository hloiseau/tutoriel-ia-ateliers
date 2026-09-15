# 3. Envoyer une question et conserver la réponse

[Sommaire de la partie](../README.md) · [Sources](.)

**TL;DR :** notre client envoie une liste de messages et enregistre la réponse complète. Les questions restent courtes pour que nous puissions comprendre chaque essai.

Le serveur tourne ? Ouvrez un deuxième terminal dans `atelier-local`. Le premier continue son travail.

## Notre première requête

Ouvrez `questions/premiere.json`. Vous y trouverez deux messages :

```json
[
  {"role": "system", "content": "Answer briefly in English."},
  {"role": "user", "content": "Explain what a variable is in programming, in two sentences."}
]
```
Code: Les messages envoyés au modèle

Le premier donne une consigne générale ; le second contient notre question. Nous commençons en anglais parce que c’est la langue principale du modèle retenu.

Lancez :

```bash
python client.py
```

Le client affiche le texte reçu et écrit `resultats/reponse.json`. Ouvrez ce fichier. Il contient la demande, la réponse brute et le temps écoulé autour de l’appel. Vous pourrez ainsi retrouver autre chose qu’une phrase recopiée de mémoire.

Lisez la réponse. Respecte-t-elle les deux phrases demandées ? Son explication d’une variable est-elle correcte ? Ces deux questions ne mesurent pas la même chose : un texte peut respecter la forme tout en racontant n’importe quoi.

Si le client finit par signaler un délai dépassé, regardez le terminal du serveur avant de recommencer. Une expiration côté client n’implique pas forcément que le calcul côté serveur s’est arrêté.

## Ce que fait le client

Le cœur de `client.py` envoie du JSON à `http://127.0.0.1:8080/v1/chat/completions`. Le client utilise la bibliothèque standard de Python. Il n’a pas besoin d’un compte chez un fournisseur pour parler à notre serveur.

Nous fixons trois choix : une température à zéro, une sortie limitée à 96 tokens et une réponse reçue en une seule fois. La température à zéro rend la sélection plus déterministe, mais ne transforme pas une réponse en vérité. Des différences de moteur ou de calcul peuvent aussi produire des différences entre exécutions.

Regardez `raison_arret` dans le fichier enregistré. Si elle vaut `length`, la limite de sortie a été atteinte. Une phrase interrompue n’est pas forcément un refus de répondre : nous avons peut-être simplement coupé le robinet trop tôt.

La limite compte des **tokens**, pas des mots. Le modèle possède son propre découpage du texte. Un mot peut occuper plusieurs tokens, et les messages comportent aussi des éléments de mise en forme utilisés par le modèle.

Pour allonger la réponse, vous pouvez modifier la valeur par défaut `max_tokens=96` dans `client.py`, par exemple en `128`. Gardez la même valeur entre deux mesures que vous voulez comparer.

## Une réponse présente, une réponse absente

Essayons maintenant une question dont nous connaissons la réponse, sans dépendre des souvenirs du modèle :

```bash
python client.py --fichier questions/document.json --sortie resultats/document.json
python client.py --fichier questions/inconnue.json --sortie resultats/inconnue.json
```

Les deux fichiers parlent d’une bibliothèque fictive. Le document indique qu’elle ouvre le mardi à 10 heures et ferme à 17 heures. Le premier demande l’heure d’ouverture du mardi. Le second demande celle du dimanche, qui n’est pas fournie.

Pour le mardi, nous attendons **10 heures**. Pour le dimanche, nous attendons que le modèle dise qu’il ne sait pas. La consigne lui demande explicitement de se limiter au document.

S’il invente un horaire du dimanche, ne complétez pas le document pour rendre sa réponse vraie. Conservez l’erreur. Nous cherchons justement à voir s’il respecte une limite d’information.

Vous venez de construire deux petits cas d’évaluation : une réponse accessible et une information absente. Ce n’est pas encore une évaluation générale du modèle, mais c’est déjà beaucoup plus précis que « j’ai discuté dix minutes, ça avait l’air bien ».

## Pourquoi le modèle ne se souvient pas du premier essai

Modifiez maintenant une question pour demander : « Quelle était ma question précédente ? » Lancez-la dans un nouveau fichier de messages.

Notre client n’ajoute aucun historique automatiquement. Le serveur reçoit uniquement les messages présents dans ce fichier. Il ne suffit donc pas que nous ayons parlé au même processus quelques secondes plus tôt pour que la nouvelle demande contienne l’ancienne conversation.

![Deux requêtes indépendantes ; la seconde n’inclut un historique que si le client le transmet](../images/historique.png)
Figure: L’historique est constitué par le programme qui prépare la demande

Pour poursuivre réellement l’échange, il faut envoyer les messages précédents et la nouvelle question. Les interfaces de discussion s’en chargent généralement pour nous, avec leurs propres choix de conservation, de résumé ou de suppression.

Il faut aussi distinguer cet historique d’un **cache de calcul**. Un moteur peut réutiliser des calculs pour accélérer le traitement d’un texte déjà rencontré. Cela ne lui donne pas une autorisation d’inventer des messages absents de la requête, ni une mémoire personnelle permanente.

Plus nous ajoutons de texte, plus il faut de place pour le traiter. Et ce texte peut contenir des instructions anciennes, des détails devenus inutiles ou des contradictions. Donner toutes ses archives au modèle n’est donc pas toujours une bonne façon de l’aider.


