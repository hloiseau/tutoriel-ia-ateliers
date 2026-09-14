# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

"""Télécharge un fichier de poids identifié, puis vérifie sa somme SHA-256."""
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent

def empreinte(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for bloc in iter(lambda: f.read(1024 * 1024), b''):
            h.update(bloc)
    return h.hexdigest()

def main():
    info = json.loads((ROOT / 'modele.json').read_text(encoding='utf-8'))
    dossier = ROOT / 'modeles'
    dossier.mkdir(exist_ok=True)
    cible = dossier / info['fichier']
    if cible.exists():
        if cible.stat().st_size == info['octets'] and empreinte(cible) == info['sha256']:
            print('Fichier déjà présent et vérifié :', cible.name)
            return
        raise SystemExit('Le fichier existant ne correspond pas. Déplacez-le avant de réessayer.')
    temporaire = cible.with_suffix('.gguf.part')
    url = f"https://huggingface.co/{info['depot']}/resolve/{info['revision']}/{info['fichier']}"
    print('Téléchargement :', info['fichier'], flush=True)
    total = 0
    try:
        with urllib.request.urlopen(url, timeout=60) as reponse, temporaire.open('wb') as sortie:
            while bloc := reponse.read(1024 * 1024):
                sortie.write(bloc)
                total += len(bloc)
                print(f'\r{total / 1_000_000:.1f} / {info["octets"] / 1_000_000:.1f} Mo', end='', flush=True)
        print()
        if total != info['octets'] or empreinte(temporaire) != info['sha256']:
            raise ValueError('Taille ou empreinte incorrecte ; le fichier n’a pas été validé.')
        temporaire.replace(cible)
    except Exception as erreur:
        raise SystemExit(f'Téléchargement interrompu : {erreur}. Relancez pour recommencer.')
    print('SHA-256 vérifié. Modèle disponible dans modeles/.')

if __name__ == '__main__':
    main()
