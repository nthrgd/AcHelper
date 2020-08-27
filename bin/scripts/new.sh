#!/usr/bin/bash

accounts_path=$(cat ../../config/accounts_path.txt)

echo "Nom du nouveau fichier :"
read filename

dep=false

if [ -e ../../config/actfile.txt ]; then
    if [ -e $accounts_path/$(cat ../../config/actfile.txt) ]; then
        line_last_total=$(cat $accounts_path/$(cat ../../config/actfile.txt) | grep Total)
        if [ "$line_last_total" != "" ]; then
            dep=${line_last_total:6}
        fi
    fi
fi


if [ "$dep" == "false" -o "$dep" == "" ]; then
    echo "Montant de depart :"
    read dep
fi


echo "Depart,$dep" > "$accounts_path/$filename.csv"
echo "," >> "$accounts_path/$filename.csv"
echo "Date,Mode,Montant" >> "$accounts_path/$filename.csv"
echo "," >> "$accounts_path/$filename.csv"
echo "Total,$dep" >> "$accounts_path/$filename.csv"


cd ../../src
echo "$filename.csv" > ../config/actfile.txt

if [ -e /usr/bin/python3 ]; then
    ./levy_manager.py
else
    python ./levy_manager.py
fi

echo "$filename.csv créé."
