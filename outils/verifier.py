# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

"""Contrôles rapides, sans API distante ni modèle à télécharger."""
from pathlib import Path
import subprocess
import sys
import re

ROOT = Path(__file__).resolve().parents[1]


def tests(dossier, nombre, echecs):
    p = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-v'],
                       cwd=ROOT / dossier, capture_output=True, text=True)
    print(p.stderr, end='')
    assert re.search(rf'Ran {nombre} tests?', p.stderr), 'Nombre de tests inattendu'
    assert p.returncode == (1 if echecs else 0), 'Résultat inattendu'
    if echecs:
        assert f'FAILED (failures={echecs})' in p.stderr


def main():
    tests('ateliers/03-modele-local/atelier-local', 6, 0)
    for etape, nombre, echecs in [('01-depart', 3, 0), ('02-test-rouge', 13, 2), ('03-corrige', 13, 0)]:
        tests('ateliers/04-developpement/atelier-developpement/' + etape, nombre, echecs)
    tests('ateliers/05-agents', 12, 0)
    print('Les résultats correspondent aux étapes attendues.')


if __name__ == '__main__':
    main()
