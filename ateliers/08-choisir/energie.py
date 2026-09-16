# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Calculer une énergie théorique à partir d’une puissance moyenne fournie."""
import argparse
import json
import math


def calculer(puissance_w, minutes):
    if any(type(v) not in (int, float) or not math.isfinite(v) or v < 0 for v in (puissance_w, minutes)):
        raise ValueError('Puissance et durée doivent être des nombres finis positifs ou nuls.')
    wh = puissance_w * (minutes / 60)
    if not math.isfinite(wh):
        raise ValueError('Résultat trop grand.')
    return {'energie_wh': wh, 'energie_kwh': wh / 1000,
            'nature': 'Calcul à partir des valeurs fournies, pas une mesure.',
            'perimetre': 'Électricité correspondant à cette puissance moyenne et à cette durée ; hors fabrication et autres impacts.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--puissance-w', type=float, required=True)
    p.add_argument('--minutes', type=float, required=True)
    a = p.parse_args()
    try:
        resultat = calculer(a.puissance_w, a.minutes)
    except ValueError as erreur:
        p.error(str(erreur))
    print(json.dumps(resultat, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
