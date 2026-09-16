# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

"""Créer les archives d’atelier, sans poids téléchargés ni sorties personnelles."""
import argparse
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SORTIE = ROOT / 'telechargements'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--atelier', help='Ne reconstruire que ce dossier, par exemple 05-agents')
    args = parser.parse_args()
    SORTIE.mkdir(exist_ok=True)
    ateliers = [
        ('02-apprentissage', 'annexes-atelier-ia-v1.zip'),
        ('03-modele-local', 'annexes-modele-local-v1.zip'),
        ('04-developpement', 'annexes-developpement-v1.zip'),
        ('05-agents', 'atelier-agents.zip'),
        ('06-mcp-skills', 'atelier-mcp-skills.zip'),
        ('07-ia-maison', 'atelier-ia-maison.zip'),
        ('08-choisir', 'atelier-choisir-ia.zip'),
    ]
    if args.atelier and args.atelier not in {d for d, _ in ateliers}:
        parser.error('Atelier inconnu.')
    for dossier, nom in ateliers:
        if args.atelier and dossier != args.atelier:
            continue
        base = ROOT / 'ateliers' / dossier
        with zipfile.ZipFile(SORTIE / nom, 'w', zipfile.ZIP_DEFLATED) as z:
            for notice in ['LICENSE', 'LICENCE-TEXTES.md', 'CREDITS.md']:
                z.write(ROOT / notice, notice)
            for fichier in sorted(base.rglob('*')):
                rel = fichier.relative_to(base)
                if not fichier.is_file() or {'__pycache__', '.venv', 'sorties', 'resultats', 'modeles', 'moteur'}.intersection(rel.parts):
                    continue
                if fichier.suffix in {'.pyc', '.gguf', '.part'}:
                    continue
                z.write(fichier, rel.as_posix())
        print(nom)


if __name__ == '__main__':
    main()
