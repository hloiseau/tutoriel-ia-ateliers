# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

import unittest
from suivi import Etat, notifier


class ComportementExistant(unittest.TestCase):
    def test_baisse_en_stock(self):
        self.assertTrue(notifier(Etat(2000, True), Etat(1500, True)))

    def test_hausse_en_stock(self):
        self.assertFalse(notifier(Etat(1500, True), Etat(2000, True)))

    def test_baisse_mais_indisponible(self):
        self.assertFalse(notifier(Etat(2000, True), Etat(1500, False)))


if __name__ == "__main__":
    unittest.main()
