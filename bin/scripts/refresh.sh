#!/usr/bin/bash

red="\e[0;31m"
neutral="\e[0;m"

if [ -e ../../config/actfile.txt ]; then
    if [ -e $(cat ../../config/accounts_path.txt)/$(cat ../../config/actfile.txt) ]; then
        cd ../../src
        if [ -e /usr/bin/python3 ]; then
            ./refresh.py
        else
            python ./refresh.py
        fi
    else
        echo -e "${red}Erreur:${neutral} Le fichier de compte le plus récent n'existe plus. Veuillez en recréer un nouveau ou restorer ce dernier."
    fi

else
    echo -e "${red}Erreur:${neutral} Aucun fichier de compte n'a encore été créer."
fi
