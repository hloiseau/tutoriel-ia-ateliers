# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Décompresser les exports fournis, sans exécuter leur contenu."""
import hashlib
import json
import shutil
import stat
import zipfile
from pathlib import Path

root = Path("imports/deplie")
if root.exists():
    raise SystemExit("Le dossier de décompression existe déjà.")
records = []

def extract(source, target, depth=0):
    target.mkdir(parents=True, exist_ok=False)
    with zipfile.ZipFile(source) as archive:
        infos = archive.infolist()
        if sum(i.file_size for i in infos) > 512 * 1024 * 1024:
            raise ValueError("Archive décompressée trop volumineuse.")
        for info in infos:
            rel = Path(info.filename)
            if rel.is_absolute() or ".." in rel.parts or "\\" in info.filename:
                raise ValueError("Chemin inattendu dans l’archive.")
            if stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError("Lien symbolique dans l’archive.")
            out = target / rel
            if info.is_dir():
                out.mkdir(parents=True, exist_ok=True)
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as inp, out.open("xb") as dest:
                shutil.copyfileobj(inp, dest)
            records.append({"archive": str(source), "path": str(out),
                            "bytes": out.stat().st_size,
                            "sha256": hashlib.sha256(out.read_bytes()).hexdigest()})
    if depth < 2:
        for nested in sorted(target.rglob("*.zip")):
            extract(nested, nested.parent / ("_contenu-" + nested.stem), depth + 1)

for filename, name in [
    ("histoire-ia-zds-v3.zip", "histoire"),
    ("apprentissage-ia-zds-v2.zip", "apprentissage"),
    ("tutoriel-ia-suite-parties-3-4.zip", "suite"),
]:
    extract(Path("imports") / filename, root / name)
(root / "inventaire.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(records)} fichiers récupérés.")
for path in sorted(root.rglob("manifest.json")):
    print(path)
