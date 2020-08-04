#!/usr/bin/env python3

from copy import deepcopy
from datetime import datetime

def sort_by_dates(list_accounts):
    list_accounts = deepcopy(list_accounts)
    sorted_list = []
    # On ajoute 2 ans à l'année actuelle
    date_max = int(str(datetime.now().year + 2) + "0101")

    while len(list_accounts) > 0:
        date_min = date_max
        for d, m, a in list_accounts:
            date = d.split("/")[::-1]
            date = int("".join(date))
            if date < date_min:
                date_min = date
                line_date_min = [d, m, a]
                
        sorted_list.append(line_date_min)
        list_accounts.remove(line_date_min)

    return sorted_list
