import argparse
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import statistics
from client import appeler

p = argparse.ArgumentParser()
p.add_argument('--nom', required=True, help='Nom du dossier de résultats, sans chemin.')
p.add_argument('--fichier', type=Path, default=Path('questions/premiere.json'))
a = p.parse_args()
if not a.nom or not all(c.isalnum() or c in '-_' for c in a.nom):
    raise SystemExit('Choisissez un nom composé de lettres, chiffres, tirets ou underscores.')
cible = Path('resultats') / a.nom
if cible.exists():
    raise SystemExit('Ce dossier existe déjà : choisissez un nouveau nom pour conserver les mesures.')
messages = json.loads(a.fichier.read_text(encoding='utf-8'))
cible.mkdir(parents=True)
try:
    for i in range(4):
        r = appeler(messages)
        r.update({'date_utc': datetime.now(timezone.utc).isoformat(), 'echauffement': i == 0})
        (cible / f'appel-{i}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding='utf-8')
        print('Échauffement' if i == 0 else f'Essai {i}', f"{r['duree_s']:.3f} s", flush=True)
    mesures = [json.loads((cible / f'appel-{i}.json').read_text(encoding='utf-8')) for i in range(1,4)]
    colonnes = ['duree_s', 'tokens_sortie', 'tokens_sortie_par_seconde_globale', 'raison_arret']
    with (cible / 'mesures.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows({k:r[k] for k in colonnes} for r in mesures)
    print('Durée médiane :', round(statistics.median(r['duree_s'] for r in mesures),3), 's')
except Exception as erreur:
    raise SystemExit(f'Mesure interrompue : {erreur}. Les appels terminés restent dans {cible}.')
