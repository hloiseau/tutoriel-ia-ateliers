# Choisir la place de l’IA

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Utiliser l’IA, s’en passer ou la réserver à une tâche précise sont trois choix possibles. Nous allons les examiner à partir des données, du travail humain, des licences, des ressources consommées et de ce que nous apprenons réellement.

Dans le parcours développement, nous avons relu des changements de code et encadré les outils d’un agent. Dans le parcours de tâches de travail, nous avons préparé un point d’équipe et séparé les propositions des décisions. Si vous avez suivi l’approfondissement sur l’IA maison, vous avez aussi rencontré une réponse qui invente une durée et une adaptation qui dégrade un ancien format. Nous avons de quoi examiner ce que nous voulons confier à ces outils, et ce que cela nous demande.

J’utilise ces outils au quotidien, mais je ne pense pas que notre métier doive s’organiser autour d’eux par défaut. Si une tâche se résout bien avec un script, gardons le script. Si une aide sur les tests nous permet de mieux travailler, regardons ce qu’elle apporte. Et si nous ne voulons pas développer avec l’IA, nous pouvons aussi faire ce choix.

Nous utiliserons les exemples du suivi de prix et de la journée d’ateliers. Automatiser une vérification de catalogue, préparer des tests ou traiter des demandes d’inscription conduit à des choix différents : les données disponibles, les personnes concernées et les conséquences d’une erreur changent.

Téléchargez [les fichiers de cette partie](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-choisir-ia.zip), ou ouvrez `ateliers/08-choisir`. Ils contiennent les cas, des fiches courtes, un exercice de lecture de code et des pistes de correction. Aucun abonnement ni modèle local n’est nécessaire pour commencer. Les documents et études cités sont consultés en septembre 2026 ; leurs dates comptent lorsqu’on compare les résultats.

Vous n’avez pas besoin d’avoir exécuté tous les ateliers pour suivre cette partie. Les exemples de code sont facultatifs pour le parcours de tâches de travail ; nous proposerons un exercice de relecture de compte rendu au même endroit. Lorsque nous ouvrons la fiche d’un modèle, les informations nécessaires se trouvent dans les fichiers fournis.

## 1. D’où viennent les données et le travail humain ?

**TL;DR** — Un modèle ne sort pas seulement d’un calcul. Il dépend de contenus, de décisions et de travail humain dont les conditions ne sont pas toujours visibles dans sa fiche.

Dans les ateliers, les données fictives sont accessibles et nous pouvons retrouver leur origine. Pour les modèles que nous utilisons, cette remontée est parfois plus difficile. Essayons de comprendre ce que leur documentation permet réellement de connaître.

### Remonter avant le téléchargement

Prenons la fiche de SmolLM2-360M-Instruct, un modèle utilisé dans le parcours développement. Vous pouvez la consulter sans avoir installé ce modèle ni suivi la partie 3. Nous y trouvons des informations sur sa famille, ses données et ses évaluations. C’est un point de départ. La fiche ne donne pas le nom de chaque personne ayant contribué à chaque texte.[^p8-carte]

Plusieurs groupes contribuent au résultat : les auteurs des contenus, les personnes qui préparent les données et celles qui conçoivent le modèle. Une documentation de bibliothèque a d’abord été écrite pour aider ses utilisateurs. Son passage éventuel dans un corpus ajoute un usage à ce premier travail.

![Des auteurs et des personnes représentées dans les données alimentent une chaîne de collecte, de préparation et d’entraînement. L’application mobilise aussi le travail de déploiement et de vérification.](images/travail.png)
Figure: Plusieurs contributions humaines derrière une réponse affichée

Ouvrez `fiches/provenance.md` dans l’archive de cette partie. Pour les courriels de la journée d’ateliers, nous pouvons indiquer qu’ils ont été écrits pour le tutoriel, qu’ils décrivent un événement inventé et qu’ils sont distribués sous CC BY-SA 4.0. Le corpus documentaire de la partie 8 a lui aussi une provenance déclarée. Pour un corpus externe, nous devons pouvoir retrouver d’où vient l’information que nous écrivons dans cette fiche.

Une source peut être décrite sans être téléchargeable ; un jeu peut être téléchargé alors que les étapes de sa préparation restent inconnues. Ces différences donnent des questions précises à inscrire dans la fiche. La seule case « transparent » ne nous apprendrait pas grand-chose.

[^p8-carte]: Hugging Face, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct), consultée en septembre 2026.

### Les personnes que le mot « automatisation » cache

Dans l’atelier d’apprentissage, les étiquettes des chiffres sont déjà fournies. Elles associent chaque image à la réponse attendue. À une autre échelle, des personnes peuvent transcrire, classer, comparer des réponses, vérifier des exemples ou modérer des contenus. Ce travail mérite d’être regardé autrement que comme une ligne « données » dans un budget.

Oskarina Veronica Fuentes Anaya raconte son expérience sur des plateformes de travail de données dans *Life of a Latin American Data Worker*. Elle décrit notamment des tâches qui arrivent de façon irrégulière et du temps passé à attendre sans être payé. C’est son témoignage et celui du milieu qu’elle décrit ; il ne permet pas d’attribuer les mêmes conditions à tous les modèles.[^p8-travail]

Prenons ce récit au sérieux sans inventer la chaîne de sous-traitance d’un fournisseur qui ne la publie pas. Dans notre fiche, une information inconnue reste inconnue. Cette absence peut tout de même peser dans notre choix ; elle n’a rien de rassurant par défaut.

