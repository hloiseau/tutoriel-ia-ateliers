# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

"""Créer les trois archives d’atelier, sans poids téléchargés ni sorties personnelles."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SORTIE = ROOT / 'telechargements'


def main():
    SORTIE.mkdir(exist_ok=True)
    ateliers = [
        ('02-apprentissage', 'annexes-atelier-ia-v1.zip'),
        ('03-modele-local', 'annexes-modele-local-v1.zip'),
        ('04-developpement', 'annexes-developpement-v1.zip'),
    ]
    for dossier, nom in ateliers:
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
