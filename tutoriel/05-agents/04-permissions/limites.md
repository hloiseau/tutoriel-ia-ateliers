Lancez les tests du banc :

```bash
python -m unittest discover -v
```

Ils vérifient notamment qu’un refus d’écriture ne crée pas la note, qu’un chemin extérieur n’est pas lu et qu’un texte ressemblant à une demande JSON reste du contenu de fichier. Ouvrez `test_banc.py` et retrouvez ces assertions.

Chaque contrôle protège le passage prévu. Si nous ajoutions un terminal générique, il faudrait examiner tout ce qu’il peut faire avec les droits du processus. Il pourrait peut-être écrire au même endroit et contourner ainsi la restriction placée sur `ecrire_note`.

Notre programme illustre des contrôles applicatifs ; il n’isole pas du code hostile. Dans un environnement réel, les comptes utilisés, les accès réseau, les répertoires montés et l’isolation du processus déterminent aussi ce qu’une action peut atteindre.

Sur votre assistant, retrouvez une permission concrète et sa portée : commande seulement, session, dossier, accès réseau ? Lisez ce qu’accorde le bouton avant d’approuver « toujours ». Une consigne guide le modèle, une confirmation vous rend la décision, une restriction du système bloque l’action ; ce sont trois protections différentes.
