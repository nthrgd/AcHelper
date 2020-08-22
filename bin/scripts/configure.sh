#!/usr/bin/bash

echo "Entrez le chemin d'accès de l'emplacement où vous souhaitez stocker vos comptes:"
echo "Si vous êtes sous Windows, remplacez les anti-slashs '\' par des slashs '/'."
read accounts_path

mkdir $accounts_path/Comptes
mkdir "$accounts_path/Comptes/NE PAS SUPPRIMER"
mkdir "$accounts_path/Comptes/NE PAS SUPPRIMER/Aide"
cp ../../Documentation/Prelevements.md "$accounts_path/Comptes/NE PAS SUPPRIMER/Aide"
cp ../../Documentation/ModeModifier.md "$accounts_path/Comptes/NE PAS SUPPRIMER/Aide"


touch "$accounts_path/Comptes/NE PAS SUPPRIMER/Prélèvements.txt"
echo "$accounts_path/Comptes" > ../../config/accounts_path.txt

cd "$accounts_path/Comptes/NE PAS SUPPRIMER/Aide"
mv Prelevements.md AidePrélèvements.md

echo ""
echo "Si aucun message d'erreur n'a été affiché, AcHelper est correctement configuré !"
