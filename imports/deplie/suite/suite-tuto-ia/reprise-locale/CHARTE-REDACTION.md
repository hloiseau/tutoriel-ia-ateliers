# Voix et progression

## Ce que l’auteur demande

Écrire en français, avec une manière de guider proche du tutoriel Vim fourni : partir d’une manipulation concrète, donner envie de l’essayer, expliquer ce qui vient de se passer et laisser le lecteur prendre la main. Le texte de Vim est une référence de ton et de rythme, pas une réserve de phrases à reproduire.

Le ton personnel de l’auteur est direct, chaleureux, nuancé et parfois familier. Il emploie naturellement « trial and error », « refacto », « skill » ou « MCP ». Ne pas les remplacer systématiquement par un langage artificiellement académique. Écrire **MCP**, pas « connecteur ».

Il n’aime pas les introductions scolaires, les slogans, les titres artificiellement spectaculaires, les séries de phrases hachées et les commentaires sur notre propre rédaction. Éviter les panneaux qui rappellent des évidences ou semblent prendre le lecteur de haut. Expliquer une limite utile à l’endroit où elle change l’action ou l’interprétation.

Utiliser quelques vrais smileys Unicode 🙂 😅, quand ils accompagnent naturellement une remarque. Pas de codes de smileys, pas de décoration à chaque paragraphe.

## Organisation

- TL;DR au début de chaque partie et de chaque chapitre.
- Petits Markdown au format ZdS, sans transformer toute la matière en un document monolithique.
- Une lecture HTML assemblée avec images intégrées et un sommaire cliquable.
- De vraies illustrations qui expliquent quelque chose ; pas seulement des boîtes vides pour occuper l’espace.
- Tableaux pour comparer des cas, listes pour les étapes ou les informations parallèles.
- Code complet et résultats détaillés dans une archive téléchargeable distincte.
- Notes de bas de page pour les sources ; identifiants uniques entre chapitres et parties.
- Légendes `Figure:`, `Code:` et `Table:` ; images importables sous `image:images/...`.

## Pratique

Une manipulation précise son dossier de départ, ses fichiers, la commande, le résultat vérifiable et la manière de reprendre en cas d’erreur. Les exercices disposent de cas attendus ou de corrections à consulter. L’auteur ne corrige pas individuellement les travaux des lecteurs.

La voie de base reste accessible sur CPU et sans abonnement. Le matériel de l’auteur sert à des variantes optionnelles. Ne jamais laisser entendre qu’une RTX 3090 Ti est nécessaire pour comprendre.

Ne pas inventer de chiffres, de réponses d’agent, de temps d’exécution ou de captures. Les scripts doivent produire les résultats cités. Les résultats de référence restent distincts des sorties que le lecteur va générer. Signaler dans le dossier éditorial ce qui est testé et ce qui attend une machine réelle.

## Ce qu’on doit garder dans le fond

Comprendre suffisamment ce qu’on livre, relire, tester et valider. Pour un junior, recevoir trop vite la solution peut empêcher l’apprentissage. L’IA peut servir à préparer des tests ou expliquer un passage sans écrire tout le code. Il est également légitime de s’en passer.

Adapter l’outil à ses difficultés concrètes, sans adapter toute son organisation à un framework populaire. Distinguer consignes au modèle et contrôles exécutables. Examiner les données, le travail humain, les licences, les coûts, l’environnement et les dépendances. L’autohébergement ne résout pas à lui seul toutes ces questions.

## Références disponibles dans le dossier

`references/vim.zip` contient le tutoriel Vim fourni par l’auteur. Lire quelques chapitres complets pour retrouver sa manière de faire essayer une commande puis d’expliquer son effet. `references/guide-zds` conserve les fichiers du guide de rédaction fournis.

Extrait du ton personnel de l’auteur :

> Utiliser correctement ces outils demande déjà une bonne compréhension de ce que l’on fait. Sinon, on peut très vite se retrouver à générer des montagnes de code là où une seule ligne aurait suffi.
>
> Sans parler des bugs et autres problèmes qui peuvent passer entre les mailles du filet… Même si ma méthode et les skills que je décris dans ce billet permettent d’en atténuer une partie, il faut malgré tout passer un temps certain à relire, tester et valider ce qui est produit.
