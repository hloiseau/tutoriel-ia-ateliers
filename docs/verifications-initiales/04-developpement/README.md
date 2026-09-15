# Vérifications de l’atelier de développement

Exécutions sous Linux, Python 3.12.14, bibliothèque standard. Les commandes et leurs sorties complètes sont dans `executions.json`.

- `01-depart` : 3 tests passent, retour en stock à prix identique => vrai.
- `02-test-rouge` : 13 tests, 2 échecs (retour en stock à prix identique et avec hausse).
- `03-corrige` : 13 tests passent ; les trois scénarios donnent faux, vrai, faux.
- Mutation `<` en `<=` : suite en échec.
- Suppression de la condition de disponibilité : suite en échec.

Les sorties sont de vraies exécutions du code. Les prompts n’ont pas été testés auprès d’un agent externe ; aucune génération n’est attribuée à un produit. Windows, macOS et l’import ZdS restent à vérifier. Les illustrations ont été inspectées et le HTML contrôlé structurellement, sans rendu complet dans un navigateur réel.
