# 8. Choisir la suite sans changer de machine par défaut

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Entraîner notre réseau depuis zéro](../07-entrainer/LECTURE.md)

**TL;DR** — La recherche et le petit entraînement restent accessibles sur CPU. L’adaptation d’un LLM demande une autre préparation ; la mémoire nécessaire dépend aussi de l’entraînement, pas seulement du fichier de poids.

Après ces essais, la bonne question n’est pas forcément « quel modèle plus gros puis-je faire tourner ? ». Nous avons déjà plusieurs problèmes précis à résoudre.

## Ce qui a réellement tourné ici

| Expérience | Matériel utilisé ici | Ce que nous avons observé |
| --- | --- | --- |
| Recherche dans les paragraphes | CPU | Une question reformulée échappe à la recherche lexicale |
| Réponses avec SmolLM2-360M-Instruct Q8_0 | CPU, serveur local | Une réponse correcte sur l’horaire, un délai inventé, une réponse confuse sur le prix |
| Entraînement du modèle de caractères | CPU | La perte baisse ; la génération reste mauvaise |
| Adaptation complète et LoRA de ce petit réseau | CPU | Le nouveau format est mieux prédit ; l’ancien se dégrade |
| Adaptation d’un LLM sur RTX 3090 Ti | À faire sur la machine locale | Aucun résultat annoncé pour cet atelier |

Ces usages n’ont pas le même coût. Notre réseau de caractères tient dans de petits tableaux. Le modèle documentaire contient beaucoup plus de paramètres, mais nous l’utilisons pour des appels courts. Nous ne lui demandons pas de conduire une session de développement avec de longs contextes et des appels d’outils répétés.

Un petit essai d’inférence sur CPU ne démontre donc pas qu’un agent de code sera agréable à utiliser sur la même machine. Pour travailler sur un dépôt, gardez les critères pratiques de la partie 4 : qualité des modifications, temps d’attente, contexte utile et vérification du résultat.

## Préparer une expérience sur la 3090 Ti

La machine prévue pour la suite dispose d’une RTX 3090 Ti de 24 Go et de 64 Go de RAM. Avant de choisir une recette d’entraînement, il faudra vérifier son système, ses pilotes et la mémoire réellement disponible.

Le fichier de poids ne représente pas toute la mémoire nécessaire. L’entraînement conserve aussi des informations pour calculer les gradients et mettre à jour les paramètres. La longueur des séquences, la taille des lots, la précision numérique et les couches adaptées changent le budget.[^p7-memoire]

LoRA réduit le nombre de paramètres entraînés, mais le calcul traverse toujours une partie du modèle de base. On ne peut donc pas déduire la consommation totale de mémoire de la seule taille du fichier d’adaptateur.

Le dossier `experience-gpu` contient un prompt à donner à Codex sur la machine. Il demande de commencer par un essai court, avec un modèle et une révision identifiés, de mesurer la mémoire, puis de sauvegarder et recharger l’adaptateur dans un nouveau processus. Il prévoit aussi la comparaison avec la base et la recherche de régressions.

Cette fois, les bibliothèques d’entraînement comme Transformers et PEFT remplaceront notre petit calcul NumPy.[^p7-peft] Le GGUF de la partie 3 n’est pas le fichier de départ de cette procédure : il faudra récupérer des poids compatibles avec la méthode d’entraînement choisie.

Vous pouvez poursuivre le tutoriel sans réaliser cette expérience GPU. Nos essais CPU permettent déjà de distinguer un document ajouté au contexte, un adaptateur et un modèle entraîné depuis zéro.

[^p7-memoire]: Hugging Face, [mémoire et optimisation des LLM](https://huggingface.co/docs/transformers/main/en/llm_tutorial_optimization).
[^p7-peft]: Hugging Face, [prise en main de PEFT](https://huggingface.co/docs/peft/main/en/quicktour).

## Revenir au besoin de départ

Si notre problème est de retrouver une règle récente, la recherche documentaire reste un bon endroit où travailler. Nous pouvons enrichir les questions, améliorer les formulations ou comparer une autre méthode de recherche.

Si les passages sont corrects mais que le modèle invente la réponse, ce n’est plus le même chantier. Il faut examiner la génération, ses consignes et le modèle utilisé. Pour certaines réponses, afficher la source ou calculer le résultat directement sera plus simple.

Si nous voulons apprendre une forme stable à partir de nombreux exemples, une adaptation peut valoir un essai. Nous savons maintenant qu’il faut regarder les anciennes tâches autant que la nouvelle, et lire les sorties en plus des métriques.

Enfin, entraîner un petit réseau peut être un excellent moyen de comprendre ces mécanismes, même lorsque son résultat n’est pas utilisable en production. Nous avons le droit d’expérimenter pour apprendre. Nous avons aussi le droit de constater qu’un script ordinaire répond mieux au besoin. 🙂

Reste une question que les fichiers de poids ne résolvent pas : que choisissons-nous de faire de ces outils ? Les données utilisées, les personnes concernées, la dépendance à un service et les ressources consommées comptent autant dans cette décision. Ce sera le sujet de la dernière partie.

Gardez les journaux et les exemples ratés avec les résultats encourageants. Ils nous disent où porter le prochain effort, sans confondre une expérience instructive avec un outil prêt à être déployé.

---

[Précédent : Entraîner notre réseau depuis zéro](../07-entrainer/LECTURE.md)
