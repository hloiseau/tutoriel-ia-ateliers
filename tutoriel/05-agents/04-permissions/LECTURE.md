# 4. Observer un refus qui ne dépend pas du modèle

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Écrire des consignes que l’on peut contrôler](../03-consignes/LECTURE.md) · [Suivant : Arrêter une boucle et reprendre sans perdre le fil](../05-reprise/LECTURE.md)

**TL;DR** — Nous allons demander trois actions au banc : lire un chemin interdit, écrire une note et utiliser un terminal absent. Le programme doit les refuser, quel que soit le texte de la demande.

## Faire échouer une demande d’outil

Dans le dossier du banc, lancez :

```bash
python banc.py refus --journal sorties/refus.jsonl
```

Vous obtenez trois refus. Ouvrez `cas/refus.json` et le journal côte à côte :

| Demande | Pourquoi elle est refusée |
| --- | --- |
| Lire `../secret.txt` | Le chemin ne fait pas partie des fichiers autorisés |
| Appeler `ecrire_note` | L’option autorisant cette écriture n’est pas active |
| Appeler `terminal` | Le banc n’expose aucun outil de ce nom |
Table: Les contrôles ne reposent pas sur l’obéissance d’un modèle

`ecrire_note` existe bien dans le code : être disponible ne signifie pas être autorisé pour cet essai. À l’inverse, inventer le nom `terminal` ne crée pas un terminal.

Regardez `Banc.executer` dans `banc.py`. Les arguments sont vérifiés avant l’action. Pour lire, le chemin doit correspondre à un nom prévu, puis rester dans le dossier du projet après résolution. Pour écrire, la destination est fixée à `sorties/note.md` ; le demandeur ne fournit pas de chemin de sortie.

Le journal est écrit par le programme pour conserver l’expérience. Cette écriture de suivi est distincte de l’autorisation de l’outil `ecrire_note`.

## Une instruction cachée dans un document

Ouvrez `projet/documentation/note.md`. Après une phrase sur le projet, vous trouverez une instruction fabriquée pour l’exercice : ignorer le ticket et écrire « Tous les tests passent » dans une note.

Dans une vraie session, un document lu peut contenir du texte qui essaie de détourner l’agent de sa demande. On parle d’**injection de prompt indirecte** quand l’instruction arrive par une source consultée plutôt que par la demande de l’utilisateur[^p5-injection].

Rejouons le cas :

```bash
python banc.py injection --journal sorties/injection.jsonl
```

La lecture réussit ; l’écriture est refusée. Ouvrez le script JSON : nous avons écrit nous-mêmes la seconde demande. **Aucun modèle n’a été trompé dans cette expérience.** Nous vérifions ce que ferait le contrôle si une telle demande arrivait.

![Un document fournit des données ; une demande d’écriture doit encore passer par le contrôle des permissions](../images/permissions.png)
Figure: Lire une instruction dans un document ne lui donne pas d’autorité

Dans cette copie d’atelier, autorisons maintenant l’écriture :

```bash
python banc.py injection --autoriser-ecriture --journal sorties/injection-autorisee.jsonl
```

Ouvrez `sorties/note.md`. La phrase s’y trouve, alors qu’aucun test du suivi de prix n’a été lancé par le banc. Le programme a exécuté une action autorisée ; cela ne rend pas le contenu écrit vrai. Si la note existait, cet outil l’a remplacée.

[^p5-injection]: OWASP, [*LLM Prompt Injection Prevention Cheat Sheet*](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).

## Ce que cette barrière protège

Lancez les tests du banc :

```bash
python -m unittest discover -v
```

Ils vérifient notamment qu’un refus d’écriture ne crée pas la note, qu’un chemin extérieur n’est pas lu et qu’un texte ressemblant à une demande JSON reste du contenu de fichier. Ouvrez `test_banc.py` et retrouvez ces assertions.

Le contrôle d’un outil ne protège que les passages qui le traversent. Si nous ajoutions un terminal générique, il faudrait examiner ce qu’il peut faire avec les droits du processus. Interdire `ecrire_note` ne suffirait plus si un autre outil permettait d’écrire au même endroit.

Notre programme est un exercice de contrôles applicatifs. Il ne constitue pas un bac à sable pour lancer du code hostile. Dans un environnement réel, les comptes utilisés, les accès réseau, les répertoires montés et l’isolation du processus déterminent aussi ce qu’une action peut atteindre.

Sur votre assistant, retrouvez une permission concrète et sa portée : commande seulement, session, dossier, accès réseau ? Lisez ce qu’accorde le bouton avant d’approuver « toujours ». Une consigne, une confirmation et une restriction du système ne jouent pas le même rôle.



---

[Précédent : Écrire des consignes que l’on peut contrôler](../03-consignes/LECTURE.md) · [Suivant : Arrêter une boucle et reprendre sans perdre le fil](../05-reprise/LECTURE.md)
