# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Additionner des catégories de tokens disjointes : exemple simplifié de coût."""
import argparse
import csv
from decimal import Decimal
from pathlib import Path


def cout(path, prix_entree, prix_cache, prix_sortie):
    tarifs = [Decimal(str(x)) for x in (prix_entree, prix_cache, prix_sortie)]
    if any(not p.is_finite() or p < 0 for p in tarifs):
        raise ValueError('Les tarifs doivent être finis et positifs ou nuls.')
    total = Decimal(0)
    with Path(path).open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f):
            quantites = [int(row[k]) for k in ('entree_hors_cache', 'entree_cache', 'sortie')]
            if any(q < 0 for q in quantites):
                raise ValueError('Les quantités doivent être positives ou nulles.')
            total += sum(q*p for q,p in zip(quantites,tarifs))/Decimal(1000000)
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv', type=Path)
    parser.add_argument('--prix-entree', required=True)
    parser.add_argument('--prix-cache', required=True)
    parser.add_argument('--prix-sortie', required=True)
    args = parser.parse_args()
    print(f'Coût simplifié : {cout(args.csv,args.prix_entree,args.prix_cache,args.prix_sortie):.6f} unités monétaires')


if __name__ == '__main__':
    main()
