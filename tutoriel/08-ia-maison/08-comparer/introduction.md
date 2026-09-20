**TL;DR** — La recherche, les trois appels documentaires et les entraînements du petit réseau ont tourné sur CPU. L’adaptation d’un LLM sur GPU reste à exécuter ; son budget mémoire ne se déduit pas de la seule taille des poids.

Nos essais ont laissé plusieurs pistes très concrètes : une formulation que la recherche manque, une durée inventée et une forte régression avec LoRA. Avant de choisir un modèle plus gros, décidons lequel de ces problèmes nous voulons réellement résoudre.
