# Balises attention, erreur, information, question et secret

Les tutoriels et articles de ZdS sont parsemés de balises telles que la balise "information" :

[[information]]
| Ceci est une balise d'information.
|
| Cool, non ?

Elle se fait avec la syntaxe suivante :

```text
[[information]]
| Ceci est une balise d'information.
|
| Cool, non ?
```

Ou dans sa version raccourcie :

```text
[[i]]
| Ceci est une balise d'information.
|
| Cool, non ?
```

Les balises disponibles sont : 

- attention
- erreur
- information
- question
- secret

La balise "secret" (appelée "spoiler" sur certains sites) a ceci de spécial qu'elle masque son contenu par défaut et ne le rend visible qu'au clic de l'utilisateur.

# Citations

Les citations permettent de séparer votre propos de celui que vous rapportez. D'ailleurs, si l'on en croit ce vieux proverbe nous venant d'une petite planète quelque part aux confins de Bételgeuse, il ne faut pas s'en priver :

> Les citations, c'est bien.
Source: Petite planète quelque part aux confins de Bételgeuse

On utilise pour cela un chevron devant chaque début de ligne, avec optionnellement votre source, écrite de la même façon que les légendes (avec le mot-clé `Source`) :

```text
> Ceci est une citation
> 
> sur plusieurs lignes
Source: Citez vos sources !
```

# Blocs à titre et blocs neutres

Parfois vous désirez mettre en avant une information (par exemple un théorème) mais aucun des blocs spéciaux ne vous convient. Vous pouvez alors utiliser un bloc *neutre*.

Ce bloc aura forcément un titre, ce qui aidera à mettre le contenu en avant. Par exemple :

```
[[neutre | Théorème de Pythagore]]
| Un triangle ABC est rectangle en a si et seulement si $AB^2 + AC^2 = BC^2$
```

[[neutre | Théorème de Pythagore]]
| Un triangle ABC est rectangle en a si et seulement si $AB^2 + AC^2 = BC^2$

Notons que tous les autres blocs peuvent aussi avoir un titre, il se présente de la même manière, c’est-à-dire en mettant `[[nom_du_bloc | titre du bloc]]`. Ils ne sont par contre pas obligatoires.