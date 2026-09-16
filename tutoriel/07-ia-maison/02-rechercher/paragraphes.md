Ouvrez `recherche.py` et regardez `charger`. La fonction lit le catalogue des documents, exclut ceux qui sont archivés, puis sépare les textes en paragraphes. Nos pages sont petites et leurs paragraphes portent chacun une idée ; cette découpe suffit pour commencer.

Chaque passage conserve un identifiant comme `notification#2`, son texte, son fichier, son statut, sa révision et l’empreinte du document. Le `#2` désigne le deuxième paragraphe dans cette version. Si nous insérons un nouveau paragraphe, les numéros peuvent changer : c’est pour cela que le journal conserve aussi le texte et la version consultés.

Un morceau trop court pourrait perdre sa condition. Séparer « une remise en stock » de « à prix égal » ferait disparaître précisément ce qui nous intéresse. Un morceau trop long ramènerait des règles sans rapport avec la question. La découpe se juge donc en lisant les passages obtenus.

Le statut est traité **avant** le classement : l’ancienne règle de notification ne doit pas gagner simplement parce qu’elle répète les mots de la question. Nous conservons en revanche le document « à arbitrer », car dire qu’une décision manque est une information utile.
