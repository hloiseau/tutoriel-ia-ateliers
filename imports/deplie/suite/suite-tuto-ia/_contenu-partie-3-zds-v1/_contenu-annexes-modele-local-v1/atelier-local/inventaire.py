import json
import os
import platform
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
rapport = {
    'systeme': platform.system(), 'version_systeme': platform.release(),
    'architecture': platform.machine(), 'python': sys.version.split()[0],
    'processeur_declare': platform.processor(), 'processeurs_logiques': os.cpu_count(),
    'espace_libre_octets': shutil.disk_usage(ROOT).free,
    'nvidia': None,
}
if shutil.which('nvidia-smi'):
    try:
        p = subprocess.run(['nvidia-smi', '--query-gpu=name,driver_version,memory.total',
                            '--format=csv,noheader'], capture_output=True, text=True, timeout=10)
        rapport['nvidia'] = p.stdout.strip() if p.returncode == 0 else 'Commande en échec'
    except (OSError, subprocess.TimeoutExpired):
        rapport['nvidia'] = 'Commande indisponible ou trop longue'
(ROOT / 'resultats').mkdir(exist_ok=True)
(ROOT / 'resultats' / 'machine.json').write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(rapport, ensure_ascii=False, indent=2))
