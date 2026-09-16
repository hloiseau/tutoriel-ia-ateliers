# Mission locale — partie 7, application documentaire et adaptation sur GPU

Applique le [prompt coordinateur](../LOCAL-COORDINATEUR.md). Lis `ateliers/07-ia-maison/README.md`, `tutoriel/07-ia-maison/VERIFICATION.md`, les chapitres et le protocole ciblé `ateliers/07-ia-maison/experience-gpu/PROMPT-CODEX.md`. Ce dernier reste fourni dans l’archive de l’atelier ; les consignes ci-dessous détaillent son exécution et les preuves attendues.

## 1. Reproduire le socle

Rejoue l’audit des données, les tests et la recherche documentaire dans un dossier de sorties neuf. Préserve les lots d’entraînement, de validation et de test. Vérifie que le moteur de recherche utilise bien les documents autorisés et que les citations pointent vers les passages transmis au modèle.

Interroge réellement l’application avec le serveur local. Conserve les documents retrouvés, le contexte envoyé et la réponse complète. La référence contient notamment une durée de dix minutes inventée par le modèle : ne corrige pas discrètement cette trace pour faire paraître l’application fiable. Observe si ton essai reproduit cette erreur ou en produit une autre.

Rejoue les petits entraînements NumPy, base et LoRA. Ils illustrent l’adaptation d’un petit modèle ; leurs pertes par caractère ne sont pas directement comparables à la perte par token d’un LLM. Conserve cette distinction dans les futurs résultats.

## 2. Préparer une véritable adaptation de LLM

L’objectif est un petit essai reproductible d’adaptation de forme sur le corpus synthétique prévu. Il ne s’agit pas de promettre un agent de code maison.

Choisis un petit modèle de base dont l’identifiant, la révision, les poids et la licence sont accessibles. SmolLM2-360M-Instruct assure une continuité possible avec le serveur, avec les limites de français déjà signalées. Justifie un changement de modèle si les essais l’imposent. Le GGUF quantifié d’inférence ne remplace pas le checkpoint prévu par la chaîne d’entraînement.

Vérifie les versions compatibles dans les documentations officielles de Transformers et PEFT. Isole et fige l’environnement réellement utilisé. N’installe pas un nouveau pilote graphique. Écris un script d’entraînement minimal, lisible, avec paramètres explicites, et un script d’évaluation/rechargement que le lecteur pourra exécuter.

Sépare les lots avant de fabriquer les fenêtres ou exemples dérivés, pour éviter qu’un même document contamine plusieurs lots. Garde le test final à l’écart des choix d’hyperparamètres. Prépare aussi quelques anciennes tâches pour détecter une dégradation après adaptation.

## 3. Mesurer un essai court

Affiche les paramètres entraînables et leur proportion, les modules ciblés, le rang LoRA, la précision, la longueur de séquence, le batch effectif et le nombre maximal d’étapes. Commence par un passage avant/arrière et mesure la mémoire avant d’engager l’essai complet. Réduis le budget si la marge manque ; conserve les incidents au lieu de relancer jusqu’à obtenir un résultat présentable.

Compare sur les mêmes entrées : base, adaptateur activé, adaptateur désactivé. Garde les conditions de génération, les sorties autoregressives complètes, les pertes par token, les temps, la mémoire et les causes d’arrêt. Une baisse de perte seule ne prouve pas une meilleure réponse utile. Utilise des critères définis avant la lecture des résultats.

Sauvegarde l’adaptateur et sa configuration, avec la révision exacte du modèle de base requise. Ne duplique pas les poids dans Git. Recharge dans un nouveau processus et refais l’évaluation ; si tu compares numériquement les sorties, précise une tolérance adaptée à la précision et au calcul utilisé, sans promettre une identité bit à bit sur tout GPU.

## 4. Rendre l’expérience publiable

Fournis scripts, dépendances, commandes, configuration, données synthétiques ou leurs références, journaux expurgés et résultats. Les poids lourds restent hors Git. Indique clairement la taille et les prérequis de téléchargement pour le lecteur.

Écris le passage pratique du chapitre seulement à partir de l’expérience accomplie. Une adaptation décevante peut constituer un résultat instructif ; ne l’efface pas au profit d’une conclusion enthousiaste. Le parcours CPU existant doit rester accessible. Signale les limites de généralisation depuis cette seule 3090 Ti et les étapes non exécutées.
