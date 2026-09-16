# Construire et adapter son IA maison

[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)

**TL;DR** — Nous allons retrouver des documents pour répondre à des questions, construire une petite application locale, puis adapter et entraîner un modèle de caractères. Les essais nous permettront aussi de voir ce qui ne fonctionne pas.

Dans la partie précédente, nous avons donné des outils et une procédure à notre agent. Ses poids, eux, n’ont pas changé. Peut-on aller plus loin et fabriquer quelque chose qui corresponde davantage à nos besoins ? Oui, mais « faire son IA » peut désigner des travaux très différents.

Pour commencer, nous allons aider un modèle à retrouver les informations de notre service de prix. Ensuite, nous regarderons ce qui se passe quand on modifie réellement les paramètres d’un réseau. Nous utiliserons alors un modèle minuscule, dont le code et les poids sont fournis : on pourra le réentraîner sur CPU sans attendre une nuit entière.

La recherche et l’entraînement de ce petit modèle ne demandent ni service payant ni carte graphique. La génération documentaire réutilise le serveur local de la partie 3. Une expérience avec un LLM plus grand sur GPU sera préparée séparément ; une RTX 3090 Ti n’est pas un prérequis pour suivre cette partie.

Nous garderons des résultats observables : les passages trouvés, les réponses réellement produites, les poids modifiés et les erreurs conservées. C’est nettement plus utile qu’un nom de modèle qui finit par « expert ». 🙂

## 1. Choisir ce que l’on veut modifier

**TL;DR** — Une information manquante, une procédure mal suivie et un comportement à apprendre ne demandent pas forcément la même intervention.

« Je veux que l’IA connaisse mon projet » est un bon point de départ, mais pas encore une tâche assez précise. Prenons quelques demandes concrètes.

### Qu’est-ce qui manque à notre outil ?

Notre assistant doit répondre à une question sur les notifications. Trois difficultés peuvent se cacher derrière une mauvaise réponse : il n’a pas reçu la règle, il l’a mal interprétée, ou il produit un format inutilisable.

| Besoin | Premier essai raisonnable |
| --- | --- |
| Lire la règle actuelle du service | Donner le document ou le retrouver par une recherche |
| Préparer une recette selon notre façon de travailler | Préciser la procédure, comme dans le skill de la partie 6 |
| Produire régulièrement une forme particulière | Comparer une consigne et des exemples, puis envisager une adaptation si nécessaire |
| Comprendre comment un modèle apprend | Entraîner un petit réseau que l’on peut examiner |

Ces possibilités peuvent se combiner. Un modèle adapté à un format peut encore avoir besoin d’une recherche documentaire pour retrouver une règle récente.

En revanche, modifier ses poids pour chaque changement d’horaire rendrait une simple mise à jour documentaire bien compliquée. Notre première question sera donc : **où l’information devrait-elle vivre ?** Dans une source que l’on consulte, une procédure que l’on suit, ou un comportement que l’on cherche à apprendre ?

Pour les notifications, gardons la règle dans un document versionné. Nous pourrons retrouver sa provenance et la corriger sans réentraîner le modèle.

### Ouvrir les fichiers de la partie

Téléchargez [l’archive de la partie 7](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/main/telechargements/atelier-ia-maison.zip), ou ouvrez `ateliers/07-ia-maison` dans le dépôt. Placez le terminal à côté de `recherche.py`.

Créez un environnement avec Python 3.12 :

```bash
python -m venv .venv
```

Activez-le comme dans les ateliers précédents : `source .venv/bin/activate` sous Bash ou Zsh, `.venv\Scripts\Activate.ps1` sous PowerShell, ou `.venv\Scripts\activate.bat` dans l’invite Windows. Si l’activation PowerShell est refusée, employez directement `.venv\Scripts\python.exe` à la place de `python`.

Installez ensuite les deux dépendances du petit réseau :

```bash
python -m pip install -r requirements.txt
```

La recherche documentaire n’en a pas besoin ; NumPy servira aux calculs du modèle. Le dossier `donnees/documents` contient nos pages fictives, et `donnees/documents.json` indique leur identifiant, leur révision et leur statut.

Ouvrez `temporisation.md`. Il n’y a aucune durée validée pour PRIX-2. Gardez ce détail en tête : nous allons poser la question au modèle plus tard.

### Une recherche n’est pas un entraînement

Nous allons sélectionner des passages, les joindre à une question et demander au modèle de répondre avec ces sources. On parle souvent de **RAG**, pour *Retrieval-Augmented Generation*, ou génération augmentée par recherche documentaire.[^p7-rag]

![Le corpus alimente un index ; la question sert à choisir les passages, puis le modèle reçoit la question et les sources sélectionnées.](images/recherche.png)
Figure: Retrouver des sources avant de générer une réponse

Dans notre application, cet appel ne déclenche aucun entraînement. Le contexte transmis change, les poids restent identiques. Si nous redémarrons sans joindre les documents, ils ne sont pas devenus une connaissance acquise par le modèle.

