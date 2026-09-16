# 4. Observer un refus qui ne dépend pas du modèle

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Écrire des consignes que l’on peut contrôler](../03-consignes/LECTURE.md) · [Suivant : Arrêter une boucle et reprendre sans perdre le fil](../05-reprise/LECTURE.md)

**TL;DR** — Nous allons demander trois actions au banc : lire un chemin interdit, écrire une note et utiliser un terminal absent. Les refus viendront du programme, indépendamment de la formulation de la demande.

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

Trois contrôles différents apparaissent. Le chemin sort de la liste autorisée ; `ecrire_note` existe mais son option d’autorisation manque ; `terminal`, lui, n’existe tout simplement pas dans le banc. Même une demande formulée avec beaucoup d’assurance ne fera pas surgir ce dernier par magie. 🙂

Regardez `Banc.executer` dans `banc.py`. Les arguments sont vérifiés avant l’action. Pour lire, le chemin doit correspondre à un nom prévu, puis rester dans le dossier du projet après résolution. Pour écrire, la destination est fixée à `sorties/note.md` : le demandeur choisit le texte, jamais le chemin de sortie.

Vous voyez pourtant un nouveau journal sur le disque. C’est le programme principal qui l’écrit pour conserver l’expérience ; l’autorisation testée concerne uniquement l’outil `ecrire_note`.

## Une instruction cachée dans un document

Ouvrez `projet/documentation/note.md`. Après une phrase sur le projet, le document ordonne d’ignorer le ticket et d’écrire « Tous les tests passent » dans une note. Cette instruction a été fabriquée pour l’exercice.

Dans une vraie session, un document lu peut contenir du texte qui essaie de détourner l’agent de sa demande. On parle d’**injection de prompt indirecte** quand l’instruction arrive par une source consultée plutôt que par la demande de l’utilisateur[^p5-injection].

Rejouons le cas :

```bash
python banc.py injection --journal sorties/injection.jsonl
```

La lecture réussit ; l’écriture est refusée. Ouvrez maintenant `cas/injection.json` : la seconde demande s’y trouvait déjà, écrite à la main. Le banc n’a ni compris le document ni décidé de lui obéir. Il nous montre seulement comment le contrôle réagit lorsqu’il reçoit cette demande d’écriture.

![Un document fournit des données ; une demande d’écriture doit encore passer par le contrôle des permissions](../images/permissions.png)
Figure: Lire une instruction dans un document ne lui donne pas d’autorité

Dans cette copie d’atelier, autorisons maintenant l’écriture :

```bash
python banc.py injection --autoriser-ecriture --journal sorties/injection-autorisee.jsonl
```

Ouvrez `sorties/note.md`. La phrase s’y trouve, alors que le banc n’a lancé aucun test du suivi de prix. L’autorisation porte sur l’écriture du fichier, pas sur la vérité de la phrase. Si une note existait déjà, l’outil l’a remplacée.

[^p5-injection]: OWASP, [*LLM Prompt Injection Prevention Cheat Sheet*](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).

## Ce que cette barrière protège

Lancez les tests du banc :

```bash
python -m unittest discover -v
```

Ils vérifient notamment qu’un refus d’écriture ne crée pas la note, qu’un chemin extérieur n’est pas lu et qu’un texte ressemblant à une demande JSON reste du contenu de fichier. Ouvrez `test_banc.py` et retrouvez ces assertions.

Chaque contrôle protège le passage prévu. Si nous ajoutions un terminal générique, il faudrait examiner tout ce qu’il peut faire avec les droits du processus. Il pourrait peut-être écrire au même endroit et contourner ainsi la restriction placée sur `ecrire_note`.

Notre programme illustre des contrôles applicatifs ; il n’isole pas du code hostile. Dans un environnement réel, les comptes utilisés, les accès réseau, les répertoires montés et l’isolation du processus déterminent aussi ce qu’une action peut atteindre.

Sur votre assistant, retrouvez une permission concrète et sa portée : commande seulement, session, dossier, accès réseau ? Lisez ce qu’accorde le bouton avant d’approuver « toujours ». Une consigne guide le modèle, une confirmation vous rend la décision, une restriction du système bloque l’action ; ce sont trois protections différentes.

Nous avons fait refuser une lecture, une écriture et un outil absent sans demander au modèle de « bien se comporter ». Reste à gérer un cas moins spectaculaire, mais très courant : l’action autorisée qui tourne en rond ou échoue à mi-chemin.

---

[Précédent : Écrire des consignes que l’on peut contrôler](../03-consignes/LECTURE.md) · [Suivant : Arrêter une boucle et reprendre sans perdre le fil](../05-reprise/LECTURE.md)
