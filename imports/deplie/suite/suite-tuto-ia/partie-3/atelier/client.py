"""Client de l’atelier : uniquement le serveur de cette machine, port 8080."""
import argparse
import json
from pathlib import Path
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent
BASE = 'http://127.0.0.1:8080'

class SansRedirection(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}), SansRedirection())

def appeler(messages, max_tokens=96):
    if not messages or type(max_tokens) is not int or not 1 <= max_tokens <= 512:
        raise ValueError('Messages requis et max_tokens compris entre 1 et 512.')
    corps = {'model': 'atelier-local', 'messages': messages, 'temperature': 0,
             'max_tokens': max_tokens, 'stream': False, 'cache_prompt': False}
    req = urllib.request.Request(BASE + '/v1/chat/completions',
            data=json.dumps(corps).encode(), headers={'Content-Type': 'application/json'})
    debut = time.perf_counter()
    with OPENER.open(req, timeout=180) as reponse:
        document = json.load(reponse)
    duree = time.perf_counter() - debut
    choix = document['choices'][0]
    texte = choix['message']['content']
    if not isinstance(texte, str):
        raise ValueError('La réponse ne contient pas de texte.')
    usage = document.get('usage') or {}
    tokens = usage.get('completion_tokens')
    return {'requete': corps, 'reponse_brute': document, 'texte': texte,
            'raison_arret': choix.get('finish_reason'), 'duree_s': duree,
            'tokens_sortie': tokens,
            'tokens_sortie_par_seconde_globale': tokens / duree if type(tokens) is int else None}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--fichier', default='questions/premiere.json', type=Path)
    p.add_argument('--sortie', default='resultats/reponse.json', type=Path)
    args = p.parse_args()
    try:
        messages = json.loads(args.fichier.read_text(encoding='utf-8'))
        rapport = appeler(messages)
        args.sortie.parent.mkdir(parents=True, exist_ok=True)
        args.sortie.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding='utf-8')
        print(rapport['texte'])
        print('\nRaison d’arrêt :', rapport['raison_arret'])
        print('Réponse enregistrée dans', args.sortie)
    except (OSError, ValueError, KeyError, IndexError, TypeError, urllib.error.URLError) as erreur:
        raise SystemExit(f'Appel impossible : {erreur}. Vérifiez le serveur, le port et le fichier de questions.')

if __name__ == '__main__':
    main()
