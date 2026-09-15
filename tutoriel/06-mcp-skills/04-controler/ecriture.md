Lancez la tentative prévue dans le client :

```bash
python client.py refus --journal sorties/refus.json
```

Elle appelle `modifier_ticket` en demandant de terminer PRIX-1. Le serveur répond que l’outil est inconnu : nous ne l’avons pas exposé. Relisez PRIX-1 avec un nouveau journal ; son statut reste `a preparer`.

Vous avez peut-être vu `readOnlyHint` dans l’inventaire. Cette annotation annonce l’intention de l’outil aux clients ; elle ne retire aucun droit au processus et ne transforme pas une fonction d’écriture en lecture seule.[^p6-annotations]

![Les paramètres sont validés, seuls les outils déclarés sont accessibles, et les droits du processus restent une limite distincte.](image:images/acces.png)
Figure: Trois contrôles différents autour d’une lecture

Notre serveur protège un périmètre précis : il ne propose pas d’opération MCP d’écriture et ses fonctions ne modifient pas les données. Il ne protège pas ces fichiers contre un autre programme lancé avec les droits de notre compte. Si l’assistant possède aussi un terminal, cette autre voie d’accès reste à considérer.

Sur un vrai service, on utiliserait en plus un compte disposant uniquement des droits nécessaires. Si le compte peut supprimer un index et qu’un outil générique accepte n’importe quelle requête, retirer seulement l’outil nommé `delete_index` ne suffit pas.

Pour vérifier notre implémentation :

```bash
python -m unittest discover -s . -p 'test_serveur.py' -v
```

Les dix tests vérifient notamment les arguments et les erreurs. Celui de la tentative d’écriture compare les empreintes des données avant et après l’appel. Il contrôle ce scénario ; il ne démontre pas l’impossibilité de toute écriture sur la machine.

[^p6-annotations]: Spécification MCP, [les annotations des outils sont des indications, pas des garanties](https://modelcontextprotocol.io/specification/2026-07-28/server/tools).
