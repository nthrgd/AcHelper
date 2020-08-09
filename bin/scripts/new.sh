#!/usr/bin/bash

ACCOUNTS_PATH=$(cat ../../config/ACCOUNTS_PATH.txt)

echo "Nom du nouveau fichier :" 
read filename
echo "Montant de depart :"
read dep 

echo "Depart;$dep" > "$ACCOUNTS_PATH/$filename.csv"
echo ";" >> "$ACCOUNTS_PATH/$filename.csv"
echo "Date;Mode;Montant" >> "$ACCOUNTS_PATH/$filename.csv"
echo ";" >> "$ACCOUNTS_PATH/$filename.csv"
echo "Total;$dep" >> "$ACCOUNTS_PATH/$filename.csv"


cd ../../src
echo "$filename.csv" > ../config/actfile.txt 
python ./levy_manager.py
echo "$filename.csv créé."