@echo off
set /p ACCOUNTS_PATH= < ../src/ACCOUNTS_PATH.txt
echo %ACCOUNTS_PATH%

set /p filename=Nom du nouveau fichier : 
set /p dep=Montant de depart : 

echo Depart;%dep% > %ACCOUNTS_PATH%/%filename%.csv
echo ; >> %ACCOUNTS_PATH%/%filename%.csv
echo Date;Mode;Montant >> %ACCOUNTS_PATH%/%filename%.csv
echo ; >> %ACCOUNTS_PATH%/%filename%.csv
echo Total;%dep% >> %ACCOUNTS_PATH%/%filename%.csv

REM On se trouve dans le même répertoire que ah.bat (../)
echo %filename%.csv > ../src/actfile.txt 
echo %filename%.csv cree.

pause > nul