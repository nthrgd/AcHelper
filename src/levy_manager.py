import files
from date import Date
from what import whatfile
from sort import sort_by_dates
from refresh import refresh


with open("../config/ACCOUNTS_PATH.txt", "r", encoding="utf-8") as _file:
    accounts_path = _file.readline().strip("\n")
levysfile = accounts_path + "/NE PAS SUPPRIMER/Prélèvements.txt"

actfile = accounts_path + "/" + whatfile()

levys = files.reader(levysfile, delimiter=":")
levys_modes = []
# levys.autoremove()

for i in range(len(levys)):
    for j in range(3):
        levys[i][j] = levys[i][j].replace(" ", "")

    # On met les lignes au format utilisé par AcHelper
    levys[i][0], levys[i][1], levys[i][2] = Date(levys[i][0] + "/").whatdate(), levys[i][1].upper(), "{:.2f}".format(float(levys[i][2]))

    # Ajout du mode après la suppression des espaces
    levys_modes.append(levys[i][1])


list_accounts = files.reader(actfile)
# Insertion des prélèvements automatiques dans le tableau
for i in range(len(levys)):
    list_accounts.insert(3 + i, levys[i])

files.writer(actfile, list_accounts)
refresh(modes=levys_modes)