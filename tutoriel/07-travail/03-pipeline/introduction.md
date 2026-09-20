**TL;DR** — Transformons les messages en données régulières, puis essayons une chaîne locale qui contrôle ces données et prépare le point. Une extraction fictive permet de faire toute la manipulation sans appeler de modèle.

Vendredi prochain, les fichiers auront changé, mais nous demanderons encore de relever les messages, de retrouver les nouveautés et de préparer un compte rendu. Un pipeline permet de conserver cet enchaînement. L’application fournie ici travaille sur le lot `quartier-01` et ses quatre messages distincts : elle nous servira à observer les contrôles, l’approbation et le rejeu. Pour recevoir d’autres lots, il faudra adapter ses sources et ses règles.

Pour l’essayer, ouvrez le dossier décompressé de l’atelier. Nous utiliserons `pipeline/index.html` dans votre navigateur. Aucun terminal, compte ou serveur n’est nécessaire. L’application reçoit une extraction par copier-coller ; les messages ne partent vers aucun service depuis cette page.
