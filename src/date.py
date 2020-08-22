#!/usr/bin/env python3

from datetime import datetime

class Date:
    """ Définit une date en format français. """

    days_per_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    @staticmethod
    def isvalid(date):
        """
        Détermine si une date est est valide ou non sans tenir compte des années bissextiles.
        """
        date = date.replace(" ", "")
        if date[0] == "/" and date != "/":
            return False
        date = date.split("/")
        while "" in date: date.remove("")
        if len(date) > 3:
            return False

        for i in range(len(date)):
            # Jour et mois
            if i < 2:
                if not date[i].isdigit() or len(date[i]) > 2:
                    return False
                if i == 0:
                    if len(date) > 1 and len(date[1]) < 3:
                        if not 0 < int(date[0]) <= Date.days_per_month[int(date[1])]:
                            return False
                    else:
                        if not 0 < int(date[0]) <= Date.days_per_month[datetime.now().month]:
                            return False
                else:
                    if 1 > int(date[i]) > 12:
                        return False
            # Année
            else:
                if not date[i].isdigit() or len(date[2]) > 4:
                    return False

        return True



    def __init__(self, value):
        self.value = value


    def whatdate(self):
        """
        Complète et formatte une date si celle-ci est valide.
        """
        if Date.isvalid(self.value):
            today = datetime.now()
            strf = self.value.split("/")
            while "" in strf:
                strf.remove("")

            # Autocomplétion
            if not strf:
                strf = [str(today.day), str(today.month), str(today.year)]
            if len(strf) < 2:
                strf.append(str(today.month))
            if len(strf) < 3:
                strf.append(str(today.year))

            # Formattage
            for i in range(2):
                if len(strf[i]) < 2:
                    strf[i] = "0" + strf[i]
            if len(strf[2]) < 4:
                strf[2] = str(today.year)[:4 - len(strf[2])] + strf[2]

            return "/".join(strf)


    def get_longformat(self):
        """
        Retourne un entier qui représente la date avec le format AAAAMMJJ.
        Cette méthode doit uniquement être utilisée sur des dates valides.
        """
        date = self.whatdate().split("/")[::-1]
        return int("".join(date))
