La première opération sera de relever les faits dans les messages. Ensuite, le programme contrôlera le format et les références, rapprochera les identifiants du suivi, puis préparera un point que nous pourrons relire. Nous gardons un arrêt avant l’approbation et l’export. L’ordre est fixé par l’application.

![Les documents servent à une extraction ; ses données passent des contrôles avant la proposition, la relecture, l’approbation et l’export. Une erreur de format arrête le traitement.](image:images/pipeline.png)
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
