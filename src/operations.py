#!/usr/bin/env python3
#_*_ coding: utf-8 -*-

from what import whatis, whatdate, whatmode
from copy import copy

def operror(op):
    print(f"Il est impossible d'utiliser la fonction '{op}' de cette manière. 'accountshelper/doc.txt' pour plus d'informations.")


def add(line, list_accounts, previous_settings):
    """
    Ajoute une nouvelle ligne dans le fichier se trouvent les comptes et renvoie
    True si l'opération a réussie, sinon False.
    """
    list_accounts = list_accounts.copy()
    line_isvalid = True
    settings = {"amount": None, "mode": None, "date": None}
    if len(line) <= 3:
        for i in range(len(line)):
            settings[whatis(line[i])] = line[i]
    else:
        line_isvalid = False
        print("Vous avez entrez des informations non attendues.")


    # Vérification de la date
    if line_isvalid and settings["date"]:
        date = settings["date"].split("/")
        while "" in date:
            date.remove("")

        for e in date:
            if not e.isdigit():
                print("La date n'est pas écrite correctement")
                line_isvalid = False
                break
        if line_isvalid:
            settings["date"] = whatdate(settings["date"])

    # Autocomplétion de la saisie si nécéssaire
    if len(line) < 3 and len(previous_settings) == 3:
        for k, v in settings.items():
            if not v:
                settings[k] = previous_settings[k]
    elif len(line) < 3 and len(previous_settings) < 3:
        print("Vous devez entrez plus d'information pour cette ligne.")
        line_isvalid = False

    if line_isvalid:
        for v in settings.values():
            if not v:
                print("Un type d'information a été entré plusieurs fois au lieu d'un autre.")
                line_isvalid = False
                break


    # DÃ©tection du mode de paiement
    if line_isvalid:
        mode = whatmode(settings["mode"])
        if mode != "UNKNOW":
            settings["mode"] = mode
        else:
            print("Le mode de paiement n'est pas reconnu.")
            line_isvalid = False


    if line_isvalid:
        settings["amount"] = "{:.2f}".format(float(settings["amount"]))
        previous_settings = copy(settings)
        list_accounts.append([settings["date"], settings["mode"], settings["amount"]])
        print("\nDate: {}  Mode de paiement: {}  Montant: {} €\n".format(settings["date"], settings["mode"], settings["amount"]))
        return True, list_accounts, previous_settings
    else:
        return False, list_accounts, previous_settings




def retour(step, list_accounts, previous_settings):
    if len(list_accounts) < 1:
        print("Vous ne pouvez pas revenir en arriÃ¨re.")
        return False, list_accounts, previous_settings

    len_list_accounts = len(list_accounts)
    if len_list_accounts - step < 0:
        if len_list_accounts > 1:
            print("Vous ne pouvez pas revenir plus de {} lignes en arrière.".format(len_list_accounts))
        else:
            print("Vous ne pouvez pas revenir plus de 1 ligne en arrière.")
        return False, list_accounts, previous_settings
    else:
        del list_accounts[len_list_accounts - step:]
        if len(list_accounts) > 0:
            previous_settings = {"amount": list_accounts[-1][2], "mode": list_accounts[-1][1], "date": list_accounts[-1][0]}
            print()
        else:
            previous_settings = {}
            print()
        return True, list_accounts, previous_settings




def view(index, list_accounts):
    if 0 <= index < len(list_accounts):
        line = "|  Ligne {} :  {}   {}   {} €  |".format(index + 1, list_accounts[index][0], list_accounts[index][1], list_accounts[index][2])
        print(" ", end="")
        print("=" * (len(line) - 2))
        print(line + "\n", end=" ")
        print("=" * (len(line) - 2))
    elif index < 0:
        print("Ce numéro de ligne n'existe pas.")




def modify(list_accounts, index):
    previous_settings = {
        "date": list_accounts[index][0],
        "mode": list_accounts[index][1],
        "amount": list_accounts[index][2]
    }

    op_sucess = False
    while not op_sucess:
        # Ici, on veut juste récupérer les infos
        print("Ligne", index + 1, ":", end=" ")
        line = input().split(" ")
        if line == [""]:
            if len(previous_settings) > 0:
                line = [previous_settings["date"]]
            else:
                line = ["_"]

        if not line[0] in ["fmod", "fmodifier"]:
            op_sucess, _, settings = add(line, list_accounts, previous_settings)
        else:
            break


    if op_sucess:
        list_accounts[index] = [
            settings["date"],
            settings["mode"],
            settings["amount"]
        ]

    return list_accounts
