# Vérifications de cette révision

Date du relevé documentaire : **14 septembre 2026**.

## Réalisé

- Consultation des pages officielles citées dans les extraits pour les tarifs, fonctionnalités, installations et fichiers de configuration.
- Lecture du README de l’atelier et de `01-depart/suivi.py` dans le dépôt, à la révision `b95165289276a45bc299d0826e3c540727e8e203`.
- Raccord au serveur HTTP de la partie 3 : adresse, port, alias et longueur de contexte explicités.
- Distinction entre la connexion avec SmolLM2 et le premier essai de code avec Qwen2.5-Coder-1.5B-Instruct.
- Aucun résultat de ce nouveau modèle présenté comme une exécution observée.
- Contrôle structurel des nouveaux extraits et de leurs références dans le fragment de manifest.
- Conservation de la séparation entre documents de rédaction et fichiers destinés à ZdS.

## Restant à exécuter

L’environnement local n’était pas disponible pour cette révision. Les vérifications antérieures du serveur et de l’atelier Python ne valident pas les nouvelles intégrations.

1. Installer VS Code et parcourir l’activation de Copilot Free avec un compte éligible ; vérifier les libellés visibles et le rôle Ask.
2. Installer Continue, charger les deux configurations YAML et vérifier la réponse de chaque serveur.
3. Télécharger le GGUF Qwen, consigner sa révision et son empreinte ; mesurer la mémoire utilisée et vérifier le lancement avec le binaire de llama.cpp de la partie 3.
4. Exécuter la demande de lecture avec Qwen sur CPU. Vérifier que les budgets de contexte et de sortie suffisent ; ajuster selon les observations.
5. Vérifier le parcours sans connexion Internet après installation et téléchargement.
6. Importer dans un brouillon ZdS le ZIP construit depuis les sources centralisées ; l’intégration des sources et la construction du ZIP ont été réalisées le 15 septembre 2026.
7. Vérifier le rendu des tableaux, notes et légendes, puis le passage vers les six chapitres conservés.

Le parcours GPU reste une variante future. Aucune vitesse, compatibilité Windows/macOS ou réussite d’agent autonome n’est déduite de la seule documentation.

## Périmètre du comparatif

Panorama d’éditeurs, de services et de harness, étendu à Pi, Kilo Code, goose, Amp, Mistral Vibe, Kiro et OpenHands. Roo Code et la transition de Gemini CLI sont également situés. Comparaison de solutions représentatives, tarifs individuels mensuels affichés en USD, sans conversion monétaire ni tarif d’entreprise. Les notes pointent vers les sources officielles, qui pourront évoluer après ce relevé. Les fonctionnalités citées ne constituent pas un benchmark.

Les transitions de noms et les interruptions temporaires d’offres sont signalées lorsqu’elles affectent le choix ou l’installation. Aucun ancien quota n’est réutilisé comme s’il était encore valable.

## Extension du panorama

Les fonctionnalités et tarifs des outils supplémentaires sont documentés par les sources officielles citées dans les extraits. Aucun de ces harness supplémentaires n’a été installé ni comparé par un benchmark dans cette session. Leur notoriété ne sert pas de classement de qualité ou d’adoption mesurée.

## Intégration du 15 septembre 2026

Les six chapitres d’origine sont désormais récupérés et les trois nouveaux chapitres insérés dans le manifest courant. Les raccords sont appliqués. `outils/assembler_tutoriel.py` a vérifié les références et construit les lectures et les ZIP ; les installations d’assistants restent à rejouer.

## Correction du périmètre CPU

La relecture a identifié une promesse non étayée : les transitions présentaient la discussion avec Qwen 1,5B sur CPU comme une autre voie pour tout l’atelier. Cette équivalence est retirée. Le parcours hébergé devient le parcours principal ; la discussion CPU reste une expérience facultative non exécutée. Le rôle `chat` dans la configuration est distingué du mode Chat sélectionné dans l’interface.

Avant toute recommandation pratique locale, relever le matériel, les versions, le modèle et sa quantification, le contexte effectif, la mémoire, le délai initial et la durée totale. Conserver les réponses et vérifier leur exactitude sur l’atelier. Si un mode agent est essayé, conserver aussi ses appels d’outils, erreurs, corrections et résultats de tests. Un chargement réussi ou une réponse courte ne suffit pas.

Cette correction ne constitue pas une nouvelle validation des tarifs, des interfaces ou des autres affirmations de la partie 4.
