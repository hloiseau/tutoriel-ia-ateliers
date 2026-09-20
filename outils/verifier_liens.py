# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Contrôler les cibles des liens locaux des pages destinées aux lecteurs."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    'README.md', 'SOMMAIRE.md', 'CONTRIBUTING.md',
    'docs/README.md', 'docs/etat-des-contenus.md', 'docs/verification.md',
    'docs/export-global.md', 'docs/archives/README.md',
)


def links(text):
    fence = None
    for line in text.splitlines():
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if marker:
            run, rest = marker.groups()
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not rest.strip():
                fence = None
            continue
        if fence is None:
            line = re.sub(r'(`+).*?\1', '', line)
            yield from re.findall(r'\]\(([^)\n]+)\)', line)


def main():
    files = {ROOT / name for name in PAGES}
    for directory in ('tutoriel', 'ateliers', 'telechargements'):
        files.update((ROOT / directory).rglob('*.md'))
    count, missing = 0, []
    for page in sorted(files):
        for url in links(page.read_text(encoding='utf-8')):
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            count += 1
            target = (page.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                missing.append(f'{page.relative_to(ROOT)} : {url}')
    if missing:
        raise SystemExit('\n'.join(missing))
    print(f'{count} liens locaux contrôlés dans {len(files)} pages : aucune cible manquante.')


if __name__ == '__main__':
    main()
