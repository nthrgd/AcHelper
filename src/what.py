#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def whatfile():
    with open("actfile.txt", "r", encoding="utf-8") as file:
        return file.readline().strip("\n")

def whatis(seizure):
    """
    Détermine si une entrée est un montant, une date ou un mode de paiement.
    """
    seizure = seizure.replace(" ", "") # pour reconnaître le montant si il contient un espace
    try:
        seizure = float(seizure)
        return "amount"
    except ValueError:
        try:
            seizure.index("/")
            return "date"
        except ValueError:
            return "mode"

def whatop(seizure):
    """ Détermine quelle opération est attendue après la saisie. """
    op = seizure[0].lower()
    if op in ["retour", "r"]:
        return "retour"
    elif op in ["modifier", "modif", "mod"]:
        return "modifier"
    elif op in ["voir", "v"]:
        return "voir"
    else:
        return "add"




def whatdate(date):
    from datetime import datetime
    today = datetime.now()
    date = date.split("/")
    while "" in date:
        date.remove("")

    # Autocomplétion
    if not date:
        date = [str(today.day), str(today.month), str(today.year)]
    if len(date) < 2:
        date.append(str(today.month))
    if len(date) < 3:
        date.append(str(today.year))

    # Formattage
    for i in range(2):
        if len(date[i]) < 2:
            date[i] = "0" + date[i]
    if len(date[2]) < 4:
        date[2] = str(today.year)[: 4 - len(date[2]) ] + date[2]

    return "/".join(date)



modes = ["CB", "CHEQUE", "VIREMENT", "RETRAIT"]
def whatmode(mode):
    mode = mode.upper()
    list_modes = [modes, ["CB", "CHEQU", "VIRM", "RET"]]
    if mode in list_modes[0] or mode in list_modes[1]:
        return mode

    # détermination du mode que l'utilisateur a voulu spécifier
    # test à part pour 'CB'
    if len(mode) == 2:
        if "C" in mode or "B" in mode:
            return "CB"

    most_matched_modes = [-1, -1]
    for i in range(2):
        max_matches = 0
        for j in range(4):
            matches = 0
            for l in mode:
                if l in list_modes[i][j]:
                    matches += 1
            if matches > max_matches:
                most_matched_modes[i], max_matches = j, matches
            elif matches == max_matches: # si il y a une hأ©sitation entre deux modes
                most_matched_modes[i] = -1

    if most_matched_modes[0] == most_matched_modes[1]:
        if most_matched_modes[0] != -1:
            return list_modes[0][most_matched_modes[0]]
        else:
            return "UNKNOW"
    else:
        if most_matched_modes[0] != -1 and most_matched_modes[1] == -1:
            return list_modes[0][most_matched_modes[0]]
        elif most_matched_modes[0] == -1 and most_matched_modes[1] != -1:
            return list_modes[0][most_matched_modes[1]]
        else:
            return "UNKNOW"

if __name__ == "__main__":
    inp = input()
    while inp != "stop":
        print(whatmode(inp))
        inp = input()
