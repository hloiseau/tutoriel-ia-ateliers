# SPDX-FileCopyrightText: 2026 Hugo Loiseau
# SPDX-License-Identifier: GPL-3.0-only
"""Variante : baisse d’au moins 100 centimes et produit disponible."""
def doit_notifier(ancien_prix, nouveau_prix, disponible):
    return disponible and ancien_prix - nouveau_prix >= 100


def main():
    cas = [(2500, 2401, True, False), (2500, 2400, True, True),
           (2500, 2399, True, True), (2500, 2400, False, False),
           (2500, 2600, True, False)]
    erreurs = 0
    for ancien, nouveau, disponible, attendu in cas:
        obtenu = doit_notifier(ancien, nouveau, disponible)
        print(f"{ancien} → {nouveau}, disponible={disponible} : obtenu={obtenu}, attendu={attendu}")
        erreurs += obtenu != attendu
    print(f"{erreurs} désaccord(s) avec la règle.")
    raise SystemExit(1 if erreurs else 0)


if __name__ == '__main__':
    main()
