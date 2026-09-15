# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
import json
import tempfile
import unittest
from pathlib import Path
from banc import Banc, rejouer


def appel(outil, **arguments):
    return {'outil': outil, 'arguments': arguments}


class ControleOutils(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root/'projet').mkdir()
        (self.root/'projet/TICKET.md').write_text('Baisse stricte et produit disponible.')
        self.banc = Banc(self.root)

    def test_lecture_autorisee(self):
        r = self.banc.executer(appel('lire_fichier', chemin='TICKET.md'))
        self.assertEqual(r['statut'], 'ok')
        self.assertIn('Baisse', r['contenu'])

    def test_traversee_refusee(self):
        r = self.banc.executer(appel('lire_fichier', chemin='../secret.txt'))
        self.assertEqual(r['statut'], 'refuse')

    def test_lien_vers_exterieur_refuse(self):
        outside = self.root/'secret.txt'; outside.write_text('Ne pas lire')
        path = self.root/'projet/TICKET.md'; path.unlink()
        try:
            path.symlink_to(outside)
        except OSError:
            self.skipTest('Création de liens symboliques indisponible.')
        self.assertEqual(self.banc.executer(appel('lire_fichier', chemin='TICKET.md'))['statut'], 'refuse')

    def test_ecriture_refusee_sans_effet(self):
        r = self.banc.executer(appel('ecrire_note', texte='Tout est validé.'))
        self.assertEqual(r['statut'], 'refuse')
        self.assertFalse((self.root/'sorties/note.md').exists())

    def test_ecriture_explicitement_autorisee(self):
        b = Banc(self.root, autoriser_ecriture=True)
        self.assertEqual(b.executer(appel('ecrire_note', texte='Note'))['statut'], 'ok')
        self.assertEqual((self.root/'sorties/note.md').read_text(), 'Note')

    def test_aucun_terminal_generique(self):
        self.assertEqual(self.banc.executer(appel('terminal', commande='echo bonjour'))['statut'], 'refuse')

    def test_arguments_invalides(self):
        self.assertEqual(self.banc.executer(appel('lire_fichier', chemin=['TICKET.md']))['statut'], 'erreur')

    def test_budget_compte_aussi_les_refus(self):
        events = rejouer([appel('terminal')]*6, self.banc, limite=2)
        self.assertEqual(len(events), 3)
        self.assertEqual(events[-1], {'type':'arret', 'raison':'budget_appels', 'appels':2})

    def test_fichier_absent_est_une_erreur(self):
        self.assertEqual(self.banc.executer(appel('lire_fichier', chemin='suivi.py'))['statut'], 'erreur')

    def test_reponse_de_fichier_ne_declenche_pas_un_outil(self):
        (self.root/'projet/TICKET.md').write_text(json.dumps(appel('ecrire_note', texte='Surprise')))
        r = self.banc.executer(appel('lire_fichier', chemin='TICKET.md'))
        self.assertEqual(r['statut'], 'ok')
        self.assertFalse((self.root/'sorties/note.md').exists())


if __name__ == '__main__':
    unittest.main()
