# Prompts de reprise du tutoriel

Ces documents servent aux assistants qui vont poursuivre le travail. Ils ne sont pas importés dans ZdS.

| Besoin | Document à ouvrir et transmettre à l’assistant |
| --- | --- |
| Rejouer les expériences sur le PC de Hugo | [LOCAL-COORDINATEUR.md](LOCAL-COORDINATEUR.md) |
| Reprendre seulement une expérience | [Missions locales](local/README.md) |
| Faire la grosse passe de rédaction | [RELECTURE-COORDINATEUR.md](RELECTURE-COORDINATEUR.md) |
| Comprendre la voix de Hugo et la pédagogie attendue | [GUIDE-VOIX-HUGO.md](GUIDE-VOIX-HUGO.md) |
| Donner une mission à chaque sous-agent de relecture | [MISSION-PARTIE.md](MISSION-PARTIE.md) |

Ouvrir un clone à jour de `hloiseau/tutoriel-ia-ateliers`. Copier le prompt du coordinateur choisi dans l’assistant ; les autres fichiers sont référencés à l’intérieur. Les chemins sont relatifs à la racine du dépôt. Les prompts restent utilisables dans une nouvelle conversation, sans accéder à celle où le tutoriel a été rédigé.

La relecture demande **huit sous-agents, un par partie**. Le coordinateur gère aussi l’introduction générale, les annexes, les raccords et l’intégration. Si l’outil limite le nombre d’agents simultanés, il procède par vagues en conservant huit missions distinctes.

Les expériences locales peuvent commencer séparément. Pour éviter les conflits, leur assistant possède les scripts et les preuves ; le coordinateur éditorial possède les textes. Ils travaillent sur des branches distinctes et échangent leurs commits ou leurs rapports. L’état courant des expériences reste dans les rapports de vérification de chaque partie.
