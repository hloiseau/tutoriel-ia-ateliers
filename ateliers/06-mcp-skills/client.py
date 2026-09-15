# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Client MCP réel, sans modèle : lancer le serveur local et examiner une réponse."""
import argparse
import asyncio
import json
import sys
from pathlib import Path
from mcp import Client
from mcp.client.stdio import StdioServerParameters

ROOT = Path(__file__).resolve().parent


async def consulter(operation, valeur=None, serveur=ROOT/'serveur.py'):
    params = StdioServerParameters(command=sys.executable, args=[str(serveur.resolve())], cwd=ROOT)
    async with Client(params, read_timeout_seconds=10) as client:
        if operation == 'inventaire':
            result = await client.list_tools()
        elif operation == 'conventions':
            result = await client.read_resource('atelier://conventions')
        else:
            noms = {'ticket':'lire_ticket', 'chercher':'chercher_documentation',
                    'document':'lire_document', 'refus':'modifier_ticket'}
            arguments = {'terme':valeur} if operation=='chercher' else {'identifiant':valeur}
            if operation=='refus':
                arguments={'identifiant':'PRIX-1', 'statut':'termine'}
            result = await client.call_tool(noms[operation], arguments)
        return {'operation':operation, 'valeur':valeur, 'serveur':serveur.name,
                'protocole':client.protocol_version,
                'reponse':result.model_dump(mode='json', by_alias=True, exclude_none=True)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['inventaire','ticket','chercher','document','conventions','refus'])
    parser.add_argument('valeur', nargs='?')
    parser.add_argument('--journal', required=True, type=Path)
    parser.add_argument('--serveur', type=Path, default=ROOT/'serveur.py',
                        help='Fichier Python à lancer (par défaut : le corrigé serveur.py).')
    args=parser.parse_args()
    if args.operation in {'ticket','chercher','document'} and args.valeur is None:
        parser.error('Cette opération demande une valeur.')
    if args.journal.exists():
        parser.error('Le journal existe déjà ; choisissez un autre nom.')
    if not args.serveur.is_file():
        parser.error('Le fichier serveur est introuvable.')
    resultat=asyncio.run(consulter(args.operation,args.valeur,args.serveur))
    texte=json.dumps(resultat,ensure_ascii=False,indent=2)
    args.journal.parent.mkdir(parents=True,exist_ok=True)
    with args.journal.open('x',encoding='utf-8') as f:f.write(texte+'\n')
    print(texte)


if __name__ == '__main__':
    main()
