# Vérification de la partie 8

Première rédaction du 16 septembre 2026, à relire par l’auteur.

## Exercices exécutés

L’archive pratique a été extraite dans un dossier distinct puis exécutée sous Linux avec Python 3.12.14, sans installation de dépendance. Le [journal](../../docs/verifications-partie8/executions.json) contient les neuf commandes, les sorties, les codes attendus et l’empreinte SHA-256 du ZIP.

- Huit tests unitaires passent. Ils couvrent le temps complet, les durées absentes ou non finies, la conservation du statut incomplet, la conversion Wh/kWh, un booléen employé comme prix et un identifiant dupliqué.
- Le calcul hypothétique de 200 W pendant 30 minutes donne 100 Wh, soit 0,1 kWh.
- Le bilan fictif donne 23 et 28 minutes. Les libellés conservent son caractère fictif ; aucune comparaison d’outils réels n’en découle.
- Le modèle de bilan non rempli est refusé avec le code 2 : une durée absente n’est pas traitée comme zéro.
- L’exercice de notification échoue sur le prix égal, comme annoncé ; le corrigé et la variante à 100 centimes passent. Le bloc de code du chapitre présente le même bug que le fichier fourni.
- Le catalogue contient trois lignes invalides ; une copie corrigée selon les indications produit zéro erreur.

Les erreurs attendues sont distinguées des échecs du parcours. Aucun des scripts ne contacte un modèle ou un service extérieur.

## Sources et présentation

Les références primaires sont recensées dans [sources.json](sources.json). Les chapitres distinguent le témoignage d’une travailleuse, la définition OSI, les recommandations de la CNIL, les publications environnementales et les expériences sur le travail des développeurs. Les résultats METR de 2025 sont accompagnés de la mise à jour méthodologique de février 2026.

Quatre illustrations originales ont été ouvertes et inspectées. Le graphique des durées est construit à partir du JSON fictif livré, sans donnée de productivité présentée comme réelle. La [passe adverse](../../docs/relecture-partie8.md) documente les points de cohérence examinés.

## Limites

Aucune mesure électrique sur le matériel, aucune comparaison avec et sans assistant, aucune évaluation d’apprentissage sur des lecteurs n’a été effectuée pour cette partie. Le carnet et les corrigés permettent de mener ces observations ; ils ne donnent pas d’avance leur résultat.

Windows et macOS n’ont pas été exécutés. Le contrôle des fichiers, liens locaux, notes et images ne remplace pas un import et une relecture dans l’interface ZdS. Aucun tutoriel n’a été publié sur ZdS depuis cette session.
