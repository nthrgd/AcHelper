#!/usr/bin/bash

accounts_path=$(cat ../../config/accounts_path.txt)

echo "Nom du nouveau fichier :"
read filename
echo "Montant de depart :"
read dep

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
