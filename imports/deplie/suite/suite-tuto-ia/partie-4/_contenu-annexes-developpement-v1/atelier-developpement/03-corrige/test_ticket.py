import unittest
from suivi import Etat, notifier


class TicketPrix(unittest.TestCase):
    def test_retour_en_stock_sans_baisse(self):
        self.assertFalse(notifier(Etat(2000, False), Etat(2000, True)))

    def test_retour_en_stock_avec_baisse(self):
        self.assertTrue(notifier(Etat(2000, False), Etat(1500, True)))

    def test_retour_en_stock_avec_hausse(self):
        self.assertFalse(notifier(Etat(2000, False), Etat(2500, True)))

    def test_prix_identique_deja_en_stock(self):
        self.assertFalse(notifier(Etat(2000, True), Etat(2000, True)))

    def test_baisse_un_centime(self):
        self.assertTrue(notifier(Etat(2000, True), Etat(1999, True)))

    def test_prix_zero(self):
        self.assertTrue(notifier(Etat(1, True), Etat(0, True)))


class DonneesInvalides(unittest.TestCase):
    def test_prix_negatif(self):
        with self.assertRaises(ValueError):
            Etat(-1, True)

    def test_prix_decimal(self):
        with self.assertRaises(ValueError):
            Etat(19.99, True)

    def test_booleen_comme_prix(self):
        with self.assertRaises(ValueError):
            Etat(True, True)

    def test_disponibilite_non_booleenne(self):
        with self.assertRaises(ValueError):
            Etat(1000, "oui")


if __name__ == "__main__":
    unittest.main()
