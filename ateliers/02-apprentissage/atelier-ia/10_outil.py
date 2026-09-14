# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

import json
import sys
from pathlib import Path

FICHES = {
    "validation": "La validation sert à comparer les réglages sans utiliser le jeu de test.",
    "test": "Le jeu de test sert au bilan final d'un modèle dont les réglages sont fixés.",
}


def executer(appel):
    if not isinstance(appel, dict) or set(appel) != {"outil", "arguments"}:
        raise ValueError("Il faut exactement outil et arguments.")
    if appel["outil"] != "lire_fiche":
        raise ValueError("Outil non autorisé.")
    arguments = appel["arguments"]
    if not isinstance(arguments, dict) or set(arguments) != {"nom"}:
        raise ValueError("L'outil attend uniquement un argument nom.")
    nom = arguments["nom"]
    if not isinstance(nom, str) or nom not in FICHES:
        raise ValueError("Fiche inconnue.")
    return {"outil": "lire_fiche", "resultat": FICHES[nom]}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage : python 10_outil.py appel.json")
    try:
        appel = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(json.dumps(executer(appel), ensure_ascii=False, indent=2))
    except (OSError, ValueError) as erreur:
        raise SystemExit(f"Appel refusé : {erreur}")
