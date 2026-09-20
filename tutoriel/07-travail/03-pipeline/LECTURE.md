# 3. Refaire le travail avec un pipeline

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Faire travailler un assistant sur le dossier](../02-assistant/LECTURE.md) · [Suivant : Donner accès aux bons outils](../04-acces/LECTURE.md)

**TL;DR** — Transformons les messages en données régulières, puis essayons une chaîne locale qui contrôle ces données et prépare le point. Une extraction fictive permet de faire toute la manipulation sans appeler de modèle.

Vendredi prochain, les fichiers auront changé, mais nous demanderons encore de relever les messages, de retrouver les nouveautés et de préparer un compte rendu. Un pipeline permet de conserver cet enchaînement. L’application fournie ici travaille sur le lot `quartier-01` et ses quatre messages distincts : elle nous servira à observer les contrôles, l’approbation et le rejeu. Pour recevoir d’autres lots, il faudra adapter ses sources et ses règles.

Pour l’essayer, ouvrez le dossier décompressé de l’atelier. Nous utiliserons `pipeline/index.html` dans votre navigateur. Aucun terminal, compte ou serveur n’est nécessaire. L’application reçoit une extraction par copier-coller ; les messages ne partent vers aucun service depuis cette page.

## Relier les étapes de traitement

La première opération sera de relever les faits dans les messages. Ensuite, le programme contrôlera le format et les références, rapprochera les identifiants du suivi, puis préparera un point que nous pourrons relire. Nous gardons un arrêt avant l’approbation et l’export. L’ordre est fixé par l’application.

![Les documents servent à une extraction ; ses données passent des contrôles avant la proposition, la relecture, l’approbation et l’export. Une erreur de format arrête le traitement.](../images/pipeline.png)
Figure: Les étapes de notre pipeline pour le dossier quartier-01

Dans la tâche du chapitre précédent, un agent pouvait décider quel fichier ouvrir ensuite. Ici, nous choisissons les étapes et leurs conditions de passage. Un pipeline peut contenir un appel de modèle, voire une tâche confiée à un agent, sans lui abandonner la décision sur tout l’enchaînement. On peut par exemple laisser le modèle extraire une demande puis faire compter les identifiants par un programme ordinaire.

Il nous faut donc un format que les étapes suivantes savent lire. Un paragraphe « Nora voudrait venir avec quelqu’un » demande encore une interprétation. Avec des champs nommés, nous pouvons transmettre le type de demande, l’atelier et le nombre de places séparément. Nous utiliserons **JSON**, un format de données en texte brut. Les accolades regroupent les champs d’un objet, les crochets une liste. Les chaînes de texte sont entre guillemets ; `null` marque ici une valeur absente ou encore indécise.

Voici l’objet attendu pour Léo, rédigé pour l’exercice :

```json
{
  "id": "M002",
  "type": "inscription",
  "atelier": null,
  "places": 2,
  "source": "courriels/02-leo.txt",
  "extrait": "Je voudrais m’inscrire avec un ami : une place pour lui et une pour moi."
}
```

Le chemin `source` part du dossier `entrees/`. L’extrait permet de revenir à la formulation reçue. Les deux places ont une justification ; le choix de l’atelier reste absent. Pour Nora, la question sur Cartographie sera un objet distinct de sa demande d’inscription et conservera `places: null`.

Ouvrez `consignes/extraction.md`. Cette consigne demande l’ensemble du lot dans ce format : quatre messages distincts, une seule occurrence de `M001`, et `M004` présent pour que l’application reconnaisse la demande déjà connue. Elle demande aussi les alertes sur les deux dates et l’horaire manquant.

Si vous avez utilisé un assistant, transmettez cette seconde consigne dans une nouvelle tâche avec les mêmes entrées et les règles. Récupérez le JSON proposé, sans les éventuelles phrases autour ni les délimiteurs d’un bloc de code. Gardez la réponse brute avant de la corriger. Choisissez `origine: "assistant"` pour cette proposition ; utilisez `"manuel"` si vous constituez vous-même l’extraction. Le mode de démonstration porte `"exemple_fictif"`. Cette étiquette nous évitera de prendre un exemple fourni pour une mesure de la qualité d’un modèle.

