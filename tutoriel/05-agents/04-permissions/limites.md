Lancez les tests du banc :

```bash
python -m unittest discover -v
```

Ils vérifient notamment qu’un refus d’écriture ne crée pas la note, qu’un chemin extérieur n’est pas lu et qu’un texte ressemblant à une demande JSON reste du contenu de fichier. Ouvrez `test_banc.py` et retrouvez ces assertions.

Le contrôle d’un outil ne protège que les passages qui le traversent. Si nous ajoutions un terminal générique, il faudrait examiner ce qu’il peut faire avec les droits du processus. Interdire `ecrire_note` ne suffirait plus si un autre outil permettait d’écrire au même endroit.

Notre programme est un exercice de contrôles applicatifs. Il ne constitue pas un bac à sable pour lancer du code hostile. Dans un environnement réel, les comptes utilisés, les accès réseau, les répertoires montés et l’isolation du processus déterminent aussi ce qu’une action peut atteindre.

Sur votre assistant, retrouvez une permission concrète et sa portée : commande seulement, session, dossier, accès réseau ? Lisez ce qu’accorde le bouton avant d’approuver « toujours ». Une consigne, une confirmation et une restriction du système ne jouent pas le même rôle.
