# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from assembler_global import assemble


class GlobalArchiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.output = self.root / 'export.zip'
        tutorial = self.root / 'tutoriel'
        tutorial.mkdir()
        (tutorial / 'introduction.md').write_text('Bonjour.\n')
        (tutorial / 'conclusion.md').write_text('')
        for name in ('LICENSE', 'LICENCE-TEXTES.md', 'CREDITS.md'):
            (self.root / name).write_text(name)
        for part_name in ('un', 'deux'):
            part = tutorial / part_name
            (part / 'images').mkdir(parents=True)
            (part / 'images/schema.png').write_bytes(part_name.encode())
            (part / 'intro.md').write_text('Introduction.\n')
            (part / 'fin.md').write_text('Fin.\n')
            (part / 'section.md').write_text(
                '![Image](image:images/schema.png)\nTexte[^source].\n'
                '[^source]: Crédit.\n\n```markdown\n'
                '![Exemple](image:absente.png)\nExemple[^sans-definition]\n```\n')
            extract = {'object': 'extract', 'slug': 'texte', 'title': 'Texte', 'text': 'section.md'}
            chapter = {'object': 'container', 'slug': 'chapitre', 'title': 'Chapitre',
                       'introduction': 'intro.md', 'conclusion': 'fin.md',
                       'children': [extract], 'ready_to_publish': True}
            manifest = {'object': 'container', 'slug': part_name, 'title': part_name,
                        'introduction': 'intro.md', 'conclusion': 'fin.md',
                        'children': [chapter], 'ready_to_publish': True}
            (part / 'manifest.json').write_text(json.dumps(manifest))

    def build(self):
        return assemble(self.root, self.output, ('un', 'deux'))

    def test_two_parts_keep_their_images_notes_and_code(self):
        source = self.root / 'tutoriel/un/section.md'
        before = source.read_bytes()
        report = self.build()
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual(report['images'], 2)
        self.assertEqual(report['notes'], 2)
        with zipfile.ZipFile(self.output) as archive:
            manifest = json.loads(archive.read('manifest.json'))
            self.assertEqual(len(manifest['children']), 2)
            self.assertFalse(manifest['ready_to_publish'])
            for part in manifest['children']:
                self.assertFalse(part['ready_to_publish'])
                self.assertFalse(part['children'][0]['ready_to_publish'])
                self.assertIn(part['children'][0]['children'][0]['text'], archive.namelist())
            self.assertEqual(archive.read('un/images/schema.png'), b'un')
            self.assertEqual(archive.read('deux/images/schema.png'), b'deux')
            text = archive.read('un/section.md').decode()
            self.assertIn('(image:un/images/schema.png)', text)
            self.assertIn('[^un-source]: Crédit.', text)
            self.assertIn('```markdown\n![Exemple](image:absente.png)\nExemple[^sans-definition]\n```', text)
        original = self.output.read_bytes()
        self.build()
        self.assertEqual(self.output.read_bytes(), original)

    def test_missing_image_fails_before_export(self):
        (self.root / 'tutoriel/un/images/schema.png').unlink()
        with self.assertRaises(ValueError):
            self.build()
        self.assertFalse(self.output.exists())

    def test_escape_is_rejected_even_when_target_exists(self):
        (self.root / 'tutoriel/secret.png').write_bytes(b'private')
        (self.root / 'tutoriel/un/section.md').write_text('![Image](image:../secret.png)')
        with self.assertRaises(ValueError):
            self.build()

    def test_unresolved_note_is_rejected(self):
        (self.root / 'tutoriel/un/section.md').write_text('Texte[^absente].')
        with self.assertRaisesRegex(ValueError, 'Notes non résolues'):
            self.build()


if __name__ == '__main__':
    unittest.main()
