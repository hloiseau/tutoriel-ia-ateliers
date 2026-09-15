# Vérifications de la partie 6

Exécutées le **15 septembre 2026**, sous Linux, Python **3.12.14**, SDK MCP **2.2.0**. Les exemples concernent des tickets et des documents fictifs.

## Exécuté

- Archive `atelier-mcp-skills.zip` extraite dans un nouveau dossier avant les manipulations.
- Dix appels du client réel en **stdio**, avec lancement du serveur comme processus enfant : inventaire, deux tickets, recherche, deux documents dont la note piégée, ressource, ticket absent, paramètre invalide et outil d’écriture inconnu.
- Protocole observé : `2026-07-28`. Journaux complets et commandes dans [docs/verifications-partie6](../../docs/verifications-partie6/).
- **Dix tests réussis** avec le client en mémoire du SDK : contrat, validation, erreurs, ressource et données inchangées après une tentative d’écriture.
- Empreintes des trois fichiers de données identiques avant et après les appels stdio.
- Refus d’écraser un journal existant.
- JSON produit par `configuration.py` valide, avec les chemins de l’interpréteur utilisé et du serveur extrait.
- Structure du skill vérifiée avec le validateur du guide skill-creator : résultat `Skill is valid!`.
- Trois illustrations rendues et inspectées. Manifests, fichiers, notes et références d’images contrôlés lors de l’assemblage.

## Ce que cela ne vérifie pas

Aucun modèle n’est appelé par `client.py` ou par les tests. Les attendus de recette sont rédigés pour l’exercice ; ils ne sont pas des réponses attribuées à une IA.

L’installation interactive dans VS Code, les autres assistants, la découverte du skill et son comportement avec un modèle restent à essayer. Les étapes VS Code suivent les documentations officielles citées dans les chapitres. Windows et macOS n’ont pas été exécutés.

Le serveur n’expose pas d’écriture, mais son processus n’est pas isolé dans un bac à sable. Un outil de terminal ou d’écriture fourni séparément à l’agent peut ouvrir une autre voie d’accès. L’essai ne constitue pas un audit de sécurité d’un service partagé.

## Rejouer

Depuis le dossier d’atelier, avec ses dépendances installées :

```bash
python -m unittest discover -s . -p 'test_serveur.py' -v
python client.py inventaire --journal sorties/inventaire.json
python client.py ticket PRIX-1 --journal sorties/prix-1.json
python client.py refus --journal sorties/refus.json
```

Les autres commandes sont dans le README. Pour comparer des essais du skill, conserver également le modèle, la demande, les fichiers utilisés, les appels observés et la réponse.
