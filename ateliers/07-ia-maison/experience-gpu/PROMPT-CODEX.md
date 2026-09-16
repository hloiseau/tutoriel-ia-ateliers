# Reprendre les expériences sur la machine de l’auteur

Prompt à transmettre à un agent local, depuis le dépôt `hloiseau/tutoriel-ia-ateliers`. Travail prévu pour la partie 7 ; aucun résultat GPU n’est encore validé.

> Tu travailles sur les expériences de la partie 7 du tutoriel, dans une branche dédiée. Lis son rapport de vérification, le README de `ateliers/07-ia-maison`, puis les scripts avant de proposer des changements.
>
> La machine annoncée possède une RTX 3090 Ti de 24 Go et 64 Go de RAM DDR4. Commence par vérifier le système, le pilote, la mémoire vidéo réellement disponible et l’environnement Python. N’installe pas un pilote et ne modifie pas l’environnement global. Prépare un environnement isolé.
>
> Rejoue d’abord l’audit des données, les tests NumPy et le client documentaire avec le serveur local existant. Conserve les résultats, les temps et les erreurs. N’écrase aucun journal précédent.
>
> Prépare ensuite un premier essai d’adaptation LoRA d’un LLM. Utilise d’abord un petit modèle dont la licence et les poids de base sont identifiés ; SmolLM2-360M-Instruct permet de garder un lien avec l’expérience précédente, mais son français est limité. Le GGUF quantifié de l’inférence ne doit pas être pris pour le checkpoint d’entraînement. Vérifie les API courantes de Transformers et PEFT dans leurs documentations officielles et épingle les versions utilisées ainsi que la révision du modèle.
>
> L’objectif initial est d’observer une adaptation de forme sur le corpus synthétique de logs, pas de promettre un agent de code. Préserve les lots séparés et compare aussi des exemples du domaine initial. Affiche les paramètres entraînables, fixe un budget court d’étapes et une longueur de séquence limitée avant le lancement. Commence par un passage avant/arrière pour mesurer le pic de VRAM, puis lance le petit essai seulement si la machine garde une marge raisonnable. N’ajoute pas de données de l’entreprise.
>
> Mesure le modèle avant adaptation, avec l’adaptateur, puis avec l’adaptateur désactivé. Conserve les pertes par token, les sorties complètes, les raisons d’arrêt, les temps et la mémoire. Ne compare pas directement la perte par token du LLM avec la perte par caractère du modèle NumPy.
>
> Sauvegarde uniquement l’adaptateur, sa configuration, le modèle de base requis et les résultats nécessaires. Vérifie son rechargement dans un nouveau processus. Note toute régression et toute étape qui manque encore ; ne transforme pas un échec ou un essai non exécuté en procédure validée. Propose les changements de chapitre à partir des résultats obtenus, sans republier sur ZdS.

Sources de départ : [PEFT](https://huggingface.co/docs/peft/main/en/quicktour), [LoRA](https://huggingface.co/docs/peft/main/package_reference/lora), [modèle SmolLM2](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct).
