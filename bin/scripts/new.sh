#!/usr/bin/bash

accounts_path=$(cat ../../config/accounts_path.txt)

echo "Nom du nouveau fichier :" 
read filename
echo "Montant de depart :"
read dep 

echo "Depart;$dep" > "$accounts_path/$filename.csv"
echo ";" >> "$accounts_path/$filename.csv"
echo "Date;Mode;Montant" >> "$accounts_path/$filename.csv"
echo ";" >> "$accounts_path/$filename.csv"
echo "Total;$dep" >> "$accounts_path/$filename.csv"


cd ../../src
echo "$filename.csv" > ../config/actfile.txt 
python ./levy_manager.py
echo "$filename.csv créé."