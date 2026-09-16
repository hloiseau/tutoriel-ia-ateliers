# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Additionner des temps déclarés, sans évaluer la qualité ni classer les outils."""
import argparse
import json
import math
from pathlib import Path

PHASES = ('preparer', 'produire', 'relire', 'corriger', 'verifier')


def duree(value, nom):
    if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
        raise ValueError(f'{nom} : durée manquante ou invalide ; indiquez un nombre fini positif ou nul.')
    return float(value)


def calculer(document):
    if not isinstance(document, dict) or document.get('origine') not in ('fictif', 'observe'):
        raise ValueError('Précisez origine : fictif ou observe.')
    essais = document.get('essais')
    if not isinstance(essais, list) or not essais:
        raise ValueError('Il faut au moins un essai.')
    resultat = []
    for essai in essais:
        if not isinstance(essai, dict):
            raise ValueError('Chaque essai doit être un objet.')
        nom = essai.get('nom')
        if not isinstance(nom, str) or not nom.strip():
            raise ValueError('Chaque essai doit avoir un nom.')
        if essai.get('mode') not in ('avec_ia', 'sans_ia'):
            raise ValueError(f'{nom} : mode inconnu.')
        if essai.get('statut') not in ('valide', 'a_corriger', 'abandonne'):
            raise ValueError(f'{nom} : statut inconnu.')
        minutes = essai.get('minutes')
        if not isinstance(minutes, dict):
            raise ValueError(f'{nom} : minutes manquantes.')
        actif = sum(duree(minutes.get(p), f'{nom}/{p}') for p in PHASES)
        attente = duree(minutes.get('attente_bloquante'), f'{nom}/attente_bloquante')
        total = actif + attente
        if not math.isfinite(total):
            raise ValueError(f'{nom} : somme trop grande.')
        resultat.append({'nom': nom, 'mode': essai['mode'], 'statut': essai['statut'],
                         'actif_min': actif, 'attente_bloquante_min': attente, 'occupation_min': total})
    return {'origine_declaree': document['origine'], 'essais': resultat,
            'limite': 'Durées déclarées sur des phases disjointes ; aucun classement ni contrôle automatique de qualité.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fichier', type=Path)
    args = parser.parse_args()
    try:
        rapport = calculer(json.loads(args.fichier.read_text(encoding='utf-8')))
    except (OSError, ValueError) as erreur:
        parser.error(str(erreur))
    print(json.dumps(rapport, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
