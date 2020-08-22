#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from what import whatfile
from table import Table
import files

def refresh(verbose=0):
    with open("../config/accounts_path.txt", "r", encoding="utf-8") as _file:
        accounts_path = _file.readline().strip("\n") + "/"

    actfile = whatfile()
    filecontent = files.reader(accounts_path + actfile)

    table = Table(filecontent)
    table.update()

    files.writer(accounts_path + actfile, table.all)
    if verbose:
        print(actfile, "mis à jour.")


if __name__ == "__main__":
    refresh(verbose=1)
