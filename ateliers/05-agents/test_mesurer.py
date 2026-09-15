# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
import tempfile
import unittest
from pathlib import Path
from decimal import Decimal
from mesurer import cout


class Couts(unittest.TestCase):
    def test_categories_disjointes_et_plusieurs_appels(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'usage.csv'
            p.write_text('entree_hors_cache,entree_cache,sortie\n1000,0,100\n200,1000,100\n')
            self.assertEqual(cout(p,'2','0.2','8'), Decimal('0.0042'))

    def test_tarif_invalide(self):
        with self.assertRaises(ValueError):
            cout('non_lu.csv', '-1', '0', '1')


if __name__ == '__main__':
    unittest.main()
