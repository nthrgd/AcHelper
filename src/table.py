#!/usr/bin/env python3

class Table:

    def __init__(self, content):
        self.all = content
        self.starting = content[0][1]
        self.total = content[-1][1]
        self.accounts = content[3:len(content) - 2]