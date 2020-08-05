#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from what import whatfile
from calcul import *
from sort import *
import files

with open("ACCOUNTS_PATH.txt", "r", encoding="utf-8") as _file:
    accounts_path = _file.readline().strip("\n") + "\\"

actfile = whatfile()
filecontent = files.reader(accounts_path + actfile)

dep = float(filecontent[0][1])
filecontent[-1][1] = "{:.2f}".format(calcul_total(dep, filecontent[3:len(filecontent) - 2]))
filecontent[3:len(filecontent) - 2] = sort_by_dates(filecontent[3:len(filecontent) - 2])
files.writer(accounts_path + actfile, filecontent)

print(actfile, "mis à jour.")
