# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Assembler les huit parties et les annexes en un seul import ZdS.

Les sources des parties restent inchangées. Les chemins d’images et les noms
internes des notes sont adaptés uniquement dans les fichiers du ZIP global.
"""
import argparse
import copy
import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath

from assembler_tutoriel import references

ROOT = Path(__file__).resolve().parents[1]
PARTS = (
    '01-histoire', '02-apprentissage', '03-modele-local', '04-developpement',
    '05-agents', '06-mcp-skills', '07-ia-maison', '08-choisir', 'annexes',
)
IMAGE = re.compile(r'\]\(image:([^\)]+)\)')
NOTE = re.compile(r'\[\^([^\]\s]+)\]')


def source_path(directory, relative):
    """Refuser les chemins ambigus et les sorties du répertoire de sources."""
    rel = PurePosixPath(relative)
    if rel.is_absolute() or '..' in rel.parts or '\\' in relative or ':' in relative:
        raise ValueError(f'Chemin interdit : {relative}')
    path = (directory / relative).resolve()
    if not path.is_relative_to(directory.resolve()) or not path.is_file():
        raise ValueError(f'Fichier absent ou hors du dossier : {directory}/{relative}')
    return path


def transform(text, prefix):
    """Réécrire les références hors blocs de code, et relever les images."""
    images, notes, definitions, lines = set(), set(), set(), []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\r\n'))
        if marker:
            run, rest = marker.groups()
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not rest.strip():
                fence = None
            lines.append(line)
            continue
        if fence is None:
            images.update(IMAGE.findall(line))
            notes.update(NOTE.findall(line))
            definition = re.match(r'^ {0,3}\[\^([^\]\s]+)\]:', line)
            if definition:
                definitions.add(definition.group(1))
            if prefix:
                line = IMAGE.sub(lambda m: f'](image:{prefix}/{m.group(1)})', line)
                line = NOTE.sub(lambda m: f'[^{prefix}-{m.group(1)}]', line)
        lines.append(line)
    return ''.join(lines), images, notes, definitions


def prefixed(node, prefix):
    result = copy.deepcopy(node)
    for key in ('introduction', 'conclusion', 'text'):
        if result.get(key):
            result[key] = f'{prefix}/{result[key]}'
    if result.get('object') == 'container':
        result['ready_to_publish'] = False
    result['children'] = [prefixed(c, prefix) for c in result.get('children', [])]
    if not result['children']:
        result.pop('children')
    return result


def assemble(root, output, parts=PARTS):
    tutorial = root / 'tutoriel'
    entries = {}
    manifest = {
        'object': 'container', 'slug': 'comprendre-lia-et-developper-avec-elle',
        'title': 'Comprendre l’IA et développer avec elle',
        'introduction': 'introduction.md', 'conclusion': 'conclusion.md',
        'children': [], 'ready_to_publish': False,
    }
    report = {'parties': 0, 'groupes_annexes': 0, 'chapitres': 0,
              'chapitres_annexes': 0, 'sections': 0, 'images': 0,
              'notes': 0, 'fichiers_markdown': 0}

    def add(name, data):
        if name in entries:
            raise ValueError(f'Entrée ZIP en double : {name}')
        entries[name] = data

    for name in ('introduction.md', 'conclusion.md'):
        text = source_path(tutorial, name).read_text(encoding='utf-8')
        transformed, images, notes, definitions = transform(text, 'global')
        if images:
            raise ValueError('Les images de l’introduction générale doivent être gérées explicitement.')
        if notes != definitions:
            raise ValueError(f'Notes non résolues dans {name} : {notes ^ definitions}')
        add(name, transformed.encode('utf-8'))
        report['notes'] += len(definitions)
        report['fichiers_markdown'] += 1

    for part_name in parts:
        part = tutorial / part_name
        source = json.loads(source_path(part, 'manifest.json').read_text(encoding='utf-8'))
        manifest['children'].append(prefixed(source, part_name))
        images, all_notes, all_definitions = set(), set(), set()
        for relative in sorted(references(source)):
            text = source_path(part, relative).read_text(encoding='utf-8')
            transformed, found, notes, definitions = transform(text, part_name)
            duplicate = all_definitions & definitions
            if duplicate:
                raise ValueError(f'Définitions de notes en double dans {part_name} : {duplicate}')
            images.update(found)
            all_notes.update(notes)
            all_definitions.update(definitions)
            add(f'{part_name}/{relative}', transformed.encode('utf-8'))
            report['fichiers_markdown'] += 1
        if all_notes != all_definitions:
            raise ValueError(f'Notes non résolues dans {part_name} : {all_notes ^ all_definitions}')
        for relative in sorted(images):
            add(f'{part_name}/{relative}', source_path(part, relative).read_bytes())
        for relative in ('CREDITS.md', 'sources.json'):
            if (part / relative).is_file():
                add(f'{part_name}/{relative}', source_path(part, relative).read_bytes())
        annex = part_name == 'annexes'
        report['groupes_annexes' if annex else 'parties'] += 1
        report['chapitres_annexes' if annex else 'chapitres'] += len(source['children'])
        report['sections'] += sum(len(c['children']) for c in source['children'])
        report['images'] += len(images)
        report['notes'] += len(all_definitions)

    for name in ('LICENSE', 'LICENCE-TEXTES.md', 'CREDITS.md'):
        add(name, source_path(root, name).read_bytes())
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    add('manifest.json', manifest_bytes)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Dates et attributs fixes : mêmes sources, mêmes octets dans l’archive.
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    (tutorial / 'manifest.json').write_bytes(manifest_bytes)
    report['entrees_zip'] = len(entries)
    report['sha256_zip'] = hashlib.sha256(output.read_bytes()).hexdigest()
    report['import_interactif_zds'] = 'non effectué'
    (root / 'docs').mkdir(exist_ok=True)
    (root / 'docs/structure-globale.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sortie', type=Path,
                        default=ROOT / 'telechargements/zds/tutoriel-ia-complet.zip')
    args = parser.parse_args()
    print(json.dumps(assemble(ROOT, args.sortie), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
