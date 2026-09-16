# Prompt — reprendre les expériences sur mon PC

Ouvrir le clone du dépôt dans Codex local, puis copier le texte ci-dessous. Le système d’exploitation sera relevé par l’assistant : il n’est pas supposé connu.

---

Tu travailles sur mon PC pour vérifier et compléter les expériences du tutoriel **« Comprendre l’IA et développer avec elle »**, par Hugo Loiseau. Le dépôt est `hloiseau/tutoriel-ia-ateliers`. Je possède une **RTX 3090 Ti de 24 Go et 64 Go de DDR4 3200**. Vérifie la configuration réelle avant de choisir les commandes.

Je veux que tu réalises les essais, conserves les preuves et corriges les procédures à partir de ce qui se passe réellement. Avance sur tout ce qui est faisable sans attendre ma validation à chaque commande. Si un accès, une manipulation physique ou un budget manque, termine les autres travaux puis indique précisément ce qu’il te faut. La grande passe de style sera faite séparément ; tu t’occupes ici des expériences et de leur reproductibilité.

## 1. Lire et préparer

Commence par les instructions du dépôt, l’état Git, `SOMMAIRE.md`, `docs/etat-des-contenus.md`, `docs/verification.md` et `docs/experiences-a-lancer.md`. Lis ensuite `docs/prompts/local/README.md`, les missions choisies, les rapports `VERIFICATION.md` des parties concernées et les scripts avant de les lancer.

Travaille sur une branche ou un worktree dédié. Préserve mes fichiers, mes modifications, mes autres projets et mes configurations d’assistants. Note le commit de départ. N’utilise pas de commande destructive pour « nettoyer » l’environnement. Ne modifie pas le pilote graphique, l’installation système de Python ou les paquets globaux. Préfère des environnements isolés et un dossier d’expériences distinct. N’arrête pas un service existant pour récupérer son port ; choisis un autre port et note l’adaptation.

Fais un diagnostic ciblé : système et version, architecture, shell, CPU, Python disponible, GPU, pilote, RAM et VRAM libres, espace disque, outils déjà installés. Évite les inventaires inutiles susceptibles de révéler des informations privées. La présence d’un GPU ou d’un paquet CUDA ne prouve pas que le processus l’utilise.

Lis les contraintes de licences et les conditions des modèles choisis. Utilise les données publiques ou fictives du dépôt. Aucun fichier de mon entreprise, token, historique de navigateur ou projet privé ne doit servir de donnée d’entraînement, de contexte de test ou de pièce jointe à une API.

## 2. Parcours de travail

Les missions détaillées sont dans `docs/prompts/local/`. Suis cet ordre, en sautant seulement les étapes effectivement bloquées :

1. **02-apprentissage.md** : reproduire l’apprentissage sur CPU et essayer la page de dessin dans un vrai navigateur.
2. **03-modele-local.md** : reproduire le serveur CPU, puis comparer le même modèle sur GPU.
3. **04-developpement.md** : parcourir l’exercice de développement et observer un véritable assistant ; vérifier séparément les interfaces documentées.
4. **05-agents.md** : recueillir des observations réelles en complément du banc déterministe.
5. **06-mcp-skills.md** : construire le MCP, le brancher à un assistant et essayer le skill.
6. **07-adaptation.md** : reproduire les expériences CPU et préparer une adaptation LoRA de LLM sur le GPU.
7. **08-observation.md** : proposer le protocole facultatif avec/sans IA ; il nécessite ma participation et ne doit pas bloquer le reste.

Il faut suivre les étapes du lecteur et vérifier leurs transitions, pas seulement exécuter le corrigé final. Quand le tutoriel demande de construire un fichier progressivement, pars de l’état initial prévu. Conserve chaque état utile et le premier échec avant correction. Ne montre pas d’avance le corrigé à un assistant dont tu veux observer la résolution du problème.

Les expériences GPU sont séquentielles afin d’éviter les conflits de mémoire et les mesures faussées. Tu peux déléguer une lecture ou un audit si ton environnement le permet, mais aucun second agent ne doit entraîner un modèle en même temps ni modifier le même fichier sans coordination. La flotte obligatoire concerne la réécriture, pas ces mesures.

## 3. Choisir des budgets réalistes

Commence par les petites expériences déjà documentées. Vérifie la taille avant un téléchargement. Réutilise les poids valides déjà présents et enregistre leur origine et leur empreinte ; ne les ajoute pas dans Git.

Pour un modèle plus grand ou une nouvelle adaptation, définis avant le lancement une taille de téléchargement, une longueur de contexte, un nombre limité d’étapes et une marge de mémoire. Mesure d’abord un petit passage avant/arrière. Ajuste le budget à partir de cette mesure. Un manque de mémoire doit conduire à revoir le protocole, pas à multiplier les essais au point de planter le bureau.

N’engage pas une nouvelle dépense, un abonnement ou une location de GPU sans budget autorisé. L’usage d’un service déjà configuré doit respecter les autorisations de la session. Quand aucune voie payante n’est autorisée, continue les essais locaux et marque la variante hébergée comme non exécutée. N’invente ni tarif ni quota disponible.

