Téléchargez [les fichiers de l’atelier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/b95165289276a45bc299d0826e3c540727e8e203/telechargements/annexes-developpement-v1.zip), puis décompressez l’archive. Le dossier `atelier-developpement` contient trois états du même projet :

| Dossier fourni | À quoi il nous servira |
| --- | --- |
| `01-depart` | Le programme avant notre modification |
| `02-test-rouge` | Les tests de référence, avant la correction |
| `03-corrige` | La correction à consulter après avoir essayé |
Table: Les fichiers de départ et les corrections

Copiez **`01-depart`** dans un nouveau dossier nommé **`mon-suivi`**, en dehors du dossier téléchargé. Gardez les trois versions fournies à leur emplacement d’origine : elles nous serviront de points de comparaison. Toutes nos modifications iront dans `mon-suivi`, sans nouveau départ au chapitre suivant.

Installez [Visual Studio Code](https://code.visualstudio.com/download), puis utilisez **Fichier → Ouvrir le dossier** pour ouvrir `mon-suivi`. Si vous avez déjà un éditeur et un assistant, ouvrez cette même copie avec eux et passez à « Observer le problème ».

Dans l’explorateur, vous devez retrouver `suivi.py`, `test_suivi.py`, `TICKET.md` et `scenarios`. Les dossiers de correction restent en dehors de l’espace de travail : autant éviter de laisser la réponse sous le nez de l’agent. 🙂

À partir d’ici, chaque commande indiquée sans autre précision est à lancer depuis `mon-suivi`.
