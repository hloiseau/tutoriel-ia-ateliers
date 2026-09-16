# 4. Dépendances techniques et économiques

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Coûts, énergie, matériel et environnement](../03-ressources/LECTURE.md) · [Suivant : Apprendre et exercer notre métier](../05-apprendre/LECTURE.md)

**TL;DR** — Suivre le trajet d’une demande révèle les services dont elle dépend. Nous préparerons aussi une façon de continuer si l’un d’eux disparaît.

Le service utilisé par l’équipe double son tarif, change un modèle ou tombe en panne ce matin. Qu’est-ce qui continue à fonctionner ?

## Suivre les données jusqu’au bout

Dans la partie 6, notre serveur MCP lisait des documents sur notre ordinateur, puis transmettait ses résultats au modèle choisi par l’assistant. Avec une interface installée localement, les fichiers du programme restent chez nous tandis que les requêtes peuvent partir ailleurs. Le mot « local » décrit ici un morceau du trajet.

Ouvrez `fiches/flux.md` et remplissez une ligne par trajet : de l’éditeur au modèle, de l’agent au serveur MCP, du serveur aux tickets, puis vers les éventuels journaux. Pour chaque trajet, notez ce qui passe, où cela arrive et ce qui vous permet de l’affirmer.

| Élément de notre atelier | Information que nous pouvons établir |
| --- | --- |
| Client documentaire de la partie 7 | Son code envoie la requête à `127.0.0.1:8080` |
| Réponse reçue | Le journal conserve le contexte transmis et la sortie |
| Assistant installé pour la partie 4 | Le trajet dépend du produit, de sa configuration et du fournisseur sélectionné |
| Politique d’un service externe | Elle doit être vérifiée pour ce service et l’offre utilisée |

Une option « non utilisé pour l’entraînement » répond à une question précise. Pour connaître la durée de conservation des journaux, l’accès de tiers et la localisation du traitement, il reste à lire les engagements applicables au service et à l’offre choisis.

Pour notre exercice, restez sur les documents fictifs fournis. Une fois la carte des trajets dessinée, vous pourrez décider quelles données de votre propre projet seraient acceptables dans cette configuration.

## Préparer le jour où l’on change d’outil

Un historique lisible, une procédure dans le dépôt et des tests exécutables nous servent même si nous changeons d’assistant. C’est moins évident pour un réglage qui n’existe que dans un compte ou un format exporté que rien d’autre ne sait relire.

Faisons un essai de sortie sans désinstaller quoi que ce soit. Copiez dans un dossier séparé le ticket fictif, les règles, les tests et le format attendu. Avec ces seuls fichiers, pouvez-vous comprendre ce qu’il reste à faire ? Si la réponse dépend d’une phrase introuvable dans une ancienne conversation, ramenez cette décision dans le dossier.

Changer d’API ne suffit pas toujours : deux modèles acceptant des messages de même forme peuvent répondre différemment, employer les outils autrement ou supporter d’autres longueurs de contexte. Nos cas de PRIX-1 et PRIX-2 permettent justement de vérifier le comportement après un changement.

Le fichier `fiches/sortie.md` distingue ce que l’on possède, ce que l’on peut exporter et ce qu’il faudra reconstruire. Il demande aussi quelle procédure permet de travailler pendant une panne. Une bonne réponse peut être très simple : reprendre les tests et la recette manuellement.

L’essai ne promet pas une migration parfaite en cinq minutes. Il localise la dépendance et donne une première idée du travail nécessaire pour la remplacer.

## Ne pas tout faire reposer sur un abonnement individuel

Le choix d’un outil dans une équipe touche aussi les personnes qui ne l’utilisent pas. Qui relit le code supplémentaire ? Qui dépanne la machine locale ? Qui peut accéder à la documentation ? Que fait un collègue qui ne souhaite pas ouvrir un compte chez ce fournisseur ?

Pour moi, imposer un framework d’IA à toute l’organisation parce qu’il est populaire est une mauvaise façon de commencer. Nous devrions d’abord identifier le problème, puis discuter de la place que l’outil prendra et du travail qu’il déplace.

L’auto-hébergement peut rendre une partie de cette dépendance plus maîtrisable. Il ajoute de l’administration, des mises à jour et une responsabilité sur la disponibilité. Un service géré retire certaines de ces tâches et crée d’autres dépendances. Comparons les deux organisations concrètes plutôt que leurs étiquettes.

Dans notre équipe fictive, les tests restent exécutables sans agent et les procédures lisibles sans abonnement. L’aide de l’IA s’ajoute à ce fonctionnement, tandis que les connaissances nécessaires au service restent accessibles à toute l’équipe.

Enfin, la dépendance peut être collective : une équipe entière risque de perdre l’habitude d’enquêter si chaque incident est confié au même assistant. C’est le bon moment pour parler de l’apprentissage du métier.

Rangez la carte des trajets et la procédure de sortie avec le projet : elles serviront lors d’une panne comme lors d’un changement d’outil. Reste une dépendance moins visible, celle de nos propres savoir-faire lorsque l’assistant prend l’habitude de chercher et d’écrire à notre place.

---

[Précédent : Coûts, énergie, matériel et environnement](../03-ressources/LECTURE.md) · [Suivant : Apprendre et exercer notre métier](../05-apprendre/LECTURE.md)
