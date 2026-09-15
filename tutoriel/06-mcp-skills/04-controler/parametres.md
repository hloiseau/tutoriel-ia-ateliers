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
