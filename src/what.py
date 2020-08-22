#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def whatfile():
    with open("../config/actfile.txt", "r", encoding="utf-8") as file:
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
    elif op in ["sup", "supprimer"]:
        return "supprimer"
    else:
        return "add"
