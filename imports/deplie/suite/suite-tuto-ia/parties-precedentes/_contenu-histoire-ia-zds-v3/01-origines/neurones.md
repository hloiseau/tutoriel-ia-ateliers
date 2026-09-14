En 1943, Warren McCulloch et Walter Pitts cherchent à décrire des réseaux de neurones avec des mathématiques. Leur modèle simplifie fortement le fonctionnement nerveux : un neurone reçoit des signaux et peut, à son tour, en transmettre un.[^h1s2-mp]

Regardons un exemple. Nous donnons deux entrées à notre neurone et nous fixons son **seuil d’activation** à deux. Il faut donc que les deux entrées lui transmettent un signal pour qu’il s’active.

![À gauche, un seul signal arrive et le neurone reste inactif ; à droite, les deux signaux arrivent et le neurone s’active.](image:images/neurone-deux-signaux.png)
Figure: Avec un seuil de deux, une seule entrée active ne suffit pas.

Les `0` et les `1` indiquent l’absence ou la présence d’un signal. Si vous avez utilisé des booléens, vous reconnaîtrez une opération **ET** : la première entrée **et** la deuxième doivent être actives pour obtenir une sortie active.

Le modèle prévoit aussi des entrées **inhibitrices** : lorsqu’elles sont actives, elles bloquent l’activation du neurone.

Ce neurone ne fait pas grand-chose tout seul. Nous sommes encore assez loin de lui demander de faire nos devoirs. 😅 Mais nous pouvons relier sa sortie à d’autres neurones et construire des réseaux qui réalisent plusieurs opérations logiques.

Dans ce modèle, les connexions sont fixées. Le réseau ne découvre pas lui-même comment les modifier à partir d’exemples.


[^h1s2-mp]: [McCulloch et Pitts, A Logical Calculus of the Ideas Immanent in Nervous Activity (1943 ; réédition de 1990)](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf).
