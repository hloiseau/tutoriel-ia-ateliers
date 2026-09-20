# 2. Licences, transparence et possibilités de vérification

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : D’où viennent les données et le travail humain ?](../01-travail/LECTURE.md) · [Suivant : Coûts, énergie, matériel et environnement](../03-ressources/LECTURE.md)

**TL;DR** — Télécharger des poids, lire le code et réutiliser un système demandent des droits et des fichiers différents. Le mot « open » ne remplit pas notre fiche à notre place.

« C’est ouvert, donc on peut tout faire avec. » Voilà une phrase qui mérite qu’on ouvre au moins le fichier de licence.

## De quoi parle la licence ?

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

## Ce que l’ouverture rend possible

La définition *Open Source AI* 1.0 de l’Open Source Initiative associe les libertés d’utiliser, d’étudier, de modifier et de partager à plusieurs éléments accessibles : paramètres, code et informations détaillées sur les données d’entraînement. Elle ne demande pas que toutes les données soient distribuées sans exception ; elle précise les informations attendues pour comprendre et reconstruire un système substantiellement équivalent.[^p8-osi]

Ce cadre explicite se prête à l’examen. Il décrit des libertés et les éléments nécessaires pour les exercer ; les conditions de travail, la consommation et la justesse des réponses demandent leurs propres informations.

L’ouverture peut nous donner des prises utiles. Si nous pouvons exécuter le modèle ailleurs, inspecter les étapes et modifier le programme, nous avons davantage de moyens d’expérimenter et de continuer sans le service d’origine. Encore faut-il disposer du matériel, du temps et des compétences nécessaires.

Ces libertés peuvent aussi s’exercer collectivement. Une équipe, une association ou un hébergeur peut porter une partie du travail. Quitter un grand fournisseur ne vous condamne donc pas à devenir administrateur système tous les week-ends. 🙂

[^p8-osi]: Open Source Initiative, [*The Open Source AI Definition — 1.0*](https://opensource.org/ai/open-source-ai-definition).

## Examiner un modèle que nous avons déjà utilisé

Reprenez SmolLM2 dans `fiches/provenance.md`. Nous avons déjà une raison d’être précis : le modèle utilisé dans les parties 3 et 8 est le 360M *Instruct*, avec un fichier GGUF déterminé, pas n’importe quel membre de sa famille.

Notez la référence, la licence annoncée, la langue indiquée, les liens vers les informations de préparation et ce que vous avez effectivement testé. La dernière colonne doit permettre de reconnaître la provenance de chaque affirmation : « indiqué par l’auteur », « vérifié dans notre essai » ou « pas établi avec les éléments consultés ».

Par exemple, l’étiquette de langue anglaise provient de la fiche. La durée de temporisation inventée vient d’un journal d’exécution conservé dans l’atelier de la partie 8 : une réponse y donne une durée alors que sa source la laisse ouverte. Vous pouvez consulter cette observation sans rejouer l’essai. Ni l’une ni l’autre ne prouve que toutes les réponses en français seront fausses. Elles nous donnent en revanche une raison concrète de ne pas valider cet usage sur la foi du nom du modèle.

Une piste de correction est disponible dans `corriges/provenance.md`. Elle contient peu de cases remplies, volontairement : mieux vaut trois informations retrouvables qu’un tableau très convaincant où l’on a deviné le reste.

Vous pouvez refaire le même travail avec un autre modèle. Gardez sa révision lorsqu’elle est disponible. Si vous changez de fichier ou de service, relisez les conditions correspondantes au lieu de transporter automatiquement la conclusion précédente.

Notre fiche dit maintenant quels éléments nous pouvons obtenir, étudier ou modifier, et quelles informations restent à établir. Le coût de l’outil mérite la même précision : une facture, une mesure électrique et un impact environnemental racontent trois choses différentes.

---

[Précédent : D’où viennent les données et le travail humain ?](../01-travail/LECTURE.md) · [Suivant : Coûts, énergie, matériel et environnement](../03-ressources/LECTURE.md)
