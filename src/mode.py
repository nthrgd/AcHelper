#!/usr/bin/env python

class Mode:
    """
    Définit un mode de paiement.
    """
    def __init__(self, value):
        self.value = value

    modes = ["CB", "CHEQUE", "VIREMENT", "RETRAIT"]
    # Ajout des 'auteurs' des prélèvements dans la liste des modes de paiement
    with open("../config/accounts_path.txt", "r", encoding="utf-8") as _file:
        accounts_path = _file.readline().strip("\n") 
        with open(accounts_path + "/NE PAS SUPPRIMER/Prélèvements.txt", "r", encoding="utf-8") as _file2:
            for line in _file2.readlines():
                line = line.split(":")
                mode = line[1].strip("\n").replace(" ", "").upper()
                modes.append(mode)


    def whatmode(self):
        mode = self.value.upper()
        list_modes = [Mode.modes, ["CB", "CHEQU", "VIRM", "RET"]]
        if mode in Mode.modes:
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
                elif matches == max_matches: # si il y a une hésitation entre deux modes
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