Les auteurs des textes et du code méritent également une place dans cette discussion. Selon moi, la disponibilité technique d’un contenu ne devrait pas suffire à écarter la question de son usage, de l’accord de ses créateurs et du partage de la valeur produite. La réponse du droit ne tranche pas à elle seule la position éthique que nous voulons adopter.

Pour un projet auquel nous contribuons, cela devient très concret : qui annote, avec quelles consignes, quel paiement et quelle possibilité de signaler une erreur ou de refuser un contenu difficile ? Si nous commandons ce travail, la rapidité de livraison n’est pas notre seul critère.

[^p8-travail]: Oskarina Veronica Fuentes Anaya, [*Life of a Latin American Data Worker*](https://data-workers.org/oskarina/), 2024, Data Workers’ Inquiry. Présentation et témoignage de l’autrice, avec une animation sous-titrée.

### Ce que nous choisissons de garder

Ouvrez `cas/documents.md`. L’équipe dispose de trois éléments : une règle publique du service, une conversation de support contenant des coordonnées fictives et une ancienne recette dont la décision a changé.

Pour expliquer la règle de notification, le premier document suffit. Ajouter les coordonnées du client ne l’explique pas mieux. Quant à l’ancienne recette, elle pourrait contredire la règle actuelle. Avant de demander quel modèle choisir, nous pouvons déjà améliorer ce que nous lui donnons.

Réduire les données aide aussi à limiter leur exposition. Pour des données personnelles réelles, leur collecte et leur réutilisation demandent une analyse adaptée au but poursuivi ; leur présence sur le Web ne dispense pas de ces questions. Les fiches de la CNIL détaillent notamment la sélection des données pertinentes et leur suivi.[^p8-cnil]

Faites une copie de travail des documents et conservez seulement ce qui sert à répondre à la question. Comparez ensuite avec `corriges/documents.md`. Un nom retiré peut laisser derrière lui assez de détails pour reconnaître la personne. Ici, toutes les personnes sont fictives : nous pouvons examiner le problème sans exposer de véritables clients.

La sélection peut également déformer ce que le modèle voit. Si nos exemples ne couvrent que des tickets bien rédigés en anglais, un bon résultat sur ceux-ci ne dit pas ce qui se passera avec des demandes courtes en français. Essayons les usages que nous voulons réellement prendre en charge.

[^p8-cnil]: CNIL, [tenir compte de la protection des données dans la collecte et la gestion des données](https://www.cnil.fr/fr/tenir-compte-de-la-protection-des-donnees-dans-la-collecte-et-la-gestion-des-donnees). Ces recommandations portent sur les données personnelles ; elles ne règlent pas à elles seules les questions de droit d’auteur.

Notre fiche de provenance contient déjà des informations, quelques inconnues et des personnes que le mot « données » aurait facilement cachées. Les fichiers disponibles et leurs licences vont maintenant préciser ce que nous pouvons étudier, modifier et partager.

## 2. Licences, transparence et possibilités de vérification

**TL;DR** — Télécharger des poids, lire le code et réutiliser un système demandent des droits et des fichiers différents. Le mot « open » ne remplit pas notre fiche à notre place.

« C’est ouvert, donc on peut tout faire avec. » Voilà une phrase qui mérite qu’on ouvre au moins le fichier de licence.

### De quoi parle la licence ?

Dans notre dépôt, le code, les textes et certains éléments tiers ont des licences distinctes. Un système d’IA peut lui aussi réunir plusieurs objets : moteur d’inférence, interface, paramètres, jeux de données et documentation.

| Élément | Question concrète |
| --- | --- |
| Interface ou agent | Peut-on étudier et modifier ce programme ? |
| Poids du modèle | Peut-on les obtenir, les utiliser et distribuer une adaptation ? |
| Code d’entraînement | Les étapes et réglages nécessaires sont-ils disponibles ? |
| Données | Leur provenance et leurs conditions de réutilisation sont-elles décrites ? |
| Service hébergé | Quelles conditions s’appliquent à nos entrées, sorties et journaux ? |

Une licence permissive annoncée pour le moteur couvre le moteur dans les conditions qu’elle énonce. Le modèle chargé possède ses propres conditions, tout comme l’interface placée devant lui.

Pour SmolLM2-360M-Instruct, la fiche annonce Apache 2.0.[^p8-carte-licence] Notons-le avec le lien et la date de consultation. Cette information porte sur le modèle indiqué par la fiche ; elle ne documente pas à elle seule tous les contenus qui ont servi à l’entraînement. Avant de redistribuer une combinaison précise de fichiers, lisons les textes, notices et conditions qui s’appliquent à chacun.[^p8-apache]

Notre exercice consiste à retrouver ces éléments. Le badge d’une page d’accueil fournit une piste ; le dossier de l’application doit conserver les références qui s’appliquent réellement.

[^p8-apache]: Apache Software Foundation, [texte de la licence Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0), notamment les conditions de redistribution. La portée dépend des éléments effectivement placés sous cette licence.

[^p8-carte-licence]: Hugging Face, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct), licence annoncée à la consultation de septembre 2026.

### Ce que l’ouverture rend possible

La définition *Open Source AI* 1.0 de l’Open Source Initiative associe les libertés d’utiliser, d’étudier, de modifier et de partager à plusieurs éléments accessibles : paramètres, code et informations détaillées sur les données d’entraînement. Elle ne demande pas que toutes les données soient distribuées sans exception ; elle précise les informations attendues pour comprendre et reconstruire un système substantiellement équivalent.[^p8-osi]

Ce cadre explicite se prête à l’examen. Il décrit des libertés et les éléments nécessaires pour les exercer ; les conditions de travail, la consommation et la justesse des réponses demandent leurs propres informations.

L’ouverture peut nous donner des prises utiles. Si nous pouvons exécuter le modèle ailleurs, inspecter les étapes et modifier le programme, nous avons davantage de moyens d’expérimenter et de continuer sans le service d’origine. Encore faut-il disposer du matériel, du temps et des compétences nécessaires.

Ces libertés peuvent aussi s’exercer collectivement. Une équipe, une association ou un hébergeur peut porter une partie du travail. Quitter un grand fournisseur ne vous condamne donc pas à devenir administrateur système tous les week-ends. 🙂

[^p8-osi]: Open Source Initiative, [*The Open Source AI Definition — 1.0*](https://opensource.org/ai/open-source-ai-definition).

### Examiner un modèle que nous avons déjà utilisé

Reprenez SmolLM2 dans `fiches/provenance.md`. Nous avons déjà une raison d’être précis : le modèle utilisé dans les parties 3 et 8 est le 360M *Instruct*, avec un fichier GGUF déterminé, pas n’importe quel membre de sa famille.

Notez la référence, la licence annoncée, la langue indiquée, les liens vers les informations de préparation et ce que vous avez effectivement testé. La dernière colonne doit permettre de reconnaître la provenance de chaque affirmation : « indiqué par l’auteur », « vérifié dans notre essai » ou « pas établi avec les éléments consultés ».

Par exemple, l’étiquette de langue anglaise provient de la fiche. La durée de temporisation inventée vient d’un journal d’exécution conservé dans l’atelier de la partie 8 : une réponse y donne une durée alors que sa source la laisse ouverte. Vous pouvez consulter cette observation sans rejouer l’essai. Ni l’une ni l’autre ne prouve que toutes les réponses en français seront fausses. Elles nous donnent en revanche une raison concrète de ne pas valider cet usage sur la foi du nom du modèle.

Une piste de correction est disponible dans `corriges/provenance.md`. Elle contient peu de cases remplies, volontairement : mieux vaut trois informations retrouvables qu’un tableau très convaincant où l’on a deviné le reste.

Vous pouvez refaire le même travail avec un autre modèle. Gardez sa révision lorsqu’elle est disponible. Si vous changez de fichier ou de service, relisez les conditions correspondantes au lieu de transporter automatiquement la conclusion précédente.

Notre fiche dit maintenant quels éléments nous pouvons obtenir, étudier ou modifier, et quelles informations restent à établir. Le coût de l’outil mérite la même précision : une facture, une mesure électrique et un impact environnemental racontent trois choses différentes.

## 3. Coûts, énergie, matériel et environnement

**TL;DR** — Le prix, l’électricité et l’impact environnemental décrivent des réalités différentes. Un calcul simple, accompagné de son périmètre, nous aidera à voir ce qu’il mesure et ce qu’il laisse de côté.

Un appel gratuit peut mobiliser des machines. Un modèle local peut éviter un abonnement tout en occupant notre carte graphique. Le mot « gratuit » n’arrête pas le compteur électrique.

### Que mettons-nous dans le calcul ?

Pour notre atelier, nous pouvons compter le temps consacré à préparer la demande, à attendre, à relire et à corriger. Pour l’électricité, il faut aussi choisir ce que l’on mesure : la carte graphique seule, l’ordinateur à la prise ou l’ensemble du service ?

![Quatre périmètres à distinguer : calcul ciblé, électricité du service, cycle de vie et évolution des usages.](images/perimetre.png)
Figure: Des périmètres différents, à annoncer avant de comparer

Dans son avis de juillet 2026, l’ADEME demande de considérer le cycle de vie ainsi que les effets indirects, notamment les effets rebonds. La fabrication du matériel, l’eau et les infrastructures ne disparaissent pas parce que l’on a mesuré l’électricité d’une requête.[^p8-ademe]

Un effet rebond peut se comprendre avec notre service : une réponse devient moins coûteuse, nous décidons alors d’en générer pour chaque ligne du catalogue, au lieu de seulement traiter les anomalies. Le coût unitaire baisse pendant que le volume augmente. Notre bilan devra suivre les deux.

Un périmètre étroit, correctement annoncé, reste utile pour comparer deux essais. Sa légende doit simplement rester avec le résultat : la consommation de la carte pendant une tâche ne devient pas le bilan environnemental complet de l’IA.

[^p8-ademe]: ADEME, [*IA générative, comment quantifier les impacts ?*](https://www.ademe.fr/presse/communique-national/ia-generative-comment-quantifier-les-impacts/), 22 juillet 2026.

### Un calcul que nous pouvons refaire

Prenons une puissance moyenne **hypothétique** de 200 W pendant 30 minutes. Avec une calculatrice, convertissez la durée en heures : 30 ÷ 60 = 0,5 heure. L’énergie correspondante vaut 200 × 0,5 = 100 Wh, soit 0,1 kWh.

Le même calcul est disponible dans l’atelier pour les lecteurs qui souhaitent utiliser Python. Cette commande est facultative ; depuis le dossier de cette partie, Python 3.12 suffit :

```bash
python energie.py --puissance-w 200 --minutes 30
```

Nous retrouvons le produit d’une puissance moyenne par une durée. Ces valeurs servent à expliquer le calcul ; elles n’ont pas été mesurées sur notre modèle ni sur la machine de l’auteur.

Pour remplacer l’hypothèse par une mesure, il faudrait relever une consommation sur l’intervalle de l’essai, avec un outil dont on connaît le périmètre. Une puissance maximale annoncée pour une carte ne donne pas sa puissance moyenne pendant notre tâche. Et une lecture instantanée ne décrit pas, à elle seule, toute l’exécution.

Si vous disposez déjà d’un compteur d’énergie à la prise, vous pouvez relever le début et la fin d’un essai. Notez ce qui était branché, les autres tâches actives et la durée. La différence inclut alors ce que le compteur a réellement mesuré, y compris le repos éventuel. Pour estimer un supplément par rapport au repos, il faudrait aussi établir une référence comparable, avec son incertitude.

Le script s’arrête aux Wh. Calculer des émissions de CO₂ demanderait notamment un facteur adapté à l’électricité considérée ; évaluer l’eau ou la fabrication de l’ordinateur élargirait encore le périmètre. En leur absence, gardons l’unité obtenue et la description de la mesure.

### Éviter une dépense qui ne sert pas la tâche

Dans `cas/equipe.md`, l’équipe veut repérer des prix négatifs et des identifiants manquants dans un catalogue. Les règles sont explicites. Nous pouvons les vérifier avec un programme déterministe : un LLM n’a pas besoin de réinterpréter chaque ligne.

Pour un texte libre, le choix peut être différent. Il reste utile de comparer une solution spécialisée à un modèle généraliste. L’étude *Power Hungry Processing* mesure justement des consommations d’inférence différentes selon les tâches et les architectures testées ; ses résultats ne fournissent pas un coût universel de « la requête IA ».[^p8-energie]

Avant d’acheter du matériel, essayez ce qui suffit déjà à votre besoin. Notre recherche lexicale fonctionne sans carte graphique. Notre génération documentaire sur CPU a montré ses limites. Partons de ces observations pour choisir entre calcul local, service distant ou programme ordinaire.

Nous pouvons aussi réduire le nombre d’appels, réutiliser un résultat encore valable ou arrêter une boucle qui ne progresse plus. Mais si une réponse plus courte provoque cinq nouvelles tentatives, l’économie annoncée mérite d’être recalculée.

Les tarifs peuvent changer indépendamment du matériel. Conservez donc séparément le prix payé, les ressources mesurées et ce que vous ne savez pas mesurer ; vous éviterez de transformer une promotion commerciale en progrès environnemental.

[^p8-energie]: Luccioni, Jernite et Strubell, [*Power Hungry Processing: Watts Driving the Cost of AI Deployment?*](https://arxiv.org/abs/2311.16863), étude publiée à FAccT 2024.

Le calcul affiche 100 Wh pour notre hypothèse et s’arrête là. Une autre question très concrète attend l’équipe : que devient son travail si le fournisseur, le réseau ou la machine devient indisponible ?

## 4. Dépendances techniques et économiques

**TL;DR** — Suivre le trajet d’une demande révèle les services dont elle dépend. Nous préparerons aussi une façon de continuer si l’un d’eux disparaît.

Le service utilisé par l’équipe double son tarif, change un modèle ou tombe en panne ce matin. Qu’est-ce qui continue à fonctionner ?

### Suivre les données jusqu’au bout

Dans la partie 6, notre serveur MCP lisait des documents sur notre ordinateur, puis transmettait ses résultats au modèle choisi par l’assistant. Avec une interface installée localement, les fichiers du programme restent chez nous tandis que les requêtes peuvent partir ailleurs. Le mot « local » décrit ici un morceau du trajet.

Ouvrez `fiches/flux.md` et remplissez une ligne par trajet : de l’éditeur au modèle, de l’agent au serveur MCP, du serveur aux tickets, puis vers les éventuels journaux. Pour chaque trajet, notez ce qui passe, où cela arrive et ce qui vous permet de l’affirmer.

Pour le parcours de tâches de travail, partez des fichiers joints à l’assistant, puis du document ou du JSON qu’il produit. La page locale reçoit ensuite ce JSON par copier-coller ; elle le traite dans le navigateur et déclenche des téléchargements, sans appeler de service. Cela ne renseigne pas sur le traitement antérieur des pièces par l’assistant choisi. Inscrivez ces deux étapes séparément dans votre carte.

| Élément de notre atelier | Information que nous pouvons établir |
| --- | --- |
| Client documentaire de la partie 8 | Son code envoie la requête à `127.0.0.1:8080` |
| Réponse reçue | Le journal conserve le contexte transmis et la sortie |
| Assistant installé pour la partie 4 | Le trajet dépend du produit, de sa configuration et du fournisseur sélectionné |
| Politique d’un service externe | Elle doit être vérifiée pour ce service et l’offre utilisée |

Une option « non utilisé pour l’entraînement » répond à une question précise. Pour connaître la durée de conservation des journaux, l’accès de tiers et la localisation du traitement, il reste à lire les engagements applicables au service et à l’offre choisis.

Pour notre exercice, restez sur les documents fictifs fournis. Une fois la carte des trajets dessinée, vous pourrez décider quelles données de votre propre projet seraient acceptables dans cette configuration.

### Préparer le jour où l’on change d’outil

Un historique lisible, une procédure dans le dépôt et des tests exécutables nous servent même si nous changeons d’assistant. C’est moins évident pour un réglage qui n’existe que dans un compte ou un format exporté que rien d’autre ne sait relire.

Faisons un essai de sortie sans désinstaller quoi que ce soit. Copiez dans un dossier séparé le ticket fictif, les règles, les tests et le format attendu. Avec ces seuls fichiers, pouvez-vous comprendre ce qu’il reste à faire ? Si la réponse dépend d’une phrase introuvable dans une ancienne conversation, ramenez cette décision dans le dossier.

Si vous venez du parcours de tâches de travail, faites ce même essai avec les sources de la journée, les règles, la consigne, le point et son état sauvegardé. Pouvez-vous retrouver les demandes à examiner et les deux dates encore ouvertes ? Préparez la suite à la main pour vérifier que ces fichiers suffisent. Une décision connue seulement de l’assistant devra rejoindre les documents de l’équipe.

Changer d’API ne suffit pas toujours : deux modèles acceptant des messages de même forme peuvent répondre différemment, employer les outils autrement ou supporter d’autres longueurs de contexte. Nos cas de PRIX-1 et PRIX-2 permettent justement de vérifier le comportement après un changement.

Le fichier `fiches/sortie.md` distingue ce que l’on possède, ce que l’on peut exporter et ce qu’il faudra reconstruire. Il demande aussi quelle procédure permet de travailler pendant une panne. Une bonne réponse peut être très simple : reprendre les tests et la recette manuellement.

L’essai ne promet pas une migration parfaite en cinq minutes. Il localise la dépendance et donne une première idée du travail nécessaire pour la remplacer.

### Ne pas tout faire reposer sur un abonnement individuel

Le choix d’un outil dans une équipe touche aussi les personnes qui ne l’utilisent pas. Qui relit le code supplémentaire ? Qui dépanne la machine locale ? Qui peut accéder à la documentation ? Que fait un collègue qui ne souhaite pas ouvrir un compte chez ce fournisseur ?

Pour moi, imposer un framework d’IA à toute l’organisation parce qu’il est populaire est une mauvaise façon de commencer. Nous devrions d’abord identifier le problème, puis discuter de la place que l’outil prendra et du travail qu’il déplace.

L’auto-hébergement peut rendre une partie de cette dépendance plus maîtrisable. Il ajoute de l’administration, des mises à jour et une responsabilité sur la disponibilité. Un service géré retire certaines de ces tâches et crée d’autres dépendances. Comparons les deux organisations concrètes plutôt que leurs étiquettes.

Dans notre équipe fictive, les tests restent exécutables sans agent et les procédures lisibles sans abonnement. L’aide de l’IA s’ajoute à ce fonctionnement, tandis que les connaissances nécessaires au service restent accessibles à toute l’équipe.

Enfin, la dépendance peut être collective : une équipe entière risque de perdre l’habitude d’enquêter si chaque incident est confié au même assistant. C’est le bon moment pour parler de l’apprentissage du métier.

Rangez la carte des trajets et la procédure de sortie avec le projet : elles serviront lors d’une panne comme lors d’un changement d’outil. Reste une dépendance moins visible, celle de nos propres savoir-faire lorsque l’assistant prend l’habitude de chercher et d’écrire à notre place.

## 5. Apprendre et exercer notre métier

**TL;DR** — Un exercice terminé ne dit pas encore ce que nous saurons refaire demain. Selon votre parcours, nous allons relire une fonction ou un compte rendu sans assistant, puis examiner l’aide qu’il pourrait apporter.

Le test est vert, ou le point d’équipe est prêt. Fermez maintenant la conversation : sauriez-vous expliquer le changement et retrouver ce qui justifie chaque décision ?

### La relecture demande quelque chose à relire avec

Si je ne connais pas la règle métier, les types manipulés ou la manière dont les tests s’exécutent, « je vais relire le code généré » reste une intention assez fragile. Le modèle peut produire un programme convaincant, et je peux manquer précisément l’erreur qu’il faudrait voir.

C’est pourquoi je ne conseillerais pas à quelqu’un qui découvre la programmation de reprendre directement ma manière de déléguer le développement à un agent. Certaines tâches sont justement des occasions d’apprendre à chercher, à réduire un problème et à comprendre une erreur. Les faire disparaître trop tôt peut nous laisser sans repères pour la suite.

Une expérience publiée par des chercheurs d’Anthropic en janvier 2026 a réparti 52 développeurs, majoritairement juniors, entre des tâches avec ou sans assistance pour découvrir une bibliothèque Python. Le groupe assisté a moins bien réussi l’évaluation immédiate de compréhension ; la différence de vitesse n’était pas statistiquement significative. Le périmètre reste celui d’une petite expérience et d’une évaluation à court terme : elle ne raconte pas toute une carrière.[^p8-apprendre]

Elle nous laisse une question pratique : **qu’est-ce que je veux apprendre pendant cette tâche ?** Si l’objectif est de comprendre une boucle, générer toute la boucle peut court-circuiter le travail intéressant. Examiner d’abord une erreur, puis demander un indice ou une explication, laisse une autre place à l’effort.

[^p8-apprendre]: Shen et Tamkin, [*How AI assistance impacts the formation of coding skills*](https://www.anthropic.com/research/AI-assistance-coding-skills), 29 janvier 2026. Étude menée par un fournisseur d’IA ; ses analyses des différentes manières d’interagir avec l’outil sont exploratoires et ne prouvent pas à elles seules un lien causal.

### Fermer l’assistant et ouvrir six lignes

Choisissez l’exercice correspondant à votre parcours. Vous pourrez essayer l’autre ensuite si le sujet vous intéresse.

#### Pour les tâches de travail

Reprenez les documents des Ateliers du quartier, puis fermez la conversation avec l’assistant. Voici une synthèse volontairement incorrecte, écrite pour cet exercice :

> La journée est confirmée le 17 octobre. Nora attend quatre places en Reliure et Léo deux places dans le même atelier. Nous pouvons envoyer les confirmations.

Cherchez dans les sources ce qui permet d’accepter ou de corriger chacune de ces phrases. Le compte rendu récent confirme-t-il la date ? Nora a-t-elle demandé quatre places ? Quel atelier Léo a-t-il choisi ? Qui a décidé des confirmations ? Vous pouvez vous aider de votre propre point, puis ouvrir le corrigé manuel du dossier pour comparer.

La correction garde la date à clarifier entre le 10 et le 17 octobre, deux places pour Nora, deux places sans atelier précisé pour Léo, et aucune confirmation envoyée. Le doublon de Nora n’ajoute aucune place. La note la plus récente ne documente pas une décision qui tranche le désaccord.

Après une autre tâche, essayez une variation : Léo répond « nous serons finalement trois, en Cartographie ». Que modifiez-vous ? Le nombre et le choix de l’atelier changent pour sa demande ; la date et l’autorisation d’envoyer les confirmations restent à vérifier. Être capable d’expliquer ce qui change vous permet de garder la main sur la suite.

#### Pour le développement

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

### Garder de la place pour apprendre au travail

L’IA peut aider à reformuler une erreur, à proposer des cas de test ou à donner un exemple plus petit. Nous pouvons demander un indice avant la solution, puis vérifier l’explication dans la documentation et par une exécution. Une explication agréable à lire reste une réponse à examiner.

Une équipe peut aussi garder des moments où l’on enquête à deux, où l’on présente pourquoi une correction fonctionne et où les débutants écrivent des changements qu’ils peuvent expliquer. Sinon, demander à un junior de « vérifier ce que l’agent a fait » lui confie une responsabilité sans forcément lui donner les moyens de l’exercer.

Les développeurs expérimentés peuvent perdre les mêmes repères. Après plusieurs semaines à déléguer un domaine, saurions-nous encore diagnostiquer sa panne ? L’exercice précédent est volontairement petit ; dans un vrai projet, la reprise peut porter sur un test qui échoue ou un incident réduit.

Quant à l’avenir du métier, les travaux de l’OIT examinent l’exposition de tâches et de métiers aux IA génératives. Ils ne prédisent pas le destin de chaque développeur ni la disparition automatique d’un emploi dès qu’une de ses tâches est exposée.[^p8-oit]

Les décisions d’organisation restent donc centrales : qui reçoit du temps pour apprendre, qui relit, qui arbitre, et que fait-on du temps éventuellement gagné ? Nous pouvons discuter de ces choix maintenant, sans attendre qu’une prédiction sur « la fin des développeurs » se réalise ou se trompe.

[^p8-oit]: OIT, [*Generative AI and Jobs: A Refined Global Index of Occupational Exposure*](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure), 2025.

L’intérêt de l’exercice se voit aussi le lendemain, lorsque nous savons encore expliquer la condition de notification ou corriger une synthèse à partir de ses sources. Ajoutons cette capacité à nos critères quand nous comparerons plusieurs façons d’accomplir une tâche.

## 6. Alternatives, logiciels libres et possibilités de s’en passer

**TL;DR** — Comparons des solutions à une tâche précise, jusqu’au résultat utilisable. Le bilan comprend la préparation, la relecture, la correction et la possibilité de travailler sans IA.

Pour repérer un prix négatif, Python sait déjà comparer deux nombres. Il n’a pas besoin qu’on lui explique gentiment de faire attention.

### Repartir de la difficulté réelle

Ouvrez les trois demandes de `cas/equipe.md`. Pour chacune, essayez d’abord de formuler ce qui est pénible ou fragile aujourd’hui.

| Difficulté | Une première possibilité |
| --- | --- |
| Vérifier les mêmes contraintes sur chaque ligne | Script, contraintes de données ou tests automatisés |
| Retrouver une règle dans quelques pages | Recherche classique ou documentation mieux rangée |
| Oublier des scénarios lors d’une recette | Gabarit, revue par un collègue ou proposition de scénarios par une IA |
| Comprendre un bug inhabituel | Débogueur, documentation, réduction du cas, discussion ou aide ciblée de l’IA |

Le choix peut combiner ces outils. Un modèle peut proposer des scénarios, puis un humain les vérifier et un programme exécuter les assertions. Nous n’avons pas besoin de lui confier également le droit de décider que le résultat est bon.

Pour gagner en autonomie, nous pouvons privilégier des formats exportables, des logiciels libres et des modèles dont les conditions permettent l’usage envisagé. Nous disposerons ainsi de davantage de moyens d’agir sur l’outil. Les données et le travail humain restent à examiner, quelle que soit la licence.

Vous pouvez aussi garder l’IA hors de votre développement. Si les tests manuels sont la partie qui vous épuise, commencez éventuellement par une aide sur leur préparation. Si cette aide ne vous convient pas, un gabarit amélioré peut rester le meilleur résultat de l’expérience.

### Compter jusqu’au résultat utilisable

Choisissez une petite tâche dont vous saurez vérifier le résultat, par exemple préparer les scénarios d’un ticket bien déterminé ou le point d’équipe à partir d’un lot de messages. Avant de commencer, définissez ce que vous attendez : les cas importants, les résultats attendus et les décisions qui doivent rester ouvertes.

Dans `fiches/comparaison.md`, préparez deux essais : l’un sans IA, avec documentation et outils habituels ; l’autre avec l’aide que vous souhaitez examiner. Évitez de faire deux fois exactement le même problème en appelant cela une comparaison équitable : le deuxième essai profite du premier. Deux tâches proches, un ordre alterné sur plusieurs essais et des critères identiques réduisent certains biais, sans transformer notre carnet personnel en étude scientifique.

Notez le temps actif consacré à préparer, produire, relire, corriger et vérifier, sans compter deux fois le même intervalle. Ajoutez séparément l’attente qui vous a réellement bloqué. Si le modèle travaille pendant que vous faites autre chose, ce temps n’est pas une attente bloquante ; vous pouvez le noter dans le commentaire.

Vous pouvez remplir cette comparaison dans un document ou un tableau, sans programme. Le script ci-dessous est une variante facultative pour calculer le bilan fourni :

```bash
python bilan.py exemples/temps-fictifs.json
```

Les nombres du fichier sont **inventés pour montrer le calcul**. Dans ce scénario fictif, l’essai assisté produit plus vite et demande davantage de relecture et de correction : son occupation totale atteint 28 minutes, contre 23 pour l’autre. Aucune comparaison avec un outil réel n’a été réalisée ici.

![Dans cet exemple fictif, la production prend 12 minutes sans IA et 3 avec IA ; les autres étapes portent le total à 23 et 28 minutes.](images/temps.png)
Figure: Durées inventées pour illustrer le calcul, sans comparaison d’outils réels

Si vous utilisez le script, copiez ensuite `exemples/temps-a-remplir.json`, remplacez ses valeurs manquantes par vos observations et lancez-le sur votre copie. Pour le parcours travail, vous pouvez conserver la fiche d’essai remplie à la main. Une durée inconnue reste inconnue dans les deux cas. Conservez aussi le statut du résultat : un travail abandonné ou encore incorrect ne devient pas « meilleur » parce qu’il s’est arrêté plus tôt.

Vous pouvez ouvrir `corriges/comparaison.md` pour examiner les pièges du bilan fictif et la façon de décrire un essai resté incomplet.

### Quand les études ne racontent pas toutes la même chose

Une expérience METR menée en 2025 sur 16 développeurs expérimentés travaillant dans leurs dépôts a mesuré un ralentissement avec les outils alors disponibles. Les participants avaient pourtant l’impression d’être accélérés. Ce résultat appartient à des développeurs, des tâches, des dépôts et des outils précis.[^p8-metr25]

En février 2026, METR explique que son expérience suivante rencontre des biais de sélection et des difficultés de mesure, notamment avec des usages parallèles. L’organisme considère ces nouvelles données insuffisantes pour donner une estimation fiable de l’effet courant. On ne peut donc pas transporter le résultat de 2025 jusqu’à aujourd’hui comme une constante, ni annoncer son contraire avec la même assurance.[^p8-metr26]

Conservons donc nos traces. « J’ai eu l’impression d’aller plus vite » et « le résultat vérifié m’a demandé moins de travail » sont deux observations possibles, qui peuvent diverger.

Le confort compte aussi. Une aide peut rendre une tâche moins pénible sans réduire son temps total, et ce résultat peut très bien nous convenir si nous le décrivons ainsi. Quant au nombre de lignes produites, il renseigne surtout sur le nombre de lignes que quelqu’un devra ensuite comprendre.

Enfin, notre essai doit inclure les personnes qui récupèrent le travail. Si nous économisons vingt minutes en passant une heure de correction à un collègue, nous avons surtout changé l’endroit où le coût apparaît.

[^p8-metr25]: Becker et al., [*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*](https://arxiv.org/abs/2507.09089), 2025.
[^p8-metr26]: METR, [*We are Changing our Developer Productivity Experiment Design*](https://metr.org/blog/2026-02-24-uplift-update/), 24 février 2026.

Le bilan fait apparaître la préparation, les corrections, l’attente et l’état du résultat derrière la vitesse d’apparition du code. Il nous reste à transformer ces observations en décision applicable par l’équipe.

## 7. Construire ses propres critères de choix

**TL;DR** — Une décision courte relie un besoin, des contraintes, une validation et une façon de revenir en arrière. Les critères bloquants passent avant la comparaison des options.

L’équipe aimerait « mettre de l’IA ». Demandons-lui quelque chose d’un peu plus utile : sur quelle tâche, pour quel résultat ?

### Ce qui se discute et ce qui bloque

Reprenez `cas/equipe.md`. Les incidents contiennent des données de clients ; aucun envoi vers un prestataire externe n’a été autorisé dans ce scénario. L’essai devra donc employer d’autres données, une autre configuration ou un autre périmètre, quelle que soit la vitesse annoncée.

![Des exigences bloquantes filtrent d’abord les options. Les options restantes sont comparées sur leurs résultats, leur coût complet et leurs effets sur l’apprentissage.](images/decision.png)
Figure: Une contrainte ne disparaît pas dans une moyenne

Notre fiche commence donc par les exigences bloquantes, sans note sur cent à « l’éthique ». Une formule qui additionnerait prix, confidentialité et confort pourrait masquer une condition que l’équipe juge indispensable.

Écrivez d’abord les exigences : données autorisées, résultat vérifiable, budget de l’essai, personne capable de valider et possibilité de reprendre sans l’outil. Comparez ensuite les options qui restent. Les informations inconnues doivent apparaître comme telles, avec leur conséquence sur la décision.

Un désaccord peut porter sur une valeur plutôt que sur un chiffre manquant. Certaines personnes ne souhaitent pas utiliser un service pour des raisons liées au travail humain ou aux contenus employés. Écoutons ces raisons pour ce qu’elles sont : un benchmark de code ne leur répond pas.

### Écrire une décision que l’on peut appliquer

Ouvrez `fiches/decision.md`. Le document tient en quelques rubriques : besoin, option retenue, données, validation, limites, solution de repli et raison de réexaminer le choix.

Pour le catalogue, nous pouvons choisir les contrôles déterministes fournis dans `catalogue.py`. Si vous suivez le parcours développement, lancez `python catalogue.py` : le fichier fictif contient trois lignes invalides et la commande sort avec le code 1 en indiquant les raisons. Vous pouvez aussi lire directement le corrigé `corriges/catalogue.md`, qui décrit les anomalies et une copie valide. Pour la recette manuelle, nous pouvons essayer une aide à la rédaction sur les documents fictifs, en gardant une relecture et les arbitrages humains. Pour les incidents clients, nous pouvons reporter l’essai tant que le trajet des données et les droits nécessaires ne sont pas établis.

Pour la journée d’ateliers, une décision possible serait de garder l’aide à la préparation du point, de conserver les sources avec chaque demande et de relire le document avant diffusion. La confirmation des places et de la date resterait à l’équipe. Si le volume de messages reste faible, le traitement manuel et le tableau peuvent suffire ; nous n’avons aucune obligation de connecter la messagerie pour terminer l’exercice.

Le script, l’aide à la rédaction et le report de l’essai répondent à trois besoins différents. Vous trouverez cette proposition développée dans `corriges/decision.md` ; d’autres choix peuvent être défendables si leurs conditions sont explicites.

La décision doit aussi dire quand s’arrêter : si l’on ne sait pas vérifier le résultat, si la sortie exige plus de réparation que la procédure habituelle, ou si les données nécessaires dépassent le périmètre accepté. Écrire ces conditions à l’avance évite la boucle de demandes supplémentaires simplement parce que nous avons déjà passé l’après-midi dessus.

Enfin, choisissez ce qui déclenchera une nouvelle lecture de la décision : changement de modèle, de contrat, de données ou problème observé. Inutile de suivre chaque annonce ; surveillez ce qui change réellement votre usage.

### Garder la méthode que l’on peut expliquer

Au début du tutoriel, l’IA pouvait ressembler à une seule grande boîte. Nous avons ouvert plusieurs morceaux : des données, des calculs, un entraînement, un serveur, des outils, des procédures et des personnes qui vérifient le résultat.

Nous pouvons ainsi discuter des critiques sans les balayer. Comprendre le fonctionnement d’un modèle laisse entière la question de sa production et de sa commercialisation. On peut également critiquer cette organisation tout en expérimentant un petit réseau chez soi, en contribuant à un logiciel libre ou en utilisant ponctuellement une aide que l’on juge utile.

Ma méthode n’a pas vocation à devenir votre nouvelle obligation. Votre contexte, votre équipe et ce que vous aimez faire comptent. Vous pouvez reprendre une idée, modifier un skill, garder seulement un outil de recherche ou fermer l’assistant.

Si une expérience vous sert, gardez les fichiers et la raison de ce choix. Si elle échoue, gardez aussi ce qu’elle vous a appris. Dans les deux cas, nous aurons fait un peu mieux que choisir notre organisation de travail au nombre d’étoiles sur GitHub. 🙂

La fiche tient en quelques rubriques, mais elle conserve l’essentiel : l’usage précis, les personnes concernées, la façon de vérifier et les conditions d’arrêt. Refermons maintenant le tutoriel avec ce que ces neuf parties nous permettent de choisir.

## Conclusion

Nous avons commencé par l’histoire de l’IA et quelques repères sur les modèles. Selon le parcours suivi, vous avez ensuite développé avec un assistant, préparé un point d’équipe et un pipeline, ou essayé les deux. Les approfondissements permettent de regarder les calculs, les modèles locaux, les MCP et l’adaptation de plus près. Nous nous retrouvons sur ce que ces usages demandent : du travail humain, des données, des ressources et du temps pour vérifier leurs productions.

Selon moi, leur intérêt tient justement à la possibilité de les adapter à nos besoins. Générer beaucoup de code ou de documents ne suffit pas à justifier que nous réorganisions le métier autour d’un agent. Si l’outil nous éloigne de ce que nous livrons au point de ne plus pouvoir l’expliquer, il a raté sa place.

Vous pouvez continuer sans IA, ou lui réserver une tâche précise dont vous savez vérifier le résultat. Aucun abonnement ne vous oblige à glisser l’outil partout. 🙂

Partez du problème qui vous occupe aujourd’hui. Essayez quelque chose d’assez petit pour en comprendre le résultat. Gardez l’outil s’il vous aide, adaptez-le s’il prend trop de place, ou abandonnez-le si une solution plus simple fait mieux le travail.