## Essayer les contrôles dans le navigateur

Ouvrez maintenant `pipeline/index.html` en double-cliquant dessus. L’adresse commence normalement par `file://` : vous lisez une page enregistrée sur votre machine. Dans la zone **Extraction JSON**, collez votre extraction, ou cliquez sur **Charger l’exemple fictif** pour utiliser les données de démonstration.

Cliquez sur **Contrôler et préparer**. Avec l’exemple fourni, la page doit proposer un point et faire apparaître le déroulement dans **Journal**. Retrouvez-y `M004`, déjà connu, puis les trois messages nouveaux `M001`, `M002` et `M005`. Nous avons trois messages à traiter, dont deux demandes d’inscription : additionner ces deux catégories aurait vite fabriqué une drôle de liste d’invités.

Lisez le **Point proposé**. La copie de Nora doit être signalée ; Léo garde ses deux places et son atelier non précisé ; la question sur Cartographie reste ouverte. Les demandes ne deviennent pas des confirmations. Pour l’instant, nous nous arrêtons à cette proposition. Les étapes d’approbation et de reprise auront leurs propres manipulations.

Pour ce dossier, le générateur ajoute des rappels déjà connus sur les dates, l’horaire, la copie de Nora et l’atelier manquant de Léo. Leur présence dans le point ne prouve donc pas que l’assistant les a retrouvés. Pour examiner son travail, gardez son extraction brute sous les yeux ; le point permet ensuite de juger l’ensemble du traitement.

Faisons échouer le contrôle exprès. Dans l’extraction, trouvez le champ `places` de Léo et remplacez le nombre `2` par le texte `"deux"`, guillemets compris. Relancez **Contrôler et préparer**. Le programme attend un entier positif ou `null` ; il doit refuser ce texte et indiquer le défaut. Rétablissez `2` et relancez. Le sens de « deux » était évident pour nous, mais l’étape qui reçoit ces données n’accepte qu’une représentation précise.

Essayez ensuite de remplacer l’extrait de Léo par `"Je choisis Reliure."`. Le contrôle doit refuser cette citation, car elle ne figure pas dans le fichier associé à `M002`. Remettez l’extrait initial. La vérification rapproche ici un passage exact d’un fichier connu ; elle repère une citation fabriquée ou attribuée au mauvais message.

Dernier essai, plus intéressant : changez seulement `"atelier": null` en `"atelier": "Reliure"` pour Léo, en gardant son vrai extrait. Relancez. Cette extraction peut passer les contrôles de structure et de provenance : Reliure est un nom d’atelier autorisé, et la citation existe. Pourtant, le fait est faux. Le programme ne déduit pas le sens complet du message pour prouver chacun des champs. Remettez `null` avant de poursuivre, puis regardez ce que cet incident nous apprend sur la relecture.

Nous pouvons vérifier automatiquement qu’une quantité a le bon type, qu’un identifiant n’apparaît qu’une fois ou qu’un extrait appartient au fichier annoncé. Vérifier que cet extrait justifie vraiment la proposition demande une lecture supplémentaire. Un indicateur vert ne nous dispense donc pas d’ouvrir le message de Léo.

Les champs globaux `date_evenement` et `horaire_cartographie` ont une règle plus stricte dans cet exercice : ils doivent rester à `null` tant que le lot n’est pas arbitré. Essayez une date si vous voulez voir le refus, puis retirez-la. Cette règle exprime ce que nous savons de ce dossier. Pour réutiliser le pipeline sur un autre événement, il faudra définir où se trouvent les décisions approuvées et comment les reconnaître ; conserver indéfiniment ces deux champs vides empêcherait aussi de travailler.

Si la page refuse votre première extraction, lisez l’erreur avant de retourner vers l’assistant. Une virgule manquante se corrige dans le texte. Un message absent demande de relire le lot. Une date affirmée malgré les deux comptes rendus demande de corriger le raisonnement. Relancer toute la tâche dix fois sans regarder le défaut risque surtout de vous offrir dix variantes du même problème.

