# Consignes proposées pour l’atelier

## Comprendre

Lis README.md, suivi.py, test_suivi.py et TICKET.md. Explique le chemin entre le fichier JSON et la décision. Cite les fonctions concernées. N’édite aucun fichier pendant cette lecture. Signale les questions auxquelles les fichiers ne répondent pas.

## Préparer les tests

À partir du ticket, propose une table de cas puis écris les tests manquants dans test_ticket.py. Ne modifie pas suivi.py. Lance python -m unittest discover -v et rapporte les échecs observés.

## Corriger

Applique le changement de comportement décrit par le ticket. Conserve les interfaces existantes et limite la modification au code nécessaire. Ne change pas les réponses attendues des tests pour les faire passer. Lance la suite, puis montre le diff et explique la condition modifiée.

## Relire

Relis le diff par rapport au ticket et aux cas limites. Pour chaque problème trouvé, donne un scénario reproductible et le comportement attendu. Ne modifie pas les fichiers pendant cette revue et ne publie aucun commentaire externe.