Une configuration capable de répondre à quelques phrases sur CPU ne devient pas automatiquement un agent de développement utilisable. Évalue chaque usage sur les tâches prévues et conserve les délais et les erreurs, y compris quand ils rendent l’usage peu intéressant.

## 4. Conserver des preuves exploitables

Crée un dossier daté `docs/experiences-locales/<date>-<machine-ou-essai>/` pour les rapports publics, avec des sous-dossiers par partie. Utilise le modèle `docs/prompts/local/RAPPORT-TYPE.md`. Les gros artefacts et les journaux privés restent dans le dossier local d’expériences, hors des fichiers suivis. Ne remplace jamais les `resultats-reference` existants par tes nouveaux résultats sans décision explicite et justifiée.

Pour chaque essai, conserve au minimum :

- identifiant de l’essai et date, commit du dépôt, état initial ;
- versions du système, de Python, du moteur, des dépendances et de l’assistant utiles à la reproduction ;
- modèle, révision, fichier de poids et empreinte quand disponibles ;
- dossier courant, commande exacte, options, variables pertinentes expurgées de secrets ;
- données d’entrée, prompt exact et historique nécessaire ;
- stdout, stderr, code de retour, réponse complète, diff produit ;
- configuration de génération et causes d’arrêt visibles ;
- mesures avec leur définition, méthode et unité ;
- ce qui a échoué, ce qui a changé pour réussir, ce qui reste non exécuté.

Sépare **observation**, **déduction**, **information de documentation**, **estimation** et **exemple fictif**. Les scripts de test qui renvoient une réponse factice n’ont pas interrogé le modèle. Les journaux MCP de l’atelier sont des réponses du SDK, pas forcément une capture brute du transport. Une commande écrite dans un rapport n’est « exécutée » que si son exécution a réellement été observée.

Ne donne un délai avant le premier token que si tu disposes du streaming ou d’une instrumentation appropriée. Sinon, indique la durée totale et laisse cette mesure indisponible. Distingue mémoire réservée, mémoire allouée et occupation totale du GPU. Le TDP ne fournit pas une mesure d’énergie consommée. Le débit du serveur et le temps global perçu par le client sont deux mesures différentes.

Avant publication, relis les journaux pour retirer secrets, noms de chemins personnels et données étrangères à l’atelier. Garde la trace des occultations : remplace les valeurs sensibles par des marqueurs explicites. Préserve les originaux privés localement si cela reste approprié. Ne réécris pas une réponse erronée pour la rendre publiable ou « représentative ».

## 5. Corriger le tutoriel avec les résultats

Corrige les commandes, prérequis et procédures qui ont effectivement posé problème. Pour les interfaces ou API qui ont changé, vérifie la documentation officielle correspondant à la version utilisée. Ne transpose pas la configuration MCP de VS Code telle quelle à Codex : vérifie le format de l’outil réellement installé. N’invente pas des commandes de lancement de sous-agents ou des options de CLI.

Écris les corrections dans les petits Markdown indiqués par les manifests. Les `LECTURE.md` et les archives sont générés. L’auteur veut conserver une voie accessible sans GPU coûteux ; une expérience facultative sur ma 3090 Ti doit rester présentée comme telle.

Le style attendu est dans `docs/prompts/GUIDE-VOIX-HUGO.md`. Pour ce travail, garde les corrections éditoriales limitées à ce que les essais imposent. La réécriture globale aura son propre agent. Si elle tourne en parallèle, travaille sur ta branche et transmets au coordinateur le commit des preuves et les passages à corriger avant toute modification concurrente.

Ne transforme pas un résultat isolé en promesse générale de rapidité, d’apprentissage ou de qualité. Si l’adaptation dégrade le modèle ou si le skill ne se déclenche pas, c’est un résultat utile à documenter.

## 6. Terminer proprement

Exécute les tests pertinents après une correction de code. Rejoue le passage corrigé depuis son état de départ, puis régénère les livrables concernés. Depuis la racine :

```bash
python outils/assembler_tutoriel.py --exports telechargements/zds
python outils/assembler_global.py
```

Si un atelier change, consulte l’aide de `outils/assembler_annexes.py` et reconstruis son archive. Vérifie les fichiers ajoutés avant de committer : aucun poids, cache, environnement Python, token ou journal privé. Mets à jour les rapports de vérification concernés avec la configuration exacte testée ; une validation sur mon PC ne valide pas Windows, Linux et macOS à la fois.

Prépare des commits cohérents et un bilan avec : essais réussis, échecs conservés, corrections, liens vers les preuves, étapes bloquées et éventuelles actions attendues de moi. Publie la branche de travail sur GitHub si les accès et autorisations de la session le permettent ; jamais de push forcé ni d’import ZdS automatique. Un refus d’accès ne doit pas faire perdre les modifications locales.

Ne t’arrête pas au premier obstacle si d’autres missions peuvent avancer. Ne me demande pas si tu peux « continuer » après chaque petit essai. En revanche, signale clairement un besoin réel de budget, d’accès ou d’intervention humaine.
