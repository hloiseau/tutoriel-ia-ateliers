# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Rejouer des demandes d'outils écrites à la main, sans modèle ni réseau."""
import argparse
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LECTURES = {'TICKET.md', 'suivi.py', 'documentation/note.md'}


class Banc:
    def __init__(self, root=ROOT, autoriser_ecriture=False):
        self.root = Path(root).resolve()
        self.autoriser_ecriture = autoriser_ecriture

    def executer(self, demande):
        try:
            if not isinstance(demande, dict) or set(demande) != {'outil', 'arguments'}:
                raise ValueError('La demande doit contenir outil et arguments.')
            outil, args = demande['outil'], demande['arguments']
            if not isinstance(args, dict):
                raise ValueError('arguments doit être un objet JSON.')
            if outil == 'lire_fichier':
                if set(args) != {'chemin'} or not isinstance(args['chemin'], str):
                    raise ValueError('lire_fichier attend uniquement un chemin texte.')
                if args['chemin'] not in LECTURES:
                    return {'statut': 'refuse', 'raison': 'Chemin absent de la liste autorisée.'}
                path = (self.root / 'projet' / args['chemin']).resolve()
                if not path.is_relative_to((self.root / 'projet').resolve()):
                    return {'statut': 'refuse', 'raison': 'Le chemin sort du projet.'}
                if path.stat().st_size > 16000:
                    return {'statut': 'erreur', 'raison': 'Fichier trop long pour cet exercice.'}
                contenu = path.read_text(encoding='utf-8')
                return {'statut': 'ok', 'contenu': contenu}
            if outil == 'ecrire_note':
                if set(args) != {'texte'} or not isinstance(args['texte'], str):
                    raise ValueError('ecrire_note attend uniquement un texte.')
                if not self.autoriser_ecriture:
                    return {'statut': 'refuse', 'raison': 'Écriture non autorisée par le programme.'}
                if len(args['texte']) > 2000:
                    raise ValueError('Note trop longue pour cet exercice.')
                path = self.root / 'sorties' / 'note.md'
                if not path.resolve().is_relative_to(self.root):
                    return {'statut': 'refuse', 'raison': 'La destination sort de l’atelier.'}
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(args['texte'], encoding='utf-8')
                return {'statut': 'ok', 'fichier': 'sorties/note.md'}
            return {'statut': 'refuse', 'raison': 'Outil inconnu.'}
        except (ValueError, OSError) as erreur:
            return {'statut': 'erreur', 'raison': str(erreur)}


def rejouer(demandes, banc, limite=4):
    if not isinstance(demandes, list) or not 1 <= limite <= 20:
        raise ValueError('Une liste de demandes et une limite entre 1 et 20 sont attendues.')
    evenements = []
    for numero, demande in enumerate(demandes, 1):
        if numero > limite:
            evenements.append({'type': 'arret', 'raison': 'budget_appels', 'appels': limite})
            break
        debut = time.perf_counter()
        resultat = banc.executer(demande)
        evenements.append({'type': 'appel', 'numero': numero, 'demande': demande,
                           'resultat': resultat,
                           'secondes_outil': round(time.perf_counter() - debut, 6)})
    else:
        evenements.append({'type': 'arret', 'raison': 'fin_du_script', 'appels': len(demandes)})
    return evenements


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cas', choices=['lecture', 'refus', 'injection', 'boucle', 'reprise'])
    parser.add_argument('--limite', type=int, default=4)
    parser.add_argument('--autoriser-ecriture', action='store_true')
    parser.add_argument('--journal', type=Path, required=True)
    args = parser.parse_args()
    if not 1 <= args.limite <= 20:
        parser.error('--limite doit être comprise entre 1 et 20.')
    if args.journal.exists():
        parser.error('Le journal existe déjà : choisissez un nouveau nom.')
    demandes = json.loads((ROOT/'cas'/f'{args.cas}.json').read_text(encoding='utf-8'))
    evenements = rejouer(demandes, Banc(autoriser_ecriture=args.autoriser_ecriture), args.limite)
    args.journal.parent.mkdir(parents=True, exist_ok=True)
    with args.journal.open('x', encoding='utf-8') as journal:
        for e in evenements:
            journal.write(json.dumps(e, ensure_ascii=False)+'\n')
            if e['type'] == 'appel':
                print(f"{e['numero']}. {e['demande'].get('outil', '?')} : {e['resultat']['statut']}")
            else:
                print(f"Arrêt : {e['raison']} ({e['appels']} appels)")
    print(f'Journal : {args.journal}')


if __name__ == '__main__':
    main()
