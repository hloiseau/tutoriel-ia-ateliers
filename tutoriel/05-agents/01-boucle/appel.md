Ouvrez maintenant `cas/lecture.json`. Sa première demande est :

```json
{"outil": "lire_fichier", "arguments": {"chemin": "TICKET.md"}}
```

Dans notre banc, le fichier JSON choisit l’appel. Dans une session d’agent, la demande vient généralement d’une réponse du modèle. Le logiciel reçoit le nom de l’outil et ses arguments, applique ses contrôles, puis exécute la fonction ou renvoie un refus. Le résultat rejoint ensuite la conversation et le modèle peut choisir l’étape suivante[^p5-outils].

![Une demande passe par le contrôle du programme ; elle mène à l’outil ou à un refus, puis le résultat revient à la conversation](image:images/boucle.png)
Figure: La demande et son exécution sont deux moments différents

Dans le journal, retrouvez le contenu du ticket sous `resultat.contenu`. Voilà l’information qu’un assistant pourrait fournir au modèle au tour suivant. Une phrase comme « je vais lire le ticket » annonce seulement une intention ; le journal permet de vérifier l’appel et son résultat.

Le banc s’arrête à la fin de la liste préparée. Un agent réel peut demander une autre action selon le résultat reçu, poser une question ou terminer. Son journal expose les actions et leurs résultats, sans nous livrer pour autant tout le raisonnement interne du modèle.

[^p5-outils]: Anthropic, [fonctionnement des appels d’outils](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview). Les noms des messages dépendent de l’API ; la demande et l’exécution restent distinctes.