MCP pourrait exposer notre recherche comme outil, de la même manière que `chercher_documentation` dans la partie 6. Le protocole ne choisirait pas pour autant la méthode de classement des passages : cette méthode appartient au programme derrière l’outil.

Commençons avec peu de documents et une recherche que nous pouvons lire. Une base vectorielle n’est pas un passage obligé pour retrouver dix paragraphes.

[^p7-rag]: Lewis et al., [*Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*](https://arxiv.org/abs/2005.11401). Notre application utilise une recherche lexicale simple ; elle ne reproduit pas le système entraîné dans cet article.

Nous avons choisi une première tâche : retrouver la source utile à une question. Avant de faire intervenir un modèle de langage, vérifions que cette recherche nous mène au bon endroit.

## 2. Construire une recherche dans nos documents

**TL;DR** — Nous allons découper les textes, comparer leurs mots à ceux de la question et conserver les références des passages sélectionnés.

Un document entier peut contenir la bonne information et beaucoup d’autres choses. Essayons de ramener seulement le morceau dont nous avons besoin.

### Garder des morceaux que l’on peut retrouver

Ouvrez `recherche.py` et regardez `charger`. La fonction lit le catalogue des documents, exclut ceux qui sont archivés, puis sépare les textes en paragraphes. Nos pages sont petites et leurs paragraphes portent chacun une idée ; cette découpe suffit pour commencer.

Chaque passage conserve un identifiant comme `notification#2`, son texte, son fichier, son statut, sa révision et l’empreinte du document. Le `#2` désigne le deuxième paragraphe dans cette version. Si nous insérons un nouveau paragraphe, les numéros peuvent changer : c’est pour cela que le journal conserve aussi le texte et la version consultés.

Un morceau trop court pourrait perdre sa condition. Séparer « une remise en stock » de « à prix égal » ferait disparaître précisément ce qui nous intéresse. Un morceau trop long ramènerait des règles sans rapport avec la question. La découpe se juge donc en lisant les passages obtenus.

Le statut est traité **avant** le classement : l’ancienne règle de notification ne doit pas gagner simplement parce qu’elle répète les mots de la question. Nous conservons en revanche le document « à arbitrer », car dire qu’une décision manque est une information utile.

### Des mots à un score de recherche

Commençons par une recherche rudimentaire. Créez `ma_recherche.py` à côté de `recherche.py` et écrivez :

```python
from recherche import charger, mots

question = "remise en stock à prix égal"
attendus = set(mots(question))
for passage in charger():
    communs = attendus & set(mots(passage["texte"]))
    if communs:
        print(len(communs), passage["id"], sorted(communs))
```

Lancez `python ma_recherche.py`. La fonction `mots` du module fourni normalise la casse et les accents, puis écarte quelques mots fréquents comme « le » et « des ». Vous voyez les mots communs qui ont fait remonter chaque passage.

Compter les intersections traite pourtant tous les mots de la même manière. Un terme présent partout distingue peu les documents. Le classement livré dans `Index` utilise **TF-IDF** : la fréquence dans le passage est pondérée par la rareté du mot dans le corpus. Les vecteurs sont ensuite normalisés et comparés par leur produit scalaire, ce qui revient ici à une similarité cosinus.[^p7-tfidf]

Lancez cette version :

```bash
python recherche.py "Une remise en stock à prix égal envoie-t-elle une notification ?" --sortie sorties/recherche.json
```

Le deuxième paragraphe de `notification` doit apparaître en tête. Ouvrez le journal et lisez le texte : **le score aide à classer, il ne certifie pas la réponse**. Le seuil de `0.12` est un choix de cet exercice, pas une probabilité minimale de vérité.

[^p7-tfidf]: Manning, Raghavan et Schütze, [pondération TF-IDF](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html). Notre code utilise une variante lissée de l’IDF.

### Quand les mots ne sont pas les mêmes

Essayez :

```bash
python recherche.py "À quelle heure purge-t-on les fixtures ?" --sortie sorties/recherche-synonymes.json
```

Notre moteur ne trouve rien. Pourtant, `staging.md` explique quand les données de démonstration sont réinitialisées. La question emploie simplement un autre vocabulaire.

Ce manque n’est pas une preuve que l’information n’existe pas. Il décrit une limite de notre recherche. On peut ajouter des synonymes adaptés au domaine, reformuler la question, ou utiliser des embeddings appris pour rapprocher certaines formulations. Mais une proximité sémantique n’est toujours pas une garantie de pertinence : il faudra tester les passages retrouvés.

Pour le constater sans ajouter un modèle, remplacez la question par « Quand les données de staging sont-elles réinitialisées ? », avec un nouveau nom de sortie. Le passage attendu remonte alors.

Notre index est reconstruit en mémoire à chaque lancement. Un corpus plus grand demanderait peut-être de le conserver ; il faudrait alors prévoir sa mise à jour et la suppression des documents retirés. Pour l’instant, gardons cette version simple et mesurons ce qu’elle retrouve réellement.

La recherche réussit sur certaines formulations et échoue sur une autre dont nous connaissons pourtant la réponse. Gardons ce cas : il nous empêchera de confondre une démonstration réussie avec une recherche fiable en général.

## 3. Évaluer les sources avant les réponses

**TL;DR** — Nous allons séparer trois questions : le passage utile a-t-il été retrouvé, la réponse est-elle juste, et ses citations la soutiennent-elles ?

Une seule note « qualité de l’IA » mélangerait ces problèmes. Regardons-les un par un.

### Garder des questions de côté

Le fichier `questions-validation.json` rassemble des questions dont nous connaissons les sources attendues. Il sert à examiner nos choix de recherche. Lancez :

```bash
python evaluer_recherche.py --lot validation --sortie sorties/recherche-validation.json
```

Le rapport indique quels identifiants ont été retrouvés. Il compte la présence d’au moins une source pertinente parmi les trois passages retenus. Il ne mesure ni la précision de chaque passage ni la qualité d’une réponse générée.

Une fois vos choix fixés, lancez le lot de test :

```bash
python evaluer_recherche.py --lot test --sortie sorties/recherche-test.json
```

Dans notre exécution, une source pertinente est présente pour trois des quatre questions de test qui en ont une. La question sur la « purge des fixtures » est manquée. La question hors corpus ne retourne aucun passage.

Ces cinq exemples ne constituent pas un benchmark général. Ils servent à révéler des erreurs concrètes. Si nous ajoutons ensuite des synonymes spécialement pour corriger la question ratée, elle devient un exemple de développement ; il faudra de nouvelles questions pour évaluer ce changement sans lui donner d’avance l’examen.

### Dire ce que l’on n’a pas trouvé

Il y a deux cas à distinguer dans nos documents. Pour l’horaire de staging, la réponse existe mais peut être mal retrouvée. Pour la temporisation de PRIX-2, le document est trouvé et dit précisément que la durée reste à décider.

Notre application pourra dire « aucun passage retrouvé » dans le premier cas. Elle ne devrait pas transformer cela en « cette information n’existe pas ». Dans le second cas, la réponse attendue est une décision ouverte, pas un nombre choisi pour remplir la phrase.

Un seuil de recherche ne tranche pas cette différence. Un score élevé peut rapprocher une question d’un paragraphe qui décrit le problème sans donner la solution. C’est ce qui rend utile le champ `reponse_attendue` du jeu de questions : un humain peut comparer le sens de la réponse aux sources.

Gardez également les questions auxquelles le système devrait s’abstenir. Tester seulement les réponses présentes dans le corpus ne nous apprendrait pas comment il se comporte lorsque les documents sont insuffisants.

### Une citation peut être vraie et mal utilisée

Une réponse pourrait écrire « la durée est de dix minutes [temporisation#2] ». L’identifiant existe, mais le passage dit qu’aucun délai chiffré n’est validé. La citation est présente ; l’affirmation reste fausse.

Notre petit contrôle automatique sait repérer un identifiant qui ne fait pas partie des passages transmis. Il ne sait pas décider si chaque phrase est soutenue par le texte cité. Pour relire une réponse, ouvrez donc la source et comparez l’affirmation exacte, notamment les nombres, les négations et les conditions.

| Observation | Ce qu’elle permet de dire |
| --- | --- |
| Le passage attendu est sélectionné | La recherche a fourni une source utile |
| L’identifiant cité appartient à la sélection | La référence n’a pas été inventée hors de cette sélection |
| La phrase correspond au contenu de la source | Cette affirmation est soutenue par ce passage |
| La source est ancienne ou incomplète | Il reste à vérifier qu’elle s’applique à la question |

Les deux premiers contrôles s’automatisent facilement. Ils ne remplacent pas les suivants. Nous allons maintenant le voir avec une réponse réellement produite par notre modèle local.

Nous savons examiner la recherche sans attribuer ses réussites ou ses échecs au modèle de langage. Passons à l’application complète, en conservant les sources dans son journal.

## 4. Assembler notre assistant documentaire

**TL;DR** — Nous allons relier la recherche au serveur local, puis comparer les réponses avec les passages transmis. Le modèle peut se tromper même lorsque la bonne source est sous ses yeux.

Nous avons les documents et leur classement. Il manque maintenant le petit programme qui fait circuler tout cela.

### Regarder ce que le modèle va recevoir

Commençons sans lancer le serveur :

```bash
python assistant_local.py "Quel délai de temporisation est validé ?" --sortie sorties/contexte-delai.json
```

Ouvrez le fichier produit. `passages` contient les résultats de recherche avec leur provenance. `messages` contient ce qui serait envoyé au modèle : une consigne, puis les passages et la question.

La consigne demande de répondre avec les sources, de citer leurs identifiants et de signaler une décision encore ouverte. Elle précise aussi que les documents sont des données à lire, pas des ordres à exécuter. Vous retrouvez le problème rencontré avec la documentation piégée de la partie 6.

La préparation n’a fait aucun appel réseau. Vous pouvez donc examiner le contexte avant de lancer quoi que ce soit. Si aucun passage n’est retrouvé, le programme le signale et ne demande pas au modèle de combler le vide.

Cela reste une décision de notre application. D’autres usages peuvent avoir besoin d’une réponse générale malgré l’absence de source locale ; ici, nous cherchons une réponse sur les règles de notre service.

### Relier les deux morceaux

Créez `mon_assistant.py` à côté de `assistant_local.py`. Nous réutilisons les fonctions de recherche et d’appel HTTP pour nous concentrer sur l’enchaînement :

```python
import argparse
from assistant_local import preparer, appeler

parser = argparse.ArgumentParser()
parser.add_argument("question")
parser.add_argument("--generer", action="store_true")
args = parser.parse_args()

contexte = preparer(args.question)
if not contexte["passages"]:
    print("Aucun passage retrouvé. Essayez une autre formulation.")
else:
    for passage in contexte["passages"]:
        print(passage["id"], "—", passage["texte"])

    if args.generer:
        reponse = appeler(contexte["messages"])
        print("\nRéponse à relire :")
        print(reponse["texte"])
```
Code: Notre première application documentaire

Essayez d’abord sans génération :

```bash
python mon_assistant.py "Quand les données de staging sont-elles réinitialisées ?"
```

Vous devez voir les sources sélectionnées. Relancez ensuite le [serveur de la partie 3](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/03-modele-local/02-installer/LECTURE.md), depuis le dossier de cet ancien atelier, avec le modèle SmolLM2-360M-Instruct Q8_0, l’alias `atelier-local` et le port `8080`. Gardez ce serveur ouvert dans un autre terminal, puis ajoutez `--generer` à la commande.

Dans `assistant_local.py`, ouvrez maintenant `appeler`. L’application envoie les messages à `http://127.0.0.1:8080/v1/chat/completions` et extrait le texte de la réponse. Le modèle reste servi par `llama-server` ; notre programme ne charge pas lui-même ses poids.

Ce premier fichier laisse apparaître une erreur Python si le serveur est absent. La version fournie gère ce cas et conserve un journal, y compris lorsque l’appel échoue :

```bash
python assistant_local.py "Quand les données de staging sont-elles réinitialisées ?" --appeler --sortie sorties/reponse-staging.json
```

Le journal contient le contexte, la requête et la réponse brute. Utilisez un autre nom de sortie pour chaque essai : le programme refuse d’écraser un fichier existant.

### Le bon document, la mauvaise réponse

Voici deux réponses réellement obtenues avec le modèle de la partie 3, sur CPU. Les journaux complets sont dans `resultats-reference/reponse-staging.json` et `reponse-delai.json`.

À propos de staging :

> Les documents de staging sont réinitialisées chaque mardi à 06 h 00 UTC. Cet horaire concerne uniquement le service fictif de cet atelier.

L’horaire correspond au document. La phrase est maladroite et ne cite aucun identifiant, malgré la consigne. Mais pour la temporisation, nous obtenons ceci :

> Délai de temporisation validé : 10 minutes.

Aïe. Le passage transmis dit pourtant qu’aucune durée n’est validée. Le nombre vient du modèle, pas de notre documentation. Une troisième question sur la baisse de prix produit également une réponse confuse, qui ne restitue pas correctement les conditions.

Nous avons donc une application qui transmet les sources, et un modèle qui ne les exploite pas de manière fiable. La fiche de ce petit modèle indique l’anglais comme langue ; notre utilisation en français ne lui facilite pas la tâche.[^p7-smollm] Cela ne suffit pas à expliquer chaque erreur, et passer à un autre modèle demanderait de rejouer les mêmes questions.

Ne modifiez pas la règle de temporisation pour qu’elle corresponde à sa réponse. 🙂 La suite logique est de conserver cet échec dans nos essais, puis de comparer une autre formulation ou un modèle plus adapté. Le journal permet de vérifier si l’amélioration vient de la recherche, du contexte ou de la génération.

Pour une question très structurée comme un horaire, nous pourrions aussi afficher directement le passage retrouvé. Générer une nouvelle phrase n’est pas toujours nécessaire.

[^p7-smollm]: Hugging Face, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct).

Notre assistant fonctionne comme programme, mais ses réponses ne sont pas assez fiables pour lui confier les décisions du service. Gardons cette différence en tête en passant à une autre expérience : modifier les poids d’un modèle.

## 5. Préparer ce que notre modèle va apprendre

**TL;DR** — Nous changeons de modèle pour pouvoir expérimenter sur CPU. Avant de toucher aux poids, nous séparons les données d’entraînement, de validation et de test.

Entraîner un grand modèle n’est pas nécessaire pour voir comment un réseau apprend. Nous allons utiliser un modèle de caractères suffisamment petit pour lire son code et recommencer nos essais.

### Un terrain de jeu que nous maîtrisons

Ouvrez `donnees/langage/base-train.txt`, puis `adaptation-train.txt`. Le premier contient des phrases de notre service fictif. Le second exprime des situations sous forme de lignes de journal :

```text
INFO produit=... prix=... stock=oui decision=...
```
Code: Forme du deuxième corpus ; les points de suspension représentent ici les valeurs

Ces textes ont été fabriqués à partir de quelques gabarits. Les journaux sont des exemples d’écriture, pas les traces d’un service qui aurait réellement exécuté ces décisions. Notre objectif sera d’apprendre une forme de texte ; ce jeu ne permet pas de conclure que le modèle sait appliquer toutes les règles métier.

Les caractères sont volontairement simples et sans accents. Le vocabulaire fixé dans le code contient 75 caractères, dont un caractère de remplissage. Nous ne sommes plus en train d’adapter SmolLM2 : `petit_modele.py` décrit un autre réseau, créé pour cet atelier.

Ces exemples nous appartiennent et leur licence est fournie. Avec des données réelles, cette étape demanderait déjà du travail : a-t-on le droit de les utiliser, contiennent-elles des données personnelles, des secrets, des réponses erronées ? Plus de lignes n’améliorent pas forcément un mauvais corpus.

### Séparer les exemples avant de les découper

Lancez l’audit :

```bash
python auditer_donnees.py
```

Pour chacun des deux formats, nous avons 180 lignes d’entraînement, 30 de validation et 30 de test. Les identifiants sont répartis avant de fabriquer les fenêtres de caractères : les groupes 10 à 69 servent à l’entraînement, 70 à 79 à la validation et 80 à 89 au test.

Pourquoi cet ordre ? Si nous découpions d’abord une phrase en fenêtres presque identiques, puis les répartissions au hasard, le test pourrait présenter au modèle des morceaux qu’il a déjà vus à un caractère près. Ce serait un examen un peu arrangeant.

L’audit vérifie l’absence de lignes et d’identifiants communs entre les lots. Il ne rend pas pour autant notre test difficile : les mêmes gabarits restent présents dans les trois lots. Nous mesurons donc un apprentissage très limité, sur des formes proches.

L’entraînement lit le lot `train`. La validation sert à observer l’évolution et à choisir les réglages lors du développement. Le test est lu séparément, une fois l’essai fixé. Si vous adaptez vos réglages après avoir étudié ses erreurs, prévoyez ensuite de nouveaux exemples pour l’évaluation finale.

### Partir d’un premier modèle déjà entraîné

Le dossier `resultats-reference/base` contient les poids d’un modèle entraîné sur le premier corpus. Nous referons cet entraînement depuis zéro au chapitre 7. Pour l’instant, essayons ce qu’il produit :

```bash
python petit_modele.py generer --modele resultats-reference/base/modele.npz
```

Le résultat commence comme une phrase du corpus, puis finit par dérailler. C’est normal au sens où nous observons les limites de cette expérience ; ce n’est pas une réponse que nous devrions accepter dans une application.

Nous allons lui faire apprendre les lignes `INFO`. Une première possibilité consiste à continuer l’entraînement en autorisant la modification de tous ses paramètres : c’est ici notre **adaptation complète**.

```bash
python petit_modele.py entrainer --base resultats-reference/base/modele.npz --mode complet --corpus adaptation --pas 800 --sortie sorties/complet
```

Le dossier de sortie doit être nouveau. Il recevra les poids, le rapport et un échantillon généré. Les poids de départ restent dans leur dossier d’origine ; nous pouvons donc toujours revenir à eux.

Cette commande ne garantit pas que le modèle deviendra bon. Elle nous donne un premier résultat auquel comparer une adaptation plus petite, avec beaucoup moins de paramètres entraînables.

Nous avons un corpus, une séparation des lots et une première adaptation complète. Voyons maintenant comment changer le comportement du modèle en laissant ses paramètres de départ figés.

## 6. Ajouter un petit adaptateur

**TL;DR** — LoRA ajoute des matrices entraînables à une transformation existante. Les poids de base peuvent rester figés, mais le comportement du modèle change quand même, parfois dans le mauvais sens.

Peut-on éviter de modifier tous les paramètres à chaque adaptation ? C’est précisément ce que nous allons essayer.

### Une correction ajoutée au calcul

Notre réseau transforme sa représentation interne `h` en scores pour les caractères suivants avec une matrice `U`. Pour l’adapter, nous remplaçons ce calcul par :

```python
scores = h @ (U + A @ B) + c
```

Le symbole `@` désigne un produit de matrices en Python. `U` et le biais `c` restent figés ; seules les matrices `A` et `B` apprennent. C’est le principe d’une adaptation de faible rang, ou **LoRA**.[^p7-lora]

![La sortie additionne le trajet de base figé et la correction passant par deux petites matrices entraînables.](images/lora.png)
Figure: Deux chemins se rejoignent avant le calcul des probabilités

Dans notre cas, `U` comporte 64 × 75 nombres. Avec un rang de 4, `A` contient 64 × 4 nombres et `B`, 4 × 75 : soit 556 paramètres entraînables, au lieu des 15 055 du modèle complet.

Le rang limite la forme de la correction possible. Ce n’est ni un nombre de connaissances ni un niveau d’intelligence. Notre exemple applique LoRA uniquement à la couche de sortie, avec un facteur d’échelle égal à 1 ; une adaptation de LLM peut viser d’autres couches et employer d’autres réglages.

[^p7-lora]: Hu et al., [*LoRA: Low-Rank Adaptation of Large Language Models*](https://arxiv.org/abs/2106.09685).

### Entraîner puis recharger l’adaptateur

Repartons des mêmes poids de base que pour l’adaptation complète :

```bash
python petit_modele.py entrainer --base resultats-reference/base/modele.npz --mode lora --corpus adaptation --pas 800 --rang 4 --sortie sorties/lora
```

Ouvrez `sorties/lora/rapport.json`. Le rapport indique les paramètres entraînables et les empreintes des poids de base avant et après. Elles doivent être identiques : notre entraînement a modifié `A` et `B`, pas les matrices d’origine.

Deux fichiers sont produits. `modele.npz` rassemble le modèle et son adaptateur pour faciliter les essais. `adaptateur.npz` contient seulement la correction et l’empreinte de la base attendue.

Rechargeons ce deuxième fichier avec la base :

```bash
python petit_modele.py generer --modele resultats-reference/base/modele.npz --adaptateur sorties/lora/adaptateur.npz --debut "INFO "
```

Le programme vérifie que les poids de base correspondent. Pour désactiver l’adaptateur, relancez la génération sans `--adaptateur`. Nous retrouvons alors le modèle de départ, sans devoir « désapprendre » ce que nous venons d’ajouter.

C’est pratique, mais cela ne prouve pas que l’adaptateur soit utile. Regardons ses résultats avant de lui donner un nom impressionnant.

### L’amélioration qui cache une régression

Évaluons chaque modèle sur les deux corpus :

```bash
python petit_modele.py evaluer --modele sorties/lora/modele.npz --corpus adaptation --sortie sorties/lora-test-adaptation.json
python petit_modele.py evaluer --modele sorties/lora/modele.npz --corpus base --sortie sorties/lora-test-base.json
```

Faites la même chose avec `sorties/complet/modele.npz`, puis avec `resultats-reference/base/modele.npz`, en choisissant de nouveaux noms de sortie. Sans option `--lot`, cette commande utilise le test.

La **perte** mesure ici à quel point le modèle attribue de mauvaises probabilités aux caractères attendus. Plus elle est basse, mieux il prédit les caractères de ce lot avec leurs vrais caractères précédents. Nous reviendrons sur ce dernier point.

| Modèle | Test sur les phrases initiales | Test sur les lignes `INFO` |
| --- | ---: | ---: |
| Base | 0,48 | 6,08 |
| Base avec LoRA | 8,77 | 0,95 |
| Adaptation complète | 1,76 | 0,84 |

![Les deux adaptations réduisent la perte sur les lignes INFO ; elles augmentent la perte sur les anciennes phrases, surtout avec l’adaptateur LoRA actif.](images/adaptation.png)
Figure: Résultats de notre essai, arrondis ; une barre plus courte indique une perte plus faible

Notre adaptateur améliore donc la prédiction du nouveau format, mais dégrade fortement celle des anciennes phrases. Les poids de base sont restés identiques, et pourtant la sortie du modèle a changé : la correction s’ajoute à chaque passage dans la couche.

Désactiver l’adaptateur permet de retrouver la base. Cela ne supprime pas la régression lorsqu’il est activé. Selon l’usage visé, nous pourrions essayer d’autres données, d’autres réglages ou un autre compromis ; il faudrait alors refaire une évaluation indépendante.

Ces résultats concernent notre minuscule réseau et nos gabarits. Ils ne classent pas LoRA et l’adaptation complète pour tous les modèles. Ils montrent surtout pourquoi nous avons gardé les anciens exemples dans l’évaluation.

Nous savons produire un adaptateur, le recharger et mesurer une régression. Mais nous avons encore utilisé des poids de départ fournis. Il est temps de fabriquer cette base nous-mêmes.

## 7. Entraîner notre réseau depuis zéro

**TL;DR** — Notre réseau prédit le prochain caractère à partir des douze précédents. Nous allons partir de nombres aléatoires, entraîner ses 15 055 paramètres, puis regarder où il échoue.

Tout le modèle tient dans `petit_modele.py`. Il n’a ni outils, ni mémoire documentaire, ni capacité particulière à développer un logiciel. Il nous permet en revanche de voir l’entraînement à une échelle accessible.

### Douze caractères pour deviner le suivant

Prenons un début de phrase : `le produit 2`. Le modèle reçoit les douze caractères et doit attribuer une probabilité à chaque caractère possible pour la suite.

![Douze identifiants de caractères deviennent douze vecteurs de douze nombres, puis une représentation de 64 nombres et enfin 75 probabilités.](images/modele.png)
Figure: Le réseau utilisé dans cet atelier

Chaque caractère devient un identifiant, puis un vecteur de douze nombres grâce à la table `E`. Nous réunissons ces vecteurs en 144 nombres. Une couche de 64 unités les transforme avec `tanh`, puis la couche de sortie produit 75 scores. `softmax` les convertit en probabilités.

Les tableaux `E`, `W`, `b`, `U` et `c` contiennent au total 15 055 paramètres. Les petits `b` et `c` sont des biais, ajoutés aux transformations. C’est un réseau à fenêtre fixe, pas un Transformer : il n’a aucun mécanisme d’attention et ne peut pas examiner le début d’une phrase situé au-delà de ses douze caractères d’entrée.

Dans `charger_lot`, chaque ligne donne plusieurs couples entrée/cible. Au début d’une ligne, un caractère spécial remplit les places encore vides. Une fenêtre ne passe jamais de la fin d’une ligne au début de la suivante.

Ouvrez `calculer` pour retrouver ces transformations dans le code. Les noms courts correspondent aux matrices du schéma ; les dimensions permettent de suivre les produits sans devoir deviner ce que contient chaque tableau.

### Des nombres aléatoires aux premières régularités

Lancez cette fois la commande sans `--base` :

```bash
python petit_modele.py entrainer --pas 1200 --sortie sorties/depuis-zero
```

Le programme initialise les paramètres, lit le corpus de base et effectue 1 200 mises à jour. À chaque pas, il sélectionne un petit lot de fenêtres, prédit les caractères suivants, calcule la perte et ajuste les paramètres.

La perte pénalise les probabilités trop faibles attribuées aux caractères attendus. La rétropropagation calcule comment chaque paramètre contribue à cette erreur. L’optimiseur Adam utilise ces gradients pour choisir les mises à jour. Ici, leurs calculs sont écrits avec NumPy ; les tests comparent également quelques gradients à des variations numériques de la perte.

Regardez `rapport.json`. Dans l’exécution fournie, la perte de validation passe d’environ 4,31 à 0,17. Le réseau a appris des régularités de nos phrases. Nous n’avons pas inscrit à la main chaque probabilité de caractère dans ses poids.

Pour rejouer l’essai avec moins de pas, choisissez un autre dossier de sortie. Comparez alors la validation et les échantillons. Gardez le test pour évaluer le réglage finalement retenu ; sinon, il devient progressivement un deuxième lot de validation.

La graine aléatoire et les versions des dépendances sont indiquées dans les fichiers. Elles rendent les essais plus faciles à reproduire, sans promettre une identité numérique sur toutes les machines.

### Pourquoi une petite perte peut produire du charabia

Ouvrez `echantillon.txt`. L’échantillon fourni commence ainsi :

```text
le produit 27 revient en stock. son prix reste a 50 centimes. le service prepare une notification.
```
Code: Début réellement généré par notre modèle de base

La phrase ressemble à notre corpus, mais son sens pose déjà problème : elle prépare une notification après un simple retour en stock à prix inchangé. Puis la génération se détériore. Avec l’adaptateur, l’échantillon commence par `INFO produit=28 prix=44`, avant de partir lui aussi dans une suite incohérente.

Comment peut-on obtenir cela avec une perte en baisse ? Pendant l’évaluation, nous donnons au modèle les **vrais caractères précédents**. Pendant la génération, il reçoit progressivement ses **propres caractères produits**. Une erreur peut donc l’amener dans un contexte qu’il a peu rencontré, puis en provoquer d’autres.

Ajoutons la courte fenêtre, le petit réseau et les gabarits très répétitifs : nous sommes loin d’un assistant capable de comprendre notre service. La génération tire aussi les caractères selon les probabilités produites, avec une graine fixée pour nos échantillons.

Notre essai a réussi à entraîner un modèle et à changer ses prédictions. Il n’a pas produit un générateur fiable de règles ou de journaux. Conserver les deux observations nous évite de transformer une courbe encourageante en promesse que les sorties ne tiennent pas.

Nous avons entraîné de vrais paramètres, mais sur une tâche volontairement minuscule. Voyons maintenant ce que cette expérience permet de préparer sur une autre machine, et ce qu’elle ne permet pas de promettre.

## 8. Choisir la suite sans changer de machine par défaut

**TL;DR** — La recherche et le petit entraînement restent accessibles sur CPU. L’adaptation d’un LLM demande une autre préparation ; la mémoire nécessaire dépend aussi de l’entraînement, pas seulement du fichier de poids.

Après ces essais, la bonne question n’est pas forcément « quel modèle plus gros puis-je faire tourner ? ». Nous avons déjà plusieurs problèmes précis à résoudre.

### Ce qui a réellement tourné ici

| Expérience | Matériel utilisé ici | Ce que nous avons observé |
| --- | --- | --- |
| Recherche dans les paragraphes | CPU | Une question reformulée échappe à la recherche lexicale |
| Réponses avec SmolLM2-360M-Instruct Q8_0 | CPU, serveur local | Une réponse correcte sur l’horaire, un délai inventé, une réponse confuse sur le prix |
| Entraînement du modèle de caractères | CPU | La perte baisse ; la génération reste mauvaise |
| Adaptation complète et LoRA de ce petit réseau | CPU | Le nouveau format est mieux prédit ; l’ancien se dégrade |
| Adaptation d’un LLM sur RTX 3090 Ti | À faire sur la machine locale | Aucun résultat annoncé pour cet atelier |

Ces usages n’ont pas le même coût. Notre réseau de caractères tient dans de petits tableaux. Le modèle documentaire contient beaucoup plus de paramètres, mais nous l’utilisons pour des appels courts. Nous ne lui demandons pas de conduire une session de développement avec de longs contextes et des appels d’outils répétés.

Un petit essai d’inférence sur CPU ne démontre donc pas qu’un agent de code sera agréable à utiliser sur la même machine. Pour travailler sur un dépôt, gardez les critères pratiques de la partie 4 : qualité des modifications, temps d’attente, contexte utile et vérification du résultat.

### Préparer une expérience sur la 3090 Ti

La machine prévue pour la suite dispose d’une RTX 3090 Ti de 24 Go et de 64 Go de RAM. Avant de choisir une recette d’entraînement, il faudra vérifier son système, ses pilotes et la mémoire réellement disponible.

Le fichier de poids ne représente pas toute la mémoire nécessaire. L’entraînement conserve aussi des informations pour calculer les gradients et mettre à jour les paramètres. La longueur des séquences, la taille des lots, la précision numérique et les couches adaptées changent le budget.[^p7-memoire]

LoRA réduit le nombre de paramètres entraînés, mais le calcul traverse toujours une partie du modèle de base. On ne peut donc pas déduire la consommation totale de mémoire de la seule taille du fichier d’adaptateur.

Le dossier `experience-gpu` contient un prompt à donner à Codex sur la machine. Il demande de commencer par un essai court, avec un modèle et une révision identifiés, de mesurer la mémoire, puis de sauvegarder et recharger l’adaptateur dans un nouveau processus. Il prévoit aussi la comparaison avec la base et la recherche de régressions.

Cette fois, les bibliothèques d’entraînement comme Transformers et PEFT remplaceront notre petit calcul NumPy.[^p7-peft] Le GGUF de la partie 3 n’est pas le fichier de départ de cette procédure : il faudra récupérer des poids compatibles avec la méthode d’entraînement choisie.

Vous pouvez poursuivre le tutoriel sans réaliser cette expérience GPU. Nos essais CPU permettent déjà de distinguer un document ajouté au contexte, un adaptateur et un modèle entraîné depuis zéro.

[^p7-memoire]: Hugging Face, [mémoire et optimisation des LLM](https://huggingface.co/docs/transformers/main/en/llm_tutorial_optimization).
[^p7-peft]: Hugging Face, [prise en main de PEFT](https://huggingface.co/docs/peft/main/en/quicktour).

### Revenir au besoin de départ

Si notre problème est de retrouver une règle récente, la recherche documentaire reste un bon endroit où travailler. Nous pouvons enrichir les questions, améliorer les formulations ou comparer une autre méthode de recherche.

Si les passages sont corrects mais que le modèle invente la réponse, ce n’est plus le même chantier. Il faut examiner la génération, ses consignes et le modèle utilisé. Pour certaines réponses, afficher la source ou calculer le résultat directement sera plus simple.

Si nous voulons apprendre une forme stable à partir de nombreux exemples, une adaptation peut valoir un essai. Nous savons maintenant qu’il faut regarder les anciennes tâches autant que la nouvelle, et lire les sorties en plus des métriques.

Enfin, entraîner un petit réseau peut être un excellent moyen de comprendre ces mécanismes, même lorsque son résultat n’est pas utilisable en production. Nous avons le droit d’expérimenter pour apprendre. Nous avons aussi le droit de constater qu’un script ordinaire répond mieux au besoin. 🙂

Reste une question que les fichiers de poids ne résolvent pas : que choisissons-nous de faire de ces outils ? Les données utilisées, les personnes concernées, la dépendance à un service et les ressources consommées comptent autant dans cette décision. Ce sera le sujet de la dernière partie.

Gardez les journaux et les exemples ratés avec les résultats encourageants. Ils nous disent où porter le prochain effort, sans confondre une expérience instructive avec un outil prêt à être déployé.

## Conclusion

Nous avons fait trois choses différentes : retrouver des informations, construire une application qui les transmet à un modèle, puis modifier les paramètres d’un petit réseau.

La recherche n’a pas toujours retrouvé le bon passage. Le modèle documentaire a inventé une durée malgré la présence de la bonne source. L’adaptateur a amélioré un format tout en dégradant l’ancien. Ces résultats ne nous empêchent pas d’avancer : ils rendent les prochaines modifications beaucoup plus concrètes.

Nous pouvons désormais choisir quoi changer à partir d’un problème observé. Et si nous décidons d’entraîner un modèle plus grand, nous aurons déjà les habitudes utiles : séparer les données, garder une référence, rejouer les essais et lire ce qui est réellement produit.
