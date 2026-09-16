# Choisir la place de l’IA

[Lire la partie 8](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/08-choisir/README.md) · [Vérifications](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/main/tutoriel/08-choisir/VERIFICATION.md)

Ouvrez ce dossier, ou décompressez `atelier-choisir-ia.zip`, puis placez le terminal à côté de `bilan.py`. Python 3.12 est la version de référence ; aucune dépendance à installer, aucun appel réseau par les scripts. Selon votre système, remplacez `python` par `python3` ou `py -3.12`.

## Suivre le parcours

1. Lire `cas/equipe.md` et les trois documents de `cas/documents.md`. Remplir une copie de `fiches/provenance.md` et comparer avec `corriges/documents.md` et `corriges/provenance.md`.
2. Examiner les trajets avec `fiches/flux.md`, puis la possibilité de changer d’outil avec `fiches/sortie.md`. `corriges/flux-et-sortie.md` reprend le cas local de la partie 7.
3. Faire le calcul hypothétique d’énergie, puis lire son périmètre :

```bash
python energie.py --puissance-w 200 --minutes 30
```

Il affiche **100 Wh / 0,1 kWh**. Ce n’est pas une mesure de notre matériel.

4. Prédire les résultats de la fonction de `cas/lecture_code.py`, l’exécuter, corriger puis essayer la variante :

```bash
python cas/lecture_code.py
python corriges/lecture_code.py
python corriges/variante.py
```

La première commande **doit sortir avec le code 1** : le prix égal révèle un bug intentionnel. Les deux corrections sortent avec le code 0. Les explications sont dans `corriges/lecture_code.md`.

5. Préparer une comparaison avec `fiches/comparaison.md`. Examiner d’abord le calcul fictif :

```bash
python bilan.py exemples/temps-fictifs.json
```

Les occupations fictives sont de **23 et 28 minutes**, sans conclusion sur un outil réel. Copier `exemples/temps-a-remplir.json`, remplir les durées observées, puis passer ce nouveau fichier au script. Les valeurs manquantes sont refusées ; zéro signifie une durée effectivement nulle. Les périodes doivent être disjointes. Le script ne classe pas les essais et ne décide pas si le résultat est acceptable.

6. Examiner l’alternative déterministe pour le catalogue :

```bash
python catalogue.py
```

Le jeu fictif contient trois lignes invalides. Le code de sortie **1 est attendu**, et les raisons sont affichées. Faire les corrections dans une copie du JSON puis la passer avec `--fichier chemin-vers-la-copie.json`. Voir `corriges/catalogue.md`.

7. Terminer une copie de `fiches/decision.md`, puis comparer avec `corriges/decision.md`.

Les corrigés proposent des raisons, pas une opinion obligatoire sur l’IA. Aucun exercice n’est à envoyer à l’auteur. Les fiches peuvent être remplies dans un éditeur texte sans installer de logiciel particulier.

## Contrôler les programmes

```bash
python -m unittest discover -s . -p "test_atelier.py" -v
```

Les tests vérifient les calculs et des entrées invalides ; ils ne prouvent aucun gain de productivité ou d’apprentissage. Les traces d’exécution sont dans `resultats-reference`. Aucune comparaison avec un lecteur ou un assistant réel n’a été réalisée dans cette partie.

Code : GPL-3.0-only. Textes et données fictives : CC BY-SA 4.0, © 2026 Hugo Loiseau. Les licences complètes sont jointes à l’archive.
