# Choisir la place de l’IA

[Lire la partie 9](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/parcours-dev-travail-2026-09-18/tutoriel/09-choisir/README.md) · [Vérifications](https://github.com/hloiseau/tutoriel-ia-ateliers/blob/parcours-dev-travail-2026-09-18/tutoriel/09-choisir/VERIFICATION.md)

Ouvrez ce dossier, ou décompressez `atelier-choisir-ia.zip`. Vous pouvez suivre le parcours avec un éditeur de texte et une calculatrice, sans Python ni compte d’IA. Les scripts plus bas permettent de prolonger les exercices.

Pour le parcours de tâches de travail, gardez aussi [le dossier des Ateliers du quartier](https://github.com/hloiseau/tutoriel-ia-ateliers/raw/parcours-dev-travail-2026-09-18/telechargements/atelier-hors-developpement.zip) de la partie 7, disponible dans `ateliers/hors-developpement` si vous avez le dépôt complet. Ce dossier distinct contient les sources et le corrigé du point d’équipe ; aucune réponse d’assistant n’est nécessaire pour les examiner.

## Suivre le parcours

1. Lisez `cas/equipe.md` et les trois documents de `cas/documents.md`. Préparez le contexte qui répond à la question posée, puis comparez avec `corriges/documents.md`. Remplissez une copie de `fiches/provenance.md` ; `corriges/provenance.md` fournit un exemple sourcé sur le modèle du parcours développement.
2. Examinez les trajets avec `fiches/flux.md`, puis la possibilité de changer d’outil avec `fiches/sortie.md`. Pour les Ateliers du quartier, distinguez les fichiers éventuellement confiés à un assistant de leur traitement dans la page locale. Reprenez ensuite le point à la main à partir des sources, sans ouvrir la conversation. `corriges/flux-et-sortie.md` fournit un autre exemple, celui de l’application documentaire locale de la partie 8.
3. Faites le calcul hypothétique d’énergie : 200 W pendant 30 minutes donnent 200 × 0,5 = **100 Wh**, soit **0,1 kWh**. Ces valeurs illustrent le calcul ; elles n’ont pas été mesurées sur notre matériel.
4. Fermez l’assistant et relisez cette synthèse volontairement fausse : « La journée est confirmée le 17 octobre. Nora attend quatre places en Reliure et Léo deux places dans le même atelier. Nous pouvons envoyer les confirmations. » Retrouvez ce qui permet de la corriger dans les fichiers des Ateliers du quartier, puis comparez avec leur `corrige/point-equipe.md`. La date reste à clarifier entre le 10 et le 17 octobre ; Nora demande deux places ; l’atelier souhaité par Léo manque et aucune confirmation n’a été envoyée. Les lecteurs du parcours développement peuvent choisir à la place l’exercice de code ci-dessous.
5. Préparez une comparaison avec `fiches/comparaison.md`, dans un document ou un tableau. Pour comprendre le calcul des durées, lisez `corriges/comparaison.md` : les occupations fictives sont de **23 et 28 minutes**, sans conclusion sur un outil réel. Dans votre propre essai, notez les temps observés et le statut du résultat ; une durée inconnue reste inconnue.
6. Examinez une alternative à l’IA pour l’une des tâches. `corriges/catalogue.md` montre les trois anomalies d’un catalogue et les règles qui suffisent à les détecter. Pour la journée d’ateliers, repartez du point préparé à la main : quels passages un modèle de document et le tableau suffisent-ils déjà à organiser ?
7. Terminez une copie de `fiches/decision.md`. Indiquez les données autorisées, qui vérifie le résultat, les conditions d’arrêt et la manière de reprendre sans l’outil. `corriges/decision.md` développe les choix du service de prix ; le dernier chapitre applique aussi cette décision à la journée d’ateliers.

Les corrigés proposent des raisons, pas une opinion obligatoire sur l’IA. Aucun exercice n’est à envoyer à l’auteur. Les fiches peuvent être remplies dans un éditeur de texte ou sur papier.

## Variantes avec Python

Placez le terminal à côté de `bilan.py`. Python 3.12 est la version de référence ; aucune dépendance à installer, aucun appel réseau par les scripts. Selon votre système, remplacez `python` par `python3` ou `py -3.12`.

Pour retrouver le calcul hypothétique d’énergie :

```bash
python energie.py --puissance-w 200 --minutes 30
```

Pour l’exercice de code, prédisez les résultats de la fonction de `cas/lecture_code.py`, exécutez-la, corrigez-la puis essayez la variante :

```bash
python cas/lecture_code.py
python corriges/lecture_code.py
python corriges/variante.py
```

La première commande **doit sortir avec le code 1** : le prix égal révèle un bug intentionnel. Les deux corrections sortent avec le code 0. Les explications sont dans `corriges/lecture_code.md`.

Pour calculer le bilan fictif :

```bash
python bilan.py exemples/temps-fictifs.json
```

Copiez `exemples/temps-a-remplir.json`, remplissez les durées observées, puis passez ce nouveau fichier au script. Les valeurs manquantes sont refusées ; zéro signifie une durée effectivement nulle. Les périodes doivent être disjointes. Le script ne classe pas les essais et ne décide pas si le résultat est acceptable.

Pour exécuter les contrôles déterministes du catalogue :

```bash
python catalogue.py
```

Le jeu fictif contient trois lignes invalides. Le code de sortie **1 est attendu**, et les raisons sont affichées. Faites les corrections dans une copie du JSON puis passez-la avec `--fichier chemin-vers-la-copie.json`. Voir `corriges/catalogue.md`.

## Contrôler les programmes, facultativement

```bash
python -m unittest discover -s . -p "test_atelier.py" -v
```

Les tests vérifient les calculs et des entrées invalides ; ils ne prouvent aucun gain de productivité ou d’apprentissage. Les traces d’exécution sont dans `resultats-reference`. Aucune comparaison avec un lecteur ou un assistant réel n’a été réalisée dans cette partie.

Code : GPL-3.0-only. Textes et données fictives : CC BY-SA 4.0, © 2026 Hugo Loiseau. Les licences complètes sont jointes à l’archive.
