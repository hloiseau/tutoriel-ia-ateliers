# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Assembler une copie de la partie 4 avec ses trois nouveaux chapitres."""

import argparse
import json
import shutil
import zipfile
from pathlib import Path


def contenu(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError(f"Fichier absent ou chemin hors du dossier : {relative}")
    return path


def verifier_manifest(root, node):
    for key in ("introduction", "conclusion", "text"):
        if node.get(key):
            contenu(root, node[key])
    for child in node.get("children", []):
        verifier_manifest(root, child)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--partie4", type=Path, required=True)
    parser.add_argument("--sortie", type=Path, required=True)
    args = parser.parse_args()
    source = args.partie4.resolve()
    destination = args.sortie.resolve()
    archive = destination.with_name(destination.name + ".zip")
    revision = Path(__file__).resolve().parent

    if destination.exists() or archive.exists():
        parser.error("La sortie ou son ZIP existe déjà ; choisir un nouveau nom.")
    if destination.is_relative_to(source) or source.is_relative_to(destination):
        parser.error("La source et la sortie doivent être des dossiers séparés.")

    manifest = json.loads(contenu(source, "manifest.json").read_text(encoding="utf-8"))
    old = manifest.get("children", [])
    if manifest.get("object") != "container" or len(old) != 6:
        parser.error("La partie source doit contenir les six chapitres existants.")
    if any(child.get("object") != "container" for child in old):
        parser.error("Structure inattendue : un enfant n’est pas un chapitre.")
    verifier_manifest(source, manifest)

    candidates = [
        child for child in old[0].get("children", [])
        if child.get("object") == "extract"
        and child.get("text", "").endswith("/installer.md")
    ]
    if len(candidates) != 1:
        parser.error("L’extrait d’installation du premier chapitre est introuvable.")

    added = json.loads(
        contenu(revision, "chapitres-a-inserer.json").read_text(encoding="utf-8")
    )
    for chapter in added:
        verifier_manifest(revision, chapter)
        if (source / chapter["slug"]).exists():
            parser.error("Un dossier de chapitre à ajouter existe déjà dans la source.")

    # Tous les contrôles de structure précèdent la création de la copie.
    shutil.copytree(source, destination)
    for chapter in added:
        shutil.copytree(revision / chapter["slug"], destination / chapter["slug"])
    intro = manifest.get("introduction")
    if not intro:
        intro = "introduction.md"
        manifest["introduction"] = intro
    shutil.copyfile(revision / "introduction.md", destination / intro)
    shutil.copyfile(revision / "raccord-01-projet.md", destination / candidates[0]["text"])
    candidates[0]["title"] = "Lancer les tests du projet"
    manifest["children"] = added + old
    manifest["ready_to_publish"] = False
    (destination / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    verifier_manifest(destination, manifest)

    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as output:
        for path in sorted(destination.rglob("*")):
            if path.is_file():
                output.write(path, path.relative_to(destination).as_posix())
    print(f"Copie préparée : {destination}")
    print(f"Archive à relire dans ZdS : {archive}")


if __name__ == "__main__":
    main()
