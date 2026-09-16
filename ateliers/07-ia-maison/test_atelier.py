# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from pathlib import Path
import numpy as np
from recherche import Index, charger
from assistant_local import preparer
from petit_modele import initialiser, calculer, CONTEXTE, VOCAB, charger_lot, lire, avec_adaptateur


class Recherche(unittest.TestCase):
    def test_archive_exclue(self):
        ids={p['id'] for p in charger()}
        self.assertFalse(any(s.startswith(('ancienne-regle#','note-piegee#')) for s in ids))

    def test_question_hors_corpus(self):
        self.assertEqual(preparer('Température de Neptune')['statut'],'aucune_source_retrouvee')

    def test_document_retrouve(self):
        passages=Index(charger()).chercher('données staging réinitialisées')
        self.assertEqual(passages[0]['id'],'staging#1')

    def test_pas_de_promesse_semantique(self):
        self.assertEqual(Index(charger()).chercher('purge fixtures'),[])

    def test_sources_retracables(self):
        p=preparer('retour en stock prix égal')
        self.assertTrue(p['passages'])
        for s in p['passages']:self.assertIn('['+s['id']+']',p['messages'][1]['content'])


class Modele(unittest.TestCase):
    def test_rechargement_adaptateur(self):
        racine=Path(__file__).resolve().parent/'resultats-reference'
        base=lire(racine/'base/modele.npz')
        recharge=avec_adaptateur(base,racine/'lora/adaptateur.npz')
        complet=lire(racine/'lora/modele.npz')
        x=np.zeros((1,CONTEXTE),dtype=int)
        np.testing.assert_array_equal(calculer(recharge,x),calculer(complet,x))
        self.assertNotIn('A',base)

    def test_adaptateur_refuse_autre_base(self):
        racine=Path(__file__).resolve().parent/'resultats-reference'
        autre=lire(racine/'complet/modele.npz')
        with self.assertRaisesRegex(ValueError,'ne correspond pas'):
            avec_adaptateur(autre,racine/'lora/adaptateur.npz')

    def test_gradients_modele(self):
        p=initialiser();rng=np.random.default_rng(4)
        x=rng.integers(len(VOCAB),size=(3,CONTEXTE));y=rng.integers(len(VOCAB),size=3)
        _,g=calculer(p,x,y,True)
        for nom in p:
            idx=np.unravel_index(np.argmax(np.abs(g[nom])),g[nom].shape)
            avant=p[nom][idx];eps=1e-5
            p[nom][idx]=avant+eps;plus=calculer(p,x,y)
            p[nom][idx]=avant-eps;moins=calculer(p,x,y);p[nom][idx]=avant
            self.assertAlmostEqual(g[nom][idx],(plus-moins)/(2*eps),places=6)

    def test_gradients_adaptateur(self):
        p=initialiser();rng=np.random.default_rng(4)
        p['A']=rng.normal(0,.1,(64,2));p['B']=rng.normal(0,.1,(2,len(VOCAB)))
        x=rng.integers(len(VOCAB),size=(3,CONTEXTE));y=rng.integers(len(VOCAB),size=3)
        _,g=calculer(p,x,y,True);self.assertEqual(set(g),{'A','B'})
        for nom in g:
            idx=np.unravel_index(np.argmax(np.abs(g[nom])),g[nom].shape)
            avant=p[nom][idx];eps=1e-5
            p[nom][idx]=avant+eps;plus=calculer(p,x,y)
            p[nom][idx]=avant-eps;moins=calculer(p,x,y);p[nom][idx]=avant
            self.assertAlmostEqual(g[nom][idx],(plus-moins)/(2*eps),places=6)

    def test_pas_de_fenetre_entre_deux_lignes(self):
        x,y=charger_lot('base','validation')
        for j in np.flatnonzero(y==VOCAB.index('\n')):
            if j+1<len(x):self.assertTrue((x[j+1]==0).all())

    def test_adaptateur_initial_ne_change_pas_les_predictions(self):
        p=initialiser();x=np.zeros((1,CONTEXTE),dtype=int);avant=calculer(p,x)
        p['A']=np.ones((64,4));p['B']=np.zeros((4,len(VOCAB)))
        np.testing.assert_array_equal(avant,calculer(p,x))


if __name__=='__main__':unittest.main()
