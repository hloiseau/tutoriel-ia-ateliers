# 5. Apprendre et exercer notre métier

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Dépendances techniques et économiques](../04-dependances/LECTURE.md) · [Suivant : Alternatives, logiciels libres et possibilités de s’en passer](../06-alternatives/LECTURE.md)

**TL;DR** — Un exercice terminé ne dit pas encore ce que nous saurons refaire demain. Nous allons lire une fonction, prévoir ses résultats et la modifier sans assistant avant d’examiner l’aide qu’il pourrait apporter.

Le test est vert. Très bien. Maintenant, fermez la conversation : pourquoi ce test est-il vert ?

## La relecture demande quelque chose à relire avec

Si je ne connais pas la règle métier, les types manipulés ou la manière dont les tests s’exécutent, « je vais relire le code généré » reste une intention assez fragile. Le modèle peut produire un programme convaincant, et je peux manquer précisément l’erreur qu’il faudrait voir.

C’est pourquoi je ne conseillerais pas à quelqu’un qui découvre la programmation de reprendre directement ma manière de déléguer le développement à un agent. Certaines tâches sont justement des occasions d’apprendre à chercher, à réduire un problème et à comprendre une erreur. Les faire disparaître trop tôt peut nous laisser sans repères pour la suite.

Une expérience publiée par des chercheurs d’Anthropic en janvier 2026 a réparti 52 développeurs, majoritairement juniors, entre des tâches avec ou sans assistance pour découvrir une bibliothèque Python. Le groupe assisté a moins bien réussi l’évaluation immédiate de compréhension ; la différence de vitesse n’était pas statistiquement significative. Le périmètre reste celui d’une petite expérience et d’une évaluation à court terme : elle ne raconte pas toute une carrière.[^p8-apprendre]

Elle nous laisse une question pratique : **qu’est-ce que je veux apprendre pendant cette tâche ?** Si l’objectif est de comprendre une boucle, générer toute la boucle peut court-circuiter le travail intéressant. Examiner d’abord une erreur, puis demander un indice ou une explication, laisse une autre place à l’effort.

[^p8-apprendre]: Shen et Tamkin, [*How AI assistance impacts the formation of coding skills*](https://www.anthropic.com/research/AI-assistance-coding-skills), 29 janvier 2026. Étude menée par un fournisseur d’IA ; ses analyses des différentes manières d’interagir avec l’outil sont exploratoires et ne prouvent pas à elles seules un lien causal.

## Fermer l’assistant et ouvrir six lignes

Ouvrez `cas/lecture_code.py`, sans le lancer tout de suite. La fonction décide si un produit doit déclencher une notification. Les prix sont des entiers en centimes ; les entrées sont supposées déjà validées.

```python
def doit_notifier(ancien_prix, nouveau_prix, disponible):
    if not disponible:
        return False
    return nouveau_prix <= ancien_prix
```
Code: Une fonction volontairement incorrecte

La règle demandée est celle de notre service : notifier uniquement si le nouveau prix baisse strictement et que le produit est disponible. Prévoyez le résultat pour un prix qui baisse, un prix inchangé, un prix qui monte et un produit indisponible. Écrivez aussi le résultat attendu par la règle.

Vous pouvez ensuite lancer :

```bash
python cas/lecture_code.py
```

Le programme affiche les cas, le résultat obtenu et le résultat attendu, puis sort avec le code 1 : le cas du prix égal révèle le bug prévu dans l’exercice. Corrigez la fonction et relancez. Le corrigé est dans `corriges/lecture_code.py`, accompagné d’une explication dans `corriges/lecture_code.md`.

Le lendemain, ou simplement après une autre tâche, essayez une petite variante sans rouvrir la réponse : ne notifier que si la baisse atteint au moins 100 centimes, toujours avec un produit disponible. Que se passe-t-il pour une baisse de 99, de 100 et de 101 centimes ? La correction de cette variante est fournie elle aussi.

Personne ne ramassera la copie. 🙂 Observez plutôt ce que vous savez encore expliquer et modifier après avoir fermé l’outil.

## Garder de la place pour apprendre au travail

L’IA peut aider à reformuler une erreur, à proposer des cas de test ou à donner un exemple plus petit. Nous pouvons demander un indice avant la solution, puis vérifier l’explication dans la documentation et par une exécution. Une explication agréable à lire reste une réponse à examiner.

Une équipe peut aussi garder des moments où l’on enquête à deux, où l’on présente pourquoi une correction fonctionne et où les débutants écrivent des changements qu’ils peuvent expliquer. Sinon, demander à un junior de « vérifier ce que l’agent a fait » lui confie une responsabilité sans forcément lui donner les moyens de l’exercer.

Les développeurs expérimentés peuvent perdre les mêmes repères. Après plusieurs semaines à déléguer un domaine, saurions-nous encore diagnostiquer sa panne ? L’exercice précédent est volontairement petit ; dans un vrai projet, la reprise peut porter sur un test qui échoue ou un incident réduit.

Quant à l’avenir du métier, les travaux de l’OIT examinent l’exposition de tâches et de métiers aux IA génératives. Ils ne prédisent pas le destin de chaque développeur ni la disparition automatique d’un emploi dès qu’une de ses tâches est exposée.[^p8-oit]

Les décisions d’organisation restent donc centrales : qui reçoit du temps pour apprendre, qui relit, qui arbitre, et que fait-on du temps éventuellement gagné ? Nous pouvons discuter de ces choix maintenant, sans attendre qu’une prédiction sur « la fin des développeurs » se réalise ou se trompe.

[^p8-oit]: OIT, [*Generative AI and Jobs: A Refined Global Index of Occupational Exposure*](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure), 2025.

Le résultat de l’exercice tient dans quelques booléens ; son intérêt se voit surtout le lendemain, lorsque nous savons encore expliquer la condition et la modifier. Ajoutons cette capacité à nos critères quand nous comparerons plusieurs façons d’accomplir une tâche.

---

[Précédent : Dépendances techniques et économiques](../04-dependances/LECTURE.md) · [Suivant : Alternatives, logiciels libres et possibilités de s’en passer](../06-alternatives/LECTURE.md)
