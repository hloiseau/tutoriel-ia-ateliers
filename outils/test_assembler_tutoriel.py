# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Vérifier l’assemblage ciblé sans modifier les statistiques du parcours global."""
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import assembler_tutoriel as assembler


class AssemblageCibleTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'docs').mkdir()
        (self.root / 'tutoriel').mkdir()
        self.report = self.root / 'docs/structure-tutoriel.json'
        self.report.write_text('rapport à préserver\n', encoding='utf-8')

    def part(self, relative):
        directory = self.root / relative
        (directory / '01-debut').mkdir(parents=True)
        manifest = {
            'title': 'Partie de test', 'introduction': 'introduction.md',
            'conclusion': 'conclusion.md', 'ready_to_publish': False,
            'children': [{
                'title': 'Début', 'introduction': '01-debut/introduction.md',
                'conclusion': '01-debut/conclusion.md', 'ready_to_publish': False,
                'children': [{'title': 'Section', 'text': '01-debut/section.md'}],
            }],
        }
        (directory / 'manifest.json').write_text(json.dumps(manifest), encoding='utf-8')
        for relative_file in assembler.references(manifest) | {'CREDITS.md'}:
            (directory / relative_file).write_text('Texte fictif de test.\n', encoding='utf-8')
        return directory

    def run_main(self, *args):
        with patch.object(assembler, 'ROOT', self.root), patch('sys.argv', ['assembler_tutoriel.py', *args]), redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            assembler.main()

    def test_cible_preserve_statistiques_et_autres_parties(self):
        draft = self.part('redaction/exemple')
        canonical = self.part('tutoriel/01-exemple')
        export = self.root / 'exports'
        self.run_main('--partie', 'redaction/exemple', '--exports', str(export))
        self.assertEqual(self.report.read_text(encoding='utf-8'), 'rapport à préserver\n')
        self.assertFalse((canonical / 'LECTURE.md').exists())
        self.assertIn('--partie redaction/exemple', (draft / 'README.md').read_text(encoding='utf-8'))
        with zipfile.ZipFile(export / 'exemple.zip') as archive:
            self.assertIsNone(archive.testzip())
            self.assertNotIn('LECTURE.md', archive.namelist())
            self.assertIn('01-debut/section.md', archive.namelist())
            self.assertFalse(json.loads(archive.read('manifest.json'))['ready_to_publish'])

    def test_parcours_par_defaut_ignore_les_brouillons(self):
        draft = self.part('redaction/exemple')
        canonical = self.part('tutoriel/01-exemple')
        self.run_main()
        self.assertTrue((canonical / 'LECTURE.md').is_file())
        self.assertFalse((draft / 'LECTURE.md').exists())
        report = json.loads(self.report.read_text(encoding='utf-8'))
        self.assertEqual([row['partie'] for row in report], ['01-exemple'])

    def test_refuse_un_dossier_sans_manifest(self):
        with self.assertRaises(SystemExit) as error:
            self.run_main('--partie', 'redaction/absent')
        self.assertEqual(error.exception.code, 2)

    def test_refuse_un_dossier_hors_depot(self):
        with self.assertRaises(SystemExit) as error:
            self.run_main('--partie', str(self.root.parent))
        self.assertEqual(error.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
