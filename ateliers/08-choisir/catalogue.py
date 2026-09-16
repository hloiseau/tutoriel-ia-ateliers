# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Contrôler un catalogue fictif avec des règles déterministes."""
import argparse
import json
from pathlib import Path


def verifier(lignes):
    if not isinstance(lignes, list):
        raise ValueError('Le catalogue doit être une liste JSON.')
    erreurs = []
    vus = set()
    for numero, ligne in enumerate(lignes, 1):
        raisons = []
        if not isinstance(ligne, dict):
            raisons.append('produit attendu sous forme d’objet')
        else:
            identifiant = ligne.get('id')
            if not isinstance(identifiant, str) or not identifiant.strip():
                raisons.append('identifiant manquant ou invalide')
            elif identifiant in vus:
                raisons.append('identifiant déjà rencontré')
            else:
                vus.add(identifiant)
            prix = ligne.get('prix_centimes')
            if type(prix) is not int or prix < 0:
                raisons.append('prix attendu : entier positif ou nul, hors booléen')
            if type(ligne.get('disponible')) is not bool:
                raisons.append('disponibilité attendue : booléen')
        if raisons:
            erreurs.append({'ligne': numero, 'raisons': raisons})
    return erreurs


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--fichier', type=Path, default=Path(__file__).parent/'cas/catalogue.json')
    a = p.parse_args()
    try:
        erreurs = verifier(json.loads(a.fichier.read_text(encoding='utf-8')))
    except (OSError, ValueError) as erreur:
        p.error(str(erreur))
    print(json.dumps({'lignes_invalides': len(erreurs), 'erreurs': erreurs}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if erreurs else 0)


if __name__ == '__main__':
    main()
