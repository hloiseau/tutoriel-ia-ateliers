import io
import json
import unittest
from unittest.mock import patch
from client import appeler, SansRedirection

class Reponse(io.BytesIO):
    pass

class ClientTest(unittest.TestCase):
    def reponse(self, usage=True):
        d = {'choices': [{'message': {'content': 'Réponse factice'}, 'finish_reason': 'stop'}]}
        if usage: d['usage'] = {'completion_tokens': 4}
        return Reponse(json.dumps(d).encode())

    def test_requete_et_reponse(self):
        with patch('client.OPENER.open', return_value=self.reponse()) as ouvrir:
            r = appeler([{'role': 'user', 'content': 'Bonjour'}])
        req = ouvrir.call_args.args[0]
        self.assertEqual(req.full_url, 'http://127.0.0.1:8080/v1/chat/completions')
        self.assertFalse(json.loads(req.data)['cache_prompt'])
        self.assertEqual(r['tokens_sortie'], 4)
        self.assertEqual(r['texte'], 'Réponse factice')

    def test_usage_absent_reste_absent(self):
        with patch('client.OPENER.open', return_value=self.reponse(False)):
            self.assertIsNone(appeler([{'role':'user','content':'x'}])['tokens_sortie_par_seconde_globale'])

    def test_pas_de_messages(self):
        with self.assertRaises(ValueError): appeler([])

    def test_trop_de_tokens(self):
        with self.assertRaises(ValueError): appeler([{'role':'user','content':'x'}], 513)

    def test_aucune_redirection(self):
        self.assertIsNone(SansRedirection().redirect_request(None,None,302,'',{},'https://example.com'))

    def test_erreur_reseau_remonte(self):
        with patch('client.OPENER.open', side_effect=TimeoutError):
            with self.assertRaises(TimeoutError): appeler([{'role':'user','content':'x'}])

if __name__ == '__main__': unittest.main()
