# 2. Licences, transparence et possibilités de vérification

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : D’où viennent les données et le travail humain ?](../01-travail/LECTURE.md) · [Suivant : Coûts, énergie, matériel et environnement](../03-ressources/LECTURE.md)

**TL;DR** — Télécharger des poids, lire du code et pouvoir réutiliser un système sont trois choses à examiner séparément. Le mot « open » ne remplit pas notre fiche à notre place.

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

Une licence permissive annoncée pour le moteur ne s’étend pas automatiquement au modèle que l’on charge. Inversement, utiliser une interface propriétaire n’efface pas la licence du modèle situé derrière.

Pour SmolLM2-360M-Instruct, la fiche annonce Apache 2.0.[^p8-carte-licence] Nous pouvons le noter avec son lien et la date de consultation. Cela ne constitue pas, à lui seul, un audit de tous les contenus ayant servi à l’entraînement. Pour redistribuer une combinaison précise de fichiers, il faut lire les textes qui leur sont effectivement applicables, avec leurs notices et conditions.[^p8-apache]

Le but de notre exercice est de retrouver ces éléments. Un badge sur une page d’accueil est un début de piste ; ce n’est pas encore le dossier de notre application.

[^p8-apache]: Apache Software Foundation, [texte de la licence Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0), notamment les conditions de redistribution. La portée dépend des éléments effectivement placés sous cette licence.

[^p8-carte-licence]: Hugging Face, [fiche de SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct), licence annoncée à la consultation de septembre 2026.

## Ce que l’ouverture rend possible

La définition *Open Source AI* 1.0 de l’Open Source Initiative associe les libertés d’utiliser, d’étudier, de modifier et de partager à plusieurs éléments accessibles : paramètres, code et informations détaillées sur les données d’entraînement. Elle ne demande pas que toutes les données soient distribuées sans exception ; elle précise les informations attendues pour comprendre et reconstruire un système substantiellement équivalent.[^p8-osi]

C’est un cadre explicite, que nous pouvons examiner, plutôt qu’une impression donnée par un nom. Il ne faut pas pour autant confondre ce cadre avec une garantie de bonnes conditions de travail, de faible consommation ou de réponses justes.

L’ouverture peut nous donner des prises utiles. Si nous pouvons exécuter le modèle ailleurs, inspecter les étapes et modifier le programme, nous avons davantage de moyens d’expérimenter et de continuer sans le service d’origine. Encore faut-il disposer du matériel, du temps et des compétences nécessaires.

Une liberté que l’on peut exercer collectivement reste intéressante même si l’on ne veut pas tout refaire seul. Une équipe, une association ou un hébergeur peut porter une partie de ce travail. L’alternative à un grand fournisseur n’est pas forcément de devenir, à soi seul, administrateur système tous les week-ends. 🙂

[^p8-osi]: Open Source Initiative, [*The Open Source AI Definition — 1.0*](https://opensource.org/ai/open-source-ai-definition).

## Examiner un modèle que nous avons déjà utilisé

Reprenez SmolLM2 dans `fiches/provenance.md`. Nous avons déjà une raison d’être précis : le modèle utilisé dans les parties 3 et 7 est le 360M *Instruct*, avec un fichier GGUF déterminé, pas n’importe quel membre de sa famille.

Notez la référence, la licence annoncée, la langue indiquée, les liens vers les informations de préparation et ce que vous avez effectivement testé. Dans la dernière colonne, séparez trois formulations : « indiqué par l’auteur », « vérifié dans notre essai » et « pas établi avec les éléments consultés ».

Par exemple, l’étiquette de langue anglaise provient de la fiche. La durée de temporisation inventée vient de notre journal d’exécution. Ni l’une ni l’autre ne prouve que toutes les réponses en français seront fausses. Elles nous donnent en revanche une raison concrète de ne pas valider cet usage sur la foi du nom du modèle.

Une piste de correction est disponible dans `corriges/provenance.md`. Elle contient peu de cases remplies, volontairement : mieux vaut trois informations retrouvables qu’un tableau très convaincant où l’on a deviné le reste.

Vous pouvez refaire le même travail avec un autre modèle. Gardez sa révision lorsqu’elle est disponible. Si vous changez de fichier ou de service, relisez les conditions correspondantes au lieu de transporter automatiquement la conclusion précédente.

Nous pouvons maintenant dire plus précisément ce qui est ouvert et ce qui reste à établir. Regardons une autre information souvent résumée trop vite : le coût de l’outil.

---

[Précédent : D’où viennent les données et le travail humain ?](../01-travail/LECTURE.md) · [Suivant : Coûts, énergie, matériel et environnement](../03-ressources/LECTURE.md)
