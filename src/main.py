#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from what import *
from operations import *
from calcul import *
from files import *
from sort import *

print("Entrez les montants, les dates et les modes de paiement dans l'ordre que vous voulez :\n")

with open("../config/accounts_path.txt", "r", encoding="utf-8") as _file:
    actfile = _file.readline().strip("\n") + "/" + whatfile()

list_accounts = reader(actfile) # lecture du fichier où se trouvent les comptes

# on ne garde que les lignes de 'comptes'
dep = float(list_accounts.pop(0)[1])
del list_accounts[:2]
del list_accounts[len(list_accounts)-2:]

n = len(list_accounts) + 1

if n > 1:
    previous_settings = {
        "amount": list_accounts[-1][2],
        "mode": list_accounts[-1][1],
        "date": list_accounts[-1][0]
     }
else:
    previous_settings = {}

print("Ligne", n, ":", end=" ")
line = input().split(" ")
if line == [""]:
    line = ["_"]

while line[0].lower() != "stop":
    while "" in line:
        line.remove("")
    op = whatop(line)

    if op == "add":
        op_sucess, list_accounts, previous_settings = add(line, list_accounts, previous_settings)
        if op_sucess:
            n += 1

    elif op == "retour":
        if len(line) == 2:
            if line[1].isdigit():
                step = int(line[1])
                op_sucess, list_accounts, previous_settings = retour(step, list_accounts, previous_settings)
                if op_sucess:
                    n -= step
        elif len(line) == 1:
            op_sucess, list_accounts, previous_settings = retour(1, list_accounts, previous_settings)
            if op_sucess:
                n -= 1
        else:
            operror("retour")

    elif op == "voir":
        if len(line) == 3:
            if line[1].isdigit() and line[2].isdigit():
                line[1], line[2] = int(line[1]), int(line[2])
                if line[2] >= line[1]:
                    print()
                    for i in range(line[1] - 1, line[2]):
                        view(i, list_accounts)
                    print()
        elif len(line) == 2:
            if line[1].isdigit():
                print()
                view(int(line[1]) - 1, list_accounts)
                print()
            else:
                print("Ce numéro de ligne n'existe pas.")
        elif len(line) == 1:
            print()
            for i in range(len(list_accounts)):
                view(i, list_accounts)
            print()
        else:
            operror("voir")

    elif op == "supprimer":
        if len(line) == 3:
            if line[1].isdigit() and line[2].isdigit():
                line[1], line[2] = int(line[1]), int(line[2])
                if line[1] <= line[2]:
                    len_list_accounts = len(list_accounts)
                    list_accounts = delete(list_accounts, line[1], line[2])

                    if line[2] > len_list_accounts:
                        line[2] -= line[2] - len_list_accounts

                    n -= line[2] - line[1] + 1

                
        elif len(line) == 2: 
            if line[1].isdigit():
                line[1] = int(line[1])
                list_accounts = delete(list_accounts, line[1], line[1])
                n -= 1

        elif len(line) == 1:
            print("Etes-vous sûr(e) de vouloir supprimer définitivement", 
                  "toutes les données de votre tableau ? [O/N]")
            if input().upper() in ["O", "OUI", "Y", "YES"]:
                list_accounts = delete(list_accounts, 1, len(list_accounts))
                n = 1
            else:
                print("Opération annulée.")
        else:
            operror("Supprimer")

        if n > 1:
            previous_settings = {
                "amount": list_accounts[-1][2],
                "mode": list_accounts[-1][1],
                "date": list_accounts[-1][0]
            }
        else:
            previous_settings = {}

    else:
        if len(line) == 2:
            if line[1].isdigit():
                if 0 <= int(line[1]) <= len(list_accounts):
                    list_accounts = modify(list_accounts, int(line[1]) - 1)
                else:
                    print("Ce numéro de ligne n'existe pas")
            else:
                print("La fonction 'modifier' reçoit uniquement des nombres " + \
                      "entiers en paramètre.")
        elif len(line) == 1:
            list_accounts = modify(list_accounts, n - 2)
        else:
            operror("modifier")

    print("Ligne", n, ":", end=" ")
    line = input().split(" ")
    if line == [""]:
        if len(previous_settings) > 0:
            line = [previous_settings["date"]]
        else:
            line = ["_"]


print("Traitement des changements en cours...")
list_accounts = sort_by_dates(list_accounts)
total = calcul_total(dep, list_accounts)

# réinsertion du montant de départ et du montant total
list_accounts.insert(len(list_accounts), ["", ""])
list_accounts.insert(len(list_accounts), ["Total", "{:.2f}".format(total)])
list_accounts[0:0] = [["Depart", "{:.2f}".format(dep)]]
list_accounts[1:1] = [["", ""]]
list_accounts[2:2] = [["Date", "Mode", "Montant"]]

writer(actfile, list_accounts)
print("Fait.")
