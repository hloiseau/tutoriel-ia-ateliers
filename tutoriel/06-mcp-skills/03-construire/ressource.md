Il reste un fichier utile : `donnees/conventions.md`. Au lieu de lui inventer un argument de recherche, exposons-le comme une ressource identifiée.

Ajoutez cette fonction avant le démarrage du serveur :

```python
@mcp.resource("atelier://conventions")
def conventions() -> str:
    """Conventions stables du projet fictif."""
    return (ROOT / "donnees" / "conventions.md").read_text(encoding="utf-8")
```

Puis lisez-la :

```bash
python client.py conventions --serveur mon_serveur.py --journal sorties/c05-conventions.json
```

La réponse contient le texte de nos conventions, notamment l’usage des centimes. L’identifiant `atelier://conventions` permet au serveur de désigner cette ressource ; votre navigateur n’a rien à ouvrir à cette adresse.

Un outil propose une opération avec des arguments ; une ressource expose un contenu identifié. Un autre serveur pourrait représenter ses tickets comme des ressources. Le client décide ensuite comment proposer ou charger ces contenus.[^p6-construire-ressource]

Notre fichier contient maintenant trois outils et une ressource. Si vous souhaitez comparer, `serveur.py` est le corrigé complet. Regardez les différences avant de remplacer quoi que ce soit : une faute de nom ou une définition après `run` suffit à expliquer un outil absent.

Pour déboguer, évitez les `print()` dans le serveur : sa sortie standard transporte MCP. Utilisez les logs ou la sortie d’erreur, par exemple `print("lecture du catalogue", file=sys.stderr)` après avoir importé `sys`. Votre diagnostic ne se retrouvera pas au milieu des messages du protocole.

[^p6-construire-ressource]: Spécification MCP, [ressources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources).
