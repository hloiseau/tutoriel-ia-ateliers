# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Rejouer le chapitre de construction depuis ses blocs de code et une archive extraite.

À lancer avec le Python de l’environnement MCP. Aucun modèle n’est appelé.
"""
import ast
import hashlib
import json
from pathlib import Path
import platform
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PART = ROOT / 'tutoriel/06-mcp-skills/03-construire'
ARCHIVE = ROOT / 'telechargements/atelier-mcp-skills.zip'
OUT = ROOT / 'docs/verifications-construction-mcp'


def blocs(nom, langage):
    return re.findall(r'^```' + langage + r'\n(.*?)^```',
                      (PART / nom).read_text(encoding='utf-8'), re.M | re.S)


def remplacer(texte, avant, apres):
    assert texte.count(avant) == 1, f'Point de remplacement ambigu : {avant[:70]}'
    return texte.replace(avant, apres)


def main():
    records = []
    traces = {}
    with tempfile.TemporaryDirectory(prefix='construction-mcp-') as dossier:
        work = Path(dossier)
        with zipfile.ZipFile(ARCHIVE) as z:
            assert z.testzip() is None
            z.extractall(work)
        def empreintes():
            return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (work/'donnees').iterdir()}
        avant = empreintes()

        def lancer(arguments, nom, code=0, cwd=None):
            p = subprocess.run([sys.executable, *arguments], cwd=cwd or work,
                               text=True, capture_output=True, timeout=30)
            traces[nom + '.txt'] = p.stdout + p.stderr
            records.append({'essai': nom, 'commande': ['python', *arguments],
                            'code_sortie': p.returncode, 'code_attendu': code})
            assert p.returncode == code, (nom, p.stdout, p.stderr)
            return p

        def commandes(section):
            for block in blocs(section, 'bash'):
                for ligne in block.splitlines():
                    if not ligne.startswith('python client.py '):
                        continue
                    arguments = shlex.split(ligne)[1:]
                    nom = Path(arguments[arguments.index('--journal') + 1]).stem
                    p = lancer(arguments, nom)
                    data = json.loads(p.stdout)
                    assert data['serveur'] == 'mon_serveur.py'
                    error = data['reponse'].get('isError', False)
                    assert error == (nom in {'c01-absent', 'c04-invalide'}), nom
                    traces[nom + '.json'] = (work/arguments[-1]).read_text()

        def sauver(texte, checkpoint):
            (work/'mon_serveur.py').write_text(texte)
            # Éliminer un cache d’import après les mutations rapides des tests.
            shutil.rmtree(work/'__pycache__', ignore_errors=True)
            attendu = (work/checkpoint).read_text()
            assert ast.dump(ast.parse(texte)) == ast.dump(ast.parse(attendu)), checkpoint

        source = blocs('demarrer.md', 'python')[0]
        fin = '\n\nif __name__ == "__main__":\n    mcp.run(transport="stdio")\n'
        sauver(source, 'construction/00-demarrage.py')
        commandes('demarrer.md')
        assert json.loads(traces['c00-inventaire.json'])['reponse']['tools'] == []

        imports, outil = [b.strip() for b in blocs('fonction.md', 'python')]
        source = remplacer(source, 'from mcp.server import MCPServer',
                           'from mcp.server import MCPServer\n' + imports)
        source = remplacer(source, fin, '\n\n' + outil + fin)
        sauver(source, 'construction/01-premier-outil.py')
        commandes('fonction.md')
        ticket = json.loads(traces['c01-ticket.json'])['reponse']['structuredContent']
        assert set(ticket) == {'id', 'titre'} and ticket['id'] == 'PRIX-1'
        # Le changement demandé dans le texte doit atteindre la réponse réelle.
        titre = 'Ne plus notifier une simple remise en stock'
        (work/'mon_serveur.py').write_text(source.replace(titre, 'Mon premier outil MCP'))
        p = lancer(['client.py', 'ticket', 'PRIX-1', '--serveur', 'mon_serveur.py',
                    '--journal', 'sorties/titre-change.json'], 'titre-change')
        assert json.loads(p.stdout)['reponse']['structuredContent']['titre'] == 'Mon premier outil MCP'
        (work/'mon_serveur.py').write_text(source)

        imports, catalogue, ticket = [b.strip() for b in blocs('catalogue.md', 'python')]
        source = remplacer(source, 'from mcp.server import MCPServer',
                           imports + '\nfrom mcp.server import MCPServer')
        source = remplacer(source, outil, catalogue + '\n\n' + ticket)
        sauver(source, 'construction/02-catalogue.py')
        commandes('catalogue.md')
        assert len(json.loads(traces['c02-ticket.json'])['reponse']['structuredContent']['questions_ouvertes']) == 2

        documents = blocs('chercher.md', 'python')[0].strip()
        source = remplacer(source, fin, '\n\n' + documents + fin)
        sauver(source, 'construction/03-documents.py')
        commandes('chercher.md')
        assert len(json.loads(traces['c03-recherche.json'])['reponse']['structuredContent']['resultats']) == 2
        p = lancer(['client.py', 'chercher', 'alerte', '--serveur', 'mon_serveur.py',
                    '--journal', 'sorties/synonyme.json'], 'synonyme-absent')
        assert json.loads(p.stdout)['reponse']['structuredContent']['resultats'] == []

        imports, contraintes, signatures = [b.strip() for b in blocs('valider.md', 'python')]
        source = remplacer(source, 'from typing import Any', imports)
        source = remplacer(source, 'ROOT = ', contraintes + '\n\nROOT = ')
        anciens = ['def lire_ticket(identifiant: str) -> dict[str, Any]:',
                   'def chercher_documentation(terme: str) -> dict[str, Any]:',
                   'def lire_document(identifiant: str) -> dict[str, Any]:']
        for ancien, nouveau in zip(anciens, signatures.splitlines()):
            source = remplacer(source, ancien, nouveau)
        assert source.count('@mcp.tool()') == 3
        source = source.replace('@mcp.tool()', '@mcp.tool(annotations=LECTURE)')
        sauver(source, 'construction/04-validation.py')
        commandes('valider.md')
        inventaire = json.loads(traces['c04-inventaire.json'])['reponse']['tools']
        assert len(inventaire) == 3
        assert all(t['annotations']['readOnlyHint'] for t in inventaire)
        schemas = {t['name']: t['inputSchema']['properties'] for t in inventaire}
        assert schemas['chercher_documentation']['terme']['maxLength'] == 80
        assert schemas['lire_ticket']['identifiant']['pattern'] == '^PRIX-[0-9]+$'

        resource = blocs('ressource.md', 'python')[0].strip()
        source = remplacer(source, fin, '\n\n' + resource + fin)
        sauver(source, 'serveur.py')
        commandes('ressource.md')
        assert 'centimes' in json.loads(traces['c05-conventions.json'])['reponse']['contents'][0]['text']

        tests = blocs('tester.md', 'python')[0]
        assert ast.dump(ast.parse(tests)) == ast.dump(ast.parse((work/'construction/test_mon_serveur.py').read_text()))
        (work/'test_mon_serveur.py').write_text(tests)
        lancer(['-m', 'unittest', 'test_mon_serveur', '-v'], 'trois-tests')
        mutant = source.replace('@mcp.tool(annotations=LECTURE)', '# Outil volontairement retiré', 1)
        (work/'mon_serveur.py').write_text(mutant)
        shutil.rmtree(work/'__pycache__', ignore_errors=True)
        p = lancer(['-m', 'unittest', 'test_mon_serveur', '-v'], 'mutation-sans-decorateur', code=1)
        assert 'FAILED (failures=1)' in p.stderr
        (work/'mon_serveur.py').write_text(source)
        shutil.rmtree(work/'__pycache__', ignore_errors=True)
        lancer(['-m', 'unittest', 'test_mon_serveur', '-v'], 'trois-tests-restaures')
        mutant = source.replace('def lire_document(identifiant: IdentifiantDocument)',
                                'def lire_document(identifiant: str)')
        (work/'mon_serveur.py').write_text(mutant)
        shutil.rmtree(work/'__pycache__', ignore_errors=True)
        p = lancer(['-m', 'unittest', 'test_mon_serveur', '-v'],
                   'mutation-sans-validation', code=1)
        assert 'FAILED (failures=1)' in p.stderr
        (work/'mon_serveur.py').write_text(source)
        shutil.rmtree(work/'__pycache__', ignore_errors=True)
        lancer(['-m', 'unittest', 'test_mon_serveur', '-v'], 'trois-tests-finaux')
        lancer(['-m', 'unittest', 'test_serveur', '-v'], 'dix-tests-corrige')

        # Adverse : confusion de cible, journal déjà présent, absence de fichier.
        p = lancer(['client.py', 'inventaire', '--journal', 'sorties/corrige.json'], 'cible-par-defaut')
        assert json.loads(p.stdout)['serveur'] == 'serveur.py'
        lancer(['client.py', 'inventaire', '--serveur', 'absent.py', '--journal', 'sorties/absent.json'],
               'serveur-absent', code=2)
        lancer(['client.py', 'inventaire', '--serveur', 'mon_serveur.py', '--journal', 'sorties/c00-inventaire.json'],
               'journal-existant', code=2)
        p = lancer(['configuration.py', '--serveur', 'mon_serveur.py'], 'configuration')
        config = json.loads(p.stdout)['servers']['atelier-tickets']
        assert config['command'] == sys.executable
        assert Path(config['args'][0]) == work/'mon_serveur.py'
        # Ne pas publier les chemins temporaires de la configuration de cette machine.
        traces['configuration.txt'] = 'JSON valide ; interpréteur et mon_serveur.py vérifiés.\n'

        for valeur in ('document-absent', '../tickets'):
            p = lancer(['client.py', 'document', valeur, '--serveur', 'mon_serveur.py',
                        '--journal', 'sorties/adverse-' + str(len(records)) + '.json'],
                       'document-' + str(len(records)))
            assert json.loads(p.stdout)['reponse']['isError']
        p = lancer(['client.py', 'chercher', '   ', '--serveur', 'mon_serveur.py',
                    '--journal', 'sorties/espaces.json'], 'espaces')
        assert json.loads(p.stdout)['reponse']['isError']
        assert empreintes() == avant

    OUT.mkdir(exist_ok=True)
    for nom, contenu in traces.items():
        (OUT/nom).write_text(contenu, encoding='utf-8')
    rapport = {'python': platform.python_version(), 'plateforme': platform.system(),
               'archive_sha256': hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
               'etats_reconstruits_depuis_markdown': 6, 'commandes': records,
               'donnees_inchangees': True, 'modele_appele': False,
               'interface_assistant_verifiee': False}
    (OUT/'executions.json').write_text(json.dumps(rapport, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'etats': 6, 'commandes': len(records), 'resultat': 'conforme',
                      'rapport': str(OUT.relative_to(ROOT))}, ensure_ascii=False))


if __name__ == '__main__':
    main()
