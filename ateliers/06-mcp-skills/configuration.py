# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Afficher une configuration VS Code, sans modifier celle du lecteur."""
import json
import sys
from pathlib import Path

if __name__ == '__main__':
    print(json.dumps({'servers': {'atelier-tickets': {
        'type': 'stdio', 'command': sys.executable,
        'args': [str(Path(__file__).resolve().parent / 'serveur.py')]
    }}}, ensure_ascii=False, indent=2))
