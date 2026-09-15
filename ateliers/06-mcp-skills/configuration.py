# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Afficher une configuration VS Code, sans modifier celle du lecteur."""
import json
import sys
import argparse
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--serveur', type=Path, default=Path(__file__).resolve().parent/'serveur.py')
    args = parser.parse_args()
    if not args.serveur.is_file():
        parser.error('Le fichier serveur est introuvable.')
    print(json.dumps({'servers': {'atelier-tickets': {
        'type': 'stdio', 'command': sys.executable,
        'args': [str(args.serveur.resolve())]
    }}}, ensure_ascii=False, indent=2))
