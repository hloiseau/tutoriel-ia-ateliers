Ouvrez maintenant `cas/lecture.json`. Sa première demande est :

```json
{"outil": "lire_fichier", "arguments": {"chemin": "TICKET.md"}}
```

Le script choisit ici l’appel. Dans une session d’agent, c’est généralement une réponse du modèle qui demande cet outil avec ces arguments. Le logiciel reçoit la demande, effectue les contrôles nécessaires, puis appelle la fonction. Il renvoie ensuite le résultat au modèle pour poursuivre la conversation[^p5-outils].

![Une demande passe par le contrôle du programme ; elle mène à l’outil ou à un refus, puis le résultat revient à la conversation](image:images/boucle.png)
Figure: La demande et son exécution sont deux moments différents

Dans le journal, retrouvez le contenu du ticket sous `resultat.contenu`. C’est cette information qu’un assistant pourrait fournir au modèle au tour suivant. La ligne « je vais lire le ticket » ne suffit pas : elle ne contient ni l’appel ni son résultat.

Notre banc s’arrête à la fin de la liste. Un agent peut, lui, choisir une autre action selon la réponse reçue, poser une question ou terminer. Le journal expose des actions et des résultats ; ce n’est pas un enregistrement de tout son raisonnement interne.

[^p5-outils]: Anthropic, [fonctionnement des appels d’outils](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview). Les noms des messages dépendent de l’API ; la demande et l’exécution restent distinctes.
