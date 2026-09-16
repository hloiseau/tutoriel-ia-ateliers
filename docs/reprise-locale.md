# Reprendre sur le PC de Hugo

Ouvrir un clone à jour de `hloiseau/tutoriel-ia-ateliers` dans Codex local, puis copier le [prompt coordinateur des expériences](prompts/LOCAL-COORDINATEUR.md). Il contient le contexte nécessaire à une nouvelle conversation, les règles de préparation et les livrables attendus.

La machine annoncée possède une RTX 3090 Ti de 24 Go et 64 Go de DDR4 3200. Le système d’exploitation reste à relever. Les [missions par atelier](prompts/local/README.md) couvrent les parties 2 à 7 et une observation humaine facultative pour la partie 8. Les [expériences restantes](experiences-a-lancer.md) distinguent les références déjà exécutées des validations à faire.

La réécriture générale dispose d’un [autre prompt](prompts/RELECTURE-COORDINATEUR.md), avec huit sous-agents et le [guide de voix de Hugo](prompts/GUIDE-VOIX-HUGO.md). L’assistant local transmettra ses preuves et ses corrections au coordinateur éditorial pour éviter les modifications concurrentes.

Les rapports publics des nouveaux essais iront dans `docs/experiences-locales/`, dans des sous-dossiers datés. Ce chemin sera créé lors des premières exécutions ; sa mention ici n’atteste pas qu’elles ont eu lieu.
