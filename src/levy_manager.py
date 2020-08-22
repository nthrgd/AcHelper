#!/usr/bin/env python3

import files
from date import Date
from what import whatfile
from refresh import refresh
from table import Table


with open("../config/accounts_path.txt", "r", encoding="utf-8") as _file:
    accounts_path = _file.readline().strip("\n")
leviesfile = accounts_path + "/NE PAS SUPPRIMER/Prélèvements.txt"

actfile = accounts_path + "/" + whatfile()

levies = files.reader(leviesfile, delimiter=":")

print()
index_to_sup = []
for i in range(len(levies)):
    for j in range(3):
        error = False
        try:
            levies[i][j] = levies[i][j].replace(" ", "")
        except IndexError:
            error = True
            index_to_sup.append(i)
            print(f"INFO: La ligne {i + 1} de 'Prélèvements.txt' contient",
                   "moins de 3 informations nécéssaires et est donc ignorée.")

    if not error:
        # On met les lignes au format utilisé par AcHelper
        levies[i][0] = Date(levies[i][0] + "/").whatdate()
        if not levies[i][0]:
            error = True
            index_to_sup.append(i)
            print(f"INFO: Le premier élément de la ligne {i + 1} de",
                   "'Prélèvements.txt' ne correspond pas à un jour",
                   "du mois actuel, cette ligne est donc ignorée.")

        if not error:
            levies[i][1] = levies[i][1].upper()
            error = True
            try:
                float(levies[i][1])
                index_to_sup.append(i)
                print(f"INFO: Le deuxième élément de la ligne {i + 1} de",
                       "'Prélèvements.txt' ne correspond pas à un 'Auteur'",
                       "(il faut minimum une lettre).\n",
                       "     Cette ligne est donc ignorée.")
            except:
                error = False

        if not error:
            try:
                levies[i][2] = "{:.2f}".format(float(levies[i][2]))
            except ValueError:
                index_to_sup.append(i)
                print(f"INFO: Le troisième élément de la ligne {i + 1} de",
                       "'Prélèvements.txt' ne correspond pas à un montant,",
                       "cette ligne est donc ignorée.")

# Delete invalid lines
n = 0
for i in index_to_sup:
    del levies[i - n]
    n += 1

if n:
    print()

list_accounts = files.reader(actfile)
# Insertion des prélèvements automatiques dans le tableau
for i in range(len(levies)):
    list_accounts.insert(3 + i, levies[i])

files.writer(actfile, list_accounts)
refresh()
