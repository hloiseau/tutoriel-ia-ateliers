# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Etat:
    prix_centimes: int
    disponible: bool

    def __post_init__(self):
        if type(self.prix_centimes) is not int or self.prix_centimes < 0:
            raise ValueError("Le prix doit être un entier positif ou nul, en centimes.")
        if type(self.disponible) is not bool:
            raise ValueError("La disponibilité doit être un booléen.")


def notifier(ancien: Etat, nouveau: Etat) -> bool:
    return nouveau.disponible and (
        nouveau.prix_centimes < ancien.prix_centimes
    )


def lire_etat(document):
    if not isinstance(document, dict) or set(document) != {"prix_centimes", "disponible"}:
        raise ValueError("Un état doit contenir exactement prix_centimes et disponible.")
    return Etat(**document)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scenario", type=Path)
    args = parser.parse_args()
    try:
        document = json.loads(args.scenario.read_text(encoding="utf-8"))
        ancien = lire_etat(document["ancien"])
        nouveau = lire_etat(document["nouveau"])
        print(json.dumps({"notifier": notifier(ancien, nouveau)}))
    except (OSError, ValueError, KeyError, TypeError) as erreur:
        raise SystemExit(f"Scénario invalide : {erreur}")


if __name__ == "__main__":
    main()
