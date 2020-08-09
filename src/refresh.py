# -*- coding: utf-8 -*-

from what import whatfile
from calcul import *
from sort import *
import files

def refresh(verbose=0):
    with open("../config/ACCOUNTS_PATH.txt", "r", encoding="utf-8") as _file:
        accounts_path = _file.readline().strip("\n") + "\\"

    actfile = whatfile()
    filecontent = files.reader(accounts_path + actfile)

    dep = float(filecontent[0][1])
    filecontent[3:len(filecontent) - 2] = sort_by_dates(filecontent[3:len(filecontent) - 2])
    filecontent[-1][1] = "{:.2f}".format(calcul_total(dep, filecontent[3:len(filecontent) - 2]))
    files.writer(accounts_path + actfile, filecontent)

    if verbose:
        print(actfile, "mis à jour.")


if __name__ == "__main__":
    refresh(verbose=1)
