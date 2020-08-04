set ACCOUNTS_PATH=C:\Users\Rudie\Desktop\Accounts 
cd %ACCOUNTS_PATH%

set /p filename=Nom du nouveau fichier : 
set /p dep=Montant de depart : 

echo Depart;%dep% > .\%filename%.csv
echo ; >> .\%filename%.csv
echo Date;Mode;Montant >> .\%filename%.csv
echo ; >> .\%filename%.csv
echo Total;%dep% >> .\%filename%.csv

echo %filename%.csv > "NE PAS SUPPRIMER\actfile.txt" 
echo %filename%.csv cree.

pause > nul