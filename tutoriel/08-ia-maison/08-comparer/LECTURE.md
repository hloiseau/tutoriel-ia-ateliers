# 8. Choisir la suite sans changer de machine par défaut

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Entraîner notre réseau depuis zéro](../07-entrainer/LECTURE.md)

**TL;DR** — La recherche, les trois appels documentaires et les entraînements du petit réseau ont tourné sur CPU. L’adaptation d’un LLM sur GPU reste à exécuter ; son budget mémoire ne se déduit pas de la seule taille des poids.

Nos essais ont laissé plusieurs pistes très concrètes : une formulation que la recherche manque, une durée inventée et une forte régression avec LoRA. Avant de choisir un modèle plus gros, décidons lequel de ces problèmes nous voulons réellement résoudre.

## Ce qui a réellement tourné ici

| Expérience | Matériel utilisé ici | Ce que nous avons observé |
| --- | --- | --- |
| Recherche dans les paragraphes | CPU | Une question reformulée échappe à la recherche lexicale |
| Réponses avec SmolLM2-360M-Instruct Q8_0 | CPU, serveur local | Une réponse correcte sur l’horaire, un délai inventé, une réponse confuse sur le prix |
| Entraînement du modèle de caractères | CPU | La perte baisse ; la génération reste mauvaise |
| Adaptation complète et LoRA de ce petit réseau | CPU | Le nouveau format est mieux prédit ; l’ancien se dégrade |
| Adaptation d’un LLM sur RTX 3090 Ti | À faire sur la machine locale | Aucun résultat annoncé pour cet atelier |

Ces usages n’ont pas le même coût. Notre réseau de caractères tient dans de petits tableaux. Le modèle documentaire contient beaucoup plus de paramètres ; nous l’avons seulement utilisé pour trois appels courts, sans longue session ni appels d’outils répétés.

Ces trois réponses sur CPU ne disent donc rien du confort d’un agent de code sur la même machine. Pour travailler sur un dépôt, reprenez les critères pratiques de la partie 4 : qualité des modifications, temps d’attente, contexte utile et vérification du résultat.

## Préparer une expérience sur la 3090 Ti

La machine prévue pour cette expérience dispose d’une RTX 3090 Ti de 24 Go et de 64 Go de RAM. Nous n’avons pas encore identifié son système ni exécuté l’adaptation. Avant de choisir une recette d’entraînement, il faudra vérifier le système, les pilotes et la mémoire réellement disponible.

Le fichier de poids ne représente pas toute la mémoire nécessaire. L’entraînement conserve aussi des informations pour calculer les gradients et mettre à jour les paramètres. La longueur des séquences, la taille des lots, la précision numérique et les couches adaptées changent le budget.[^p7-memoire]

LoRA réduit le nombre de paramètres entraînés, mais le calcul traverse toujours une partie du modèle de base. On ne peut donc pas déduire la consommation totale de mémoire de la seule taille du fichier d’adaptateur.

Le dossier `experience-gpu` contient un protocole de reprise à donner à un agent de code sur cette machine. Il demande de commencer par un essai court, avec un modèle et une révision identifiés, de mesurer la mémoire, puis de sauvegarder et recharger l’adaptateur dans un nouveau processus. Il prévoit aussi la comparaison avec la base et la recherche de régressions. Tant que ce protocole n’a pas été exécuté, il ne constitue ni une procédure validée ni un résultat.

Lors de cet essai, des bibliothèques d’entraînement comme Transformers et PEFT remplaceront notre petit calcul NumPy.[^p7-peft] Le GGUF de la partie 3 ne servira pas de fichier de départ : il faudra récupérer des poids compatibles avec la méthode d’entraînement choisie.

Vous pouvez poursuivre le tutoriel sans cette expérience GPU. Les essais CPU que nous venons de faire suffisent pour distinguer un document ajouté au contexte, un adaptateur et un modèle entraîné depuis zéro.

[^p7-memoire]: Hugging Face, [mémoire et optimisation des LLM](https://huggingface.co/docs/transformers/main/en/llm_tutorial_optimization).
[^p7-peft]: Hugging Face, [prise en main de PEFT](https://huggingface.co/docs/peft/main/en/quicktour).

## Revenir au besoin de départ

Pour retrouver une règle récente, travaillons d’abord sur la recherche documentaire. La question « purge des fixtures » nous donne déjà un cas à conserver pendant que nous enrichissons les formulations ou comparons une autre méthode.

Lorsque les bons passages sont présents et que le modèle invente tout de même dix minutes, le chantier se déplace vers la génération, ses consignes et le modèle utilisé. Pour certaines réponses, afficher la source ou calculer directement le résultat sera plus simple.

Une adaptation peut valoir un essai pour apprendre une forme stable à partir de nombreux exemples. Notre régression sur les anciennes phrases nous a appris à garder ces tâches dans l’évaluation, et le charabia généré à lire les sorties en plus des métriques.

Enfin, entraîner un petit réseau aide à comprendre ces mécanismes, même lorsque son résultat reste inutilisable en production. Nous pouvons expérimenter pour apprendre, puis constater honnêtement qu’un script ordinaire répond mieux au besoin. 🙂

Les fichiers de poids ne décident cependant pas de la place que nous voulons donner à ces outils. Les données utilisées, les personnes concernées, la dépendance à un service et les ressources consommées vont maintenant entrer dans le choix : c’est le sujet de la dernière partie.

Gardez les journaux et les exemples ratés avec les résultats encourageants. Ensemble, ils indiquent où porter le prochain effort. La dernière partie élargit maintenant la question : voulons-nous consentir cet effort, avec quelles données, quelles dépendances et quelles conséquences ?

---

[Précédent : Entraîner notre réseau depuis zéro](../07-entrainer/LECTURE.md)
