Un modèle répond dans notre terminal. Très bien. Mais comment passer de cette conversation à une modification dans un vrai projet ?

Il existe des extensions pour les éditeurs, des éditeurs qui intègrent directement l’IA, des assistants en ligne de commande et des agents qui travaillent sur une machine distante. Certains utilisent un abonnement, d’autres une API facturée à l’usage. Certains peuvent parler à notre serveur local. On peut vite passer davantage de temps à choisir son outil qu’à s’en servir. 😅

Nous allons prendre le temps de nous y retrouver, puis installer de quoi travailler. Pour commencer sans carte graphique dédiée, nous utiliserons un assistant dont le modèle est hébergé, avec un accès gratuit si votre compte y est éligible. Nous garderons aussi une expérience facultative avec notre serveur local, pour voir ce que donne une discussion sur quelques lignes de code. Cet essai ne constitue pas un parcours d’agent de code sur CPU.

Nous ouvrirons ensuite un petit projet Python de suivi de prix. Ses tests passent, mais il envoie une notification dans un cas où nous n’en voulons plus. Nous suivrons la modification jusqu’au bout : comprendre le programme, préciser la demande, reproduire le problème, corriger le code et vérifier le résultat.

Si vous débutez, prenez aussi le temps de faire votre propre lecture du code. Une explication très convaincante peut être fausse ; pour s’en apercevoir, il faut pouvoir suivre ce que fait le programme.

**TL;DR**

- Nous choisissons un assistant en regardant ses fonctions, son coût et l’endroit où il traite nos données.
- Le parcours principal utilise VS Code avec GitHub Copilot ; vous pouvez conserver un assistant que vous utilisez déjà.
- L’essai local avec Continue est facultatif. Faire répondre un modèle ne suffit pas à montrer qu’il peut prendre en charge notre atelier.
- Nous commençons par discuter du code, avant de laisser un outil le modifier.
- Le même atelier sert ensuite à apprendre à relire, tester et valider une correction, avec ou sans agent.
