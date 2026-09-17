# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Cohérence des matériaux fictifs. Aucun modèle et aucune action extérieure."""
import csv
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parent
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def read(relative):
    return (ROOT / relative).read_text(encoding='utf-8')


def message_id(text):
    return re.search(r'^Message-ID: (.+)$', text, flags=re.MULTILINE).group(1)


class DossierTest(unittest.TestCase):
    def test_cinq_fichiers_quatre_messages(self):
        messages = list((ROOT / 'entrees/courriels').glob('*.txt'))
        self.assertEqual(len(messages), 5)
        self.assertEqual(len({message_id(p.read_text(encoding='utf-8')) for p in messages}), 4)

    def test_copie_identique(self):
        self.assertEqual((ROOT / 'entrees/courriels/01-nora.txt').read_bytes(),
                         (ROOT / 'entrees/courriels/03-copie-nora.txt').read_bytes())

    def test_meme_expediteur_question_distincte(self):
        first = read('entrees/courriels/01-nora.txt')
        question = read('entrees/courriels/05-question-nora.txt')
        for text in (first, question):
            self.assertIn('De: Nora <nora@example.org>', text)
        self.assertNotEqual(message_id(first), message_id(question))
        self.assertIn('À quelle heure commence l’atelier Cartographie', question)

    def test_suivi_initial_et_nouveautes(self):
        with (ROOT / 'entrees/suivi-initial.csv').open(encoding='utf-8', newline='') as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], {
            'id_demande': 'D001', 'message_id': '<M004@atelier.example>',
            'nom': 'Samir', 'atelier': 'Reliure', 'places': '1',
            'statut': 'demande_enregistree', 'source': 'courriels/04-samir.txt',
        })
        self.assertEqual(message_id(read('entrees/' + rows[0]['source'])), rows[0]['message_id'])
        ids = {message_id(p.read_text(encoding='utf-8')) for p in (ROOT / 'entrees/courriels').glob('*.txt')}
        self.assertEqual(ids - {r['message_id'] for r in rows}, {
            '<M001@atelier.example>', '<M002@atelier.example>', '<M005@atelier.example>',
        })

    def test_atelier_absent_nombre_explicite(self):
        text = read('entrees/courriels/02-leo.txt')
        self.assertIn('une place pour lui et une pour moi', text)
        self.assertNotIn('Reliure', text)
        self.assertNotIn('Cartographie', text)

    def test_dates_et_horaires_ouverts(self):
        first = read('entrees/reunions/01-preparation.md')
        second = read('entrees/reunions/02-communication.md')
        self.assertIn('10 octobre 2026', first)
        self.assertIn('17 octobre 2026', second)
        self.assertIn('restent à préciser', first)
        self.assertIn('ne sont pas encore renseignés', second)

    def test_fiction_et_adresses(self):
        for path in (ROOT / 'entrees/courriels').glob('*.txt'):
            text = path.read_text(encoding='utf-8')
            self.assertIn('données fictif', text)
            addresses = re.findall(r'[\w.-]+@([\w.-]+)', text)
            self.assertTrue(addresses)
            self.assertLessEqual(set(addresses), {'atelier.example', 'example.org'})
        for path in (ROOT / 'entrees/reunions').glob('*.md'):
            self.assertIn('ficti', path.read_text(encoding='utf-8'))

    def test_references_du_corrige(self):
        text = read('corrige/point-equipe.md')
        references = re.findall(r'`(entrees/[^`]+)`', text)
        self.assertTrue(references)
        for reference in references:
            self.assertTrue((ROOT / reference).is_file(), reference)
        self.assertIn('pas une sortie observée', text)
        self.assertIn('Aucun message n’a été envoyé', text)

    def test_xlsx_meme_donnees_sans_formule_ni_macro(self):
        with (ROOT / 'entrees/suivi-initial.csv').open(encoding='utf-8', newline='') as stream:
            expected = list(csv.reader(stream))
        with zipfile.ZipFile(ROOT / 'supports/suivi-initial.xlsx') as archive:
            self.assertIsNone(archive.testzip())
            self.assertFalse(any('vbaProject' in name or 'externalLinks/' in name for name in archive.namelist()))
            strings = []
            if 'xl/sharedStrings.xml' in archive.namelist():
                strings = [''.join(item.itertext()) for item in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
            sheet = ET.fromstring(archive.read('xl/worksheets/sheet1.xml'))
            self.assertEqual(sheet.findall('.//s:f', NS), [])
            actual = []
            for row in sheet.findall('.//s:sheetData/s:row', NS):
                if int(row.attrib['r']) > 2:
                    continue
                values = []
                for cell in row.findall('s:c', NS):
                    value = cell.find('s:v', NS)
                    if cell.attrib.get('t') == 's':
                        values.append(strings[int(value.text)])
                    elif cell.attrib.get('t') == 'inlineStr':
                        values.append(''.join(cell.find('s:is', NS).itertext()))
                    else:
                        values.append(value.text if value is not None else '')
                actual.append(values)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
