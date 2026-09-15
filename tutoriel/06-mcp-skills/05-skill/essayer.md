Dans VS Code, copiez le dossier complet `skills/preparer-recette` dans `.github/skills/`, à la racine du dossier d’atelier ouvert. Vous devez obtenir `.github/skills/preparer-recette/SKILL.md`, avec son sous-dossier `references` à côté. Cet emplacement est pris en charge pour les skills de projet.[^p6-vscode-skill]

Si `/preparer-recette` apparaît dans le chat, sélectionnez-le puis demandez :

> Prépare la recette de PRIX-1 avec le MCP atelier-tickets. Présente-la dans la conversation.

Avec un autre assistant, utilisez son emplacement de skills ou demandez explicitement la lecture du fichier fourni. Cette dernière possibilité permet d’essayer les instructions, même sans découverte automatique du dossier. Elle ne valide pas le mécanisme d’activation du produit.

Dans la réponse, cherchez des cas concrets. Le retour en stock à prix égal doit être distingué du retour en stock accompagné d’une baisse. L’indisponibilité nouvelle doit aussi être couverte. Un tableau très long qui répète seulement « le système fonctionne correctement » ne nous aide pas beaucoup. 😅

Comparez la proposition avec `attendus-recette.md`. Ce document contient des cas rédigés pour l’exercice. Les données y sont en centimes, comme dans nos conventions. Il explique aussi ce qui manque pour exécuter une vraie recette : notre jeu ne décrit ni interface de staging ni compte ni moyen d’observer un envoi.

La préparation peut donc être utile sans prétendre que les tests ont eu lieu. Pour annoncer un résultat, il faudrait encore disposer de l’application et jouer les scénarios.

[^p6-vscode-skill]: [Utiliser les skills dans VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills).
