# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Vérifier les sources ZdS et générer les lectures GitHub et les ZIP d’import."""
import argparse
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def references(node):
    result = set()
    for key in ('introduction', 'conclusion', 'text'):
        if node.get(key):
            result.add(node[key])
    for child in node.get('children', []):
        result.update(references(child))
    return result


def lecture(text, level, image_prefix):
    result, fence = [], None
    for line in text.splitlines():
        marker = re.match(r'^(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker.group(1)
            elif marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence):
                fence = None
            result.append(line)
            continue
        if fence is None:
            title = re.match(r'^(#{1,6}) (.*)', line)
            if title:
                line = '#' * min(6, len(title.group(1)) + level) + ' ' + title.group(2)
            line = re.sub(r'\]\(image:([^\)]+)\)', lambda m: '](' + image_prefix + m.group(1) + ')', line)
        result.append(line)
    return '\n'.join(result).strip() + '\n'


def read(part, path):
    return (part / path).read_text(encoding='utf-8') if path else ''


def build(part, export):
    manifest = json.loads((part / 'manifest.json').read_text())
    files = references(manifest)
    images = set()
    for rel in files:
        path = (part / rel).resolve()
        if not path.is_relative_to(part.resolve()) or not path.is_file():
            raise ValueError(f'Référence manquante : {part.name}/{rel}')
        text = path.read_text()
        images.update(re.findall(r'\]\(image:([^\)]+)\)', text))
    for rel in images:
        path = (part / rel).resolve()
        if not path.is_relative_to(part.resolve()) or not path.is_file():
            raise ValueError(f'Image manquante : {part.name}/{rel}')

    title = manifest['title']
    index = f'# {title}\n\n[Sommaire global](../../SOMMAIRE.md) · [Lecture complète](LECTURE.md)\n\n'
    guided = part.name in {'04-developpement', '05-agents'}
    annexes = part.name == 'annexes'
    workshop_count = len(manifest['children'])
    if part.name == '04-developpement':
        index += 'Les sept chapitres ci-dessous se suivent dans le même dossier de travail. Le [comparatif des outils](../annexes/comparatif/LECTURE.md) et l’[expérience locale](../annexes/essai-local/LECTURE.md) se trouvent dans les annexes.\n\n'
    elif part.name == '05-agents':
        index += '[Atelier Python](../../ateliers/05-agents/README.md) · [Résultats et limites des vérifications](VERIFICATION.md)\n\n'
    complete = f'# {title}\n\n[Sommaire de la partie](README.md) · [Sommaire global](../../SOMMAIRE.md)\n\n'
    complete += lecture(read(part, manifest.get('introduction')), 1, '')
    for i, chapter in enumerate(manifest['children'], 1):
        directory = Path(chapter['introduction']).parent
        label = f'Annexe {chr(64 + i)}' if annexes else str(i)
        index += (f"- **{label}** — " if annexes else f'{i}. ') + f"[{chapter['title']}]({directory.as_posix()}/LECTURE.md)\n"
        nav_title = 'Sommaire des annexes' if annexes else 'Sommaire de la partie'
        page = f"# {label}. {chapter['title']}\n\n[{nav_title}](../README.md) · [Sources](.)\n\n"
        nav = ''
        if guided:
            if i <= workshop_count:
                links = []
                for offset, label in ((-1, 'Précédent'), (1, 'Suivant')):
                    target = i - 1 + offset
                    if 0 <= target < workshop_count:
                        other = manifest['children'][target]
                        other_dir = Path(other['introduction']).parent.as_posix()
                        links.append(f"[{label} : {other['title']}](../{other_dir}/LECTURE.md)")
                nav = ' · '.join(links) + '\n'
            page += nav + '\n'
        elif annexes:
            nav = '[Revenir à l’atelier de développement](../../04-developpement/README.md)\n'
            page += nav + '\n'
        page += lecture(read(part, chapter.get('introduction')), 1, '../')
        complete += f"\n## {label}. {chapter['title']}\n\n" + lecture(read(part, chapter.get('introduction')), 2, '')
        for section in chapter['children']:
            text = read(part, section['text'])
            page += f"\n## {section['title']}\n\n" + lecture(text, 2, '../')
            complete += f"\n### {section['title']}\n\n" + lecture(text, 3, '')
        page += '\n' + lecture(read(part, chapter.get('conclusion')), 1, '../')
        if nav:
            page += '\n---\n\n' + nav
        complete += '\n' + lecture(read(part, chapter.get('conclusion')), 2, '')
        (part / directory / 'LECTURE.md').write_text(page, encoding='utf-8')
    complete += '\n## Conclusion\n\n' + lecture(read(part, manifest.get('conclusion')), 1, '')
    index += '\n[Introduction](introduction.md) · [Conclusion](conclusion.md) · [Crédits](CREDITS.md)\n\n'
    index += 'Les fichiers `LECTURE.md` sont générés. Pour corriger un passage, modifier le petit Markdown déclaré dans `manifest.json`, puis lancer `python outils/assembler_tutoriel.py` depuis la racine du dépôt.\n\n'
    index += '[État de relecture et des vérifications](../../docs/etat-des-contenus.md)\n'
    (part / 'README.md').write_text(index, encoding='utf-8')
    (part / 'LECTURE.md').write_text(complete, encoding='utf-8')
    if (part / 'SOMMAIRE.md').exists():
        (part / 'SOMMAIRE.md').write_text('# Sommaire de la partie\n\n[Consulter le sommaire courant](README.md).\n')
    if export:
        export.mkdir(parents=True, exist_ok=True)
        paths = files | images | {'manifest.json', 'CREDITS.md'}
        if (part/'sources.json').exists():
            paths.add('sources.json')
        with zipfile.ZipFile(export / (part.name + '.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
            for rel in sorted(paths):
                z.write(part / rel, rel)
    return {'partie': part.name, 'chapitres': len(manifest['children']),
            'sections': sum(len(c['children']) for c in manifest['children']),
            'images': len(images), 'fichiers_sources': len(files)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exports', type=Path, help='Dossier de sortie des ZIP ZdS des parties et des annexes')
    args = parser.parse_args()
    reports = [build(p, args.exports) for p in sorted((ROOT/'tutoriel').iterdir()) if (p/'manifest.json').is_file()]
    (ROOT/'docs/structure-tutoriel.json').write_text(json.dumps(reports, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(reports, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
