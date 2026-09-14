"""Assembler une partie ZdS depuis les Markdown déclarés dans son manifeste.
Usage : python assembler.py ../partie-3
Dépendance : Markdown (python -m pip install Markdown==3.10.3).
"""
import argparse
import base64
import html
import json
from pathlib import Path
import re
import zipfile
import markdown

p=argparse.ArgumentParser();p.add_argument('dossier',type=Path);a=p.parse_args();R=a.dossier.resolve()
M=json.loads((R/'manifest.json').read_text(encoding='utf-8'));files=[]
def read(path):
 cible=(R/path).resolve()
 if not cible.is_relative_to(R):raise ValueError('Chemin hors de la partie')
 files.append(path);return cible.read_text(encoding='utf-8')
intro=read(M['introduction']);fin=read(M['conclusion']);chapters=[];raw='# '+M['title']+'\n\n'+intro;outline='# '+M['title']+'\n\n'
for i,c in enumerate(M['children'],1):
 ci=read(c['introduction']);cc=read(c['conclusion']);secs=[];outline+=f'## {i}. '+c['title']+'\n\n';raw+='\n## '+c['title']+'\n\n'+ci
 for s in c['children']:
  body=read(s['text']);secs.append((s['title'],body));raw+='\n### '+s['title']+'\n\n'+body;outline+='- '+s['title']+'\n'
 raw+='\n'+cc;outline+='\n';chapters.append((c['title'],ci,secs,cc))
raw+='\n## Conclusion\n\n'+fin
refs=re.findall(r'!\[[^\]]*\]\(image:([^\)]+)\)',raw)
for ref in refs:
 assert (R/ref).is_file(),ref
 assert (R/ref).resolve().is_relative_to(R)
notes=re.findall(r'^\[\^([^\]]+)\]:',raw,re.M);calls=re.findall(r'\[\^([^\]]+)\](?!:)',raw)
assert len(notes)==len(set(notes)), 'Identifiant de note dupliqué'
assert set(notes)==set(calls), (set(notes)-set(calls),set(calls)-set(notes))
assert not re.search(r'\{src:|TODO|À RÉDIGER',raw)
assert raw.count('```')%2==0
assets={ref:'data:image/png;base64,'+base64.b64encode((R/ref).read_bytes()).decode() for ref in refs}
# Render each source independently; footnote identifiers are unique across the part.
def render(s):
 out=[];fence=False
 for line in s.splitlines():
  if line.startswith('```'):fence=not fence
  if not fence and re.match(r'^(Figure|Table|Code): ',line):out.append('\n<div class="caption">'+markdown.markdown(line.split(': ',1)[1])+'</div>\n')
  else:out.append(line)
 s='\n'.join(out)
 for ref,data in assets.items():s=s.replace('image:'+ref,data)
 return markdown.markdown(s,extensions=['tables','fenced_code','footnotes'])
nav='<nav aria-label="Sommaire"><p>Les chapitres</p><ol>'+''.join(f'<li><a href="#chapitre-{i}">{html.escape(c[0])}</a></li>' for i,c in enumerate(chapters,1))+'</ol></nav>'
body='<header><p class="kicker">Comprendre l’IA • '+html.escape(R.name.replace('-',' '))+'</p><h1>'+html.escape(M['title'])+'</h1></header>'+render(intro)+nav
for i,(title,ci,secs,cc) in enumerate(chapters,1):
 body+=f'<section class="chapter" id="chapitre-{i}"><p class="kicker">Chapitre {i} / {len(chapters)}</p><h2>'+html.escape(title)+'</h2>'+render(ci)
 for title,s in secs:body+='<h3>'+html.escape(title)+'</h3>'+render(s)
 body+=render(cc)+'</section>'
body+='<section class="chapter"><h2>Conclusion</h2>'+render(fin)+'</section>'
css=(Path(__file__).parent/'lecture.css').read_text(encoding='utf-8')
css+='\npre code{background:transparent;padding:0;white-space:pre}pre{font-size:14px}sup{line-height:0}table{display:block;overflow-x:auto} @media print{nav{break-after:page}}'
ht='<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(M['title'])+'</title><style>'+css+'</style><main>'+body+'</main></html>'
ids=re.findall(r'\bid="([^"]+)"',ht);assert len(ids)==len(set(ids)), 'Identifiant HTML dupliqué'
for target in re.findall(r'href="#([^"]+)"',ht):assert target in ids,target
assert 'image:images/' not in ht
(R/'relecture.html').write_text(ht,encoding='utf-8');(R/'relecture.md').write_text(raw.replace('image:images/','images/'),encoding='utf-8');(R/'sommaire.md').write_text(outline,encoding='utf-8')
name='annexes-modele-local-v1.zip' if R.name=='partie-3' else 'annexes-developpement-v1.zip'
folder='atelier-local' if R.name=='partie-3' else 'atelier-developpement'
with zipfile.ZipFile(R/name,'w',zipfile.ZIP_DEFLATED) as z:
 for path in sorted((R/'atelier').rglob('*')):
  rel=path.relative_to(R/'atelier')
  if path.is_file() and not {'__pycache__','modeles','moteur','resultats'}.intersection(rel.parts) and path.suffix not in {'.pyc','.part'}:
   z.write(path,folder+'/'+rel.as_posix())
 # Observed results live in a separate folder, not in the learner's output folder.
 if (R/'atelier/resultats').is_dir():
  for path in sorted((R/'atelier/resultats').rglob('*')):
   if path.is_file():z.write(path,'resultats-reference/'+path.relative_to(R/'atelier/resultats').as_posix())
 for path in sorted((R/'verification').rglob('*')):
  if path.is_file():z.write(path,'verification/'+path.relative_to(R/'verification').as_posix())
report={'chapitres':len(chapters),'sections':sum(len(c[2]) for c in chapters),'illustrations':len(refs),'notes':len(notes),'mots_avec_code':len(raw.split())}
(R/'verification').mkdir(exist_ok=True)
(R/'verification/structure.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
archive=R.parent/(R.name+'-zds-v1.zip')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for path in sorted(R.rglob('*')):
  rel=path.relative_to(R)
  if path.is_file() and 'atelier' not in rel.parts and '__pycache__' not in rel.parts:z.write(path,rel.as_posix())
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 for path in files+refs:assert path in z.namelist(),path
 assert 'manifest.json' in z.namelist()
print(json.dumps({**report,'archive_octets':archive.stat().st_size},ensure_ascii=False))
