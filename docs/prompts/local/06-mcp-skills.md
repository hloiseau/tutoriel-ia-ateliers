# Mission locale — partie 6, construire et utiliser son MCP et son skill

Applique le [prompt coordinateur](../LOCAL-COORDINATEUR.md). Lis `ateliers/06-mcp-skills/README.md`, `tutoriel/06-mcp-skills/VERIFICATION.md` et les sept chapitres. Le serveur et le client ont déjà été testés ; l’intégration interactive et l’usage par un modèle restent à observer.

## 1. Rejouer la construction

Prépare un environnement isolé à partir des dépendances figées. La référence utilise le SDK MCP 2.2.0 ; vérifie le fichier courant. N’installe pas aveuglément la dernière version pour contourner un problème.

Suis le chapitre 3 depuis un `mon_serveur.py` vide, en ajoutant les étapes et les trois tests du lecteur. Les six états intermédiaires fournis servent de secours. Vérifie que les commandes du client portent bien `--serveur mon_serveur.py` et que les journaux identifient le serveur construit.

Rejoue inventaire, tickets, recherche, document, conventions et refus d’écriture. Utilise des noms de journaux nouveaux. Le client lance son propre serveur stdio : inutile de démarrer un deuxième serveur dans un terminal.

Le script `outils/verifier_construction_mcp.py` peut compléter le contrôle du parcours, mais inspecte ses destinations avant de le lancer : il produit des traces de vérification. Exécute-le dans une copie isolée si nécessaire pour préserver les références existantes. Les tests du serveur fourni vérifient le corrigé ; ils ne remplacent pas les tests de ton propre fichier.

## 2. Relier à l’assistant

Génère la configuration avec `configuration.py --serveur mon_serveur.py`. Les chemins obtenus sont privés et propres à la machine ; ne les commite pas. Si tu utilises VS Code, conserve les autres entrées de `.vscode/mcp.json`. Si tu utilises Codex ou un autre produit, vérifie son format courant dans sa documentation officielle : les clés JSON de VS Code ne sont pas universelles.

Observe le démarrage, la liste des outils et les erreurs éventuelles. Demande réellement au modèle de consulter PRIX-1, sa documentation et les conventions. Garde sa réponse et les appels visibles. Vérifie ensuite PRIX-2 et ses questions encore ouvertes. Une erreur attendue sur un outil d’écriture inexistant doit rester distinguée d’une panne de transport.

Le serveur expose des lectures ; son processus garde les permissions du compte qui le lance. N’en déduis pas que l’ensemble de l’assistant est incapable d’écrire par un autre outil.

## 3. Essayer le skill

Installe dans le périmètre de l’atelier le dossier complet `skills/preparer-recette`, références comprises, à l’emplacement reconnu par le produit testé. Préserve tout skill existant et relève le format et la version du produit.

Vérifie séparément la découverte automatique du skill et l’exécution de sa procédure. Si tu dois demander explicitement la lecture de `SKILL.md`, tu peux tester les consignes ; tu n’as pas validé la découverte automatique.

Utilise une session neuve pour chaque ticket. Compare les propositions aux critères de `attendus-recette.md` sans donner d’avance ce corrigé au modèle. Cherche les sources consultées, les données manquantes, les questions à arbitrer, les scénarios et les résultats attendus. Conserve les erreurs et les oublis.

Fais ensuite une seule adaptation de consigne répondant à un problème réellement constaté. Rejoue le ticket concerné, puis l’autre pour repérer une régression. L’analogie de la recette de cuisine doit se traduire ici par une règle adaptée à un besoin, pas par une promesse que toutes les consignes seront suivies.

## Livrable

Rapport séparant SDK et transport testés, serveur construit, intégration produit, découverte du skill et comportement du modèle. Donne les versions, traces expurgées, prompts, recettes réellement produites, comparaison aux critères et corrections. Aucun faux dialogue de démonstration ne doit prendre la place d’un essai manquant.