## Transporter le parcours dans n8n

Notre page locale rend l’enchaînement facile à essayer. Dans une équipe, on peut vouloir relier un dépôt de fichiers, une extraction et un dossier de sortie avec un outil visuel. Un **orchestrateur** comme n8n représente les opérations par des nœuds reliés entre eux. Il transporte les données d’un nœud au suivant et conserve des informations sur les exécutions. Le petit programme que nous venons d’ouvrir joue déjà ce rôle à son échelle.

Une variante facultative est fournie dans `n8n/point-equipe.json`, avec son `README.md`, dans le même dossier d’atelier. Elle contient un lancement manuel, une extraction fictive, des contrôles et une sortie interne. Elle reste inactive, sans accès à un modèle et sans nœud d’envoi. Son JSON peut être examiné sans disposer de n8n ; l’import et l’exécution dans l’interface restent à vérifier dans votre installation.

Si vous avez déjà une instance n8n, ouvrez le menu à trois points de l’éditeur, puis **Import from File**, selon le parcours documenté au 17 septembre 2026.[^p7-n8n-import] Choisissez `n8n/point-equipe.json`. Les connexions relient **Lancer manuellement**, **Extraction fictive ou collée**, **Contrôler le lot** et **Préparer le point interne**. Examinez-les avant le lancement manuel. Le deuxième nœud fournit les données de démonstration ; son origine doit rester visible. Le `README.md` explique comment remplacer ces données par votre extraction, sans modifier les contrôles.

Suivez ensuite la sortie de chaque nœud. Retrouvez les trois messages nouveaux et les alertes dans le point. Cette variante s’arrête à la proposition interne : elle ne conserve pas l’avancement d’un lancement à l’autre et ne propose pas les boutons d’approbation de la page locale. Rejouer son lot prépare donc une nouvelle proposition identique.

Pour alimenter cette chaîne avec un modèle réel, il faudra remplacer l’extraction fictive par une étape configurée pour votre fournisseur ou votre modèle local, lui transmettre les fichiers et la consigne, puis conserver les contrôles en sortie. Le simple import de l’export fourni n’effectue pas ce travail. Dans n8n, le nœud **Basic LLM Chain** permet de définir une consigne et de lui associer un modèle de conversation ; son paramètre de format peut aussi recevoir un analyseur de sortie.[^p7-n8n-chaine] Le `README.md` situe cette adaptation, encore à exécuter avec le service choisi.

Avant cette adaptation, prévoyez où seront stockés les accès au service, comment limiter les dépenses et quelles données quitteront votre système. Un abonnement à une application de conversation ne vous donne pas nécessairement des appels d’API pour un orchestrateur. Pour une première comparaison, le copier-coller depuis l’assistant vers la page locale permet de garder la même extraction et d’observer chaque étape. Vous pourrez ensuite décider quels transferts automatiser, une fois leurs erreurs plus faciles à comprendre.

[^p7-n8n-import]: n8n, [Export and import](https://docs.n8n.io/build/manage-workflows/export-and-import/), documentation consultée le 17 septembre 2026.
[^p7-n8n-chaine]: n8n, [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm/), documentation consultée le 17 septembre 2026.

L’extraction peut maintenant venir d’un modèle, de votre lecture ou de l’exemple fictif. Les étapes suivantes gardent le même contrat : contrôler, retrouver les nouveautés, préparer le point, puis attendre sa relecture.

Nous avons aussi réussi à faire accepter un atelier inventé en lui associant un extrait authentique. Gardez cet incident en tête lorsque vous adapterez le pipeline : chaque contrôle répond à une question précise. Le prochain chapitre s’intéresse aux accès aux fichiers et aux outils, pour que le périmètre réel reste cohérent avec le travail demandé.

---

[Précédent : Faire travailler un assistant sur le dossier](../02-assistant/LECTURE.md) · [Suivant : Donner accès aux bons outils](../04-acces/LECTURE.md)
