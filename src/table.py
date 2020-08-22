#!/usr/bin/env python3
import sys
from copy import deepcopy
from date import datetime
from date import Date
from mode import Mode

class Table:
    """
    Table(content)

    Define a account table using a list of list representing
    the content of a account file in csv format.

    If the content is invalid, the program is stopped.
    """

    @staticmethod
    def isvalid(table):
        if len(table) < 4:
            return False, "Le tableau est trop petit pour être valide."

        # Tests header and footer
        error_msg = "L'entête et/ou le pied de page est/sont invalide(s)."
        if len(table[0]) == 2:
            if not table[0][0].lower() in ["départ", "depart"]:
                return False, error_msg
            else:
                try:
                    float(table[0][1])
                except ValueError:
                    return False, error_msg
        else:
            return False, error_msg
        if len(table[-1]) == 2:
            if table[-1][0].lower() != "total":
                return False, error_msg
            else:
                try:
                    float(table[-1][1])
                except ValueError:
                    return False, error_msg
        else:
            return False, error_msg

        if not (table[1] in [["", ""], [""], []] and table[-2] in [["", ""], [""], []]):
            return False, error_msg

        if len(table[2]) == 3:
            if not ("date" == table[2][0].lower() and "mode" == table[2][1].lower() and "montant" == table[2][2].lower()):
                return False, error_msg
        else:
            return False, error_msg


        # Test account lines
        # We don't need to check if the order is respected because if it's not the case,
        # the tests will not be passed and then the table will in any case be considered invalid.
        error_msg = "La ligne de compte numéro ? est invalide."
        for i in range(3, len(table) - 2):
            if len(table[i]) != 3:
                return False, error_msg.replace("?", str(i - 2))
            else:
                date, mode = Date(table[i][0]), Mode(table[i][1])
                if not (date.whatdate() and mode.whatmode() != "UNKNOW"):
                    return False, error_msg.replace("?", str(i - 2))
                else:
                    try:
                        float(table[i][2])
                    except ValueError:
                        return False, error_msg.replace("?", str(i - 2))


        return True, ""




    def __init__(self, content):
        valid, error_msg = Table.isvalid(content)
        if valid:
            self.all = deepcopy(content)
            self.starting = float(self.all[0][1])
            self.total = float(self.all[-1][1])
            self.accounts = self.all[3:len(self.all) - 2]
        else:
            print("Programme stoppé:", error_msg)
            sys.exit()


    def autocomplete(self):
        """
        Autocomplete the columns of self.accounts and update self.all.
        """
        for i in range(len(self.accounts)):
            date, mode, amount = self.accounts[i]

            self.accounts[i][0] = Date(date).whatdate()          # Date
            self.accounts[i][1] = Mode(mode).whatmode()          # Mode
            self.accounts[i][2] = "{:.2f}".format(float(amount)) # Amount


        # Update self.all
        self.all[3:len(self.all) - 2] = self.accounts



    def sort_by_dates(self):
        list_accounts = deepcopy(self.accounts)
        sorted_list = []
        # Add 2 years to current year
        date_max = int(str(datetime.now().year + 2) + "0101")

        while len(list_accounts) > 0:
            date_min = date_max
            for d, m, a in list_accounts:
                d = Date(d)
                date = d.get_longformat() # We know that d is a valid date
                if date < date_min:
                    date_min = date
                    line_date_min = [d.value, m, a]

            sorted_list.append(line_date_min)
            list_accounts.remove(line_date_min)

        self.accounts = deepcopy(sorted_list)
        self.all[3:len(self.all) - 2] = self.accounts



    def update_total(self):
        new_total = self.starting
        for i in range(len(self.accounts)):
            date, mode, montant = self.accounts[i]
            if mode == "VIREMENT":
                new_total += float(montant)
            else:
                new_total -= float(montant)

        self.total = round(new_total, 2)
        self.all[-1][1] = "{:.2f}".format(self.total)


    def update(self):
        """
        Autocomplete, sort and recalcul the total of the table.
        """
        self.autocomplete()
        self.sort_by_dates()
        self.update_total()
