# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Mesurer la présence d’une source pertinente, pas la qualité d’une réponse générée."""
import argparse
import json
from pathlib import Path
from recherche import ROOT, Index, charger, sauver


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--lot',choices=['validation','test'],default='validation')
    p.add_argument('--sortie',type=Path,required=True)
    a=p.parse_args()
    questions=json.loads((ROOT/f'donnees/questions-{a.lot}.json').read_text())
    index=Index(charger()); details=[]
    for q in questions:
        trouves=index.chercher(q['question'])
        ids=[p['id'] for p in trouves]
        attendu=set(q['sources'])
        details.append({'id':q['id'],'question':q['question'],'attendus':q['sources'],
                        'trouves':ids,'source_pertinente_presente':bool(attendu.intersection(ids)) if attendu else None,
                        'aucun_passage':not ids})
    connues=[d for d in details if d['attendus']]
    absentes=[d for d in details if not d['attendus']]
    rapport={'lot':a.lot,'k':3,'seuil':0.12,'questions_avec_source':len(connues),
             'avec_au_moins_une_source_pertinente':sum(d['source_pertinente_presente'] for d in connues),
             'questions_sans_source':len(absentes),'sans_passage_sur_questions_sans_source':sum(d['aucun_passage'] for d in absentes),
             'details':details}
    sauver(a.sortie,rapport);print(json.dumps(rapport,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
