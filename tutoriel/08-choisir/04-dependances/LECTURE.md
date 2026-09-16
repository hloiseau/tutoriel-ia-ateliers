# 4. Dépendances techniques et économiques

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Coûts, énergie, matériel et environnement](../03-ressources/LECTURE.md) · [Suivant : Apprendre et exercer notre métier](../05-apprendre/LECTURE.md)

**TL;DR** — Nous allons suivre le trajet d’une demande et préparer une sortie possible. Héberger un morceau chez soi ne rend pas automatiquement toute l’application locale.

Imaginez que le service utilisé par l’équipe double son tarif, change un modèle ou soit indisponible ce matin. Qu’est-ce qui continue à fonctionner ?

## Suivre les données jusqu’au bout

Dans la partie 6, notre serveur MCP lisait des documents sur notre ordinateur. Cela ne décidait pas où tournait le modèle qui recevait ensuite les résultats. Nous retrouvons la même question avec une interface installée localement : ses fichiers sont chez nous, mais ses requêtes peuvent partir ailleurs.

Ouvrez `fiches/flux.md` et remplissez une ligne par trajet : de l’éditeur au modèle, de l’agent au serveur MCP, du serveur aux tickets, puis vers les éventuels journaux. Pour chaque trajet, notez ce qui passe, où cela arrive et ce qui vous permet de l’affirmer.

| Élément de notre atelier | Information que nous pouvons établir |
| --- | --- |
| Client documentaire de la partie 7 | Son code envoie la requête à `127.0.0.1:8080` |
| Réponse reçue | Le journal conserve le contexte transmis et la sortie |
| Assistant installé pour la partie 4 | Le trajet dépend du produit, de sa configuration et du fournisseur sélectionné |
| Politique d’un service externe | Elle doit être vérifiée pour ce service et l’offre utilisée |

« Non utilisé pour l’entraînement » ne signifie pas forcément « jamais conservé ». La rétention des journaux, l’accès de tiers et la localisation du traitement sont des questions distinctes. Il faut lire les engagements applicables plutôt que déduire toutes les réponses d’une seule option.

Pour notre exercice, restez sur les documents fictifs fournis. Une fois la carte des trajets dessinée, vous pourrez décider quelles données de votre propre projet seraient acceptables dans cette configuration.

## Préparer le jour où l’on change d’outil

Un historique lisible, une procédure dans le dépôt et des tests exécutables nous servent même si nous changeons d’assistant. C’est moins évident pour un réglage qui n’existe que dans un compte ou un format exporté que rien d’autre ne sait relire.

Faisons un essai de sortie sans désinstaller quoi que ce soit. Copiez dans un dossier séparé le ticket fictif, les règles, les tests et le format attendu. Avec ces seuls fichiers, pouvez-vous comprendre ce qu’il reste à faire ? Si la réponse dépend d’une phrase introuvable dans une ancienne conversation, ramenez cette décision dans le dossier.

Changer d’API ne suffit pas toujours : deux modèles acceptant des messages de même forme peuvent répondre différemment, employer les outils autrement ou supporter d’autres longueurs de contexte. Nos cas de PRIX-1 et PRIX-2 permettent justement de vérifier le comportement après un changement.

Le fichier `fiches/sortie.md` distingue ce que l’on possède, ce que l’on peut exporter et ce qu’il faudra reconstruire. Il demande aussi quelle procédure permet de travailler pendant une panne. Une bonne réponse peut être très simple : reprendre les tests et la recette manuellement.

Nous n’avons pas besoin d’une migration parfaite en cinq minutes. Nous avons besoin de savoir où se trouve la dépendance et ce que son remplacement coûterait en travail.

## Ne pas tout faire reposer sur un abonnement individuel

Le choix d’un outil dans une équipe touche aussi les personnes qui ne l’utilisent pas. Qui relit le code supplémentaire ? Qui dépanne la machine locale ? Qui peut accéder à la documentation ? Que fait un collègue qui ne souhaite pas ouvrir un compte chez ce fournisseur ?

Pour moi, imposer un framework d’IA à toute l’organisation parce qu’il est populaire est une mauvaise façon de commencer. Nous devrions d’abord identifier le problème, puis discuter de la place que l’outil prendra et du travail qu’il déplace.

L’auto-hébergement peut rendre une partie de cette dépendance plus maîtrisable. Il ajoute aussi de l’administration, des mises à jour et une responsabilité sur la disponibilité. Un service géré peut retirer certaines de ces tâches, en échange d’autres dépendances. Comparons les deux organisations concrètes, plutôt que deux étiquettes.

Dans notre équipe fictive, les tests restent exécutables sans agent et les procédures restent lisibles sans abonnement. L’aide de l’IA peut s’ajouter à ce fonctionnement ; elle ne devient pas la seule façon de savoir comment fonctionne le service.

Enfin, la dépendance peut être collective : une équipe entière risque de perdre l’habitude d’enquêter si chaque incident est confié au même assistant. C’est le bon moment pour parler de l’apprentissage du métier.

Nous avons une carte des trajets et une possibilité de continuer sans l’outil. Voyons maintenant ce que nous voulons être capables de faire nous-mêmes.

---

[Précédent : Coûts, énergie, matériel et environnement](../03-ressources/LECTURE.md) · [Suivant : Apprendre et exercer notre métier](../05-apprendre/LECTURE.md)
