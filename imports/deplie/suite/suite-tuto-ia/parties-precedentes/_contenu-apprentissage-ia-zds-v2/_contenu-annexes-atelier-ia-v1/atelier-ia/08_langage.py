import argparse
import numpy as np
from commun import RACINE, SORTIES

parser = argparse.ArgumentParser()
parser.add_argument("--debut", default="le ")
parser.add_argument("--temperature", type=float, default=1.0)
parser.add_argument("--graine", type=int, default=42)
parser.add_argument("--longueur", type=int, default=180)
args = parser.parse_args()
if not np.isfinite(args.temperature) or args.temperature <= 0 or not 0 <= args.longueur <= 10000:
    parser.error("Température positive et finie ; longueur entre 0 et 10000.")
texte = (RACINE / "corpus.txt").read_text(encoding="utf-8")
vocabulaire = sorted(set(texte))
vers_id = {c: i for i, c in enumerate(vocabulaire)}
if not args.debut or any(c not in vers_id for c in args.debut):
    parser.error("Le début doit contenir des caractères présents dans le corpus.")
comptes = np.zeros((len(vocabulaire), len(vocabulaire)))
for a, b in zip(texte, texte[1:]):
    comptes[vers_id[a], vers_id[b]] += 1
np.savez_compressed(SORTIES / "bigrammes.npz", comptes=comptes, vocabulaire=np.array(vocabulaire))
rng = np.random.default_rng(args.graine)
resultat = args.debut
for _ in range(args.longueur):
    frequences = comptes[vers_id[resultat[-1]]]
    possibles = frequences > 0
    if not possibles.any():
        break
    scores = np.log(frequences[possibles]) / args.temperature
    poids = np.exp(scores - scores.max())
    choix = rng.choice(np.flatnonzero(possibles), p=poids / poids.sum())
    resultat += vocabulaire[choix]
print(f"Corpus : {len(texte)} caractères ; vocabulaire : {len(vocabulaire)} tokens")
print(f"Contexte utilisé : 1 caractère ; température : {args.temperature}")
print(resultat)
(SORTIES / "texte-genere.txt").write_text(resultat, encoding="utf-8")
