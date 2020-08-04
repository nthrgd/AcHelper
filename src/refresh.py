#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from what import whatfile
from calcul import *
import files

actfile = whatfile()
filecontent = files.reader("../Accounts/" + actfile)
dep = float(filecontent[0][1])
filecontent[-1][1] = "{:.2f}".format(calcul_total(dep, filecontent[3:len(filecontent) - 2]))
files.writer("../Accounts/" + actfile, filecontent)
print(actfile, "mis à jour.")
