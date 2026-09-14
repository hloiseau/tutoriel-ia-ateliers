Afin de vous aider à rédiger un contenu agréable à lire, le moteur markdown de zeste de savoir inclus un module de typographie automatique.

Cela signifie que certains caractères (par exemples les apostrophes anglais) seront remplacés par des caractères typographiquement corrects.

De même, nous nous occupons de mettre les espaces insécables aux bons endroits.

[[q]]
| Espace quoi?

Lorsque vous écrivez une phrase longue, votre navigateur va automatiquement passer à la ligne une fois la limite atteinte. Pour faire cela, il va "couper" la phrase. Le meilleur endroit pour couper une phrase, c'est l'espace entre deux mots.

Mais voilà, il existe certaines règles de typographie qui rendent ce comportement gênant. Par exemple, lorsque vous vous préparez à faire une liste et que vous terminez votre phrase par `:`.

Logiquement, vous devez entourer votre caractère `:` d'espaces. Ce qui peut amener un cas étrange : votre phrase étant trop longue, votre navigateur met les `:` à la ligne.

C'est ce problème que résout l'espace insécable. Son nom elle ne l'usurpe pas : c'est une espace qui ne peut pas être coupée. En fait l'espace qui est avant les `:` doit être une espace insécable. 

Le problème c'est que la majorité des claviers et des systèmes d'exploitation n'ont pas de moyen simple de faire cette espace. Et c'est pourquoi nous la faisons pour vous. En plus ça vous évitera de vous demander quels types et combien d'espaces vous devez mettre autour d'un signe de ponctuation.

## Aide mémoire :

Caractère | Remplacement
----------|-------------
`%o` | `‰`
`<<`  | `« `
`>>` | `»`
`--mot--` | `– mot –`
`---mot---` | `— mot —`
`...`| `…`
`.:;!?()` | les espaces sécables ou non sont correctement placées autour des signes
Table: Tableau des remplacements