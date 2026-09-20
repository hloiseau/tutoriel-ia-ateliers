# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Format commun aux exports de contenu et d’images pour Zeste de Savoir."""
import copy
import re
import zipfile

IMAGE = re.compile(r'\]\((?:image|archive):([^\)]+)\)')
NOTE = re.compile(r'\[\^([^\]\s]+)\]')


def transform(text, prefix=''):
    """Adapter les liens et les notes hors blocs de code."""
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
            line = IMAGE.sub(lambda m: f'](archive:{prefix + "/" if prefix else ""}{m.group(1)})', line)
            if prefix:
                line = NOTE.sub(lambda m: f'[^{prefix}-{m.group(1)}]', line)
        lines.append(line)
    return ''.join(lines), images, notes, definitions


def import_manifest(source):
    manifest = copy.deepcopy(source)
    manifest.update(version=2.1, type='TUTORIAL', licence='CC BY-SA')
    manifest.setdefault('description', manifest['title'])
    return manifest


def write_zip(output, entries):
    """Produire la même archive pour les mêmes sources."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)


def images_path(content_path):
    return content_path.with_name(content_path.stem + '-images.zip')
