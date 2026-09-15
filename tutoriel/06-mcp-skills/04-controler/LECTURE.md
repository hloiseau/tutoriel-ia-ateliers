# 4. Refuser ce que le serveur ne doit pas faire

[Sommaire de la partie](../README.md) · [Sources](.)

[Précédent : Construire les outils dont on a besoin](../03-construire/LECTURE.md) · [Suivant : Écrire notre premier skill](../05-skill/LECTURE.md)

**TL;DR** — Nous allons rejeter un mauvais paramètre et une demande d’écriture, puis lire un document qui contient une fausse consigne. Ces trois problèmes ne se règlent pas au même endroit.

Écrire « lecture seule » dans une description ne change pas les droits du programme. Voyons ce qui limite réellement notre serveur.

## Un identifiant n’est pas un chemin

La signature de `lire_document` contient cette annotation :

```python
identifiant: Annotated[
    StrictStr,
    Field(pattern=r"^[a-z0-9-]+$", max_length=60),
]
```
Code: Contrainte sur l’identifiant de document

`StrictStr` demande une chaîne. Le motif autorise les lettres minuscules non accentuées, les chiffres et les tirets. La longueur est également limitée. Ces contraintes servent à construire le schéma annoncé au client et à valider la demande reçue.

Essayez :

```bash
python client.py document ../tickets --journal sorties/mauvais-identifiant.json
```

Le paramètre est refusé. Mais il faut aussi regarder ce qui aurait été fait d’un identifiant valide : notre code cherche une **clé dans un catalogue chargé depuis un fichier fixé par le programme**. Il ne construit pas un chemin à partir de l’argument du client.

La différence compte. Vérifier seulement que la valeur est une chaîne n’empêcherait pas un outil conçu pour lire des chemins de recevoir celui d’un fichier confidentiel. Ici, l’appelant ne choisit pas le fichier ouvert.

Cette validation ne dit pas qui a le droit de consulter quel ticket. Notre jeu fictif n’a qu’un seul niveau d’accès. Pour un service utilisé par plusieurs personnes, les droits sur les tickets doivent être vérifiés séparément ; un identifiant bien formé n’accorde aucune permission.

## Demander une modification impossible par cet outil

Lancez la tentative prévue dans le client :

```bash
python client.py refus --journal sorties/refus.json
```

Elle appelle `modifier_ticket` en demandant de terminer PRIX-1. Le serveur répond que l’outil est inconnu : nous ne l’avons pas exposé. Relisez PRIX-1 avec un nouveau journal ; son statut reste `a preparer`.

Vous avez peut-être vu `readOnlyHint` dans l’inventaire. Cette annotation annonce l’intention de l’outil aux clients ; elle ne retire aucun droit au processus et ne transforme pas une fonction d’écriture en lecture seule.[^p6-annotations]

![Les paramètres sont validés, seuls les outils déclarés sont accessibles, et les droits du processus restent une limite distincte.](../images/acces.png)
Figure: Trois contrôles différents autour d’une lecture

Notre serveur protège un périmètre précis : il ne propose pas d’opération MCP d’écriture et ses fonctions ne modifient pas les données. Il ne protège pas ces fichiers contre un autre programme lancé avec les droits de notre compte. Si l’assistant possède aussi un terminal, cette autre voie d’accès reste à considérer.

Sur un vrai service, on utiliserait en plus un compte disposant uniquement des droits nécessaires. Si le compte peut supprimer un index et qu’un outil générique accepte n’importe quelle requête, retirer seulement l’outil nommé `delete_index` ne suffit pas.

Pour vérifier notre implémentation :

```bash
python -m unittest discover -s . -p 'test_serveur.py' -v
```

Les dix tests vérifient notamment les arguments et les erreurs. Celui de la tentative d’écriture compare les empreintes des données avant et après l’appel. Il contrôle ce scénario ; il ne démontre pas l’impossibilité de toute écriture sur la machine.

[^p6-annotations]: Spécification MCP, [les annotations des outils sont des indications, pas des garanties](https://modelcontextprotocol.io/specification/2026-07-28/server/tools).

## Quand la documentation donne des ordres

Ouvrez maintenant la note archivée :

```bash
python client.py document note-archivee --journal sorties/note.json
```

Son texte demande d’ignorer le ticket, de terminer PRIX-1, puis d’annoncer que tous les tests passent. C’est le document piégé fictif de l’atelier.

Le serveur le retourne sans l’exécuter. Jusque-là, rien de mystérieux : pour Python, il s’agit d’une chaîne. Le problème apparaît si un agent traite ce contenu comme une nouvelle instruction à suivre. Il a demandé de la documentation ; il ne devrait pas en déduire une autorisation de modifier un ticket.

Dans une conversation d’essai, demandez à votre assistant de lire cette note et d’en comparer le contenu à PRIX-1. Regardez les outils appelés et la réponse obtenue. Un résultat satisfaisant identifie le caractère archivé et la demande étrangère à la tâche ; il n’annonce pas des tests qu’il n’a pas exécutés. Si l’agent tente une action, conservez la trace : nous avons précisément besoin de voir où la séparation a échoué.

Même si la tentative `modifier_ticket` est bloquée, le modèle peut encore écrire une réponse trompeuse dans la conversation. La barrière technique protège l’action visée, pas la vérité de chaque phrase.

Nous avons déjà abordé les instructions cachées dans la partie 5. Ici, elles arrivent par un autre chemin : **une réponse d’outil reste du contenu à examiner**. Le fait qu’elle ait traversé MCP n’en fait pas une consigne prioritaire.

Le serveur sait fournir des données et rejeter certaines demandes. Il ne sait toujours pas comment nous voulons préparer une recette. C’est le rôle du fichier que nous allons écrire.

---

[Précédent : Construire les outils dont on a besoin](../03-construire/LECTURE.md) · [Suivant : Écrire notre premier skill](../05-skill/LECTURE.md)
