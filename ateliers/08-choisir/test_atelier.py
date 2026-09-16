# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
import copy
import json
from pathlib import Path
import unittest
from bilan import calculer as bilan
from energie import calculer as energie
from catalogue import verifier

ROOT = Path(__file__).resolve().parent


class Atelier(unittest.TestCase):
    def exemple(self):
        return json.loads((ROOT/'exemples/temps-fictifs.json').read_text())

    def test_temps_complet_au_lieu_de_production_seule(self):
        rapport = bilan(self.exemple())
        self.assertEqual([e['occupation_min'] for e in rapport['essais']], [23, 28])
        self.assertEqual(rapport['essais'][1]['actif_min'], 26)
        self.assertEqual(rapport['origine_declaree'], 'fictif')

    def test_duree_absente_ne_devient_pas_zero(self):
        doc = self.exemple()
        del doc['essais'][0]['minutes']['relire']
        with self.assertRaises(ValueError):
            bilan(doc)

    def test_durees_invalides(self):
        for value in (None, True, -1, float('nan'), float('inf')):
            with self.subTest(value=value):
                doc = self.exemple()
                doc['essais'][0]['minutes']['verifier'] = value
                with self.assertRaises(ValueError):
                    bilan(doc)

    def test_statut_incomplet_conserve(self):
        doc = self.exemple()
        doc['essais'][1]['statut'] = 'a_corriger'
        self.assertEqual(bilan(doc)['essais'][1]['statut'], 'a_corriger')

    def test_conversion_wh_kwh(self):
        resultat = energie(200, 30)
        self.assertEqual(resultat['energie_wh'], 100)
        self.assertEqual(resultat['energie_kwh'], .1)

    def test_puissance_invalide(self):
        for valeur in (-1, float('nan'), float('inf'), True):
            with self.assertRaises(ValueError):
                energie(valeur, 30)

    def test_catalogue_booleen_pas_prix(self):
        self.assertEqual(len(verifier([{'id': 'A', 'prix_centimes': True, 'disponible': True}])), 1)

    def test_catalogue_doublon(self):
        ligne = {'id': 'A', 'prix_centimes': 0, 'disponible': False}
        self.assertEqual(verifier([ligne]), [])
        erreurs = verifier([ligne, copy.copy(ligne)])
        self.assertEqual(erreurs[0]['ligne'], 2)
        self.assertIn('identifiant déjà rencontré', erreurs[0]['raisons'])


if __name__ == '__main__':
    unittest.main()
