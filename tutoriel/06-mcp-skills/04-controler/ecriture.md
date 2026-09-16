Lancez la tentative prévue dans le client :

```bash
python client.py refus --serveur mon_serveur.py --journal sorties/controle-refus.json
```

Elle appelle `modifier_ticket` en demandant de terminer PRIX-1. Le serveur répond que l’outil est inconnu : nous ne l’avons pas exposé. Relisez PRIX-1 avec un nouveau journal ; son statut reste `a preparer`.

Vous avez peut-être vu `readOnlyHint` dans l’inventaire. Cette annotation annonce l’intention de l’outil aux clients. Elle ne change ni le code de la fonction ni les droits du processus qui l’exécute.[^p6-annotations]

![Les paramètres sont validés, seuls les outils déclarés sont accessibles, et les droits du processus restent une limite distincte.](image:images/acces.png)
Figure: Trois contrôles différents autour d’une lecture

Notre serveur protège un périmètre précis : il ne propose aucune opération MCP d’écriture et ses fonctions laissent les données intactes. Un assistant qui possède aussi un terminal dispose toutefois d’une autre voie vers les fichiers, avec les droits de notre compte.

Sur un vrai service, on utiliserait en plus un compte limité aux droits nécessaires. Un outil générique capable d’envoyer n’importe quelle requête avec un compte administrateur contournerait facilement notre belle absence de bouton `delete_index`.

Notre troisième test couvre l’absence de l’outil d’écriture. La relecture du ticket compare aussi son état avant et après la demande. Ces vérifications portent sur les appels que nous venons de jouer ; les droits des autres programmes de la machine restent à traiter séparément.

[^p6-annotations]: Spécification MCP, [les annotations des outils sont des indications, pas des garanties](https://modelcontextprotocol.io/specification/2026-07-28/server/tools).
