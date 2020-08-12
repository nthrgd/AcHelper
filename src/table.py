#!/usr/bin/env python3
from date import Date
from mode import Mode

class Table:

    def __init__(self, content):
        self.all = content
        self.header = content[:3]
        self.footer = content[len(content) - 2:]
        self.starting = content[0][1]
        self.total = content[-1][1]
        self.accounts = content[3:len(content) - 2]


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