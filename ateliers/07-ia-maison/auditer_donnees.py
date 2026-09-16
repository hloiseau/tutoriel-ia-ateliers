# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Contrôler les lots de texte de notre petit modèle avant l’entraînement."""
import json
from pathlib import Path
import re
from recherche import ROOT


def auditer():
    rapport={}
    for corpus in ['base','adaptation']:
        lots={lot:(ROOT/f'donnees/langage/{corpus}-{lot}.txt').read_text().splitlines()
              for lot in ['train','validation','test']}
        groupes={lot:{int(re.search(r'(?:produit[ =]|ticket )([0-9]+)',s)[1]) for s in lignes}
                 for lot,lignes in lots.items()}
        for a,b in [('train','validation'),('train','test'),('validation','test')]:
            if set(lots[a])&set(lots[b]):raise ValueError('Lignes identiques entre deux lots.')
            if groupes[a]&groupes[b]:raise ValueError('Identifiants partagés entre deux lots.')
        rapport[corpus]={lot:{'lignes':len(v),'groupes':len(groupes[lot])} for lot,v in lots.items()}
    return rapport


if __name__=='__main__':print(json.dumps(auditer(),ensure_ascii=False,indent=2))
