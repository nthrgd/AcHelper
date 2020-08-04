#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reader(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = []
        for line in file.readlines():
            line = line.replace("\n", "").split(";")
            if not line[-1]: # Si line[-1] est une chaine vide
                del line[-1]
            content.append(line)
        return content

def writer(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        for line in content:
            file.write(";".join(line) + "\n")
