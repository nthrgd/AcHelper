@echo off
set /p accounts_path=Entrez le chemin d'acces de l'emplacement ou vous souhaitez stocker vos tableaux : 

md %accounts_path%/Comptes
md "%accounts_path%/Comptes/NE PAS SUPPRIMER"
type > "%accounts_path%/Comptes/NE PAS SUPPRIMER/Prelevements.txt"
echo %accounts_path%\Comptes> ../config/accounts_path.txt

pause > nul